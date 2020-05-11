#-*- coding: utf-8 -*-
"""Globals module.

Module for handling global references. Is used as a singleton
Todo:

@author:         Philipp Noertersheuser
@GIT Repository: https://github.com/dimentorium/PresetManager
@License
"""
from tkinter import Tk
from core.ui import main
#reference to root and view
root: Tk
main_window: main.main_view

#reference to folder where application is started from. Either script or exe
application_folder = ""
