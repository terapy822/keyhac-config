import sys
import os
import datetime

import pyauto
from keyhac import *

# keylist https://crftwr.github.io/keyhac/doc/ja/

def get_path_is_func(paths=None, not_=False):
    def path_is(wnd):
        if paths is None:
            return True
        else:
            pname = wnd.getProcessName()
            print("bb", pname)
            if not_:
                return not pname in paths
            else:
                return pname in paths
    return path_is

def configure(keymap):
    keymap.replaceKey("RCtrl", 235)
    keymap.defineModifier( 235, "User0" )

    # global
    def undo_replace_yen():
        keymap.replaceKey("Yen", "Yen")
        keymap.replaceKey("BackSlash", "BackSlash")

    keymap.replaceKey("RCtrl", 235)
    keymap_global = keymap.defineWindowKeymap(check_func=get_path_is_func(["freepiano.exe"], True))
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
    keymap_global[ "U0-I" ] = "Ctrl-I"
    keymap_global.applying_func = undo_replace_yen

    # freepiano
    def replace_yen():
        keymap.replaceKey("Yen", "Esc")
        keymap.replaceKey("BackSlash", "P")

    keymap_piano = keymap.defineWindowKeymap(check_func=get_path_is_func(["freepiano.exe"]))
    keymap_piano.applying_func = replace_yen
	
