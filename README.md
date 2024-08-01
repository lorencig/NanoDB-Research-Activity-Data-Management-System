[![Codacy Badge](https://app.codacy.com/project/badge/Grade/3729226af24c46e7807c89f630f6341e)](https://app.codacy.com/gh/lorencig/NanoDB-Research-Activity-Data-Management-System/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

# NanoDB: Research Activity Data Management System
NanoDB is a versatile Python-based application that provides a graphical user interface (GUI) for entering, managing, and exporting laboratory experiment data. The application allows users to submit data to a database, generate PDF reports, and handle image files efficiently.


## Table of Contents

- [Features](#features)
- [Data Flow](#data-flow)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Files](#files)
- [Creating Executable](#creating-executable)
- [Function Documentation](#function-documentation)
- [License](#license)
- [Disclaimer](#disclaimer)

## Features

1. **Intuitive User Interface**: The application is divided into four main tabs:
   - Intro: For basic sample information
   - Synthesis: For detailed synthesis parameters
   - Characterization: For recording characterization results
   - Save & Export: For saving data and generating reports

2. **Data Persistence**: All entered data is saved locally in an Excel file, ensuring data integrity and easy access.

3. **Dynamic Form Fields**: The interface adapts based on user input, showing or hiding relevant fields as needed.

4. **PDF Report Generation**: Users can generate comprehensive PDF reports of their experiments with a single click.

5. **Image Management**: The application allows users to attach and manage images related to their experiments.

6. **Data Search**: Users can easily search and edit previously entered data.

7. **Data Export**: Experimental data can be exported in various formats, including Excel and PDF.

## Data Flow

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

1. Users input data through the graphical interface.
2. The application processes and validates the data.
3. Data is saved to a local Excel file.
4. Users can generate PDF reports or export data as needed.

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/lorencig/NanoDB-Research-Activity-Data-Management-System.git
    cd NanoDB-Research-Activity-Data-Management-System
    ```

2. Install the required Python packages:

    ```shell
    pip install -r requirements.txt
    ```
    

## Usage

1. Start the application:

    ```shell
    python main.py
    ```
  
2.  Use the tabs to navigate through different sections of the application.
    
3.  Input your research data in the appropriate fields.
    
4.  Use the "Save & Export" tab to save your data and generate reports.
    

## Code Structure

- `main.py`: The entry point of the application, sets up the main window and tabs.
    
- `intro_tab.py`: Contains the IntroTab class for basic sample information.
    
- `synthesis_tab.py`: Implements the SynthesisTab class for synthesis parameters.
    
- `characterization_tab.py`: Defines the CharacterizationTab class for characterization results.
    
- `save_export_tab.py`: Handles saving data and generating reports.

## Files

- `main.py`: The main script to run the application.
- `requirements.txt`: List of Python packages required to run the application.
- `logo.png`, `fly.png`, `report.png`, `quote.png`, `TEM.png`, `nuclear.png`: Icons used in the GUI.
- `README.md`: Documentation file.
- `LICENSE`: License file.    


## Creating Executable

To create a standalone executable (.exe) for Windows using PyInstaller, follow these steps:

1. Install PyInstaller:

    ```shell
    pip install pyinstaller
    ```

2. Create the executable:

    ```shell
    pyinstaller --onefile --windowed main.py
    ```

   - `--onefile`: Packages the application into a single executable file.
   - `--windowed`: Ensures no console window is opened when running the application.

3. The .exe file will be located in the `dist` directory.

Function Documentation
----------------------

This section provides an overview of the main functions in each file of the NanoDB application, along with guidance on how to edit them.

### Table of Contents

1.  [main.py](#mainpy)
    
2.  [intro\_tab.py](#intro_tabpy)
    
3.  [synthesis\_tab.py](#synthesis_tabpy)
    
4.  [characterization\_tab.py](#characterization_tabpy)
    
5.  [save\_export\_tab.py](#save_export_tabpy)
    

### main.py

#### Class: App

*   **\_\_init\_\_(self, parent)**:
    
    *   **Purpose**: Initializes the main application window.
        
    *   **How to edit**:
        
        *   Add new tabs by creating new instances of tab classes and adding them to self.notebook.
            
        *   Modify the Excel file path in excel\_path = os.path.join(base\_path, 'registration\_data.xlsx') if needed.
            
*   **setup\_notebook(self)**:
    
    *   **Purpose**: Sets up the tabbed interface.
        
    *   **How to edit**:
        
        *   Add new tabs by creating new instances and using self.notebook.add().
            
        *   Change tab order by reordering the self.notebook.add() calls.
            

### intro\_tab.py

#### Class: IntroTab

*   **setup\_widgets(self)**:
    
    *   **Purpose**: Creates and arranges widgets in the Intro tab.
        
    *   **How to edit**:
        
        *   Add new widgets by creating new ttk elements and using the grid() method to position them.
            
        *   Modify existing widgets by changing their properties or grid positions.
            
*   **show\_warning\_if\_duplicate(self, event)**:
    
    *   **Purpose**: Checks for duplicate sample names and shows a warning.
        
    *   **How to edit**:
        
        *   Modify the warning message or condition for showing the warning.
            
        *   Add additional checks or validations for the sample name.
            
*   **update(self, data)**:
    
    *   **Purpose**: Updates the search list with new data.
        
    *   **How to edit**:
        
        *   Change how data is displayed in the search list.
            
        *   Add additional processing of the data before updating the list.
            
*   **check(self, event)**:
    
    *   **Purpose**: Filters the search list based on user input.
        
    *   **How to edit**:
        
        *   Modify the filtering logic to change how searches are performed.
            
        *   Add additional criteria for searching.
            
*   **fillout(self, event)**:
    
    *   **Purpose**: Fills out the form with data from the selected item.
        
    *   **How to edit**:
        
        *   Change which fields are filled out and how.
            
        *   Add new fields to be filled out when an item is selected.
            

### synthesis\_tab.py

#### Class: SynthesisTab

*   **setup\_widgets(self)**:
    
    *   **Purpose**: Creates and arranges widgets in the Synthesis tab.
        
    *   **How to edit**:
        
        *   Add new widgets for additional synthesis parameters.
            
        *   Modify the layout by changing the grid positions of widgets.
            
*   **update\_entries(self, event)**:
    
    *   **Purpose**: Updates visible entries based on precursor selection.
        
    *   **How to edit**:
        
        *   Modify the conditions for showing/hiding widgets.
            
        *   Add new widgets to be shown/hidden based on selection.
            
*   **update\_dopant(self, event) and update\_dopant2(self, event)**:
    
    *   **Purpose**: Updates visible entries based on dopant selection.
        
    *   **How to edit**:
        
        *   Change the logic for showing/hiding dopant-related fields.
            
        *   Add new fields or conditions related to dopants.
            

### characterization\_tab.py

#### Class: CharacterizationTab

*   **setup\_widgets(self)**:
    
    *   **Purpose**: Creates and arranges widgets in the Characterization tab.
        
    *   **How to edit**:
        
        *   Add new characterization parameters by creating new widgets.
            
        *   Modify the layout by changing the grid positions or frame structure.
            
*   **create\_label\_frame(self, text, row, col, colspan=1)**:
    
    *   **Purpose**: Creates a labeled frame for grouping widgets.
        
    *   **How to edit**:
        
        *   Modify the appearance or behavior of the label frames.
            
        *   Add additional customization options for frames.
            
*   **create\_label\_and\_spinbox(self, parent, label\_text, row, col, col2=None, increment=0.1, from\_=0.0, to=99.9, width=4)**:
    
    *   **Purpose**: Creates a label and associated spinbox.
        
    *   **How to edit**:
        
        *   Change default values or range for spinboxes.
            
        *   Modify the appearance or behavior of labels and spinboxes.
            
*   **Similar methods for combobox and entry creation**:
    
    *   **Purpose**: Create standardized label-input pairs.
        
    *   **How to edit**:
        
        *   Modify default values, appearances, or behaviors of these widgets.
            
        *   Add new types of standardized input widgets.
            

### save\_export\_tab.py

#### Class: SaveExportTab

*   **setup\_widgets(self)**:
    
    *   **Purpose**: Creates and arranges widgets in the Save & Export tab.
        
    *   **How to edit**:
        
        *   Add new buttons or options for additional export formats.
            
        *   Modify the layout or appearance of existing buttons.
            
*   **register(self)**:
    
    *   **Purpose**: Saves the entered data to the Excel file.
        
    *   **How to edit**:
        
        *   Modify how data is collected from other tabs.
            
        *   Change the way data is written to the Excel file.
            
*   **generate\_pdf(self, file\_path)**:
    
    *   **Purpose**: Generates a PDF report of the experiment.
        
    *   **How to edit**:
        
        *   Modify the structure or content of the PDF report.
            
        *   Add new sections or data to be included in the report.
            
*   **add\_images(self)**:
    
    *   **Purpose**: Allows users to add images to their experiment record.
        
    *   **How to edit**:
        
        *   Change how images are processed or stored.
            
        *   Modify the types of images that can be added.
            
*   **create\_zip(self, zip\_path)**:
    
    *   **Purpose**: Creates a zip file of experiment images.
        
    *   **How to edit**:
        
        *   Modify how images are compressed or named in the zip file.
            
        *   Add additional files or data to be included in the zip.

## Technologies & Tools

- **Tkinter**: Standard GUI toolkit for Python.
- **ttkbootstrap**: Theming extension for Tkinter.
- **ReportLab**: Library for PDF generation.
- **Pillow**: Python Imaging Library (PIL Fork).

## License

This project is licensed under the CC BY 4.0 License - see the LICENSE file for details.

## Disclaimer

- This software is separated from the author's research and activity roles at their own institutions.

## Links

![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-%23FF6F00.svg?style=for-the-badge&logo=python&logoColor=white)
![ttkbootstrap](https://img.shields.io/badge/ttkbootstrap-%230081CB.svg?style=for-the-badge&logo=python&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-%232536A4.svg?style=for-the-badge&logo=python&logoColor=white)
![ReportLab](https://img.shields.io/badge/ReportLab-%234B8BBE.svg?style=for-the-badge&logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-%232B2B2B.svg?style=for-the-badge&logo=python&logoColor=white)
