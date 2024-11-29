import time, sys, os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class BotFileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.py'):
            logging.log(logging.INFO, f" File {event.src_path} changed\nRestarting bot...")
            os.execv(sys.executable, ['python'] + sys.argv)

def start_watchdog(path, bot):
    event_handler = BotFileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()

    try:
        while True:
            bot.getUpdates()
    except KeyboardInterrupt:
        observer.stop()
        sys.exit(1)
    observer.join()