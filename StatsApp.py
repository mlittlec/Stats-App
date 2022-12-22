from pathlib import Path

from rich.text import Text

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import (
    Header, 
    Footer, 
    Static,
)


class Notification(Static):
    def on_mount(self) -> None:
        self.set_timer(3, self.remove)

    def on_click(self) -> None:
        self.remove()

class StatsApp(App):
    """" A template Textual application to process our Usage Stats"""
    # pass

    TITLE = "OL Train Stats Reporter Demo"
    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode"), 
        ("ctrl+s", "app.screenshot()", "Screenshot"),
        Binding("ctrl+c,ctrl+q", "app.quit", "Quit", show=True)]

    def compose(self) -> ComposeResult:
        """Create Child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.dark = not self.dark

    def action_screenshot(self, filename: str | None = None, path: str = "./") -> None:
        """Save an SVG "screenshot". This action will save an SVG file containing the current contents of the screen.
        
        Args: 
            filename (str | None, optional): Filename of screenshot, or None to auto-generate.  Defaults to None.
            path (str, optional): Path to directory. Defaults to "./".
        """
        self.bell()
        path = self.save_screenshot(filename, path)
        message = Text.assemble("Screenshot saved to ", (f"'{path}'", "bold green"))
        self.add_note(message)
        self.screen.mount(Notification(message))


if __name__ == "__main__":
    app = StatsApp()
    app.run()
