import os
import time
import json
import pyautogui
import pygetwindow
from pygetwindow import PyGetWindowException

def create_saved_groups_folder():
    if not os.path.exists('saved-groups'):
        os.makedirs('saved-groups')

def save_group():
    group_name = input('Enter the name of the group: ')
    group = []
    while True:
        link = input('Enter a link to save in the group (enter nothing to stop): ')
        if link == '':
            break
        group.append(link)
    with open(f'saved-groups/{group_name}.txt', 'w') as f:
        f.write(json.dumps(group))
    print('Group saved successfully!')

def open_group():
    group_name = input('Enter the name of the group to open: ')
    with open(f'saved-groups/{group_name}.txt', 'r') as f:
        group = json.loads(f.read())
    
    try:
        chrome = pygetwindow.getWindowsWithTitle('Google Chrome')[0]
        pyautogui.hotkey('win', 'm')
        chrome.maximize()
        width, _ = pyautogui.size()
        pyautogui.click(width / 2, 10)
        
    except PyGetWindowException:
        print('Google Chrome not found. Please open Google Chrome first')
        return
    for link in group:
        print(f'Opening {link}')
        time.sleep(1)

        pyautogui.hotkey('ctrl', 't')
        pyautogui.typewrite(link)
        pyautogui.press('enter')
        time.sleep(1)

def main():
    create_saved_groups_folder()
    while True:
        print('1. Save group')
        print('2. Open group')
        print('3. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            save_group()
        elif choice == '2':
            open_group()
        elif choice == '3':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()