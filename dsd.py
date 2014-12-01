#!/usr/bin/python
import os
import json
from subtitles import Subtitle

class DSD(object):

    def __init__(self, config):
        self.config = config

    def run(self):
        self.download_subtitle_queue(self.search_missing_subtitles(self.config["shows_folder"]))


    """
        Search in the directory for missing subtitles
        Returns a dictionary with video files missing subtitles
    """
    def search_missing_subtitles(self, directory):
        directory_dict = self.directory_to_dict(directory)
        
        video_dict = self.separate_video_files(directory_dict)
        subtitle_dict = self.separate_srt_files(directory_dict)

        # Remove from dict files already with subtitles
        to_remove = []
        for subtitle in subtitle_dict:
            for video in video_dict:
                if (subtitle_dict[subtitle]['file_name'][:-4] == video_dict[video]['file_name'][:-4]):
                    to_remove.append(video)

        for remove in to_remove:
            del video_dict[remove]

        return video_dict


    """
        Creates a dictionary with all files from the directory
    """
    def directory_to_dict(self, directory):
        directory_files = {}
        cnt = 0
        for path, subdirs, files in os.walk(directory):
            for name in files:
                loop_dict = {}
                file_extension = os.path.splitext(name)[1]
                if (file_extension == ".mp4" or file_extension == ".avi" or file_extension == ".mkv" or file_extension == ".srt"):
                    loop_dict = {cnt: {"file_name" : name, "file_location" : path}}

                    directory_files.update(loop_dict)
                    cnt += 1

        return directory_files


    """
        Remove all video files from dictionary
    """
    def separate_video_files(self, directory_dict):
        subtitle_dict = {}
        cnt = 0
        for i in directory_dict:
            if (directory_dict[i]['file_name'][-3:]) != 'srt':
                subtitle_dict[cnt] = directory_dict[i]
            cnt += 1
        return subtitle_dict


    """
        Remove all video files from dictionary
    """
    def separate_srt_files(self, directory_dict):
        video_dict = {}
        cnt = 0
        for i in directory_dict:
            if (directory_dict[i]['file_name'][-3:]) == 'srt':
                video_dict[cnt] = directory_dict[i]
            cnt += 1
        
        return video_dict


    """
        Loop on the missing subtitles list and start the downloads
    """
    def download_subtitle_queue(self, missing_subtitles):
        for subtitle in missing_subtitles:
            print 'Downloading', missing_subtitles[subtitle]['file_name']
            new_subtitle = Subtitle(missing_subtitles[subtitle], self.config)
            new_subtitle.start_download()

        missing_subtitles.clear()
        print 'DONE!\n'

