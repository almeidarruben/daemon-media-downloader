import json
from subtitles import Subtitle

config = {}

def main():
    with open('config.json') as handle:
        config.update(json.load(handle))

    #shows_folder = config['shows_folder']

    file_name = "Penny.Dreadful.S01E07.HDTV.x264-KILLERS.mp4"
    new_subtitle = Subtitle(file_name, config)
    new_subtitle.start_download()
    
    #content = download_subtitle(file_name)
    #create_srt_file(file_name, content)


if __name__ == '__main__':
    main()
