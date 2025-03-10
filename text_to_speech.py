import tkinter as tk
from gtts import gTTS
from playsound import playsound
import os

def text_to_audio():
    text = text_input.get("1.0", "end-1c")  # Get text from input box
    if text.strip():
        tts = gTTS(text=text, lang='en')  # Convert text to speech
        audio_file = "output.mp3"
        tts.save(audio_file)  # Save audio to file
        playsound(audio_file)  # Play the audio
        os.remove(audio_file)  # Remove the audio file after playing

# GUI Setup
root = tk.Tk()
root.title("Text to Audio Converter")

# Text input
text_input = tk.Text(root, height=10, width=40)
text_input.pack(pady=10)

# Button to trigger TTS conversion
listen_button = tk.Button(root, text="Listen", command=text_to_audio)
listen_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
