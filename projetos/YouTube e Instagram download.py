# YouTube download

import subprocess, sys
try:
  from pytube import YouTube 
except ModuleNotFoundError:
  subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pytube"]) 
  from pytube import YouTube 

url = "http://youtube.com/watch?v=2lAe1cqCOXo"
yt = YouTube(url)
video = yt.streams.filter(progressive = True)[-1]
video.download()

# Instagram download

import subprocess, sys
try:
  from instaloader import Instaloader, Post
except ModuleNotFoundError:
  subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "instaloader"]) 
  from instaloader import Instaloader, Post

url = "https://www.instagram.com/p/CVvp8tNPBLW/?utm_medium=copy_link"
url = url[url.index("p/") + 2:]
url = url[:url.index("/")]
insta = Instaloader(download_pictures=True, download_videos=True, download_video_thumbnails=False, download_geotags=False, download_comments=False, save_metadata=False, compress_json=False) 
post = Post.from_shortcode(insta.context, url)
insta.download_post(post, ".")
