#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dsd import DSD
import json, sys

config = {}

class MyHandler(FileSystemEventHandler):
    
    def on_modified(self, event):
        start_queue = DSD(config)
        start_queue.run()



def main(argv):
    with open('config.json') as handle:
        config.update(json.load(handle))


    if len(sys.argv) > 1:
        # Set language without changing the configuration file
        if (sys.argv[1] == '-l'):
            config['languages'] = sys.argv[2]

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=config["shows_folder"], recursive=False)
    observer.start()
    print "Daemon Subtitle Downloader started..."

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
	main(sys.argv[1:])