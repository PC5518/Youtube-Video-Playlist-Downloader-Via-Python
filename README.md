# YouTube Playlist Downloader (Educational Use Only)

This is a simple Python tool that automatically downloads videos from a YouTube playlist.  
It uses `yt-dlp` (a powerful YouTube downloader) to extract and download each video individually.



Things that you need to download manually 
Downloaded from ffmpeg.org

Unzipped and placed inside a system folder or project folder

Added to PATH so that yt-dlp can use it silently in the background
In order to check whether it's placed properly or not, you can use your terminal  Open Command Prompt and type:

bash Copy Edit ffmpeg -version
 
 
### 🔹 What It Does
- Takes a YouTube playlist URL  
- Extracts all video links  
- Downloads each video one by one to a folder of your choice

Great for personal use — like backing up your own uploaded videos, saving educational content, or offline access to Creative Commons content.

---

### ⚠️ Disclaimer
> This tool is intended **strictly for personal or educational use**.  
> Do **not** use it to download copyrighted content without permission.  
> Respect YouTube’s Terms of Service.

---

### 🔧 Tech Used
- Python  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (open-source library)

---

### ▶️ How to Run

1. Install yt-dlp:
```bash
pip install yt-dlp
python final_integration_of_code.py
