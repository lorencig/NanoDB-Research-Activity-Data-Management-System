
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/3729226af24c46e7807c89f630f6341e)](https://app.codacy.com/gh/lorencig/NanoDB-Research-Activity-Data-Management-System/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

# NanoDB: Research Activity Data Management System

**NanoDB** is a Python-based application developed to optimize the management of experimental data in research settings. Designed with flexibility in mind, it supports the collection, organization, and export of laboratory metadata across diverse research line types. Built on the FAIR principles, by ensuring clean and well-structured datasets, NanoDB also lays the foundation for integrating machine learning, enabling more advanced data analysis and modeling in future research stages.
 
---

## ✨ Key Features

1. **Intuitive User Interface**:
   - Our example contains four main tabs guide users through the data collection process, **but all the tabs, frames and entries can be easily changed**:
     - **Intro**: Enter basic information about the sample, create new entry or call old sample data throught the search bar. All entries will appear in the listbox. Type of entries used: Combobox, Comment, Date, Simple Entry.
     - **Synthesis**: Type of entries used: Combobox, Simple Entry, dynamic entries based on selected values.
     - **Characterization**: Type of entries used: Combobox, Spinbox, Simple Entry, dynamic entries based on selected values.
     - **Save & Export**: Save the data to the local DB, generate report in PDF and zip images renamed after the sample name.

2. **Dynamic Data Fields**:
   - The form fields are adaptive based on user input, offering a customized experience that evolves as different data is input across the tabs.

3. **Data Persistence**:
   - All data is saved locally in an Excel file, ensuring offline access and secure data management.

4. **Easy Data Retrieval**:
   - Users can recall previous entries, modify them, or add new data to existing records.

5. **PDF Report Generation**:
   - Quickly generate comprehensive PDF reports of your experiments.

6. **Image Management**:
   - Attach and manage images related to your experiments directly from the app.

7. **Data Export**:
   - Export the experimental data in various formats, ensuring compatibility with external tools.

---

## 🚀 How to Run the Application

1. Ensure you have **Python 3.7 or higher** installed on your system.

2. Clone the NanoDB repository:
   ```
   git clone https://github.com/lorencig/NanoDB-Research-Activity-Data-Management-System.git
   cd NanoDB-Research-Activity-Data-Management-System
   ```
3. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the application by running:
   ```bash
   python main.py
   ```

---

## 🛠️ Code Structure aka Documentation

## 📂 Files

- **`main.py`**: The core script for running the app.
- **`README.md`**: Documentation and instructions.
- **`/images`**: Directory containing assets such as images or logos used within the app.
- **`/screenshots`**: Directory containing screenshots of what the application should look like while running.
- **`registration_data.xlsx`**: The excel file where all the data will be stored. Keeping the file open while writing new data or opening the app, may cause problems. Recommended to keep it close while operating.
- **`main.spec`**: Ready for use if executable is inteded to be created using Pyinstaller library.
- **`requirements.txt`**: List of libraries to be installed prior of launching the app.
- **`intro_tab.py`**: The first tab of the app, containing the logo, date type of entry, comment type of entry, combobox type of entry and simple text entry. Also the search bar based on the sample name.
- **`synthesis_tab.py`**: The second tab of the app, containing generally combobox and simple text type of entry.
- **`characterization_tab.py`**: The third tab of the app, containing generally spinbox, combobox and simple text type of entry.
- **`save_export_tab.py`**: The last tab of the app, containing the functions to write/edit the entry on the DB, generate the PDF containing also images (optional), compressing images saving it with the Sample name prefix, restart the app to ensure a clean insertion of a new entry.
---
## 🧠 Functions and code logic

### main.py

#### Class: App

*   **\_\_init\_\_(self, parent)**:
    
    *   **Purpose**: Initializes the main application window.
        
    *   **Use**:
        
        *   Add new tabs by creating new instances of tab classes and adding them to self.notebook.
            
        *   Modify the Excel file path in excel\_path = os.path.join(base\_path, 'registration\_data.xlsx') if needed.
            
*   **setup\_notebook(self)**:
    
    *   **Purpose**: Sets up the tabbed interface.
        
    *   **Use**:
        
        *   Add new tabs by creating new instances and using self.notebook.add().
            
        *   Change tab order by reordering the self.notebook.add() calls.
            

### intro\_tab.py

#### Class: IntroTab

*   **setup\_widgets(self)**:
    
    *   **Purpose**: Creates and arranges widgets in the Intro tab.
        
    *   **Use**:
        
        *   Add new widgets by creating new ttk elements and using the grid() method to position them.
            
        *   Modify existing widgets by changing their properties or grid positions.
            
*   **show\_warning\_if\_duplicate(self, event)**:
    
    *   **Purpose**: Checks for duplicate sample names and shows a warning.
        
    *   **Use**:
        
        *   Modify the warning message or condition for showing the warning.
            
        *   Add additional checks or validations for the sample name.
            
*   **update(self, data)**:
    
    *   **Purpose**: Updates the search list with new data.
        
    *   **Use**:
        
        *   Change how data is displayed in the search list.
            
        *   Add additional processing of the data before updating the list.
            
*   **check(self, event)**:
    
    *   **Purpose**: Filters the search list based on user input.
        
    *   **Use**:
        
        *   Modify the filtering logic to change how searches are performed.
            
        *   Add criteria for searching.
            
*   **fillout(self, event)**:
    
    *   **Purpose**: Fills out the form with data from the selected item.
        
    *   **Use**:
        
        *   Select which fields are filled out and how.
            
        *   Add new fields to be filled out when an item is selected.
            

### synthesis\_tab.py and characterization\_tab.py

#### Class: SynthesisTab and CharacterizationTab

*   **update\_entries(self, event)**:
    
    *   **Purpose**: Updates visible entries based on combobox (list) value selection.
        
    *   **How to edit**:
        
        *   Bind the event with the entry configuration (self.{entry}_combobox.bind)
            
        *   Change the parameters in the update definition.

            
*   **create\_label\_frame(self, text)**:
    
    *   **Purpose**: Creates a labeled frame for grouping widgets.
        
    *   **Use**:
        
        *   Create the appearance or behavior of the label frames.
            
        *   Add additional customization options for frames.
            
### save\_export\_tab.py

#### Class: SaveExportTab
          
*   **register(self)**:
    
    *   **Purpose**: Saves the entered data to the Excel file.
        
    *   **Use**:
        
        *   Designate how data is collected from other tabs.
            
        *   Specify the order the way data is written to the Excel file.
            
*   **generate\_pdf(self, file\_path)**:
    
    *   **Purpose**: Generates a PDF report of the experiment.
        
    *   **Use**:
        
        *   Define the structure or content of the PDF report.
            
        *   Select sections or metadata to be included in the report.

        *   Give to the user the choice of where to save localy.

*   **add\_images(self)**:
    
    *   **Purpose**: Allows users to add images to their experiment record.
        
    *   **Use**:
        
        *   Define how images are processed or stored.
            
        *   Assign the types of images that can be added.

        *   Limit the maximal number of images that can be added.
        

            
*   **create\_zip(self, zip\_path)**:
    
    *   **Purpose**: Creates a zip file of experiment images.
        
    *   **Use**:
        
        *   Modify how images are compressed or named in the zip file.
            
        *   Add additional files or data to be included in the zip.

        *   Give to the user the choice of where to save localy.
---
## 〰 Data Flow

```plaintext
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   User      │    │   NanoDB    │    │    Local    │
│  Interface  │ -> │    App      │ -> │  Excel File │
└─────────────┘    └─────────────┘    └─────────────┘
                          │
                          │
                          ▼
                   ┌─────────────┐
                   │ PDF Reports │
                   │ & ZIP Images│
                   └─────────────┘
```

## 📤Exporting Data

NanoDB offers multiple export options:

- Excel: Full dataset export
- PDF: Formatted report of individual experiments
- Image ZIP: Collated images for each experiment
---

## 💾 Creating Executable

To create a standalone executable (.exe) for Windows using PyInstaller, follow these steps:

1. Install PyInstaller:

    ```shell
    pip install pyinstaller
    ```

2. Create the executable:

    ```shell
    pyinstaller main.spec
    ```


3. The .exe file will be located in the `dist` directory.

---

## 🛠️ Technologies & Tools Used

- **Tkinter**: GUI toolkit for Python.
- **ttkbootstrap**: Provides a sleek interface and theming for the app.
- **OpenPyXL**: Used for handling Excel files for data storage.
- **ReportLab**: Library for generating PDF reports.
- **Pillow**: Handles image management within the app.

---



## 🆘 Need Help?

- Check out our [Documentation](#)
- Contact the maintainers directly


## 📜 License

This project is licensed under the **Creative Commons BY 4.0 License** - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

This software is separate from the author’s academic and professional roles at their institution.

---

## 📎 Additional Links

![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-%23FF6F00.svg?style=for-the-badge&logo=python&logoColor=white)
![ttkbootstrap](https://img.shields.io/badge/ttkbootstrap-%230081CB.svg?style=for-the-badge&logo=python&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-%232536A4.svg?style=for-the-badge&logo=python&logoColor=white)
![ReportLab](https://img.shields.io/badge/ReportLab-%234B8BBE.svg?style=for-the-badge&logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-%232B2B2B.svg?style=for-the-badge&logo=python&logoColor=white)

---
