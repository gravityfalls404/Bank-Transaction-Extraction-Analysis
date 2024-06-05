from utils.config import FileType
import os
from utils.parsers import *
from utils.config import Config

class Request:
    def __init__(self, file, filename):
        self.file = file
        self.filename = filename.split('.')[-1]
        self.file_type = self.get_file_type()
        self.raw_parsed_content = self.parse_file_and_store()

    def get_file_type(self) -> FileType:
        """Method to return type enum from config.FileType based on the extension"""
        file_extension = self.filename.split('.')[-1]
        types = {file_type.value: file_type for file_type in FileType}
        try:
            file_type = types[file_extension.lower()]
            return file_type
        except:
            raise TypeError("File type not supported!")

    def parse_file_and_store(self) -> str:
        """Maethod which uses one of the parsing classes to parse the self.file based on the file type"""
        if self.file_type == FileType.XLSX:
            parser = ExcelParser(self.file, self.filename)
        elif self.file_type == FileType.DOCX:
            parser = DocxParser(self.file, self.filename)
        elif self.file_type == FileType.PDF:
            parser = PdfParser(self.file, self.filename)
        else:
            raise TypeError("File type not supported!")
        parsed_text = parser.parse_file(self.file)

        with open(os.path.join(Config.RAW_FILE_PATH, self.filename+'.txt'), 'w') as f:
            f.write(parsed_text)

        return parsed_text

        