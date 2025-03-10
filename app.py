import os
from flask import Flask, render_template, request, url_for
from gtts import gTTS

app = Flask(__name__)

# Ensure the static folder exists
if not os.path.exists('static'):
    os.makedirs('static')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        if text:
            tts = gTTS(text=text, lang="en")
            audio_file = os.path.join('static', 'output.mp3')
            tts.save(audio_file)  # Save the audio file
            return render_template("index.html", audio_file=url_for('static', filename='output.mp3'))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
