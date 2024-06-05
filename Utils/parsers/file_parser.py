import pandas as pd
from utils.config import Config
import os
class FileParser():
    def __init__(self, file, filename):
        self.file = file
        self.filename = filename
        self.parsed_text = None

    def store_parsed_text(self):
        
        with open(os.path.join(Config.RAW_FILE_PATH, self.filename+'.txt'), 'w') as f:
            f.write(self.parsed_text)
        


    