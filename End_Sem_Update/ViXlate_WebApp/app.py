# The UI is a template taken from "https://github.com/creativetimofficial/argon-design-system"

from flask import Flask, redirect, url_for, render_template, request, Response
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/'

OUTPUT_VIDEO = "/content/DownloadedVideos/downloadedVideo.mkv"
OUTPUT_AUDIO = "/content/OutcomeAudios/extractedAudio.wav"
AUDIO_FOLDER = "/content/OutcomeAudios/"
VIDEO_FOLDER = "/content/DownloadedVideos/"
SAMPLING_RATE = 28000


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/how-it-works')
def howItWorks():
    return render_template('howItWorks.html')


@app.route('/translate')
def translate():
    return render_template('code.html', showVideos=False)


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


@app.route("/translate_video", methods=["GET", "POST"])
def translate_video():
    isURL = False
    if os.path.isfile(OUTPUT_VIDEO):
        os.remove(OUTPUT_VIDEO)
    if os.path.isfile(OUTPUT_AUDIO):
        os.remove(OUTPUT_AUDIO)
    if os.path.isfile('/content/static/translatedVideo.mkv'):
        os.remove("/content/static/translatedVideo.mkv")

    video_url = request.form.get('videoUrl')
    video_file = request.files.get('videoFile')
    print("-------------- VIDEO URL: " + video_url)
    if video_url:
        isURL = True
        print("Download Video")
        print("Extract Audio")
    elif video_file:
        # Handle uploaded file
        filename = video_file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        video_file.save(file_path)
        print("Extract Audio")

    return render_template('code.html', showVideos=True)


if __name__ == "__main__":
    app.run()
