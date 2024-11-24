# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-12-01
"""
import os, requests
from pytube import YouTube
from bs4 import BeautifulSoup
from rich.console import Console

class YTube:
    def __init__(self, obj):
        self.type = obj.type.lower()
        self.path = obj.path
        self.url = obj.url
        self.console = Console()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/111.25 (KHTML, like Gecko) Chrome/99.0.2345.81 Safari/123.36'}

    @staticmethod
    def check_folder(path: str):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)

    @staticmethod
    def replace_symbol(symbol, filename) -> str:
        return filename.translate({ord(symbol): None}) if symbol in filename else filename

    @staticmethod
    def title_name(url, headers) -> str:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        tags = soup.find_all('title')

        filename = tags[0].string[:-10]
        filename = YTube.replace_symbol('/', filename)
        filename = YTube.replace_symbol('.', filename)

        # If the file name is too long, an error will occur.
        filename = filename[:20] if len(filename) > 20 else filename
        return filename

    def progress_bar(self, title: str, content: str):
        match title:
            case 'args':
                self.console.print(f"Get Parameter... {'━' * 46} 100%")
            case 'type':
                if content in ['m' , 'music']:
                    self.console.print('- Target Type : Music')
                elif content in ['v', 'video']:
                    self.console.print('- Target Type : Video')
                else:
                    self.console.print(f'- Target Type : *** {self.type} ***')
            case 'url':
                self.console.print(f'- Target Url : {content}')
            case 'path':
                self.console.print(f'- Target Path : {content}')
            case 'mp3':
                self.console.print('MP3 Has Been Successfully Downloaded !')
            case 'mp4':
                self.console.print('MP4 Has Been Successfully Downloaded !')

    def check_file(self, new, old):
        if not os.path.exists(new):
            os.rename(old, new)
            if new[-3:] == 'mp3':
                self.progress_bar('mp3', 'None')
            elif new[-3:] == 'mp4':
                self.progress_bar('mp4', 'None')
        else:
            self.console.print('- Warning ! There are already files in the path.')
            # Duplicate files occurred, but the program startup process generated webm/mp4, so cleared them.
            media_type = new.split('.')[-1]
            if media_type == 'mp3':
                os.remove(old)
            elif media_type == 'mp4':
                pass
            else:
                self.console.print(f'Error -> other type: {media_type}')

    def yt_downloads(self):
        new, old = None, None
        yt = YouTube(self.url)
        filename = YTube.title_name(self.url, self.headers)

        if self.type in ['m', 'music']:
            video = yt.streams.filter(only_audio=True)[-1]
            old = video.download(output_path=self.path)
            new = self.path + filename + '.mp3'

        elif self.type in ['v', 'video']:
            video = yt.streams.filter(file_extension='mp4')[1]
            old = video.download(output_path=self.path)
            new = self.path + filename + '.mp4'

        else:
            self.console.print(f'Error Type: {self.type}')

        if new is not None and old is not None and filename is not None:
            self.progress_bar('path', filename)
            self.check_file(new, old)

    def main(self):
        YTube.check_folder(self.path)
        self.progress_bar('args', 'None')
        self.progress_bar('type', self.type)
        self.progress_bar('url', self.url)
        self.yt_downloads()