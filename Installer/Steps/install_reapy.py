from tkinter import *
from tkinter.ttk import *
from tkinter.constants import DISABLED, GROOVE, NORMAL
import core.globals as glob
import logging

class install_reapy(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        logging.debug("Starting Step: Install REAPY")

        header = Label(self, text="Install REAPY API in Reaper")
        header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        Separator(self, orient="horizontal").grid(row=1, columnspan=4, padx=5, pady=5, sticky='ew')

        #configure label and button to select Reaper Folder
        reapy_script_folder = glob.reaper_folder + "\\Python\\Reaper\\reapy\\reascripts\\enable_dist_api.py"
        self._lbl_reapy_script = Label(self, relief=GROOVE, text=reapy_script_folder)
        self._lbl_reapy_script.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

        Separator(self, orient="horizontal").grid(row=3, columnspan=4, padx=5, pady=5, sticky='ew')

        #configure label and button to select Reaper ini
        self._lbl_reaper_info = Label(self, text="""Instruction for installing REAPY:
                                                    1. Start Reaper
                                                    2. Menu => Options => Preferences
                                                    3. Goto Plugins => Reascript
                                                    4. Check "Enable Python"
                                                    5. Click Apply
                                                    =================================
                                                    6. Menu => Actions
                                                    7. Click "Show Actions List"
                                                    8. Click Button "Load" 
                                                    9. Open file from above
                                                    10. Click Button "Run"
                                                    11. Restart Reaper and click "Validate" Button
                                                    """)
        self._lbl_reaper_info.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        self.btn_validate = Button(self,text="Validate REAPY", command=self.validate)
        self.btn_validate.grid(row=5, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

    def perform_action(self):
        pass

    def validate(self):
        messagebox.showinfo("Restart Reaper", "Please make sure to restart REAPER before validating REAPY")
        logging.debug("Validating REAPY")
        try:
            import reapy
            test = reapy.get_ini_file()
            if test != "":
                reapy.show_console_message("Validation successfull")
                logging.debug("Validation successfull")
            else:
                messagebox.showerror('Failed', 'Could not validate REAPY')
                logging.debug('Failed', 'Could not validate REAPY')
        except Exception as e:
            messagebox.showerror('Failed', 'Could not validate REAPY')
            logging.debug("Error validating REAPY: " + str(e))
            
