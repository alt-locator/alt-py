# From: https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import config
import network_utils