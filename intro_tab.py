from logging import root  # Import the root logger (not used in this code)
import tkinter as tk  # Import the standard Tkinter library
from tkinter import ttk  # Import the themed Tkinter widgets
import ttkbootstrap as ttk  # Import ttkbootstrap for themed widgets
from ttkbootstrap import Style  # Import the Style class from ttkbootstrap
from ttkbootstrap.widgets import DateEntry  # Import the DateEntry widget for date selection
import os  # Import the OS library for interacting with the operating system
import sys  # Import the sys library to manipulate the Python runtime environment

def get_resource_path(relative_path):
    """Get the absolute path to a resource, works for both development and PyInstaller."""
    try:
        base_path = sys._MEIPASS  # Base path for PyInstaller bundle
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))  # Base path for normal Python environment
    return os.path.join(base_path, relative_path)

class IntroTab(ttk.Frame):
    def __init__(self, parent, wb, sheet, column_list):
        """Initialize the IntroTab with the parent notebook, workbook, sheet, and column list."""
        super().__init__(parent)
        self.parent = parent
        self.wb = wb
        self.sheet = sheet
        self.column_list = column_list

        # Setup the widgets in the tab
        self.setup_widgets()

    def setup_widgets(self):
        """Setup the widgets in the Intro tab."""
        # Frame for the Intro section
        self.Intro_frame = ttk.LabelFrame(self, text="Intro", padding=(20, 20))
        self.Intro_frame.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
        # Frame for the Storage notes section
        self.Storage_frame = ttk.LabelFrame(self, text="Storage notes", padding=(20, 20))
        self.Storage_frame.grid(row=5, column=0, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
        # Configure grid weights to make the layout responsive
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Logo
        photo_path = get_resource_path('images/logo.png')
        photo = tk.PhotoImage(file=photo_path)
        label = ttk.Label(self, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.grid(row=0, column=0, columnspan=2, padx=(50, 50), pady=(50, 50), sticky="nsew")

        # Search Area
        self.search_label = ttk.Label(self, text="Search the *Sample* name if you want to edit a previous entry")
        self.search_label.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="e")
        
        self.Search_entry = ttk.Entry(self)
        self.Search_entry.grid(row=1, column=1, padx=20, pady=(0, 10), sticky="w")
        self.Search_entry.bind("<Key>", self.check)  # Bind key press to the check method

        self.Search_list = tk.Listbox(self)
        self.Search_list.grid(row=3, column=0, columnspan=2, padx=20, pady=(0, 10), sticky="nsew")
        self.Search_list.bind("<ButtonRelease-1>", self.fillout)  # Bind mouse click to the fillout method

        # Sample Name Input
        self.SampleName_label = ttk.Label(self.Intro_frame, text="Sample Name")
        self.SampleName_label.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="w")
        self.SampleName_entry = ttk.Entry(self.Intro_frame)
        self.SampleName_entry.grid(row=0, column=1, padx=5, pady=(0, 10), sticky="nsew")
        self.SampleName_entry.bind("<FocusOut>", self.show_warning_if_duplicate)  # Check on focus out
        self.SampleName_entry.bind("<KeyRelease>", self.show_warning_if_duplicate)  # Check on key release
        
        # Label for warning message
        self.warning_message = ttk.Label(self.Intro_frame, text="", foreground="orange")
        self.warning_message.grid(row=1, column=0, columnspan=2, padx=5, pady=(0, 10), sticky="w")

        # Availability Input
        self.Availability_label = ttk.Label(self.Intro_frame, text="Is the sample available in the lab?")
        self.Availability_label.grid(row=0, column=2, padx=5, pady=(10, 10), sticky="w")
        self.Availability_var = tk.StringVar()
        self.Availability_combobox = ttk.Combobox(
            self.Intro_frame,
            textvariable=self.Availability_var,
            values=["Yes", "No​"])     
        self.Availability_combobox.grid(row=0, column=3, padx=5, pady=(10, 10), sticky="ew")

        # Date Input
        self.SynthesisDate_label = ttk.Label(self.Intro_frame, text="Synthesis Date")
        self.SynthesisDate_label.grid(row=0, column=4, padx=5, pady=(10, 10), sticky="w")
        self.SynthesisDate_entry = DateEntry(self.Intro_frame)
        self.SynthesisDate_entry.grid(row=0, column=5, padx=5, pady=(10, 10), sticky="nsew")
        
        # Separator
        separator = ttk.Separator(self.Intro_frame, orient='vertical')
        separator.grid(row=0, column=6, padx=75)

        # User Name Input
        self.UserName_label = ttk.Label(self.Intro_frame, text="Name Surname")
        self.UserName_label.grid(row=0, column=7, padx=5, pady=(0, 10), sticky="w")
        self.UserName_entry = ttk.Entry(self.Intro_frame)
        self.UserName_entry.grid(row=0, column=8, padx=5, pady=(0, 10), sticky="nsew")

        # Storage Comments
        self.Comment_text = tk.Text(self.Storage_frame, width=1, height=3)
        self.Comment_text.grid(row=1, column=0, columnspan=2, padx=5, pady=(0, 10), sticky="nsew")
        self.Storage_frame.columnconfigure(1, weight=1)

    def show_warning_if_duplicate(self, event):
        """Show a warning message if the sample name is already in use."""
        sample_name = self.SampleName_entry.get().strip().lower()  # Convert input to lowercase
        
        # Check if self.column_list is None and initialize it if necessary
        if self.column_list is None:
            self.column_list = []

        # Filter out None values and convert to lowercase
        column_list_lower = [name.lower() for name in self.column_list if name is not None]

        if sample_name in column_list_lower:
            self.warning_message.config(text="Sample name already in use! Careful.")
        else:
            self.warning_message.config(text="")  # Clear the message if no duplicate

    def update(self, data):
        """Update the search list with new data."""
        self.Search_list.delete(0, tk.END)
        for item in data:
            self.Search_list.insert(tk.END, item)

    def check(self, event):
        """Check the search entry and update the search list based on the input."""
        typed = self.Search_entry.get().lower()
        if not typed:
            data = self.column_list
        else:
            data = [item for item in self.column_list if item.lower().startswith(typed)]
        self.update(data)

    def fillout(self, event):
        """Fill out the form with data from the selected item in the search list."""
        selected_item = self.Search_list.get(tk.ANCHOR)
        if selected_item:
            row_index = self.column_list.index(selected_item) + 2
            # Clear all values
            self.Comment_text.delete("1.0", tk.END)
            self.SampleName_entry.delete(0, tk.END)
            self.Availability_combobox.set("")
            self.SynthesisDate_entry.entry.delete(0, tk.END)    
            self.UserName_entry.delete(0, tk.END)
            
            # Insert new values
            Comment_value = self.sheet.cell(row=row_index, column=50).value
            self.Comment_text.insert("1.0", str(Comment_value or ""))
            self.Availability_combobox.set(str(self.sheet.cell(row=row_index, column=3).value))
            self.SynthesisDate_entry.entry.insert(0, self.sheet.cell(row=row_index, column=4).value) 
            SampleName_value = self.sheet.cell(row=row_index, column=2).value
            self.SampleName_entry.insert(0, str(SampleName_value or ""))
            UserName_value = self.sheet.cell(row=row_index, column=5).value
            self.UserName_entry.insert(0, str(UserName_value or ""))

            # Fill Synthesis Tab Data
            synthesis_tab = self.parent.master.synthesis_tab
            # Clear all values in the Synthesis tab
            synthesis_tab.PrecursorVolume_entry.delete(0, tk.END)
            synthesis_tab.Precursor2Weight_entry.delete(0, tk.END)
            synthesis_tab.Precursor3Weight_entry.delete(0, tk.END)
            synthesis_tab.PrecursorDoping1Mass_entry.delete(0, tk.END)
            synthesis_tab.PrecursorDoping2Mass_entry.delete(0, tk.END)
            synthesis_tab.agentMass_entry.delete(0, tk.END)
            synthesis_tab.SilverMass_entry.delete(0, tk.END)
            synthesis_tab.GoldMass_entry.delete(0, tk.END)
            synthesis_tab.PrecipitatingCycles.delete(0, tk.END)
            synthesis_tab.PrecipitatingSpeed_entry.delete(0, tk.END)
            synthesis_tab.CyclesTime_entry.delete(0, tk.END)
            synthesis_tab.Precursor_combobox.set("")
            synthesis_tab.Precursorcheck_combobox.set("")
            synthesis_tab.PrecursorDoping1_combobox.set("")
            synthesis_tab.PrecursorDoping2_combobox.set("")
            synthesis_tab.PrecursorDoping1Name_combobox.set("")
            synthesis_tab.PrecursorDoping2Name_combobox.set("")
            synthesis_tab.agent_combobox.set("")

            # Insert new values in the Synthesis tab
            synthesis_tab.Precursor_combobox.set(str(self.sheet.cell(row=row_index, column=6).value))
            synthesis_tab.Precursorcheck_combobox.set(str(self.sheet.cell(row=row_index, column=7).value))
            synthesis_tab.PrecursorDoping1_combobox.set(str(self.sheet.cell(row=row_index, column=8).value))
            synthesis_tab.PrecursorDoping2_combobox.set(str(self.sheet.cell(row=row_index, column=9).value))
            synthesis_tab.PrecursorDoping1Name_combobox.set(str(self.sheet.cell(row=row_index, column=10).value))
            synthesis_tab.PrecursorDoping2Name_combobox.set(str(self.sheet.cell(row=row_index, column=11).value))
            synthesis_tab.agent_combobox.set(str(self.sheet.cell(row=row_index, column=12).value))
            PrecursorVolume_value = self.sheet.cell(row=row_index, column=13).value
            Precursor2Weight_value = self.sheet.cell(row=row_index, column=14).value
            Precursor3Weight_value = self.sheet.cell(row=row_index, column=15).value
            PrecursorDoping1Mass_value = self.sheet.cell(row=row_index, column=16).value
            PrecursorDoping2Mass_value = self.sheet.cell(row=row_index, column=17).value
            agentMass_value = self.sheet.cell(row=row_index, column=18).value
            SilverMass_value = self.sheet.cell(row=row_index, column=19).value
            GoldMass_value = self.sheet.cell(row=row_index, column=20).value
            PrecipitatingCycles_value = self.sheet.cell(row=row_index, column=22).value
            PrecipitatingSpeed_value = self.sheet.cell(row=row_index, column=23).value
            CyclesTime_value = self.sheet.cell(row=row_index, column=24).value
            synthesis_tab.PrecursorVolume_entry.insert(0, str(PrecursorVolume_value or ""))
            synthesis_tab.Precursor2Weight_entry.insert(0, str(Precursor2Weight_value or ""))
            synthesis_tab.Precursor3Weight_entry.insert(0, str(Precursor3Weight_value or ""))
            synthesis_tab.PrecursorDoping1Mass_entry.insert(0, str(PrecursorDoping1Mass_value or ""))
            synthesis_tab.PrecursorDoping2Mass_entry.insert(0, str(PrecursorDoping2Mass_value or ""))
            synthesis_tab.agentMass_entry.insert(0, str(agentMass_value or ""))
            synthesis_tab.SilverMass_entry.insert(0, str(SilverMass_value or ""))
            synthesis_tab.GoldMass_entry.insert(0, str(GoldMass_value or ""))
            synthesis_tab.PrecipitatingCycles.insert(0, str(PrecipitatingCycles_value or ""))
            synthesis_tab.PrecipitatingSpeed_entry.insert(0, str(PrecipitatingSpeed_value or ""))
            synthesis_tab.CyclesTime_entry.insert(0, str(CyclesTime_value or ""))

            # Fill Characterization Tab Data
            characterization_tab = self.parent.master.characterization_tab
            # Clear all values in the Characterization tab
            characterization_tab.Dispersity_combobox.set("")
            characterization_tab.Precipitation_combobox.set("")
            characterization_tab.Concentration_entry.delete(0, tk.END)
            characterization_tab.Size.delete(0, tk.END)
            characterization_tab.SizeSTD.delete(0, tk.END)
            characterization_tab.Metal1.delete(0, tk.END)
            characterization_tab.PrecursorDoping1Analysis.delete(0, tk.END)
            characterization_tab.PrecursorDoping2Analysis.delete(0, tk.END)
            characterization_tab.FinalVolume.delete(0, tk.END)

            # Insert new values in the Characterization tab
            characterization_tab.Dispersity_combobox.set(str(self.sheet.cell(row=row_index, column=27).value))
            characterization_tab.Precipitation_combobox.set(str(self.sheet.cell(row=row_index, column=32).value))
            Concentration_value = self.sheet.cell(row=row_index, column=33).value   
            Size_value = self.sheet.cell(row=row_index, column=25).value
            SizeSTD_value = self.sheet.cell(row=row_index, column=26).value
            Metal1_value = self.sheet.cell(row=row_index, column=28).value
            PrecursorDoping1Analysis_value = self.sheet.cell(row=row_index, column=29).value
            PrecursorDoping2Analysis_value = self.sheet.cell(row=row_index, column=30).value
            FinalVolume_value = self.sheet.cell(row=row_index, column=31).value
            characterization_tab.Size.insert(0, str(Size_value or ""))
            characterization_tab.SizeSTD.insert(0, str(SizeSTD_value or ""))
            characterization_tab.Metal1.insert(0, str(Metal1_value or ""))
            characterization_tab.PrecursorDoping1Analysis.insert(0, str(PrecursorDoping1Analysis_value or ""))
            characterization_tab.PrecursorDoping2Analysis.insert(0, str(PrecursorDoping2Analysis_value or ""))
            characterization_tab.FinalVolume.insert(0, str(FinalVolume_value or ""))
            characterization_tab.Concentration_entry.insert(0, str(Concentration_value or ""))
