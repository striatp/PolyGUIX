import tkinter
import customtkinter
from typing import List, Union

class MissingArgumentError(Exception):
  """Raised error for missing arguments."""
  pass

class PolyGUIX():
  def __init__(self, title: str = "My App", ) -> None:

    # im not done
