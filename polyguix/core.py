import tkinter as tk
import customtkinter as ctk
from typing import Tuple, Optional, Union

class InvalidWindowStateError(Exception):
    """Raised when an invalid window state is provided."""
    pass

class PolyGUIX():
    def __init__(self, title: str = "My App", width: int = 200, height: int = 200,
                 position_x: int = 0, position_y: int = 0, min_size: Optional[Tuple[int, int]] = None,
                 always_on_top: str = "normal", fullscreen_mode: bool = False, resizable: Tuple[bool, bool] = (True, True),
                 transparency: float = 1.0, window_icon: Optional[str] = None, use_customtk: bool = False,
                 ctk_theme: str = "blue", ctk_appearance_mode: str = "light", ctk_bg_color: Optional[str] = None,
                 parent: Optional[Union[tk.Tk, tk.Toplevel]] = None) -> None:
        """
        Initialize the GUI window with the specified parameters.
        
        :param title: Title of the window.
        :param width: Width of the window.
        :param height: Height of the window.
        :param position_x: X position on the screen.
        :param position_y: Y position on the screen.
        :param min_size: Optional tuple for (min_width, min_height).
        :param always_on_top: "normal", "iconic", or "zoomed" to define the window state.
        :param fullscreen_mode: Boolean to enable fullscreen mode.
        :param resizable: Tuple of (horizontal, vertical) booleans for window resizability.
        :param transparency: Float between 0 (fully transparent) and 1 (opaque) for window transparency.
        :param window_icon: Path to the window icon (.ico file).
        :param use_customtk: Boolean to use CustomTkinter instead of Tkinter.
        :param ctk_theme: The CustomTkinter theme ("blue", "green", or "dark-blue").
        :param ctk_appearance_mode: The appearance mode for CustomTkinter ("light" or "dark").
        :param ctk_bg_color: CustomTkinter window background color (hex color string).
        :param parent: Parent window (None for root window, Toplevel for additional windows).
        """
# i might have cooked, not sure tho. will test it later
