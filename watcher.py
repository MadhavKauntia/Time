import time
import pytesseract
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image

class Watcher:
    DIRECTORY_TO_WATCH = "/home/chaitanya/Pictures/"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            print("#STARTOFSNAP#")
            im = Image.open(event.src_path)
            new_size = tuple(2 * x for x in im.size)
            im = im.resize(new_size, Image.ANTIALIAS)
            print(pytesseract.image_to_string(im))
            print("#ENDOFSNAP#")


if __name__ == '__main__':
    w = Watcher()
    w.run()