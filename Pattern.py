from typing import Pattern
from clint.textui import puts, colored, indent


class Pattern:
    def __init__(self):
        self.standard = {
            'Documents': ['zip', 'rar', 'pdf', 'doc', 'docx', 'xls', 'csv', 'txt', 'ppt', 'pptx', 'cpp', 'py', 'js'],
            'Videos': ['mp4', 'flv', 'avi', 'mkv'],
            'Music': ['mp3', 'wav'],
            'Images': ['png', 'jpg', 'jpeg', 'webp', 'gif']
        }

    def update(self):
        newUpdate = True
        while newUpdate:
            puts(colored.green('Do you want to '), False)
            puts(colored.magenta('ADD '), False)
            puts(colored.green('a new group, '), False)
            puts(colored.magenta('DEL '), False)
            puts(colored.green('an existing group? '), False)
            action = input()
            if action == 'ADD' or action == 'add':
                self.newGroup()
            elif action == 'DEL' or action == 'del':
                self.delGroup()
            else:
                puts(colored.magenta("Invalid option"))
            puts(colored.green('Do you want to make another update?[Y/N] '), False)
            choice = input()
            if not (choice == 'Y' or choice == 'y'):
                newUpdate = False

    def printPattern(self):
        for key, value in self.standard.items():
            puts(colored.magenta(key+': '+str(value)))

    def create(self):
        self.standard = {}
        self.newGroup()
        puts(colored.green('Are you finished?[Y/N] '), False)
        choice = input()
        if not (choice == 'N' or choice == 'n'):
            self.update()

    def newGroup(self):
        puts(colored.green("What's the name of the new group "), False)
        groupName = input()
        puts(colored.green("What are the extensions for this group? Separate them with a comma "), False)
        groupExt = input().split(',')
        self.standard[groupName] = groupExt
        puts(colored.magenta("Group created"))

    def delGroup(self):
        puts(colored.green("What group do you want to delete? "), False)
        groupToDelete = input()
        if groupToDelete in self.standard:
            self.standard.pop(groupToDelete, None)
            puts(colored.magenta("Group removed"))
        else:
            puts(colored.magenta("This group doesn't exists "))
