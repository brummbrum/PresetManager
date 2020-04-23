# -*- coding: utf-8 -*-
"""Render Module.

Functions to render files in Reaper

Functions
    set_output_path: Set render path of project in project file
    render_audio: perform rendering

Todo:

@author:         Philipp Noertersheuser
@GIT Repository: https://github.com/dimentorium/PresetManager
@License
"""
import reapy
import rpp
import os
import reaper.preset as rp
import time

def set_output_path(folder: str):
    """Set Render Path.

    Changes current project render path

    Parameters
    ----------
        folder: folder where to render audio

    """
    reapy.perform_action(40859)
    #reapy.open_project("C:\\Users\\phili\\Desktop\\PM\\PresetManager\\reaper\\renderproject.rpp")
    #reference to project
    #project = reapy.Project()
    #save project to not get the dialog
    #project.save()

    #open project file
    #project_file_path = project.path + "\\" + project.name
    project_file_path = "C:\\Users\\phili\\Desktop\\PM\\PresetManager\\reaper\\renderproject.rpp"
    project_file=open(project_file_path, "r+")
    file_content = rpp.loads(project_file.read())

    #change render file setting
    render_file = file_content.find("RENDER_FILE")
    render_file[1] = folder

    #empty file
    project_file.seek(0)
    project_file.truncate()

    #write new content
    rpp.dump(file_content,project_file)
    project_file.close()

    #reopen project to make changes effective
    reapy.open_project(project_file_path)

def render_audio(folder: str, preset_name: str, chunk) -> str:
    """Render Audio.

    Renders audio inside Reaper

    Parameters
    ----------
        folder: folder where to store audio
        preset_name: name of audio file


    Returns
    -------
    renderpath: full path to rendered audio

    """
    #set renderpath in project file
    renderpath = folder + "\\" + preset_name + ".mp3"
    set_output_path(renderpath)

    #set name of track,as rendering takes trackname for filename
    project = reapy.Project()
    vst_track = project.tracks[0]
    vst_track.name = preset_name

    #load preset to track 1
    project.select_all_tracks()
    rp.load(chunk)
    time.sleep(2)

    #save project so changes get updated
    project.save()

    project.select_all_tracks()

    #call render action by ID
    reapy.perform_action(42230)

    print("Finished Rendering")
    project.save()
    reapy.perform_action(40860)
    return renderpath