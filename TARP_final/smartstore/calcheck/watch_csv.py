# import os
# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
#
# from .views import upload_csv
#
# #watchdog function for running upload_csv every time csv file gets updated
# class MyHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         if event.src_path.endswith('.csv'):
#             print("CSV file modified!")
#             # Call the function in views.py that should be executed
#             # whenever the CSV file is updated
#
#
#
# if __name__ == "__main__":
#     event_handler = MyHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path='/path/to/directory/containing/csv', recursive=False)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()