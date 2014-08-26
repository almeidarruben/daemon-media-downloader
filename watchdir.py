#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dsd import DSD

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        start_queue = DSD()
        start_queue.run()


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/Users/rubenalmeida/TV Shows/', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()