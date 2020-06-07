from colors import *

import pyperclip as pc
import keyboard as kb
from configparser import ConfigParser

from time import sleep
import os

init()
class Clipboard:
    def __init__(self, config_file):
        self.config_file = config_file
        self.get_options()
        self.dir = os.getcwd() + '/clipboards' # dir with all clipboards
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        # add hotkeys to insert text to clipboard
        kb.add_hotkey('Ctrl + 1', lambda: self.paste_text('1'))
        kb.add_hotkey('Ctrl + 2', lambda: self.paste_text('2'))
        kb.add_hotkey('Ctrl + 3', lambda: self.paste_text('3'))
        kb.add_hotkey('Ctrl + 4', lambda: self.paste_text('4'))
        kb.add_hotkey('Ctrl + 5', lambda: self.paste_text('5'))
        kb.add_hotkey('Ctrl + 6', lambda: self.paste_text('6'))
        kb.add_hotkey('Ctrl + 7', lambda: self.paste_text('7'))
        kb.add_hotkey('Ctrl + 8', lambda: self.paste_text('8'))
        kb.add_hotkey('Ctrl + 9', lambda: self.paste_text('9'))
        kb.add_hotkey('Ctrl + C', self.copy_trigger)
        kb.wait('Ctrl + Q') # Ctrl + Q to quit
        if self.save_changes:
            self.end_script()


    # getting parameters
    def get_options(self):
        self.config = ConfigParser()
        self.config.read(self.config_file)
        self.clipboard = int(self.config['options']['clipboard'])
        self.is_logging = int(self.config['options']['logging'])
        self.save_changes = int(self.config['options']['save_changes'])


    # when 'Ctrl + C' is pressed
    def copy_trigger(self):
        sleep(0.1) # wait for value
        current_text = pc.paste() # get value from clipboard
        if self.is_logging:
            print('{color}Ctrl + C was triggered\nText in clipboard:\n{white}{}\n' \
                .format(current_text, color=green, white=white))
        with open(os.getcwd() + '/clipboards/' + str(self.clipboard) + '.txt', 'w') as file:
            file.write(current_text)
            if self.clipboard != 9:
                self.clipboard += 1
            else:
                print(f'{red}`Bufer` is overloaded')
                self.clipboard = 1


    # paste text to clipboard
    def paste_text(self, num_file):
        list_dir = os.listdir(self.dir) # dir with clipboards
        files = [i[:1] for i in list_dir if i.endswith('.txt')]
        if num_file in files:
            with open(self.dir + '/' + num_file + '.txt', 'r') as file:
                text = file.read().strip()
                pc.copy(text) # set value to clipboard
            print(f'{yellow}Text inserted')
        else:
            print(f'{red}Clipboard is missing')


    # update config
    def end_script(self):
        self.config.set('options', 'clipboard', str(self.clipboard))
        with open(self.config_file, "w") as configfile:
            self.config.write(configfile)

cp = Clipboard('config.cfg')
