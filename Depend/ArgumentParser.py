# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-11-24
"""
from argparse import ArgumentParser, Namespace

class AP:
    def __init__(self, obj):
        self.obj = obj

    @staticmethod
    def parse_args() -> Namespace:
        parse = ArgumentParser()
        parse.add_argument("-t", "--type",
                           help="give a type | ex: 'music(m) / video(v)'",
                           default="m", type=str)

        parse.add_argument("-p", "--path",
                           help="give a path | ex: './Downloads/'",
                           default="./Downloads/", type=str)

        parse.add_argument("-u", "--url",
                           help="give a YouTube URL | ex: 'https://...'",
                           default="https://www.youtube.com/watch?v=JsHqEpWQl-8", type=str)

        return parse.parse_args()

    def config_once(self):
        args = AP.parse_args()
        self.obj.type = args.type
        self.obj.path = args.path
        self.obj.url = args.url