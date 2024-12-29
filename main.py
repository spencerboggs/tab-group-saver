import os
import time
import json
import webbrowser
import keyboard
import pyperclip
import pyautogui
import pygetwindow as gw

def create_saved_groups_folder():
    if not os.path.exists('saved-groups'):
        os.makedirs('saved-groups')

def save_group_manually():
    group_name = input('Enter the name of the group: ').strip()
    if not group_name:
        print("Group name cannot be empty!")
        return

    group = []
    while True:
        link = input('Enter a link to save in the group (enter nothing to stop): ').strip()
        if link == '':
            break
        group.append(link)

    with open(f'saved-groups/{group_name}.txt', 'w') as f:
        json.dump(group, f)
    print(f'Group "{group_name}" saved successfully!')

def save_group_auto():
    group_name = input('Enter the name of the group: ').strip()
    if not group_name:
        print("Group name cannot be empty!")
        return

    group = []
    print("Ensure Google Chrome is active and all tabs are loaded.")
    time.sleep(4)

    max_tabs = 50

    for _ in range(max_tabs):
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'insert')
        time.sleep(0.5)

        link = pyperclip.paste().strip()
        if not link or link in group:
            print("Duplicate or invalid link detected, stopping.")
            break

        group.append(link)
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)

    if group:
        with open(f'saved-groups/{group_name}.txt', 'w') as f:
            json.dump(group, f)
        print(f'Group "{group_name}" saved successfully! Total links saved: {len(group)}')
    else:
        print("No tabs detected or saved.")

def open_group():
    files = [file for file in os.listdir('saved-groups') if file.endswith('.txt')]
    if not files:
        print('No groups saved yet.')
        return

    print('Select a group to open:')
    for i, file in enumerate(files, start=1):
        print(f'{i}. {file[:-4]}')

    while True:
        try:
            choice = int(input('Enter the number of the group to open: '))
            if 1 <= choice <= len(files):
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid choice. Please enter a valid number.')

    with open(f'saved-groups/{files[choice - 1]}', 'r') as f:
        group = json.load(f)

    for link in group:
        print(f'Opening {link}')
        webbrowser.open(link)
        time.sleep(1)

def open_group_sequentially():
    files = [file for file in os.listdir('saved-groups') if file.endswith('.txt')]
    if not files:
        print('No groups saved yet.')
        return

    print('Select a group to open:')
    for i, file in enumerate(files, start=1):
        print(f'{i}. {file[:-4]}')

    while True:
        try:
            choice = int(input('Enter the number of the group to open: '))
            if 1 <= choice <= len(files):
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid choice. Please enter a valid number.')

    with open(f'saved-groups/{files[choice - 1]}', 'r') as f:
        group = json.load(f)
        file_name = files[choice - 1][:-4]

    file = open(f'saved-groups/{file_name}-remaining.txt', "w")

    webbrowser.open('https://www.google.com')

    for link in group:
        webbrowser.open(link)
        keyboard.wait('space')
        keyboard.press_and_release('ctrl+w')
        print(f'Opening {link}')
        remaining_file = open(f'saved-groups/{file_name}-remaining.txt', "r")
        remaining_lines = remaining_file.readlines()
        remaining_file.close()
        remaining_file = open(f'saved-groups/{file_name}-remaining.txt', "w")
        remaining_file.writelines(remaining_lines[1:])
        remaining_file.close()
        print(f'saved-groups/{file_name}-remaining.txt updated')

    print('All links opened')
    os.remove(f'saved-groups/{file_name}-remaining.txt')
    print(f'saved-groups/{file_name}-remaining.txt deleted')

def add_links_to_group():
    files = [file for file in os.listdir('saved-groups') if file.endswith('.txt')]
    if not files:
        print('No groups saved yet.')
        return

    print('Select a group to add links to:')
    for i, file in enumerate(files, start=1):
        print(f'{i}. {file[:-4]}')

    while True:
        try:
            choice = int(input('Enter the number of the group to open: '))
            if 1 <= choice <= len(files):
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid choice. Please enter a valid number.')
            
    with open(f'saved-groups/{files[choice - 1]}', 'r') as f:
        group = json.load(f)

    while True:
        link = input('Enter a link to save in the group (enter nothing to stop): ').strip()
        if link == '':
            break
        group.append(link)

    with open(f'saved-groups/{files[choice - 1]}', 'w') as f:
        json.dump(group, f)

    print(f'Group "{files[choice - 1][:-4]}" saved successfully!')

def add_links_to_group_auto():
    files = [file for file in os.listdir('saved-groups') if file.endswith('.txt')]
    if not files:
        print('No groups saved yet.')
        return

    print('Select a group to add links to:')
    for i, file in enumerate(files, start=1):
        print(f'{i}. {file[:-4]}')

    while True:
        try:
            choice = int(input('Enter the number of the group to open: '))
            if 1 <= choice <= len(files):
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid choice. Please enter a valid number.')
            
    with open(f'saved-groups/{files[choice - 1]}', 'r') as f:
        group = json.load(f)

    print("Ensure Google Chrome is active and all tabs are loaded.")
    time.sleep(4)

    max_tabs = 50
    new_tabs = []

    for _ in range(max_tabs):
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'insert')
        time.sleep(0.5)

        link = pyperclip.paste().strip()
        if not link or link in new_tabs:
            print("Duplicate or invalid link detected, stopping.")
            break

        new_tabs.append(link)
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)

    for link in new_tabs:
        group.append(link)

    with open(f'saved-groups/{files[choice - 1]}', 'w') as f:
        json.dump(group, f)

    print(f'Group "{files[choice - 1][:-4]}" saved successfully! Total links saved: {len(group)}')

def remove_tab_group_entries():
    files = [file for file in os.listdir('saved-groups') if file.endswith('.txt')]
    if not files:
        print('No groups saved yet.')
        return

    print('Select a group to remove links from:')
    for i, file in enumerate(files, start=1):
        print(f'{i}. {file[:-4]}')

    while True:
        try:
            choice = int(input('Enter the number of the group to open: '))
            if 1 <= choice <= len(files):
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid choice. Please enter a valid number.')
            
    with open(f'saved-groups/{files[choice - 1]}', 'r') as f:
        group = json.load(f)

    while True:
        for i, link in enumerate(group):
            print(f'{i}. {link}')

        remove = input('Enter the number of the link to remove (enter nothing to stop): ').strip()
        if remove == '':
            break
        try:
            remove = int(remove)
            if remove < 0 or remove >= len(group):
                raise ValueError
        except ValueError:
            print('Invalid choice. Please enter a valid number.')
            continue

        group.pop(remove)

    with open(f'saved-groups/{files[choice - 1]}', 'w') as f:
        json.dump(group, f)

    print(f'Group "{files[choice - 1][:-4]}" saved successfully!')

def remove_duplicate_links():
    files = [file for file in os.listdir('saved-groups') if file.endswith('.txt')]
    if not files:
        print('No groups saved yet.')
        return

    print('Select a group to remove links from:')
    for i, file in enumerate(files, start=1):
        print(f'{i}. {file[:-4]}')

    while True:
        try:
            choice = int(input('Enter the number of the group to open: '))
            if 1 <= choice <= len(files):
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid choice. Please enter a valid number.')
            
    with open(f'saved-groups/{files[choice - 1]}', 'r') as f:
        group = json.load(f)

    group = list(set(group))

    with open(f'saved-groups/{files[choice - 1]}', 'w') as f:
        json.dump(group, f)

    print(f'Group "{files[choice - 1][:-4]}" saved successfully!')

def main():
    create_saved_groups_folder()
    while True:
        print('\nMenu:')
        print('1. Save group manually')
        print('2. Save group automatically')
        print('3. Open group (All at once)')
        print('4. Open group (One at a time)')
        print('5. Add to a tab group manually')
        print('    - Input links one at a time')
        print('6. Add to a tab group automatically')
        print('    - Will add all links you have open')
        print('7. Remove tab group entries')
        print('8. Remove duplicate links from group')
        print('9. Exit')
        choice = input('Enter your choice: ').strip()

        if choice == '1':
            save_group_manually()
        elif choice == '2':
            save_group_auto()
        elif choice == '3':
            open_group()
        elif choice == '4':
            open_group_sequentially()
        elif choice == '5':
            add_links_to_group()
        elif choice == '6':
            add_links_to_group_auto()
        elif choice == '7':
            remove_tab_group_entries()
        elif choice == '8':
            remove_duplicate_links()
        elif choice == '9':
            break
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    main()
