import sys
import os
import webbrowser
import keyboard

file_name = input("Enter the file name (without extension): ")
file = open(f'saved-groups/{file_name}.txt', "r")
lines = file.read().replace('[', '').replace(']', '').replace('"', '').replace(',', '').split()
file.close()

file = open(f'saved-groups/{file_name}-remaining.txt', "w")
for line in lines:
    file.write(f'{line}')
file.close()

webbrowser.open('https://www.google.com')

for line in lines:
    webbrowser.open(line)
    keyboard.wait('space')
    keyboard.press_and_release('ctrl+w')
    print(f'Opening {line}')
    remaining_file = open(f'saved-groups/{file_name}-remaining.txt', "r")
    remaining_lines = remaining_file.readlines()
    remaining_file.close()
    remaining_file = open(f'saved-groups/{file_name}-remaining.txt', "w")
    remaining_file.writelines(remaining_lines[1:])
    remaining_file.close()
    print(f'saved-groups/{file_name}-remaining.txt updated')

print('All links opened')
# delete the remaining file if we make it to the end
os.remove(f'saved-groups/{file_name}-remaining.txt')
print(f'saved-groups/{file_name}-remaining.txt deleted')

      