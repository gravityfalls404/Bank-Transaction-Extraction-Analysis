import pdf2image
import layoutparser as lp
import pytesseract
import numpy as np
import pandas as pd
import os
from utils.parsers.file_parser import FileParser
from utils.config import Config

class PdfParser(FileParser):
    def __init__(self, file, filename):
        super().__init__(file, filename)
        self.pdf_image = pdf2image.convert_from_path(os.path.join(Config.UPLOADED_FILE_PATH.value, filename))[0]
    
    def parse_file(self):
        model = lp.Detectron2LayoutModel('lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config',
                                 extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.5],
                                 label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"})
        layout_result = model.detect(self.pdf_image)

        pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # Adjust the path according to your installation

        # Filter for table blocks
        table_blocks = lp.Layout([b for b in layout_result if b.type == 'Table'])
        self.parsed_text = ''
        for table_block in table_blocks:
            # Extract the table image
            table_image = self.pdf_image.crop(table_block.coordinates)
            
            # Optionally use OCR to extract text from the table image
            self.parsed_text = pytesseract.image_to_string(table_image)

        super().store_parsed_text()
        return self.parsed_text
            
            