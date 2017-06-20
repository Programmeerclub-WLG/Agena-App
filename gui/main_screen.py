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
#print("Importing Kivy")
import kivy
#print("Checking kivy-version")
kivy.require('1.10.0')

#print("Importing App")
from kivy.app import App

#print("Importing config and disabling multitouch")
from kivy.config import Config
Config.set("input", "mouse", "mouse,disable_multitouch")

#print("Importing Builder")
from kivy.lang.builder import Builder
#print("Importing Properties")
from kivy.properties import ObjectProperty

# Layouts
#print("Importing BoxLayout")
from kivy.uix.boxlayout import BoxLayout
#print("Importing TabbedPanel")
from kivy.uix.tabbedpanel import TabbedPanelItem, TabbedPanel


# Attributes
#print("Importing Label")
from kivy.uix.label import Label
#print("Importing Popup")
from kivy.uix.popup import Popup

# kv's
#print("Load kv File Home Screen")
Builder.load_file('main_screen.kv')

#print("Start Program")

# Classes #

# Main widgets

"""TODO?:
After deleting a tab the width isn't updated.
Sometimes, when there is no tab left, the last tab
stays visible and clickable, resulting in an AttributeError.
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


# Script

if __name__=='__main__':
    AgendaApp().run()