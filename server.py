"""
The server file exposes routes for emotion detection application
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Route to call package function
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response=emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return {"message":"Invalid text! Please try again!"}
    result = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )
    return result

@app.route("/")
def render_index_page():
    """
    render index page
    """
    return render_template('index.html')
