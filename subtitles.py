import os
import sys
import json
import urllib
import hashlib

config = {}

def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()


def download_subtitle(name):
    parameters = {'action' : 'download',
                'hash' : get_hash(name),
                'language' : config['languages']}

    encoded_url = urllib.parse.urlencode(parameters)
    final_url = "http://api.thesubdb.com/?" + encoded_url

    req_object = urllib.request.Request(final_url)
    req_object.add_header('User-Agent', config['user_agent'])

    page_content = urllib.request.urlopen(req_object)

    content_srt = page_content.read()
    return content_srt


def create_srt_file(file_name, content):
    srt_name = file_name[:-3] + "srt"
    f = open(srt_name, "w")
    f.write(content)
    f.close()


def main():
    with open('config.json') as handle:
        config.update(json.load(handle))

    shows_folder = config['shows_folder']

    file_name = "Penny.Dreadful.S01E08.HDTV.x264-KILLERS.mp4"
    content = download_subtitle(file_name)
    create_srt_file(file_name, content)


if __name__ == '__main__':
    main()


#try:
    #page_content = urlopen(req_object)

 #   except URLError, e:
  #      if e.code == 404:
   #         print "Subtitle ", name, " not found"
  
    #content_srt = page_content.read()