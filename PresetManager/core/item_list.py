# -*- coding: utf-8 -*-
"""Item List module.

Module for handling the list of all items. Is used as a singleton

Functions
initialized: Shows if database has been initialized and ca be used

Todo:

@author:         Philipp Noertersheuser
@GIT Repository: https://github.com/dimentorium/PresetManager
@License
"""

import os
import pickle
import core.globals as glob
import core.items as items

__DATABASE_FILE = ""
__ITEMS = {}
__INITIALIZED = False

def initialized() -> bool:
    """Check if database is initialized.

    Reads variable to make sure the database can be used and accessed
    """
    return __INITIALIZED

def new(filepath: str):
    """Create New Database.

    Creates new empty database
    """
    global __ITEMS
    __ITEMS = {}
    set_file_path(filepath)
    global __INITIALIZED
    __INITIALIZED = True
    save()

def file_path() -> str:
    """File Path.

    Returns filepath of database
    """
    global __DATABASE_FILE
    return __DATABASE_FILE

def set_file_path(filepath: str):
    """Set Database File Path.

    Checks file path and ending and stores it
    """
    global __DATABASE_FILE
    db_folder, db_file = os.path.split(filepath)

    #check if file ends on .bin otherwise replace this
    base, ext = os.path.splitext(db_file)
    if ext != ".bin":
        ext = ".bin"

    __DATABASE_FILE = os.path.normpath(os.path.join(db_folder, base + ext))

def folder_name() -> str:
    """Return folder.

    Returns the folderpath where the database is located
    """
    global __DATABASE_FILE
    return os.path.split(__DATABASE_FILE)[0]

def file_name() -> str:
    """Return filename.

    Returns the filenam of the database
    """
    global __DATABASE_FILE
    return os.path.split(__DATABASE_FILE)[1]

def save():
    """Save database.

    Saves the complete database of presets into a binary file with pickle.
    """
    global __ITEMS
    pickle.dump(__ITEMS, open(file_path(), "wb"))

def load(filename):
    """Load database.

    Loads a database of presets from a binary file with pickle.
    User is asked for file where to load from
    """
    set_file_path(filename)
    global __ITEMS
    __ITEMS = pickle.load(open(filename, "rb"))
    global __INITIALIZED
    __INITIALIZED = True

def add(newitem):
    """Add item.

    Adds an itme to the list
    """
    global __ITEMS
    __ITEMS[newitem.preset_name] = newitem

def update(newitem):
    """Update item.

    Updates an item in the list
    """
    global __ITEMS
    __ITEMS[newitem.preset_name] = newitem

def get() -> dict:
    """Get all items.

    returns full list of items
    """
    global __ITEMS
    return __ITEMS
