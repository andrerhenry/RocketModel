import sys
from pathlib import Path

def get_resource_path(relative_path: str) -> Path:
    """
    Get the absolute path to a resource. 
    Works for both development and PyInstaller.
    """
    # Determine the base path
    base_path = Path(sys._MEIPASS) if hasattr(sys, '_MEIPASS') else Path(__file__).parent

    # Construct the full path
    return base_path / relative_path
