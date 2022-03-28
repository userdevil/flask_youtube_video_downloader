import logging
import os
from pytube import YouTube
from flask import Flask, flash, request, send_file, render_template
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
 
@app.route("/")
def youtube_downloader():
    """Render HTML form to accept YouTube URL."""
    return render_template('index.html')
 
@app.route("/download_video", methods=["GET","POST"])
def download_video():
    try:
        youtube_url = request.form["URL"]
        download_path = YouTube(youtube_url).streams[0].download()
        fname = download_path.split("//")[-1]
        return send_file(fname, as_attachment=True)
    except:
        logging.exception("Failed download")
        logging.exception("Failed download")
        flash(u'Video Download Failed! ⚠️', 'error')
        return render_template('index.html',eror = "Video Download Failed! ⚠️")

@app.route('/api/', methods=['GET'])
def user_encode():
    message = request.args.get('url')
    un = request.args.get('f')
    if un == 1080:
       youtube_url = message
       srteam = YouTube(youtube_url).streams.filter(res="1080p")
       download_path = srteam.download()
       fname = download_path.split("//")[-1]
       return send_file(fname, as_attachment=True)
    if un == 720:
       youtube_url = message
       sretam = YouTube(youtube_url).streams.filter(res="720p")
       download_path = sretam.download()
       fname = download_path.split("//")[-1]
       return send_file(fname, as_attachment=True)
    if un == 360:
       youtube_url = message
       sreatm = YouTube(youtube_url).streams.filter(res="360p")
       download_path = sreatm.download()
       fname = download_path.split("//")[-1]
       return send_file(fname, as_attachment=True)
    if un == 240:
       youtube_url = message
       sreamt = YouTube(youtube_url).streams.filter(res="240p")
       download_path = sreamt.download()
       fname = download_path.split("//")[-1]
       return send_file(fname, as_attachment=True)
    if un == 144:
       youtube_url = message
       sream = YouTube(youtube_url).streams.filter(res="144p")
       download_path = sream.download()
       fname = download_path.split("//")[-1]
       return send_file(fname, as_attachment=True)
    if un == 'mp3':
       yt = message
       st = YouTube(yt).streams.filter(only_audio=True)
       download_path = st[0].download()
       fname = download_path.split("//")[-1]
       return send_file(fname, as_attachment=True)
    youtube_url = message
    download_path = YouTube(youtube_url).streams[0].download()
    fname = download_path.split("//")[-1]
    return send_file(fname, as_attachment=True)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
