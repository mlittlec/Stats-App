from textual.app import App, ComposeResult
from textual.widgets import Header


class StatsApp(App):
    # pass
    def compose(self) -> ComposeResult:
        yield Header()


if __name__ == "__main__":
    app = StatsApp()
    app.run()
