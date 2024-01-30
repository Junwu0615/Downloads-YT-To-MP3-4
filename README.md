<a href='https://github.com/Junwu0615/Downloads-YT-To-MP3-4'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Downloads-YT-To-MP3-4.svg'> 
<a href='https://github.com/Junwu0615/Downloads-YT-To-MP3-4'><img alt='GitHub Clones' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/acb7aeb93f554e94a7a6db8e909bc0c6/raw/Downloads-YT-To-MP3-4_clone.json&logo=github'> </br>
[![](https://img.shields.io/badge/Project-YouTubeDownloads-blue.svg?style=plastic)](https://github.com/Junwu0615/Downloads-YT-To-MP3-4) 
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) </br>
[![](https://img.shields.io/badge/Package-pytube_15.0.0-green.svg?style=plastic)](https://pypi.org/project/pytube/) 
[![](https://img.shields.io/badge/Package-BeautifulSoup_4.12.2-green.svg?style=plastic)](https://pypi.org/project/beautifulsoup4/) 
[![](https://img.shields.io/badge/Package-Requests_2.31.0-green.svg?style=plastic)](https://pypi.org/project/requests/) 
[![](https://img.shields.io/badge/Package-ArgumentParser_1.2.1-green.svg?style=plastic)](https://pypi.org/project/argumentparser/) 


## A.　研究動機
Web 2.0 壟罩下，我們的生活樣態就是使用互聯網的內容，並享受著這一切 ! 眾多影音平台中，YouTube 是我的首選，相信人人都想把喜歡的作品收藏起來並隨時使用，我也不外乎...至此本專案粗淺目的就此誕生。

<br/>

## B.　歷史紀錄
| 事件 | 敘述 | 更新時間 |
| :--: | :-- | :--: |
| 專案上架 | Downloads-YT-To-MP3-4 | 2024/01/02 |
| 加快下載效率 | 得到 YT 標題方式是透過爬蟲的方法，雖能抓到標題，但也多一道程序 | - |
| 一次性下載大量檔案 | 透過 txt 寫入要載的 url，接著用多執行緒一次下載 | - |
| 視窗程式 (.exe) 呈現專案 | 可不需安裝 Python，即可使用本專案功能 | - |
| 聲音 / 畫質規格提高 | 目前品質為 Music: OPUS 150kbps / Video: 720p 25fps | - |

<br/>

## C.　如何使用

### STEP.1　CLONE
```py
https://github.com/Junwu0615/Downloads-YT-To-MP3-4.git
```

### STEP.2　INSTALL PACKAGES
```py
pip install -r requirements.txt
```

### STEP.3　RUN
```py
python Downloads-YT-To-MP3-4.py -h
```

### STEP.4　HELP
- `-h`　Help:　Show this help message and exit.
- `-t`　Type:　Give a type | ex: music(m) / video(v)
- `-p`　Path:　Give a path | ex:　./Downloads/
- `-u`　Url :　 Give a YT URL | ex:　https://www.youtube.com/...

### STEP.5　EXAMPLE
#### I.　下載音樂 (Downloads Music)
```py
python Downloads-YT-To-MP3-4.py -t m -p ./Downloads/ -u https://www.youtube.com/watch?v=JsHqEpWQl-8
```
<img src="https://github.com/Junwu0615/Downloads-YT-To-MP3-4/blob/main/sample_gif/music.gif">

- `-t` m
- `-P` ./Downloads/
- `-u` https://www.youtube.com/watch?v=JsHqEpWQl-8

#### II.　下載影片 (Downloads Video)
```py
python Downloads-YT-To-MP3-4.py -t v -p ./Downloads/ -u https://www.youtube.com/watch?v=JsHqEpWQl-8
```
<img src="https://github.com/Junwu0615/Downloads-YT-To-MP3-4/blob/main/sample_gif/video.gif">

- `-t` v
- `-P` ./Downloads/
- `-u` https://www.youtube.com/watch?v=JsHqEpWQl-8

<br/>

## D.　YouTube 來源
- [YouTube 音樂庫](https://www.youtube.com/watch?v=JsHqEpWQl-8)

## E.　參考來源
- [GeeksforGeeks | Download-Video-In-mp3-Format-Using-Pytube](https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/)