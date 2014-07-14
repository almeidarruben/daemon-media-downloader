import os
import sys
import json
import urllib.parse
import urllib.request
import hashlib

class Subtitle(object):
    
    def __init__(self, file_name, config):
        self.file_name = file_name
        self.config = config

    
    """
    Returns the hashcode from the file
    """
    def get_hash(self, file_name):
        readsize = 64 * 1024
        with open(file_name, 'rb') as f:
            size = os.path.getsize(file_name)
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()


    """
    Downloads the subtitle

    Available Languages (need to be separated by canvas)
    en,es,fr,it,nl,pl,pt,ro,sv,tr
    """
    def download_subtitle(self, file_name):
        parameters = {'action' : 'download',
                    'hash' : self.get_hash(file_name),
                    'language' : self.config['languages']}

        encoded_url = urllib.parse.urlencode(parameters)
        final_url = "http://api.thesubdb.com/?" + encoded_url

        req_object = urllib.request.Request(final_url)
        req_object.add_header('User-Agent', self.config['user_agent'])

        try:
            page_content = urllib.request.urlopen(req_object)

        except urllib.error.URLError as e:
            if e.code == 404:
                print("Subtitle not found: ", file_name)

        # The content_srt need to be decoded with UTF-8 encoding
        content_srt = page_content.read()

        self.create_srt_file(file_name, content_srt.decode(encoding='UTF-8'))


    """
        Creates the srt file to store the downloaded data
    """
    def create_srt_file(self, file_name, content):
        srt_name = file_name[:-3] + "srt"
        f = open(srt_name, "w")
        f.write(content)
        f.close()


    def start_download(self):
        self.download_subtitle(self.file_name)
