#pip install pytube
#python 17_youtube.py
from pytube import YouTube
import  tkinter as tk
from tkinter import filedialog

def download_video(url,save_path):
    try:
        yt=YouTube(url)
        streams=yt.streams.filter(progressive=True,fle_extension="mp4")
        highest_res_stream=streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video download successfully...")
    except Exception as e:
        print(e)
        
        
        
def open_file_dialogue():
    folder=filedialog.askdirectory()
    if folder:
        print(f"Selcted Folder : {folder}")
    return folder
        

if __name__=="__main__":  
    root=tk.Tk()
    root.withdraw()
    
    video_url=input("Please enetr a URL : ") 
    save_dir=open_file_dialogue() 
    
    if not save_dir:
        print("Invalid save location...")
    else:
        print("Started download..")
        download_video(video_url,save_dir)
          
# url="https://www.youtube.com/watch?v=NpmFbWO6HPU&list=PPSV"
# save_path ="D:/Krishna_CurrentTerm/python/21_pythonProject/17_pythonAutomation"
# download_video(url,save_path)       