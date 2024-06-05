from enum import Enum

class Config(Enum):
    """
    Enum class to store all the configuration variables.
    """
    MAX_FILE_SIZE = 3 # Maximum size of a file that can be uploaded on a streamlit server.
    SUPPORTED_FILE_TYPES = ["pdf", "docx", "xlsx"] # List of supported file types for bank statements.
    