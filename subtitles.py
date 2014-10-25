#!/usr/bin/python
import os
import sys
import json
import hashlib
import requests

class Subtitle(object):
    
    def __init__(self, file_name, config):
        self.file_name = file_name
        self.config = config

    
    """
        Returns the hashcode from the file
    """
    def get_hash(self, file_name):
        if (os.path.getsize(file_name) == 0):
            print('ERROR: File size is too short')

        else:
            readsize = 64 * 1024
            with open(file_name, 'rb') as f:
                size = os.path.getsize(file_name)
                data = f.read(readsize)
                f.seek(-readsize, os.SEEK_END)
                data += f.read(readsize)
            return hashlib.md5(data).hexdigest()


    """
        Downloads the subtitle

        Available Languages (need to be separated by commas)
        en,es,fr,it,nl,pl,pt,ro,sv,tr
    """
    def download_subtitle(self, file_name):
        headers = {'User-Agent' : self.config['user_agent']}

        params = {'action' : 'download',
                    'hash' : self.get_hash(file_name['file_location'] + '/' + file_name['file_name']),
                    'language' : self.config['languages']}

        subtitle_url = 'http://api.thesubdb.com'
        req_object = requests.get(subtitle_url, headers=headers, params=params, stream=True)
        
        if req_object.status_code  == requests.codes.ok:
            self.create_srt_file(file_name['file_location'] + '/' + file_name['file_name'], 
                req_object)

        else:
            print('Subtitle not found: ' + file_name['file_name'])

        
    """
        Creates the srt file to store the downloaded data
    """
    def create_srt_file(self, file_name, req_object):
        srt_name = file_name[:-3] + "srt"
        f = open(srt_name, "w")
        f.write(req_object.text)
        f.close()


    """
        Initiates the subtitle download
    """
    def start_download(self):
        self.download_subtitle(self.file_name)
