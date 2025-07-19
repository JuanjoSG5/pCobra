import sys
import os

parent = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Add the sibling project folder
sys.path.insert(0, parent)
backend_path = os.path.join(parent, 'backend')
sys.path.insert(0, os.path.join(backend_path, 'src'))
sys.path.insert(0, os.path.join(backend_path, 'corelibs'))

from core.nativos import *
from standard_library import *
print('Hola, mundo!')