import tkinter
import customtkinter
from typing import List, Union

class MissingArgumentError(Exception):
    """Raised error for missing arguments."""
    pass

class PolyGUIX():
    def __init__(self, title: str = "My App", width: int = 200, height: int = 200, position_x: int = 0, position_y: int = 0) -> None:

      # currently working on arguments for the init. 
