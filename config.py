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

   
