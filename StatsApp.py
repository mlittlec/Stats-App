from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class StatsApp(App):
    """" A template Textual application to process our Usage Stats"""
    # pass

    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]

    def compose(self) -> ComposeResult:
        """Create Child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle daerk mode"""
        self.dark = not self.dark


if __name__ == "__main__":
    app = StatsApp()
    app.run()
