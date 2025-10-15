from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector  

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotionDetector():
    statement = ''
    if request.method == 'POST':
        statement = request.form.get('statement', '')
    elif request.method == 'GET':
        statement = request.args.get('textToAnalyze', '')
    if statement:
        result = emotion_detector(statement)
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
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
