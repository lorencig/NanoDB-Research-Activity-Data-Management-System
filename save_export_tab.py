import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import ttkbootstrap as ttk
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from PIL import Image
import os
import sys
import shlex
import subprocess
import zipfile
import tempfile

def get_resource_path(relative_path):
    """ Get absolute path to resource, works for both development and PyInstaller. """
    try:
        # PyInstaller creates a temp folder for your files
        base_path = sys._MEIPASS
    except AttributeError:
        # Get the path where the script is located
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

class SaveExportTab(ttk.Frame):
    def __init__(self, parent, wb, sheet, column_list, intro_tab):
        super().__init__(parent)
        self.parent = parent
        self.wb = wb
        self.sheet = sheet
        self.column_list = column_list
        self.intro_tab = intro_tab
        self.image_list = []
        self.zip_image_list = []
        self.pdf_image_list = []

        self.setup_widgets()

    def setup_widgets(self):
        self.save_export_frame = ttk.LabelFrame(self, text="Final", padding=(20, 10))
        self.save_export_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        
        # Configure grid weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.submit_icon = tk.PhotoImage(file=get_resource_path('images/fly.png')).subsample(3, 3)
        self.register_button = ttk.Button(self.save_export_frame, bootstyle="light", image=self.submit_icon, text="Submit to DB", compound=tk.TOP, command=self.register)
        self.register_button.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.pdf_icon = tk.PhotoImage(file=get_resource_path('images/report.png')).subsample(3, 3)
        self.pdf_button = ttk.Button(self.save_export_frame, bootstyle="light", image=self.pdf_icon, text="Generate PDF", compound=tk.TOP, command=self.prompt_pdf_save_location)
        self.pdf_button.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

        self.love_icon = tk.PhotoImage(file=get_resource_path('images/quote.png')).subsample(3, 3)
        self.love_button = ttk.Button(self.save_export_frame, bootstyle="light", image=self.love_icon, text="Credits", compound=tk.TOP, command=self.on_button_click)
        self.love_button.grid(row=2, column=4, padx=20, pady=20, sticky="nsew")

        self.tem_icon = tk.PhotoImage(file=get_resource_path('images/TEM.png')).subsample(3, 3)
        self.image_button = ttk.Button(self.save_export_frame, bootstyle="light", image=self.tem_icon, text="TEM Images", compound=tk.TOP, command=self.add_images)
        self.image_button.grid(row=0, column=4, padx=20, pady=20, sticky="nsew")

        self.restart_icon = tk.PhotoImage(file=get_resource_path('images/nuclear.png')).subsample(3, 3)
        self.clear_button = ttk.Button(self.save_export_frame, bootstyle="light", image=self.restart_icon, text="Abort and Restart", compound=tk.TOP, command=self.restart_app)
        self.clear_button.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        separator = ttk.Separator(self.save_export_frame, orient='vertical')
        separator.grid(row=0, column=1, padx=40)
        separator = ttk.Separator(self.save_export_frame, orient='vertical')
        separator.grid(row=0, column=3, padx=40)
        separator = ttk.Separator(self.save_export_frame, orient='horizontal')
        separator.grid(row=1, column=0, padx=40)
        separator = ttk.Separator(self.save_export_frame, orient='horizontal')
        separator.grid(row=1, column=4, padx=40)

        self.save_export_frame.columnconfigure(1, weight=1)
        self.save_export_frame.columnconfigure(3, weight=1)
        self.save_export_frame.rowconfigure(1, weight=1)

    def restart_app(self):
        """Restart the main application."""
        python = sys.executable
        subprocess.Popen([python] + sys.argv)
        self.parent.quit()  # Close the main Tkinter loop
        self.parent.destroy()  # Destroy the Tkinter root window


    def on_button_click(self):
        def copy_to_clipboard():
            self.parent.clipboard_clear()
            self.parent.clipboard_append(message)
            self.parent.update()  # now it stays on the clipboard after the window is closed

        message = "Gjurgjaj, L., Silvestri, N., Hysa, E., & Pellegrino, T. (2024). NanoDB: Research Activity Data Management System. Zenodo. https://doi.org/10.XXX/zenodo.XXX"
        
        # Create a new top-level window
        top = tk.Toplevel(self)
        top.title("Please cite this work")
        top.geometry("300x150")
        
        # Create a label for the message
        label = ttk.Label(top, text=message, wraplength=250)
        label.pack(pady=20)
        
        # Create a copy button
        copy_button = ttk.Button(top, text="Copy", command=copy_to_clipboard)
        copy_button.pack(pady=10)

    def register(self):
        self.data_for_pdf = self.get_data_from_widgets()

        selected_item = self.intro_tab.Search_list.get(tk.ANCHOR)
        if selected_item:
            row_index = self.column_list.index(selected_item) + 2
            self.update_excel_row(row_index)
            messagebox.showinfo("Success", "Entry edited successfully!")
        else:
            last_row = self.sheet.max_row + 1
            self.update_excel_row(last_row)
            messagebox.showinfo("Success", "New entry created successfully!")

    def get_data_from_widgets(self):

        UserName = self.intro_tab.UserName_entry.get()
        SampleName = self.intro_tab.SampleName_entry.get()
        Comment = self.intro_tab.Comment_text.get("1.0", "end-1c")
        SynthesisDate = self.intro_tab.SynthesisDate_entry.entry.get()
        Availability = self.intro_tab.Availability_combobox.get()

        # Fetch data from Synthesis tab
        synthesis_tab = self.parent.master.synthesis_tab
        Precursor = synthesis_tab.Precursor_combobox.get()
        Precursorcheck = synthesis_tab.Precursorcheck_combobox.get()
        PrecursorDoping1 = synthesis_tab.PrecursorDoping1_combobox.get()
        PrecursorDoping2 = synthesis_tab.PrecursorDoping2_combobox.get()
        PrecursorDoping1Name = synthesis_tab.PrecursorDoping1Name_combobox.get()
        PrecursorDoping2Name = synthesis_tab.PrecursorDoping2Name_combobox.get()
        agent = synthesis_tab.agent_combobox.get()
        PrecursorVolume = synthesis_tab.PrecursorVolume_entry.get()
        Precursor2Weight = synthesis_tab.Precursor2Weight_entry.get()
        Precursor3Weight = synthesis_tab.Precursor3Weight_entry.get()
        PrecursorDoping1Mass = synthesis_tab.PrecursorDoping1Mass_entry.get()
        PrecursorDoping2Mass = synthesis_tab.PrecursorDoping2Mass_entry.get()
        agentMass = synthesis_tab.agentMass_entry.get()
        SilverMass = synthesis_tab.SilverMass_entry.get()
        GoldMass = synthesis_tab.GoldMass_entry.get()
        PrecipitatingCycles = synthesis_tab.PrecipitatingCycles.get()
        PrecipitatingSpeed = synthesis_tab.PrecipitatingSpeed_entry.get()
        CyclesTime = synthesis_tab.CyclesTime_entry.get()


        # Fetch data from Characterization tab
        characterization_tab = self.parent.master.characterization_tab  
        Size = characterization_tab.Size.get()
        SizeSTD = characterization_tab.SizeSTD.get()
        Dispersity = characterization_tab.Dispersity_combobox.get()
        Metal1 = characterization_tab.Metal1.get()
        PrecursorDoping1Analysis = characterization_tab.PrecursorDoping1Analysis.get()
        PrecursorDoping2Analysis = characterization_tab.PrecursorDoping2Analysis.get()
        FinalVolume = characterization_tab.FinalVolume.get()
        Precipitation = characterization_tab.Precipitation_combobox.get()
        Concentration = characterization_tab.Concentration_entry.get()



        return {
            'SampleName': SampleName,
            'Availability' : Availability,
            'SynthesisDate': SynthesisDate,
            'UserName': UserName,
            'Comment': Comment,
            'Precursor' : Precursor,
            'Precursorcheck' : Precursorcheck,
            'PrecursorDoping1' : PrecursorDoping1,
            'PrecursorDoping2' : PrecursorDoping2,
            'PrecursorDoping1Name' : PrecursorDoping1Name,
            'PrecursorDoping2Name' : PrecursorDoping2Name,
            'agent' : agent,
            'PrecursorVolume' : PrecursorVolume,
            'Precursor2Weight' : Precursor2Weight,
            'Precursor3Weight' : Precursor3Weight,
            'PrecursorDoping1Mass' : PrecursorDoping1Mass,
            'PrecursorDoping2Mass' : PrecursorDoping2Mass,
            'agentMass' : agentMass,
            'SilverMass' : SilverMass,
            'GoldMass' : GoldMass,
            'PrecipitatingCycles' : PrecipitatingCycles,
            'PrecipitatingSpeed' : PrecipitatingSpeed,
            'CyclesTime' : CyclesTime,
            'Size' : Size,
            'SizeSTD' : SizeSTD,
            'Dispersity' : Dispersity,
            'Metal1' : Metal1,
            'PrecursorDoping1Analysis' : PrecursorDoping1Analysis,
            'PrecursorDoping2Analysis' : PrecursorDoping2Analysis,
            'FinalVolume' : FinalVolume,
            'Precipitation' : Precipitation,
            'Concentration' : Concentration,
            }

    def update_excel_row(self, row):
        data = self.data_for_pdf
        self.sheet.cell(row=row, column=50).value = data['Comment']
        self.sheet.cell(row=row, column=2).value = data['SampleName']
        self.sheet.cell(row=row, column=3).value = data['Availability']
        self.sheet.cell(row=row, column=4).value = data['SynthesisDate']
        self.sheet.cell(row=row, column=5).value = data['UserName']
        self.sheet.cell(row=row, column=6).value = data['Precursor']	
        self.sheet.cell(row=row, column=7).value = data['Precursorcheck']	
        self.sheet.cell(row=row, column=8).value = data['PrecursorDoping1']	
        self.sheet.cell(row=row, column=9).value = data['PrecursorDoping2']	
        self.sheet.cell(row=row, column=10).value = data['PrecursorDoping1Name']	
        self.sheet.cell(row=row, column=11).value = data['PrecursorDoping2Name']	
        self.sheet.cell(row=row, column=12).value = data['agent']	
        self.sheet.cell(row=row, column=13).value = data['PrecursorVolume']	
        self.sheet.cell(row=row, column=14).value = data['Precursor2Weight']	
        self.sheet.cell(row=row, column=15).value = data['Precursor3Weight']	
        self.sheet.cell(row=row, column=16).value = data['PrecursorDoping1Mass']	
        self.sheet.cell(row=row, column=17).value = data['PrecursorDoping2Mass']
        self.sheet.cell(row=row, column=18).value = data['agentMass']
        self.sheet.cell(row=row, column=19).value = data['SilverMass']	
        self.sheet.cell(row=row, column=20).value = data['GoldMass']		
        self.sheet.cell(row=row, column=22).value = data['PrecipitatingCycles']	
        self.sheet.cell(row=row, column=23).value = data['PrecipitatingSpeed']	
        self.sheet.cell(row=row, column=24).value = data['CyclesTime']	
        self.sheet.cell(row=row, column=25).value = data['Size']
        self.sheet.cell(row=row, column=26).value = data['SizeSTD']
        self.sheet.cell(row=row, column=27).value = data['Dispersity']
        self.sheet.cell(row=row, column=28).value = data['Metal1']
        self.sheet.cell(row=row, column=29).value = data['PrecursorDoping1Analysis']
        self.sheet.cell(row=row, column=30).value = data['PrecursorDoping2Analysis']
        self.sheet.cell(row=row, column=31).value = data['FinalVolume']
        self.sheet.cell(row=row, column=32).value = data['Precipitation']
        self.sheet.cell(row=row, column=33).value = data['Concentration']
        self.wb.save(get_resource_path("registration_data.xlsx"))

    def prompt_pdf_save_location(self):
        pdf_file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
            title="Save PDF As",
            initialfile=f"{self.intro_tab.SampleName_entry.get()}_report"
        )
        if pdf_file_path:
            self.ask_add_images_to_pdf(pdf_file_path)

    def ask_add_images_to_pdf(self, pdf_file_path):
        answer = messagebox.askyesno("Add Images", "Do you want to add images to the PDF?")
        if answer:
            self.add_images_to_pdf(pdf_file_path)
        else:
            self.generate_pdf(pdf_file_path)

    def add_images_to_pdf(self, pdf_file_path):
        filenames = filedialog.askopenfilenames(title="Select Images for PDF", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
        if filenames:
            self.pdf_image_list = filenames
        self.generate_pdf(pdf_file_path)

    def generate_pdf(self, file_path):
        try:
            data = self.get_data_from_widgets()
            filtered_data = {k: v for k, v in data.items() if v != ''}
            
            # Define the PDF document
            doc = SimpleDocTemplate(file_path, pagesize=letter)
            
            # Get sample styles
            styles = getSampleStyleSheet()
            story = []

            # Add logo
            logo_path = get_resource_path('images/logo.png')
            if os.path.exists(logo_path):
                logo = RLImage(logo_path)
                story.append(logo)
                story.append(Spacer(1, 12))
            else:
                raise FileNotFoundError(f"Logo file {logo_path} not found.")

            # Title
            title = Paragraph("Synthesis Report", styles['Title'])
            story.append(title)
            story.append(Spacer(1, 12))

            styles = getSampleStyleSheet()
            # Customize subtitle style
            subtitle_style = ParagraphStyle(
                name='CustomSubtitle',
                parent=styles['Normal'],
                alignment=1  # Center alignment
            )
            # Subtitle
            subtitle = Paragraph("Generated automatically from NanoDB", style=subtitle_style)
            story.append(subtitle)
            story.append(Spacer(1, 12))

            for field_name, field_value in filtered_data.items():
                text = f"<b>{field_name.replace('_', ' ')}:</b> {field_value}"
                story.append(Paragraph(text, styles['Normal']))
                story.append(Spacer(1, 12))

            for i, image_path in enumerate(self.pdf_image_list[:4]):
                story.append(Spacer(1, 24))
                story.append(Paragraph(f"Image {i+1}", styles['Normal']))
                story.append(Spacer(1, 6))
                rl_image = self.resize_image_for_pdf(image_path)
                story.append(RLImage(rl_image))
                story.append(Spacer(1, 24))

            doc.build(story)
            messagebox.showinfo("Success", f"PDF generated: {file_path}")
                
            self.open_pdf(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate PDF: {str(e)}")

    def open_pdf(self, file_path):
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            if sys.platform == 'win32':  # Windows
                os.startfile(os.path.normpath(file_path))
            elif sys.platform == 'darwin':  # macOS
                os.system(f'open "{shlex.quote(file_path)}"')
            elif sys.platform.startswith('linux'):  # Linux
                os.system(f'xdg-open "{shlex.quote(file_path)}"')
            else:
                messagebox.showinfo("Info", "Please open the PDF manually.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open PDF: {str(e)}")

    def resize_image_for_pdf(self, image_path):
        img = Image.open(image_path)
        width, height = img.size
        aspect_ratio = height / width
        img_width = 250
        img_height = int(img_width * aspect_ratio)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_img_file:
            img = img.resize((img_width, img_height), Image.LANCZOS)
            img.save(tmp_img_file, format='JPEG')
            return tmp_img_file.name

    def compress_image(self, image_path):
        img = Image.open(image_path)
        img_compressed = img.convert('RGB')
        sample_name = self.intro_tab.SampleName_entry.get()
        suffix = f"{len(self.image_list):02}"
        compressed_image_name = f"{sample_name}_{suffix}.jpg"
        compressed_image_path = os.path.join(os.path.dirname(image_path), compressed_image_name)
        img_compressed.save(compressed_image_path)
        self.image_list.append(compressed_image_path)


    def resize_image(self, image_path, max_width=500):
        img = Image.open(image_path)
        img.thumbnail((max_width, max_width))
        resized_image_path = os.path.join(tempfile.gettempdir(), f"resized_{os.path.basename(image_path)}")
        img.save(resized_image_path)
        return resized_image_path

    def add_images(self):
        filenames = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
        self.image_list.extend(filenames)
        
        self.prompt_zip_save_location()

    def prompt_zip_save_location(self):
        zip_path = filedialog.asksaveasfilename(
            defaultextension=".zip",
            filetypes=[("ZIP files", "*.zip"), ("All files", "*.*")],
            title="Save ZIP As",
            initialfile=f"{self.intro_tab.SampleName_entry.get()}_images.zip"
        )
        if zip_path:
            self.create_zip(zip_path)

    def create_zip(self, zip_path):
        for image_path in self.image_list:
            zip_image_path = self.save_temp_image(image_path)
            self.zip_image_list.append(zip_image_path)
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for image_path in self.zip_image_list:
                zipf.write(image_path, os.path.basename(image_path))
        messagebox.showinfo("Success", f"ZIP file created: {zip_path}")

    def save_temp_image(self, image_path):
        temp_dir = tempfile.gettempdir()
        temp_image_path = os.path.join(temp_dir, os.path.basename(image_path))
        img = Image.open(image_path)
        img.save(temp_image_path)
        return temp_image_path

    def get(self):
        return self.image_list
