from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, Button, TextBox, Widget
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import char_shadowrun_5e as Chargen
import sys


class ContactModel():
    def __init__(self):
        self.ch, self.nuyen, self.karma_log = Chargen.generate_character()
        self.current_id = None

    def get_summary(self):
        return Chargen.print_shit(self.ch, self.nuyen, self.karma_log)

    def get_skills(self):
        return Chargen.format_skills(self.ch)

    def get_gear(self):
        return Chargen.format_gear(self.ch)

    def get_qualities(self):
        return Chargen.format_qualities(self.ch)

    def get_attributes(self):
        return Chargen.format_attributes(self.ch)


class ListView(Frame):
    def __init__(self, screen, model):
        super(ListView, self).__init__(screen,
                                       screen.height * 2 // 3,
                                       screen.width * 2 // 3,
                                       on_load=self._reload_list,
                                       hover_focus=True,
                                       can_scroll=False,
                                       title="Shadowrun Chargen")

        self._model = model

        self._list_view = ListBox(
            Widget.FILL_FRAME,
            model.get_summary(),
            name="character",
            on_select=self._skills)
        self._skills_button = Button("Skills", self._skills)
        self._attrs_button = Button("Attributes", self._attrs)
        layout=Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Qualities", self._qualities), 0)
        layout2.add_widget(self._skills_button, 1)
        layout2.add_widget(self._attrs_button, 2)
        layout2.add_widget(Button("Quit", self._quit), 3)
        self.fix()

    def _reload_list(self, new_value=None):
        self._list_view.options = self._model.get_summary()
        self._list_view.value = new_value

    def _skills(self):
        self._model.current_id = None
        raise NextScene("Skills Screen")

    def _qualities(self):
        self._model.current_id = None
        raise NextScene("Qualities Screen")

    def _attrs(self):
        self._model.current_id = None
        raise NextScene("Attributes Screen")

    @staticmethod
    def _quit():
        raise StopApplication("User Pressed Quit")


class ContactView(Frame):
    def __init__(self, screen, model):
        super(ContactView, self).__init__(screen,
                                          screen.height * 2 // 3,
                                          screen.width * 2 // 3,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Contact Details",
                                          reduce_cpu=True)
        # Save off the model that accesses the contacts database.
        self._model = model

        # Create the form for displaying the list of contacts.
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Text("Name:", "name"))
        layout.add_widget(Text("Address:", "address"))
        layout.add_widget(Text("Phone number:", "phone"))
        layout.add_widget(Text("Email address:", "email"))
        layout.add_widget(TextBox(
            Widget.FILL_FRAME, "Notes:", "notes", as_string=True, line_wrap=True))
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("OK", self._ok), 0)
        layout2.add_widget(Button("Cancel", self._cancel), 3)
        self.fix()

    def reset(self):
        # Do standard reset to clear out form, then populate with new data.
        super(ContactView, self).reset()

    def _ok(self):
        self.save()
        self._model.get_skills(self.data)
        raise NextScene("Main")

    @staticmethod
    def _cancel():
        raise NextScene("Main")


def demo(screen, scene):
    scenes = [
        Scene([ListView(screen, contacts)], -1, name="Main"),
        Scene([ContactView(screen, contacts)], -1, name="Skills Screen"),
        Scene([ContactView(screen, contacts)], -1, name="Attributes Screen"),
        Scene([ContactView(screen, contacts)], -1, name="Qualities Screen"),
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)


contacts = ContactModel()
last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
