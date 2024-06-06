import os
from enum import Enum

class Config(Enum):
    """
    Enum class to store all the configuration variables along with storage paths.
    """
    MAX_FILE_SIZE = 3 # Maximum size of a file that can be uploaded on a streamlit server.
    SUPPORTED_FILE_TYPES = ["pdf", "docx", "xlsx"] # List of supported file types for bank statements.

    UPLOADED_FILE_PATH = os.path.join("files", "statements") #Path to store the statements uploaded to the API.
    CLASSIFIED_FILE_PATH = os.path.join("files", "classified") #Path to store the parsed and classified statements.
    RAW_FILE_PATH = os.path.join("files", "raw_files") #Path to store the raw statements uploaded to the API.
    PROPMPT_FILE_PATH = os.path.join("files", "prompt.txt") #Path to the custamized prompt file for the LLM
    
class FileType(Enum):
    """
        Enum class representing a file type.
    """
    PDF = "pdf"
    DOCX = "docx"
    XLSX = "xlsx"
