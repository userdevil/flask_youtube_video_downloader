import logging
import os
from pytube import YouTube
from flask import Flask, request, send_file
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)
 
@app.route("/")
def youtube_downloader():
    """Render HTML form to accept YouTube URL."""
    html_page = f"""<html><head>
                    <Title>YouTube Downloader</Title></head>
                    <body><h2>Enter URL to download YouTube Vids!</h2>
                    <div class="form">
                    <form action="/download_video" method="post">
                    <input type="text" name="URL">
                    <input type="submit" value="Submit">
                    </form></div><br><br>
                    </body></html>"""
    return html_page
 
@app.route("/download_video", methods=["GET","POST"])
def download_video():
    try:
        youtube_url = request.form["URL"]
        download_path = YouTube(youtube_url).streams[0].download()
        fname = download_path.split("//")[-1]
        return send_file(fname, as_attachment=True)
    except:
        logging.exception("Failed download")
        return "Video download failed!"

@app.route('/api/', methods=['GET'])
def user_encode():
    message = request.args.get('url')
    un = request.args.get('f')
    if un == 1080:
       youtube_url = message
       srteam = YouTube(youtube_url).streams.get_by_resolution('1080p')
       download_path = srteam.download()
       fname = download_path.split("//")[-1]
       return send_file(fname, as_attachment=True)
    if un == 720:
       youtube_url = message
       sretam = YouTube(youtube_url).streams.get_by_resolution('720p')
       download_path = sretam.download()
       fname = download_path.split("//")[-1]
       return send_file(fname, as_attachment=True)
    if un == 360:
       youtube_url = message
       sreatm = YouTube(youtube_url).streams.get_by_resolution('360p')
       download_path = sreatm.download()
       fname = download_path.split("//")[-1]
       return send_file(fname, as_attachment=True)
    if un == 240:
       youtube_url = message
       sreamt = YouTube(youtube_url).streams.get_by_resolution('240p')
       download_path = sreamt.download()
       fname = download_path.split("//")[-1]
       return send_file(fname, as_attachment=True)
    if un == 144:
       youtube_url = message
       sream = YouTube(youtube_url).streams.get_by_resolution('144p')
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
