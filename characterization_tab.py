import tkinter as tk
from tkinter import ttk

class CharacterizationTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setup_widgets()

    def setup_widgets(self):
        self.grid_columnconfigure(0, weight=1)

        # Frame for Imaging
        self.imaging_frame = self.create_label_frame("Imaging", 0, 0, 2)
        self.setup_imaging_widgets()

        # Frame for Elemental Analysis
        self.elemental_frame = self.create_label_frame("Elemental Analysis", 1, 0)
        self.setup_elemental_widgets()

        # Frame for Final Remarks
        self.final_frame = self.create_label_frame("Final Remarks", 2, 0)
        self.setup_final_widgets()

    def create_label_frame(self, text, row, col, colspan=1):
        frame = ttk.LabelFrame(self, text=text, padding=(20, 10))
        frame.grid(row=row, column=col, columnspan=colspan, padx=10, pady=10, sticky="nsew")
        return frame

    def create_label_and_spinbox(self, parent, label_text, row, col, col2=None, increment=0.1, from_=0.0, to=99.9, width=4):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=col, padx=5, pady=(0, 10), sticky="w")
        spinbox = ttk.Spinbox(parent, from_=from_, to=to, increment=increment, width=width)
        col2 = col2 if col2 is not None else col + 1
        spinbox.grid(row=row, column=col2, padx=5, pady=10, sticky="ew")
        return label, spinbox

    def create_label_and_combobox(self, parent, label_text, values, row, col, col2=None):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=col, padx=5, pady=(0, 10), sticky="w")
        combobox_var = tk.StringVar()
        combobox = ttk.Combobox(parent, textvariable=combobox_var, values=values)
        col2 = col2 if col2 is not None else col + 1
        combobox.grid(row=row, column=col2, padx=5, pady=(0, 10), sticky="ew")
        return label, combobox

    def create_label_and_entry(self, parent, label_text, row, col, col2=None):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=col, padx=5, pady=(0, 10), sticky="w")
        entry = ttk.Entry(parent)
        col2 = col2 if col2 is not None else col + 1
        entry.grid(row=row, column=col2, padx=5, pady=(0, 10), sticky="ew")
        return label, entry

    def setup_imaging_widgets(self):
        # Size
        self.Size_label, self.Size = self.create_label_and_spinbox(self.imaging_frame, "Size (nm)", 0, 0)
        self.SizeSTD_label, self.SizeSTD = self.create_label_and_spinbox(self.imaging_frame, "\u00B1", 0, 2)

        # Dispersity
        self.Dispersity_label, self.Dispersity_combobox = self.create_label_and_combobox(
            self.imaging_frame, "Dispersity", ["Monodisperse", "Double population", "Polydisperse"], 1, 0
        )

    def setup_elemental_widgets(self):
        # Precursor
        self.Metal1_label, self.Metal1 = self.create_label_and_spinbox(self.elemental_frame, "Precursor (g/L)", 0, 0)

        # Dopants
        self.PrecursorDoping1Analysis_label, self.PrecursorDoping1Analysis = self.create_label_and_spinbox(self.elemental_frame, "Dopant 1 (g/L)", 1, 0)
        self.PrecursorDoping2Analysis_label, self.PrecursorDoping2Analysis = self.create_label_and_spinbox(self.elemental_frame, "Dopant 2 (g/L)", 2, 0)

    def setup_final_widgets(self):
        # Final Volume
        self.FinalVolume_label, self.FinalVolume = self.create_label_and_spinbox(
            self.final_frame, "Final Volume (mL)", 0, 0, increment=0.1, to=99999.9
        )

        # Precipitation
        self.Precipitation_label, self.Precipitation_combobox = self.create_label_and_combobox(
            self.final_frame, "Precipitation", ["Yes", "No"], 1, 0
        )

        # Concentration
        self.Concentration_label, self.Concentration_entry = self.create_label_and_entry(
            self.final_frame, "Concentration (M)", 2, 0
        )

