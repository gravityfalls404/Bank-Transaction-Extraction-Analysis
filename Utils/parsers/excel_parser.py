from utils.parsers.file_parser import FileParser
import pandas as pd
class ExcelParser(FileParser):
    def __init__(self, file, filename):
        super.__init__(self, file, filename)

    def parse_file(self):
        self.parsed_text = pd.read_excel(self.file).fillna('').to_string(index=False)
        super().store_parsed_text()
        return self.parsed_text