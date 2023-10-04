from random import randint
from asciimatics.screen import Screen
def demo(screen):
    while True:
        screen.print_at('Hello World!',
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours -1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()


from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene

def demo2(screen):
    effects = [
            Cycle(
                screen,
                FigletText("SHADOWRUN 5E", font='big'),
                int(screen.height / 3 - 8)
                ),
            Cycle(
                screen,
                FigletText("CHARGEN", font='big'),
                int(screen.height / 2 + 3)
                )
            ]
    screen.play([Scene(effects, 500)])

from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text
from asciimatics.widgets import Button, TextBox, Widget
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys

class CharacterView(Frame):
    def __init__(self, screen, model):
        super(CharacterView, self).__init__(screen,
                                            screen.height * 2 // 3,
                                            screen.width * 2 // 3,
                                            hover_focus=True,
                                            can_scroll=False,
                                            title="Shadowrun 5E Character Gen",
                                            reduce_cpu=True)
        self._model = model

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Text("Name", model.Name))
        layout.add_widget(Text("Metatype", model.Name))
        layout.add_widget(TextBox(
            Widget.FILL_FRAME, "Notes:", "notes", as_string=True, line_wrap=True))
        layout2 = ([[1, 1, 1, 1]])
        self.add_layout(layout2)
        layout2.add_widget(Button("Ok", self._ok), 0)
        layout2.add_widget(Button("Cancel", self._cancel), 3)
        self.fix()

    def _reset(self):
        super(CharacterView, self).reset()
        self.data = model

    def _ok(self):
        self.save()
        self._model.update_currr



