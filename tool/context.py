# From: https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
libdir = os.path.join(os.path.dirname(currentdir), 'lib')
sys.path.insert(0, libdir) 

import config
import network_utils
import storage