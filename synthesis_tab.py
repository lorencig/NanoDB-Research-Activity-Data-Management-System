import tkinter as tk
from tkinter import ttk

class SynthesisTab(ttk.Frame):
    def __init__(self, parent, characterization_tab):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.characterization_tab = characterization_tab
        self.setup_widgets()

    def setup_widgets(self):
        # Configure grid weights
        #self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Frame for the Precursors
        self.synthesis_frame = ttk.LabelFrame(self, text="Metal precursors", padding=(20, 10))
        self.synthesis_frame.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")
        # Frame for the Agents
        self.agents_frame = ttk.LabelFrame(self, text="Agents", padding=(20, 10))
        self.agents_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        # Frame for the Catalyst
        self.Catalysts_frame = ttk.LabelFrame(self, text="Catalysts", padding=(20, 10))
        self.Catalysts_frame.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        # Frame for the Precipitating
        self.Precipitating_frame = ttk.LabelFrame(self, text="Precipitating", padding=(20, 10))
        self.Precipitating_frame.grid(row=4, column=0, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # First Precursor label - Responsive
        self.Precursor_label = ttk.Label(self.synthesis_frame, text="Precursor")
        self.Precursor_label.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="w")
        # Precursor dropdown
        self.Precursor_var = tk.StringVar()
        self.Precursor_combobox = ttk.Combobox(
            self.synthesis_frame,
            textvariable=self.Precursor_var,
            values=["Precursor 1", "Precursor 2"])     
        self.Precursor_combobox.grid(row=0, column=1, padx=5, pady=(0, 10), sticky="ew")
        self.Precursor_combobox.bind("<<ComboboxSelected>>", self.update_entries)
        # "Quality check" checkbox (initially hidden)
        self.Precursorcheck_label = ttk.Label(self.synthesis_frame, text="Quality check")
        #Quality combobox
        self.Precursorcheck_var = tk.StringVar()
        self.Precursorcheck_combobox = ttk.Combobox(
            self.synthesis_frame,
            textvariable=self.Precursorcheck_var,
            values=["Yes", "No"]) 

        # Precursor Volume (initially hidden)
        self.PrecursorVolume_label = ttk.Label(self.synthesis_frame, text="Volume of Precursor (µL)")
        self.PrecursorVolume_entry = ttk.Entry(self.synthesis_frame)      
        # Precursor 2/3 Weight (initially hidden)
        self.Precursor2Weight_label = ttk.Label(self.synthesis_frame, text="Mass of Precursor 2 (mg)")
        self.Precursor2Weight_entry = ttk.Entry(self.synthesis_frame)
        self.Precursor3Weight_label = ttk.Label(self.synthesis_frame, text="Mass of Precursor 3 (mg)")
        self.Precursor3Weight_entry = ttk.Entry(self.synthesis_frame)


        #Doping
        self.PrecursorDoping1_label = ttk.Label(self.synthesis_frame, text="Doping precursor")
        self.PrecursorDoping1_label.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="w")
        #Doping combobox
        self.PrecursorDoping1_var = tk.StringVar()
        self.PrecursorDoping1_combobox = ttk.Combobox(
            self.synthesis_frame,
            textvariable=self.PrecursorDoping1_var,
            values=["Yes", "No"])     
        self.PrecursorDoping1_combobox.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="ew")
        self.PrecursorDoping1_combobox.bind("<<ComboboxSelected>>", self.update_dopant)

        #Doping name (initially hidden)
        self.PrecursorDoping1Name_label = ttk.Label(self.synthesis_frame, text="Doping element")
        self.PrecursorDoping1Name_var = tk.StringVar()
        self.PrecursorDoping1Name_combobox = ttk.Combobox(self.synthesis_frame, textvariable=self.PrecursorDoping1Name_var, values=["A", "B", "C", "D"])     
        #Doping mass (initially hidden)
        self.PrecursorDoping1Mass_label = ttk.Label(self.synthesis_frame, text="Mass of Doping salt (mg)")
        self.PrecursorDoping1Mass_entry = ttk.Entry(self.synthesis_frame)

        #Other doping
        self.PrecursorDoping2_label = ttk.Label(self.synthesis_frame, text="Other Doping precursor?")
        self.PrecursorDoping2_var = tk.StringVar()
        self.PrecursorDoping2_combobox = ttk.Combobox(
            self.synthesis_frame,
            textvariable=self.PrecursorDoping2_var,
            values=["Yes", "No"])
        self.PrecursorDoping2_combobox.bind("<<ComboboxSelected>>", self.update_dopant2)
        #Doping2 name (initially hidden)
        self.PrecursorDoping2Name_label = ttk.Label(self.synthesis_frame, text="Doping element nr 2")
        self.PrecursorDoping2Name_var = tk.StringVar()
        self.PrecursorDoping2Name_combobox = ttk.Combobox(self.synthesis_frame, textvariable=self.PrecursorDoping2Name_var, values=["A", "B", "C", "D"])     
        #Doping mass (initially hidden)
        self.PrecursorDoping2Mass_label = ttk.Label(self.synthesis_frame, text="Mass of Doping salt nr 2(mg)")
        self.PrecursorDoping2Mass_entry = ttk.Entry(self.synthesis_frame)


        # agent Label
        self.agent_label = ttk.Label(self.agents_frame, text="Agent used")
        self.agent_label.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="w")
        # agent dropdown
        self.agent_var = tk.StringVar()
        self.agent_combobox = ttk.Combobox(
            self.agents_frame,
            textvariable=self.agent_var,
            values=["Agent 1", "Agent 2", "Agent 3​"])     
        self.agent_combobox.grid(row=0, column=1, padx=5, pady=(0, 10), sticky="ew")
        self.agentMass_label = ttk.Label(self.agents_frame, text="Volume or Mass (µL or mg)")
        self.agentMass_entry = ttk.Entry(self.agents_frame)
        self.agentMass_label.grid(row=0, column=2, padx=5, pady=(0, 10), sticky="w")
        self.agentMass_entry.grid(row=0, column=3, padx=5, pady=(0, 10), sticky="nsew")  


        self.SilverMass_label = ttk.Label(self.Catalysts_frame, text="Silver (mg)")
        self.SilverMass_entry = ttk.Entry(self.Catalysts_frame)
        self.SilverMass_label.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="w")
        self.SilverMass_entry.grid(row=0, column=1, padx=5, pady=(0, 10), sticky="nsew")
        self.GoldMass_label = ttk.Label(self.Catalysts_frame, text="Gold (mg)")
        self.GoldMass_entry = ttk.Entry(self.Catalysts_frame)
        self.GoldMass_label.grid(row=0, column=2, padx=5, pady=(0, 10), sticky="w")
        self.GoldMass_entry.grid(row=0, column=3, padx=5, pady=(0, 10), sticky="nsew")


        self.PrecipitatingCycles_label = ttk.Label(self.Precipitating_frame, text="Precipitating cycles")
        self.PrecipitatingCycles = ttk.Spinbox(self.Precipitating_frame, from_=0, to=99, increment=1)
        self.PrecipitatingCycles_label.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="w")
        self.PrecipitatingCycles.grid(row=0, column=1, padx=5, pady=(0, 10), sticky="nsew")
        self.PrecipitatingSpeed_label = ttk.Label(self.Precipitating_frame, text="RPM")
        self.PrecipitatingSpeed_entry = ttk.Entry(self.Precipitating_frame)
        self.PrecipitatingSpeed_label.grid(row=0, column=2, padx=5, pady=(0, 10), sticky="w")
        self.PrecipitatingSpeed_entry.grid(row=0, column=3, padx=5, pady=(0, 10), sticky="nsew")
        self.CyclesTime_label = ttk.Label(self.Precipitating_frame, text="Cycles duration (min)")
        self.CyclesTime_entry = ttk.Entry(self.Precipitating_frame)
        self.CyclesTime_label.grid(row=0, column=4, padx=5, pady=(0, 10), sticky="w")
        self.CyclesTime_entry.grid(row=0, column=5, padx=5, pady=(0, 10), sticky="nsew")
                                     
    def update_entries(self, event):
        selected = self.Precursor_var.get()
        if selected == "Precursor 1":
            self.Precursorcheck_label.grid(row=0, column=2, padx=5, pady=(0, 10), sticky="w")
            self.Precursorcheck_combobox.grid(row=0, column=3, padx=5, pady=(0, 10), sticky="w")
            self.PrecursorVolume_label.grid(row=0, column=4, padx=5, pady=(0, 10), sticky="w")
            self.PrecursorVolume_entry.grid(row=0, column=5, padx=5, pady=(0, 10), sticky="w")
            self.Precursor2Weight_label.grid_remove()
            self.Precursor2Weight_entry.grid_remove()
            self.Precursor3Weight_label.grid_remove()
            self.Precursor3Weight_entry.grid_remove()
    
        else:
            self.Precursor2Weight_label.grid(row=0, column=2, padx=5, pady=(0, 10), sticky="w")
            self.Precursor2Weight_entry.grid(row=0, column=3, padx=5, pady=(0, 10), sticky="w")
            self.Precursor3Weight_label.grid(row=0, column=4, padx=5, pady=(0, 10), sticky="w")
            self.Precursor3Weight_entry.grid(row=0, column=5, padx=5, pady=(0, 10), sticky="w")
            self.PrecursorVolume_label.grid_remove()
            self.PrecursorVolume_entry.grid_remove()
            self.PrecursorVolume_entry.delete(0, tk.END)
            self.Precursorcheck_label.grid_remove()
            self.Precursorcheck_combobox.grid_remove()

    def update_dopant(self, event):
        selected = self.PrecursorDoping1_var.get()
        if selected == "Yes":
            self.PrecursorDoping1Name_label.grid(row=1, column=2, padx=5, pady=(0, 10), sticky="ew")
            self.PrecursorDoping1Name_combobox.grid(row=1, column=3, padx=5, pady=(0, 10), sticky="ew")
            self.PrecursorDoping1Mass_label.grid(row=1, column=4, padx=5, pady=(0, 10), sticky="w")
            self.PrecursorDoping1Mass_entry.grid(row=1, column=5, padx=5, pady=(0, 10), sticky="nsew")
            self.PrecursorDoping2_label.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="w")
            self.PrecursorDoping2_combobox.grid(row=2, column=1, padx=5, pady=(0, 10), sticky="ew")
            self.characterization_tab.PrecursorDoping1Analysis_label.grid(row=0, column=2, padx=5, pady=(0, 10), sticky="w")
            self.characterization_tab.PrecursorDoping1Analysis.grid(row=0, column=3, padx=5, pady=10, sticky="ew")
        else:
            self.PrecursorDoping1Name_label.grid_remove()
            self.PrecursorDoping1Name_combobox.grid_remove()
            self.PrecursorDoping1Mass_label.grid_remove()
            self.PrecursorDoping1Mass_entry.grid_remove()
            self.PrecursorDoping1Mass_entry.delete(0, tk.END)
            self.PrecursorDoping2_label.grid_remove()
            self.PrecursorDoping2_combobox.grid_remove()
            self.characterization_tab.PrecursorDoping1Analysis_label.grid_remove()
            self.characterization_tab.PrecursorDoping1Analysis.grid_remove()

    def update_dopant2(self, event):
        selected = self.PrecursorDoping2_var.get()
        if selected == "Yes":
            self.PrecursorDoping2Name_label.grid(row=2, column=2, padx=5, pady=(0, 10), sticky="ew")
            self.PrecursorDoping2Name_combobox.grid(row=2, column=3, padx=5, pady=(0, 10), sticky="ew")
            self.PrecursorDoping2Mass_label.grid(row=2, column=4, padx=5, pady=(0, 10), sticky="w")
            self.PrecursorDoping2Mass_entry.grid(row=2, column=5, padx=5, pady=(0, 10), sticky="nsew")
            self.characterization_tab.PrecursorDoping2Analysis_label.grid(row=0, column=4, padx=5, pady=(0, 10), sticky="w")
            self.characterization_tab.PrecursorDoping2Analysis.grid(row=0, column=5, padx=5, pady=10, sticky="ew")
        else:
            self.PrecursorDoping2Name_label.grid_remove()
            self.PrecursorDoping2Name_combobox.grid_remove()
            self.PrecursorDoping2Mass_label.grid_remove()
            self.PrecursorDoping2Mass_entry.grid_remove()
            self.PrecursorDoping2Mass_entry.delete(0, tk.END)
            self.characterization_tab.PrecursorDoping2Analysis_label.grid_remove()
            self.characterization_tab.PrecursorDoping2Analysis.grid_remove()
