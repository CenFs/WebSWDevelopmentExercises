# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 23:21:22 2017

@author: Jingyi
"""
import json

class Song:
    def __init__(self, stri):
        self.directory = 'lastfm_subset/' + stri[2] + '/' + stri[3] + '/' + stri[4] + '/'
        self.location = self.directory + stri + '.json'
        # print self.location
        with open(self.location, 'r') as fp:
            jsdata = json.load(fp)
            # print jsdata
            self.track_id = jsdata['track_id']
            self.title = jsdata['title']
            self.timestamp = jsdata['timestamp']
            self.tags = jsdata['tags']
            self.similars = jsdata['similars']
            self.artist = jsdata['artist']
    def get_tags(self, limit):
    def get_similars(self, limit):
    def shared_tags(self, other_song_instance):
    def combined_tags(self, other_song_instance):



some_song = Song('TRAWHKS128F9330619')


# 待解决问题：
# 怎么判断文件读取成功还是失败，catch异常


with open('lastfm_subset/A/W/H/TRAWHKS128F9330619.json', 'r') as fp:
    data = json.load(fp)
    s = data['tags']
    print json.dumps(s)