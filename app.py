from flask import Flask, render_template, request, send_file
import pyttsx3
import pdfplumber
import os

app = Flask(__name__)

# Route for the Text-to-Audio page
@app.route('/text-to-audio', methods=['GET', 'POST'])
def text_to_audio():
    if request.method == 'POST':
        text = ""
        # Handle text area input
        if 'textInput' in request.form:
            text = request.form['textInput']

        # Handle PDF upload
        if 'fileInput' in request.files:
            file = request.files['fileInput']
            if file.filename.endswith('.pdf'):
                with pdfplumber.open(file) as pdf:
                    text = "\n".join([page.extract_text() for page in pdf.pages])
            elif file.filename.endswith('.txt'):
                text = file.read().decode('utf-8')

        if text.strip() == "":
            return "No text provided", 400

        # Voice selection
        voice_choice = request.form.get('voiceSelect', 'female1')

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        # Simple mapping
        if "female" in voice_choice:
            engine.setProperty('voice', voices[1].id)
        else:
            engine.setProperty('voice', voices[0].id)

        # Save audio
        output_file = "output.mp3"
        engine.save_to_file(text, output_file)
        engine.runAndWait()

        return send_file(output_file, as_attachment=True)

    return render_template('text-to-audio.html')

# Home route
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
