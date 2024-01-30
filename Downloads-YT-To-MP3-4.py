import os
import requests
from pytube import YouTube
from bs4 import BeautifulSoup
from argparse import ArgumentParser

def get_filename(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/111.25 (KHTML, like Gecko) Chrome/99.0.2345.81 Safari/123.36"}
    web = requests.get(url, headers = headers); soup = BeautifulSoup(web.text, "html.parser"); 
    tags = soup.find_all("title"); filename = tags[0].string[:-10]; 
    if "/" in filename: filename = filename.translate({ord("/"): None}) # Check_File_Title
    if len(filename) > 20: filename = filename[:20] # If the file name is too long, an error will occur.
    return filename
    
def parse_args():
    parse = ArgumentParser()
    parse.add_argument("-t", "--type", help = "give a type | ex: 'music(m) / video(v)'", default = "m", type = str)
    parse.add_argument("-p", "--path", help = "give a path | ex: './Downloads/'", default = "./", type = str)
    parse.add_argument("-u", "--url", help = "give a YT URL | ex: 'https://...'", default = "https://www.youtube.com/watch?v=JsHqEpWQl-8", type = str)
    args = parse.parse_args()
    return args

def mkdir(path):
    folder = os.path.exists(path)
    if not folder: os.makedirs(path)

def progress_bar(task, item):
    match task: 
        case "args": print("Get Parameter... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%")
        case "type_":
            item = item.lower()
            if item == "m" or item == "music": print("- Target Type : Music" )
            elif item == "v" or item == "video": print("- Target Type : Video")
        case "url": print("- Target Url : " + item) 
        case "path": print("- Target Path : " + item)
        case "mp3": print("MP3 Has Been Successfully Downloaded !")
        case "mp4": print("MP4 Has Been Successfully Downloaded !")
            
def check_file(new_file, path):
    file = os.path.exists(new_file)
    if not file:
        os.rename(out_file, new_file)
        if new_file[-3:] == "mp3": progress_bar("mp3", None)
        elif new_file[-3:] == "mp4": progress_bar("mp4", None)
    else:
        print("- Warning ! There are already files in the path.")
        #Duplicate files occurred, but the program startup process generated webm/mp4, so I cleared them.
        remove_filename = filename
        if "/" in filename: remove_filename = filename.translate({ord("/"): None})
        if "." in filename: remove_filename = filename.translate({ord("."): None})
        if new_file[-3:] == "mp3": remove_txt = "./" + path + remove_filename + ".webm"; os.remove(remove_txt); 
        elif new_file[-3:] == "mp4": pass
    
def YT_downloads(type_, url, path):
    global out_file, new_file, yt, filename
    progress_bar("type_", type_); progress_bar("url", url); yt = YouTube(url); 
    mkdir(path) # Check Folder
    filename = get_filename(url) # Get FileName
    type_ = type_.lower() # Choose Type / Get The Highest Specification File Format
    if type_ == "m" or type_ == "music":
        video = yt.streams.filter(only_audio=True)[-1]
        out_file = video.download(output_path=path)
        new_file = path + filename + ".mp3"
    elif type_ == "v" or type_ == "video":
        video = yt.streams.filter(file_extension='mp4')[1]
        out_file = video.download(output_path=path)
        new_file = path + filename + ".mp4"
    progress_bar("path", filename) # Output
    check_file(new_file, path)
    
if __name__ == "__main__":
    args = parse_args()
    progress_bar("args", None)
    YT_downloads(args.type, args.url, args.path)