import re
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import pyperclip

class EmailExtractorApp:
    def __init__(self, master):
        self.master = master
        master.title("Email Extractor by @Arslanr369")

        # Create the input text box
        self.input_label = tk.Label(master, text="Enter the text:")
        self.input_label.pack()

        self.input_text = tk.Text(master, height=10)
        self.input_text.pack()

        # Create the output text box
        self.output_label = tk.Label(master, text="Extracted emails:")
        self.output_label.pack()

        self.output_text = tk.Text(master, height=5)
        self.output_text.pack()

        # Create the extract button
        self.extract_button = tk.Button(master, text="Extract Emails", command=self.extract_emails)
        self.extract_button.pack()

        # Create the copy button
        self.copy_button = ttk.Button(master, text="Copy Emails", command=self.copy_emails)
        self.copy_button.pack()

    def extract_emails(self):
        # Get the input text
        text = self.input_text.get("1.0", "end-1c")

        # Use regular expressions to extract email addresses
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

        # Display the extracted emails in the output text box
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", "\n".join(emails))

    def copy_emails(self):
        # Get the extracted emails from the output text box
        emails = self.output_text.get("1.0", "end-1c")

        # Copy the emails to the clipboard
        pyperclip.copy(emails)

        # Display a message box to confirm the copy action
        messagebox.showinfo("Emails Copied", "The extracted emails have been copied to the clipboard.")

# Create the GUI app
root = tk.Tk()
app = EmailExtractorApp(root)
root.mainloop()
