from tkinter import *
from tkinter import filedialog, messagebox
import os

class FileExplorer:
    def __init__(self, window):
        self.window = window
        self.window.title('File Explorer')
        self.window.geometry("600x600")
        self.window.config(background="white")
        
        self.current_directory = ""

        # Create a grid layout with different background colors for visibility
        for i in range(6):  # 6 rows
            for j in range(3):  # 3 columns
                frame = Frame(window, width=100, height=100, bg='lightgray', relief=SUNKEN)
                frame.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
                frame.grid_propagate(False)  # Prevent the frame from resizing with contents

        # Center title at the top
        self.label_file_explorer = Label(window, 
                                          text="File Explorer using Tkinter",
                                          width=25, height=2, 
                                          fg="blue", bg='white', anchor=CENTER)
        self.label_file_explorer.grid(row=0, column=0, columnspan=3)

        # Button layout
        button_explore_file = Button(window, text="Browse File", command=self.browseFile)
        button_explore_directory = Button(window, text="Browse Directory", command=self.browseDirectory)
        button_create_file = Button(window, text="Create File", command=self.createFile)
        button_rename_file = Button(window, text="Rename File", command=self.renameFile)
        button_delete_file = Button(window, text="Delete File", command=self.deleteFile)
        button_exit = Button(window, text="Exit", command=self.window.quit)

        # Arrange buttons in a grid
        button_explore_file.grid(row=1, column=0, padx=10, pady=5)
        button_explore_directory.grid(row=1, column=1, padx=10, pady=5)
        button_create_file.grid(row=2, column=0, padx=10, pady=5)
        button_rename_file.grid(row=2, column=1, padx=10, pady=5)
        button_delete_file.grid(row=3, column=0, padx=10, pady=5)
        button_exit.grid(row=3, column=1, padx=10, pady=5)

        # File preview area centered below buttons
        self.file_preview = Text(window, width=70, height=20)
        self.file_preview.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

        # Status bar at the bottom
        self.status_bar = Label(window, text="", bd=1, relief=SUNKEN, anchor=W)
        self.status_bar.grid(row=5, column=0, columnspan=3, sticky=W+E)

        # Configure grid weights
        for i in range(6):
            window.grid_rowconfigure(i, weight=1)
        for j in range(3):
            window.grid_columnconfigure(j, weight=1)

    def browseFile(self):
        filenames = filedialog.askopenfilenames(initialdir=self.current_directory or "/",
                                                 title="Select Files",
                                                 filetypes=(("Text files", "*.txt"),
                                                            ("All files", "*.*")))
        if filenames:
            self.label_file_explorer.config(text="Files Opened: " + ", ".join(filenames))
            self.current_directory = os.path.dirname(filenames[0])
            self.previewFiles(filenames)

    def browseDirectory(self):
        self.current_directory = filedialog.askdirectory()
        if self.current_directory:
            try:
                files = os.listdir(self.current_directory)
                self.label_file_explorer.config(text="Directory: " + self.current_directory)
                file_list = "\n".join(files)
                self.file_preview.delete(1.0, END)
                self.file_preview.insert(END, file_list)
                self.status_bar.config(text=f"Opened directory: {self.current_directory}")
            except PermissionError:
                messagebox.showerror("Error", "You don't have permission to access this directory.")

    def createFile(self):
        file_name = filedialog.asksaveasfilename(initialdir=self.current_directory,
                                                  title="Create New File",
                                                  defaultextension=".txt",
                                                  filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_name:
            with open(file_name, 'w') as file:
                file.write("")  # Creating an empty file
            self.status_bar.config(text=f"Created file: {file_name}")

    def renameFile(self):
        current_file = filedialog.askopenfilename(initialdir=self.current_directory,
                                                   title="Select File to Rename")
        if current_file:
            new_file_name = filedialog.asksaveasfilename(initialdir=self.current_directory,
                                                          title="Rename File",
                                                          defaultextension=".txt",
                                                          filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
            if new_file_name:
                os.rename(current_file, new_file_name)
                self.status_bar.config(text=f"Renamed file to: {new_file_name}")

    def deleteFile(self):
        file_to_delete = filedialog.askopenfilename(initialdir=self.current_directory,
                                                    title="Select File to Delete")
        if file_to_delete:
            confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{os.path.basename(file_to_delete)}'?")
            if confirm:
                os.remove(file_to_delete)
                self.status_bar.config(text=f"Deleted file: {file_to_delete}")
                self.browseDirectory()  # Refresh the file list

    def previewFiles(self, filenames):
        self.file_preview.delete(1.0, END)  # Clear previous text
        for filename in filenames:
            try:
                with open(filename, 'r') as file:
                    contents = file.read()
                    self.file_preview.insert(END, f"Contents of {filename}:\n{contents}\n\n")
            except Exception as e:
                messagebox.showwarning("Warning", f"Could not read {filename}: {e}")

if __name__ == "__main__":
    window = Tk()
    app = FileExplorer(window)
    window.mainloop()
