# keyhac-config

Enjoy Your Emacs Keybinds ;)  

## Setup
1. Run `CapsLock2Ctrl.reg`.
2. Restart windows.
3. Download and extract [Keyhac](https://sites.google.com/site/craftware/keyhac-ja)
4. Run `keyhac.exe` in the extracted folder.
5. Right-click Keyhac icon in the task tray and click **Edit setting**.
6. Replace all the exsiting codes with the following,
    ~~~python
    import sys
    import os
    import datetime

    import pyauto
    from keyhac import *

    def configure(keymap):
        keymap.replaceKey("RCtrl", 235)
        keymap.defineModifier( 235, "User0" )

        # global
        keymap_global = keymap.defineWindowKeymap()
        keymap_global[ "U0-A" ] = "Home"
        keymap_global[ "U0-E" ] = "End"
        keymap_global[ "U0-F" ] = "Right"
        keymap_global[ "U0-B" ] = "Left"
        keymap_global[ "U0-N" ] = "Down"
        keymap_global[ "U0-P" ] = "Up"
        keymap_global[ "U0-D" ] = "Delete"
        keymap_global[ "U0-H" ] = "Back"
        keymap_global[ "U0-K" ] = "Shift-End", "Delete"
        keymap_global[ "U0-U" ] = "Shift-Home", "Delete"
    ~~~
5. Save the changes.
6. Right-click Keyhac icon in the task tray and click **Reload setting**.
7. Press **Win + R** and type `shell:startup` to open a directory `Startup`.
8. Copy `keyhac.exe` in the extracted directory and paste its **shortcut** in the `Startup` directory.
