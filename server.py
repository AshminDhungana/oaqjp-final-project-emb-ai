"""Flask application for NLP Emotion Detection."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def home():
    """Render the main page."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Handle emotion detection requests from GET or POST.
    
    Returns:
        str: Formatted response text or error message for invalid input.
    """
    statement = ''

    if request.method == 'POST':
        statement = request.form.get('statement', '')
    elif request.method == 'GET':
        statement = request.args.get('textToAnalyze', '')

    result = emotion_detector(statement)

    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
