import tkinter as tk  # Import the standard Tkinter library
from tkinter import ttk  # Import the themed Tkinter widgets
import openpyxl  # Library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files
from ttkbootstrap import Style  # Library to style Tkinter widgets
from intro_tab import IntroTab  # Import the IntroTab class from intro_tab.py
from synthesis_tab import SynthesisTab  # Import the SynthesisTab class from synthesis_tab.py
from characterization_tab import CharacterizationTab  # Import the CharacterizationTab class from characterization_tab.py
from save_export_tab import SaveExportTab  # Import the SaveExportTab class from save_export_tab.py
import os  # Import the OS library for interacting with the operating system
import sys  # Import the sys library to manipulate the Python runtime environment
from tkinter import PhotoImage  # Import the PhotoImage class to work with images

class App(ttk.Frame):
    def __init__(self, parent):
        # Initialize the parent class (ttk.Frame)
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        # Determine the path to the directory containing the executable or script
        if getattr(sys, 'frozen', False):
            # Running in a bundle (compiled with PyInstaller)
            base_path = sys._MEIPASS
        else:
            # Running in a normal Python environment
            base_path = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the Excel file
        excel_path = os.path.join(base_path, 'registration_data.xlsx')
        
        # Load the Excel workbook and select the active sheet
        self.wb = openpyxl.load_workbook(excel_path)
        self.sheet = self.wb.active
        
        # Extract values from column B, skipping the first row (header)
        self.column_list = [cell.value for cell in self.sheet['B'][1:]]
        
        # Setup the notebook (tabbed interface)
        self.setup_notebook()

    def setup_notebook(self):
        # Create a Notebook widget (for tabbed pages)
        self.notebook = ttk.Notebook(self)
        self.notebook.grid()  # Place the notebook in the grid layout

        # Initialize and add tabs to the notebook
        self.intro_tab = IntroTab(self.notebook, self.wb, self.sheet, self.column_list)
        self.characterization_tab = CharacterizationTab(self.notebook)
        self.synthesis_tab = SynthesisTab(self.notebook, self.characterization_tab)
        self.save_export_tab = SaveExportTab(self.notebook, self.wb, self.sheet, self.column_list, self.intro_tab)

        # Add tabs to the notebook with respective labels
        self.notebook.add(self.intro_tab, text="Intro")
        self.notebook.add(self.synthesis_tab, text="Synthesis")
        self.notebook.add(self.characterization_tab, text="Characterization")
        self.notebook.add(self.save_export_tab, text="Save & Export")

# Create the main tkinter window
root = tk.Tk()
root.title("NanoDB")  # Set the title of the window

# Use absolute path for the icon
current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, 'images', 'logo.png')
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(True, icon)  # Set the window icon

# Simply set the theme
style = Style(theme='darkly')

# Initialize the application class and place it in the main window
app = App(root)
app.grid()

# Set a minimum size for the window, and place it in the middle of the screen
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

# Start the Tkinter event loop
root.mainloop()
