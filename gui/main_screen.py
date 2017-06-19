"""
Dit is het bestand voor het algemene scherm van de Agenda-App
Het heeft een aantal functies en dezen staat beschreven in de drive.

<LICENSE>
<COPYRIGHT NOTICE>
Animajosser <Animajosser@gmail.com>
"""
__version__="0.5"
__date__="19-06-2017"
__kivyversion__="1.10.0"
__pythonversion__="3.6.1"
##############################################################################################

# imports #

# Most important
print("Importing Kivy")
import kivy
print("Checking kivy-version")
kivy.require('1.10.0')
print("Importing App")
from kivy.app import App
print("Importing config and disabling multitouch")
from kivy.config import Config
Config.set("input", "mouse", "mouse,disable_multitouch")
#print("Importing Window")
#from kivy.core.window import Window
print("Importing Builder")
from kivy.lang.builder import Builder
print("Importing Properties")
from kivy.properties import ObjectProperty

# Layouts
print("Importing BoxLayout")
from kivy.uix.boxlayout import BoxLayout
#print("Importing StackLayout")
#from kivy.uix.stacklayout import StackLayout
print("Importing TabbedPanel")
from kivy.uix.tabbedpanel import TabbedPanelItem, TabbedPanel


# Attributes
#print("Importing Button")
#from kivy.uix.button import Button
#print("Importing TextInput")
#from kivy.uix.textinput import TextInput
#print("Importing CheckBox")
#from kivy.uix.checkbox import CheckBox
print("Importing Label")
from kivy.uix.label import Label

# popups
print("Importing Popup")
from kivy.uix.popup import Popup

# kv's
print("Load kv File Home Screen")
Builder.load_file('main_screen.kv')

# python modules

print("Importing Time")
import time

print("Start Program")

# Classes #

# Main widgets

"""TODO?:
After deleting a tab the width isn't updated sometimes
When there is no tab left, the last tab stays visible and 
clickable, resulting in an AttributeError
"""

class CreditsPopup(Popup):
    pass

class CreateNewAppointment(TabbedPanelItem):
    def close_tab(self):
        # close procedure
        self.parent.remove_widget(self.parent.parent.parent.parent.current_tab)

class RecycleBin(TabbedPanelItem):
    def close_tab(self):
        # close procedure
        self.parent.remove_widget(self.parent.parent.parent.parent.current_tab)

class Appointment(TabbedPanelItem):
    def close_tab(self):
        # close procedure
        self.parent.remove_widget(self.parent.parent.parent.parent.current_tab)

class ProgramSettings(TabbedPanelItem):
    def close_tab(self):
        # close procedure
        self.parent.remove_widget(self.parent.parent.parent.parent.current_tab)

class BaseScreen(BoxLayout):
    creditspopup = CreditsPopup()
    tabsscreens_op = ObjectProperty(None)

    def open_new_tab(self, name):
        """This opens a new tab in de tab side"""

        present = False

        if name == "create_appointment":
            self.tabsscreens_op.add_widget(CreateNewAppointment())
        elif name=="trash":
            for a in self.tabsscreens_op.tab_list:
                if "RecycleBin" in str(a):
                    self.tabsscreens_op.switch_to(RecycleBin())
                    present=True
                    break
            if not present:
                self.tabsscreens_op.add_widget(RecycleBin())
        elif name=="settings":
            for a in self.tabsscreens_op.tab_list:
                if "ProgramSettings" in str(a):
                    self.tabsscreens_op.switch_to(ProgramSettings())
                    present=True
                    break
            if not present:
                self.tabsscreens_op.add_widget(ProgramSettings())
        else:
            print("Can't find tab: ", name)

    def close_tab(self):
        self.tabsscreens_op.remove_widget(self.tabsscreens_op.current_tab)

# Screens

class AgendaApp(App):
    """Home class and home screen"""

    icon = 'icon.ico'
    title = 'Agenda App'

    def build(self):

        return BaseScreen()

    # Easter Egg
    """TODO?:
    This is quite buggy, but I just had to make an easter egg
    Sometimes a click isn't forgotten or when you click a dropdown,
    it stays clicked resulting in an easter egg, when released
    """
    t0 = False
    easter_egg = Popup(
        size_hint=(.75, .75), auto_dismiss=True,
        title="Pieter rookt peukjes",
        content=Label(text="Roken is heel ongezond\n Doo Da Doo Da"))
    def start_measure_time(self):
        self.t0 = time.time()
    def stop_measure_time(self):
        if self.t0:
            t1 = time.time()
            time_used=t1-self.t0
            if time_used>=5:
                self.easter_egg.open()
                self.t0=False


# Script

if __name__=='__main__':
    AgendaApp().run()