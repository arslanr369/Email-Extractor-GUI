# Email Extractor by @Arslanr369

Welcome to the **Email Extractor** application, a simple and efficient tool for extracting email addresses from any text input. This application, built with Python and Tkinter, allows users to enter a block of text, extract email addresses, and copy them directly to the clipboard for easy access.

---

## Features
- **Text Input**: Enter or paste any text containing email addresses.
- **Email Extraction**: Automatically extracts all valid email addresses using regular expressions.
- **Copy to Clipboard**: Copies extracted emails to the clipboard with a single click.
- **User-Friendly Interface**: Intuitive layout with buttons for easy interaction.

---

## Prerequisites
To run this application, make sure you have Python installed along with the following dependencies:
- **tkinter** (for GUI interface, included in standard Python library)
- **pyperclip** (for clipboard functionality)

Install `pyperclip` by running:
```bash
pip install pyperclip
```

---

## Usage

1. **Run the application**:
   ```bash
   python email_extractor.py
   ```
2. **Input Text**: Enter or paste the text containing emails into the provided text box.
3. **Extract Emails**: Click the **"Extract Emails"** button to display all detected email addresses.
4. **Copy Emails**: Use the **"Copy Emails"** button to copy the extracted email list to your clipboard for easy sharing.

---

## Code Overview

This application consists of:
- **EmailExtractorApp class**: Manages the GUI and email extraction functionality.
  - **extract_emails()**: Extracts emails using regular expressions and displays them in the output text box.
  - **copy_emails()**: Copies extracted emails to the clipboard and confirms the action.
  
---


## License
This project is open-source and available under the MIT License.

---

## About the Developer
Developed by **Arslan (@Arslanr369)**, a dedicated full-stack developer with a focus on creating useful applications for the community.

Enjoy using the Email Extractor!
