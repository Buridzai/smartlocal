from flask import Flask, render_template, request, redirect, url_for
from grpc_client import send_audio_to_grpc
from tts import speak
from logic import handle_question

app = Flask(__name__)
spoken_text = ""

@app.route("/", methods=["GET", "POST"])
def index():
    global spoken_text
    if request.method == "POST":
        if "speak" in request.form:
            text = send_audio_to_grpc()
            reply = handle_question(text)
            speak(reply)
            spoken_text = reply
        elif "submit" in request.form:
            text = request.form["text"]
            speak(text)
            spoken_text = text
        elif "ask" in request.form:
            text = request.form["question"]
            reply = handle_question(text)
            speak(reply)
            spoken_text = reply
        return redirect(url_for('index'))
    return render_template("index.html", spoken_text=spoken_text)

if __name__ == "__main__":
    app.run(debug=True)
