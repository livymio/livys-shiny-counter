import tkinter as tk 
from tkinter import messagebox
from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

class Setup:

    def __init__(self):

        #defines variable x
        self.countVar = 0
        
        #layout of setup window
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.title("Setup")

        self.root['background']='#525252'


        self.label = tk.Label(self.root, text="What are you shiny hunting?", font=('Arial', 18), fg='white', bg='#525252')
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=1, font=('Arial', 16))
        self.textbox.pack(padx=50, pady=10)
        self.textbox.bind("<Return>", lambda event: "break")

        self.button = tk.Button(self.root, text="Start", font=('Arial', 18), fg='white', bg='#313131', command=self.save)
        self.button.pack(padx=10, pady=10)

        self.loadbutton = tk.Button(self.root, text="Load Save", font=('Arial', 18), fg='white', bg='#313131', command=self.load)
        self.loadbutton.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    #function of load button
    def load(self):
        #function of count button
        def count():
            self.countVar += 1
            self.label2.config(text=self.countVar)
        #grabs title from config
        global title
        title = (config['SAVE 1']['TITLE'])

        #layout of counter window
        self.load_window = tk.Toplevel()
        self.load_window.geometry("300x150")
        self.load_window['background']='#525252'

        self.load_window.title(config['SAVE 1']['TITLE'])
        self.countVar = int(config['SAVE 1']['COUNT']) 
        self.label = tk.Label(self.load_window, text=(config['SAVE 1']['TITLE']), font=('Arial', 18), fg='white', bg='#525252')
        self.label.pack(padx=10)
        self.label2 = tk.Label(self.load_window, text=self.countVar, font=('Arial', 18), fg='white', bg='#525252')
        self.label2.pack(padx=10)
        self.button = tk.Button(self.load_window, text="Encounters +1", font=('Arial', 18), fg='white', bg='#525252', command=count)
        self.button.pack(padx=10)
        self.saveButton = tk.Button(self.load_window, text="Save", font=('Arial', 12), fg='white', bg='#525252', command=self.deticated_save)
        self.saveButton.pack(padx=10, pady=5)

        self.root.wm_state('iconic')

        self.load_window.protocol("WM_DELETE_WINDOW", self.save_on_close)

    #Sets function of the messagebox 
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    #save the textbox as config var title and open counter
    def save(self):
        global title
        title = self.textbox.get('1.0', tk.END).strip()
        
        self.parent = self
        
        global countVar
        countVar = 0
        
        self.load_window = tk.Toplevel()
        self.load_window.geometry("300x150")
        self.load_window.title(title)
        self.load_window['background']='#525252'
        self.label = tk.Label(self.load_window, text=title, font=('Arial', 18), fg='white', bg='#525252')
        self.label.pack(padx=10)
        self.label2 = tk.Label(self.load_window, text=countVar, font=('Arial', 18), fg='white', bg='#525252')
        self.label2.pack(padx=10)
        self.button = tk.Button(self.load_window, text="Encounters +1", font=('Arial', 18), fg='white', bg='#525252', command=self.count)
        self.button.pack(padx=10)
        self.saveButton = tk.Button(self.load_window, text="Save", font=('Arial', 12), fg='white', bg='#525252', command=self.deticated_save)
        self.saveButton.pack(padx=10, pady=5)

        self.root.wm_state('iconic')

        self.load_window.protocol("WM_DELETE_WINDOW", self.save_on_close)

    # increment x by 1
    def count(self):
        self.countVar += 1
        self.label2.config(text=self.countVar)

    #prompts user to safe on close
    def save_on_close(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            if messagebox.askyesno(title="Quit?", message="Do you want to save? This will overwrite any previous saves."):
                if not config.has_section('SAVE 1'): #if the config is empty or doesn't contain SAVE 1 it will write it
                    config.add_section('SAVE 1')
                config.set('SAVE 1', 'TITLE', str(title))
                config.set('SAVE 1', 'COUNT', str(self.countVar))
                with open(file, 'w') as f:
                    config.write(f)
            self.load_window.destroy()
            self.root.destroy()

    def deticated_save(self):
        if messagebox.askyesno(title="Save?", message="Do you want to save? This will overwrite any previous saves."):
            if not config.has_section('SAVE 1'): #if the config is empty or doesn't contain SAVE 1 it will write it
                    config.add_section('SAVE 1')
                    config.set('SAVE 1', 'TITLE', str(title))
                    config.set('SAVE 1', 'COUNT', str(self.countVar))
                    with open(file, 'w') as f:
                        config.write(f)

Setup()
