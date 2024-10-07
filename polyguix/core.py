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
        
        # Ensure the always_on_top parameter is valid
        valid_states = ["normal", "iconic", "zoomed"]
        if always_on_top not in valid_states:
            raise InvalidWindowStateError(f"Invalid window state: {always_on_top}. Choose from {valid_states}.")
        
        # Determine whether to use CustomTkinter or Tkinter
        if use_customtk:
            ctk.set_default_color_theme(ctk_theme)
            ctk.set_appearance_mode(ctk_appearance_mode)
            self.app = ctk.CTkToplevel(parent) if parent else ctk.CTk()
        else:
            self.app = tk.Toplevel(parent) if parent else tk.Tk()
        
        # Set title and geometry
        self.app.title(title)
        self.app.geometry(f"{width}x{height}+{position_x}+{position_y}")
        
        # Set window state (normal, iconic, zoomed)
        self.app.state(always_on_top)
        
        # Set minimum window size if provided
        if min_size:
            min_width, min_height = min_size
            self.app.minsize(min_width, min_height)
        
        # Set fullscreen mode
        if fullscreen_mode:
            self.app.attributes("-fullscreen", True)
        
        # Set window resizability
        self.app.resizable(resizable[0], resizable[1])  # resizable = (horizontal, vertical)
        
        # Set window transparency
        if 0 <= transparency <= 1:
            self.app.attributes("-alpha", transparency)
        
        # Set window icon (only works with .ico files for Tkinter)
        if window_icon:
            self.app.iconbitmap(window_icon)
        
        # CustomTkinter background color
        if use_customtk and ctk_bg_color:
            self.app.configure(bg=ctk_bg_color)
        
        # Store the values in the instance
        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y
        self.min_size = min_size
        self.title = title
        self.always_on_top = always_on_top
        self.fullscreen_mode = fullscreen_mode
        self.resizable = resizable
        self.transparency = transparency
        self.window_icon = window_icon
        self.ctk_theme = ctk_theme
        self.ctk_appearance_mode = ctk_appearance_mode
        self.ctk_bg_color = ctk_bg_color
        
    def run(self):
        """Run the main event loop."""
        self.app.mainloop()

# i might have cooked, not sure tho. will test it later
