# Multi-Clipboard
This is a simple, possibly broken code that implements reusable copying
# Requirements
  - colorama==0.4.3
  - pyperclip==1.8.0
  - configparser==5.0.0
  - keyboard==0.13.5

# Config
 - `clipboard` - number of the file to which the copied text will be written (max 9)
 - `logging` - logging in the console ('0' - false; '1' - true)
 - `save_changes` - will it be saved *clipboard* ('0' - false; '1' - true)


# Usage
 When you press ```Ctrl + C```, the script saves the copied text to a file. To restore it back to the clipboard, press ```Ctrl + {clipboard}```
```{clipboard}``` is a number from 1 to 9
