import sys
import os
import datetime

import pyauto
from keyhac import *


def configure(keymap):
    keymap_global = keymap.defineWindowKeymap()
    keymap_global[ "LAlt-A" ] = "Home"
    keymap_global[ "LAlt-E" ] = "End"
    keymap_global[ "LAlt-F" ] = "Right"
    keymap_global[ "LAlt-B" ] = "Left"
    keymap_global[ "LAlt-N" ] = "Down"
    keymap_global[ "LAlt-P" ] = "Up"
    keymap_global[ "LAlt-D" ] = "Delete"
    keymap_global[ "LAlt-H" ] = "Back"

