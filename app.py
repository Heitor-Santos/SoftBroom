from __future__ import print_function
import collections
from DirectoriesManager import DirectoriesManager
from Pattern import Pattern
from os import times
import sys
from clint.arguments import Args
from clint.textui import puts, colored, indent
import tkinter as tk
from tkinter import filedialog
from pyfiglet import Figlet
import time

f = Figlet(font='slant')
print(f.renderText('SoftBroom'))
args = Args()
puts(colored.green('Welcome to the SoftBroom, a tool to help you organize your files'))
puts(colored.green('First of all, pick some folders to clean'))
print('')
time.sleep(1)

userPattern = Pattern()
nastyDirs = DirectoriesManager()
nastyDirs.loadDirectoriesToClean()

print('')
puts(colored.green('Folders to clean:'))
for dir in nastyDirs.directories:
    with indent(4, quote='>>>'):
        puts(colored.magenta(dir))

print('')
puts(colored.green("Now, how do you want to aggregate the files? Here's our standard:"))
userPattern.printPattern()
puts(colored.green('You can '), False)
puts(colored.magenta('USE '), False)
puts(colored.green('it standard as it is, '), False)
puts(colored.magenta('UPDATE '), False)
puts(colored.green('standard or '), False)
puts(colored.magenta('CREATE '), False)
puts(colored.green('a new pattern'))
choice = input()
if choice == 'UPDATE' or choice == 'update':
    userPattern.update()
elif choice == 'CREATE' or choice == 'create':
    userPattern.create()
elif choice != 'USE' and choice != 'use':
    puts(colored.magenta("Invalid option!"))
else:
    puts(colored.green("Your new pattern:"))
    userPattern.printPattern()
    puts(colored.green('Can I start cleaning?[Y/N] '), False)
    choice = input()
    if (choice == 'Y' or choice == 'y'):
        nastyDirs.defPattern(userPattern.standard)
        nastyDirs.loadDirectoriesTarget()
        nastyDirs.cleanDirectiories()
    print('')
    puts(colored.green("Alright! Everything's done!"))
