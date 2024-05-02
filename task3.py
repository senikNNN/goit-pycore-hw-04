import sys
import os
from pathlib import Path
from colorama import Fore, Style

dir_path = sys.argv[1]

def visualizer(start_directory: Path):
    for root, dirs, files in os.walk(start_directory):
        level = root.replace(start_directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(Fore.LIGHTBLUE_EX + '{}{}/'.format(indent, os.path.basename(root)) + Style.RESET_ALL)
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(Fore.LIGHTYELLOW_EX + '{}{}'.format(subindent, f) + Style.RESET_ALL)



visualizer(dir_path)