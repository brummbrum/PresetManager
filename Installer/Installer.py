from tkinter import *
from tkinter.ttk import *
from tkinter.constants import DISABLED, GROOVE, NORMAL
from tkinter import simpledialog, filedialog
import core.globals as glob
import os
import ctypes
from Steps.install_python import install_python
from Steps.install_reapy import install_reapy
from Steps.install_welcome import install_welcome
from Steps.install_presetmanager import install_presetmanager
from Steps.install_finished import install_finished
import logging

class Wizard():
    def __init__(self):
        self.root = Tk()
        self.root.title("Preset Manager Installer")

        self.current_step = None
        
        self.content_frame = Frame(self.root, relief=GROOVE, padding=5)
        self.content_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        self.button_frame = Frame(self.root, padding=5)
        self.back_button = Button(self.button_frame, text="<< Back", command=self.back)
        self.back_button.pack(side=LEFT, padx=5, pady=5)
        self.next_button = Button(self.button_frame, text="Next >>", command=self.next)
        self.next_button.pack(side=LEFT, padx=5, pady=5)
        self.finish_button = Button(self.button_frame, text="Finish", command=self.finish)
        self.finish_button.pack(side=LEFT, padx=5, pady=5)
        self.button_frame.grid(row=1, column=1, sticky="se")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.steps = [install_welcome, install_python, install_reapy, install_presetmanager, install_finished]
        self.show_step(0)

        # Gets the requested values of the height and widht.
        windowWidth = 640
        windowHeight = 480
        self.root.minsize(windowWidth, 480)
        print("Width",windowWidth,"Height",windowHeight)
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.root.winfo_screenheight()/2 - windowHeight/2)
        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(positionRight, positionDown))

        logging.debug("Starting Main Loop")
        self.root.mainloop()

    def show_step(self, step):
        if self.current_step is not None:
            # remove current step
            self.current_step.pack_forget()

        self.step_no = step
        self.current_step = self.steps[step](self.content_frame)
        logging.debug("Current Step: " + str(type(self.current_step)))
        self.current_step.pack(fill="both", expand=True)
        
        if step == 0:
            # first step
            self.back_button["state"] = DISABLED
            self.next_button["state"] = NORMAL
            self.finish_button["state"] = DISABLED

        elif step == len(self.steps)-1:
            # last step
            self.back_button["state"] = NORMAL
            self.next_button["state"] = DISABLED
            self.finish_button["state"] = NORMAL

        else:
            # all other steps
            self.back_button["state"] = NORMAL
            self.next_button["state"] = NORMAL
            self.finish_button["state"] = DISABLED

    def next(self):
        try:
            logging.debug("Performing Action: " + str(type(self.current_step)))
            self.current_step.perform_action()
            self.show_step(self.step_no + 1)
        except Exception as e:
            logging.debug("Error: " + str(e))

    def back(self):
        logging.debug("Stepping Back")
        self.show_step(self.step_no - 1)

    def finish(self):
        logging.debug("Closing Installer")
        self.root.quit()
        self.root.destroy()


if __name__ == '__main__':
    logging.basicConfig(filename='installer.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)

    logging.debug('Starting Preset manager Installer, V0.3.0, 17.05.2020')

    logging.debug('Setting Application Folder: ' + os.path.dirname(os.path.realpath(__file__)))
    glob.set_application_folder(os.path.dirname(os.path.realpath(__file__)))

    #check if application is started with admin privileges
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if is_admin:
        logging.debug('User has admin privileges')
        logging.debug('Starting UI')
        wiz = Wizard()
        logging.debug("Installer finished")
    else:
        logging.debug('User does not have admin privileges')
        simpledialog.messagebox.showinfo("Warning", "This installer needs admin privileges. Please right-click exe and select: Run as Admin")
        logging.debug("Installer cancelled")
    