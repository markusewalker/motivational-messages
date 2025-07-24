import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

tests_dir = os.path.join(project_root, 'tests')
if tests_dir not in sys.path:
    sys.path.insert(0, tests_dir)