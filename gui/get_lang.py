"""
Dit is het bestand voor krijgen en terugsturen van de talen
Het heeft een aantal functies en dezen staat beschreven in de drive.

<LICENSE>
<COPYRIGHT NOTICE>
Animajosser <Animajosser@gmail.com>
"""

__version__="0.2"
__date__="19-06-2017"
__pythonversion__="3.6.1"

########################################################################################################################

# imports

import os

# variables
tussenquotes=False
languages={}

needed_list=[
    "topbar_file",
    "topbar_settings",
    "topbar_credits",
    "topbar_create_appointment",
    "topbar_trash",
    "topbar_close",
    "credits_text",
    "credits_popup_title",
    "topbar_close_screen",
    "welcome_tab",
    "welcome_text",
    "create_appointment_tab",
    "recycle_bin_tab",
    "settings_tab",
    "close_tab",
]

# functions

def get_lang_from_file():
    """ This returns the language, read from the settings file """
    return "en"


def assign(line):
    """ this interprets a line from the langauge-file """
    further = False
    first = False
    name = ""
    key = ""
    for a in line:
        if a=="|":
            name=name[:-1]
            further=True
            first=True
        elif not further:
            name+=a
        elif further and first:
            first=False
        elif a=="\n":
            continue
        else:
            key+=a
    return name, key


def sort_out(line):
    """
    this pre-interprets lines the language file
    it keeps track of multiline texts, too
    """
    global tussenquotes
    global name
    global key

    if "#" not in line and line!="" and line!=" ":
        if '"""' in line:
            if not tussenquotes:
                tussenquotes=True
            else:
                tussenquotes=False
        if not tussenquotes and not '"""' in line:
            name, key=assign(line)
            languages[name]=key
            key = ""
            name = ""
        else:
            if tussenquotes:
                if '"""' in line:
                    name, key=assign(line.replace('"""', ""))
                    key+="\n"
                else:
                    key+=line
            else:
                key+=line.replace('"""', "")
                languages[name]=key
                key=""
                name=""


def language_request(text):
    """This function returns the requested text"""
    if text in languages:
        return languages[text]
    else:
        print("Illegal request:", text)
        return "N/A"


# script

language=get_lang_from_file()

file=open(os.path.join("lang", language+".lang"), mode="r")

for line in file:
    sort_out(line)

for a in needed_list:
    if a not in languages:
        print(a, "was'nt found in the file:", language+".lang")
        languages[a]="N/A"
