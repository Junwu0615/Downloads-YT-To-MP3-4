# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-11-24
"""

import os
import requests
from pytube import YouTube
from bs4 import BeautifulSoup
from argparse import ArgumentParser

class YTube:
    def __init__(self, obj):
        self.type = obj.type.lower()
        self.path = obj.path
        self.url = obj.url
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/111.25 (KHTML, like Gecko) Chrome/99.0.2345.81 Safari/123.36'}

    def check_folder(self, path: str):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)

    def get_filename(self, url: str) -> str:
        web = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(web.text, 'html.parser')
        tags = soup.find_all('title')
        name = tags[0].string[:-10]
        if '/' in name:
            name = name.translate({ord('/'): None})  # Check_File_Title
        if len(name) > 20:
            name = name[:20]  # If the file name is too long, an error will occur.
        return name

    def progress_bar(self, task, item):
        match task:
            case 'args':
                print('Get Parameter... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%')
            case 'type':
                if item in ['m' , 'music']:
                    print('- Target Type : Music')
                elif item in ['v', 'video']:
                    print('- Target Type : Video')
            case 'url':
                print('- Target Url : ' + item)
            case 'path':
                print('- Target Path : ' + item)
            case 'mp3':
                print('MP3 Has Been Successfully Downloaded !')
            case 'mp4':
                print('MP4 Has Been Successfully Downloaded !')

    def check_file(self, new, out, filename):
        file = os.path.exists(new)
        if not file:
            os.rename(out, new)
            if new[-3:] == 'mp3':
                self.progress_bar('mp3', None)
            elif new[-3:] == 'mp4':
                self.progress_bar('mp4', None)
        else:
            print('- Warning ! There are already files in the path.')
            # Duplicate files occurred, but the program startup process generated webm/mp4, so I cleared them.
            remove_filename = filename
            if '/' in filename: remove_filename = filename.translate({ord('/'): None})
            if '.' in filename: remove_filename = filename.translate({ord('.'): None})
            if new[-3:] == 'mp3':
                remove_txt = self.path + remove_filename + '.webm'
                os.remove(remove_txt)
            elif new[-3:] == 'mp4':
                pass

    def yt_downloads(self):
        new, out, filename = None, None, None
        yt = YouTube(self.url)
        filename = self.get_filename(self.url)  # Get FileName
        if self.type in ['m', 'music']:
            video = yt.streams.filter(only_audio=True)[-1]
            out = video.download(output_path=self.path)
            new = self.path + filename + '.mp3'
        elif self.type in ['v', 'video']:
            video = yt.streams.filter(file_extension='mp4')[1]
            out = video.download(output_path=self.path)
            new = self.path + filename + '.mp4'

        if new is not None and out is not None and filename is not None:
            self.progress_bar('path', filename) # Output
            self.check_file(new, out, filename)

    def main(self):
        self.progress_bar('args', None)
        self.progress_bar('type', self.type)
        self.progress_bar('url', self.url)
        self.check_folder(self.path)
        self.yt_downloads()