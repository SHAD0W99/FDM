#!/usr/bin/env python3

import requests

class FileDownloader:

    def __init__(self, fileURL, filePath):
        self.fileURL = fileURL
        self.filePath = filePath
        self.status = None
        self.chunk_size = 1023 * 1023 
    
    def start(self):
       response = requests.get(self.fileURL, stream=True) 
       handle = open(self.filePath, "wb")
       for chunk in response.iter_content(chunk_size=self.chunk_size):
           if chunk:
               handle.write(chunk)



