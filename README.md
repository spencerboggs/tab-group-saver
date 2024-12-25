# Tab Group Saver

A Python script that allows you to save and open groups of links in Google Chrome. You can save a set of links as a group, and later open them all at once in a new Chrome window or tab. It provides an easy way to organize and open multiple tabs for different tasks or projects.

## Features
* **Save Link Groups**: Save multiple links into named groups for easy access.
* **Open Saved Groups**: Open all the links in a saved group in new tabs of Google Chrome automatically.
* **User-friendly Interface**: Simple command-line interface for saving and opening groups.
* **Automatic Chrome Window Handling**: The script attempts to find and maximize the Google Chrome window before opening the links.

## Dependencies
The project requires the following Python libraries:
* `pyautogui`
* `pygetwindow`

You can install them via pip:
```
pip install pyautogui pygetwindow
```

## Usage
1. Clone the repo and navigate into the project directory:
```
git clone https://github.com/spencerboggs/tab-group-saver.git cd tab-group-saver
```

2. Run the script:
```
python main.py
```


3. The script will prompt you with the following options:
   - **1**: Save a new group of links
   - **2**: Open a saved group of links
   - **3**: Exit the program

### Saving a Group
When selecting **1** to save a new group, you will be asked to enter the name of the group and then provide the links you want to include in that group. You can enter multiple links and press enter without typing anything to stop.

### Opening a Group
When selecting **2**, the script will display a list of all saved groups. You can choose which group to open by entering its corresponding number. It will open all links in that group in new tabs in your Google Chrome browser.

### Notes
* Ensure that Google Chrome is open before using the "Open Group" function. The script will attempt to maximize the Chrome window and open the links in new tabs.
* The saved groups are stored in a folder named `saved-groups`. Each group is saved as a `.txt` file containing the list of links in JSON format.
