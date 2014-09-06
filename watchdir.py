#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dsd import DSD
import json

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        start_queue = DSD()
        start_queue.run()


if __name__ == "__main__":
    config = {}
    with open('config.json') as handle:
        config.update(json.load(handle))

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=config["shows_folder"], recursive=False)
    observer.start()
    print("Daemon Subtitle Downloader started...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()