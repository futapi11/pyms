import sys

from textual import on
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static, Label
from control import Control

class Filename(Static):
    def compose(self) -> ComposeResult:
        yield Label(str(sys.argv[1]))

class MusicControl(Static):

    def compose(self) -> ComposeResult:
        yield Button("<<", id="backward", variant="success")
        yield Button("||", id="playpause", variant="error")
        yield Button(">>", id="forward")


class MusicPlayer(App):

    CSS_PATH = "main.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"), 
                ('q', 'quit', 'quit'),
                ('p', 'toggle_play', 'play/pause'),
                ('f', 'forward', 'skip forward'),
                ('b', 'backward', 'skip backward')
               ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield ScrollableContainer(Filename(), MusicControl(), id='maincon')

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_quit(self) -> None:
        Control.quit()

    def action_toggle_play(self) -> None:
        Control.play_pause()
    
    def action_forward(self) -> None:
        Control.fast_forward()

    def action_backward(self) -> None:
        Control.rewind()

    @on(Button.Pressed, '#backward')
    def backward(self):
        Control.rewind()

    @on(Button.Pressed, '#playpause')
    def playpause(self):
        Control.play_pause()

    @on(Button.Pressed, '#forward')
    def Fast_Forward(self):
        Control.fast_forward()
