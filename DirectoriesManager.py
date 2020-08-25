import time
import tkinter as tk
from tkinter import filedialog
from clint.textui import puts, colored, indent
import os

class DirectoriesManager():
    def loadDirectoriesToClean(self):
        self.directories = []
        newDirectory = True
        while newDirectory:
            root = tk.Tk()
            root.withdraw()
            dirPath = filedialog.askdirectory()
            self.directories.append(dirPath)
            puts(colored.magenta('New Folder: '+dirPath))
            print('')
            puts(colored.green('Do you want to add another folder?[Y/N] '), False)
            choice = input()
            if not (choice == 'Y' or choice == 'y'):
                newDirectory = False
    
    def defPattern(self, pattern):
        self.pattern = pattern
        self.target ={}

    def loadDirectoriesTarget(self):
        for group in self.pattern:
            puts(colored.green('Please tell us where to put '+group+' files'))
            time.sleep(1)
            root = tk.Tk()
            root.withdraw()
            dirPath = filedialog.askdirectory()
            self.target[group]=dirPath
            puts(colored.magenta('Folder target: '+dirPath))

    def cleanDirectiories(self):
        for dir in self.directories:
            dirItems = os.listdir(dir)
            for item in dirItems:
                path = str(dir+'/'+item)
                if os.path.isfile(path):
                    for group in self.pattern:
                        if list(filter(path.endswith,self.pattern[group]))!=[]:
                            os.replace(path, self.target[group]+'/'+item)
                            break