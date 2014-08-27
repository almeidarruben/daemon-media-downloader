# daemon-tvsubs-downloader
Automatically downloads TV Shows subtitles.


## Installation
Python packages

    pip install -r requirements.txt


## Configuration
In `config.json`

    {
        "user_agent": "SubDB/1.0 (download_srt/0.1; http://github.com/username)",
	
        "shows_folder": "/path/to/your/tv_shows/folder",

        "languages": "en"
    }


### Subtitle Languages
Subtitles can be downloaded at the same time in all of the available languages below.

Just sepcify them separated by commas in the configuration file.

### Available Languages
* en
* es
* fr
* it
* nl
* pl
* pt
* ro
* sv
* tr


## Execution
Run `python watchdir.py`