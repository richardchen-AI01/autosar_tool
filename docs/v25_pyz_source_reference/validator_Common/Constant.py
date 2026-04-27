# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\Constant.py
import os, sys
PROJ_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMON_PATH = os.path.join(PROJ_ROOT, "Common")
EXE_RUN_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
LOG_FOLDER = os.path.join(EXE_RUN_PATH, "logs")
LOG_FILE = os.path.join(EXE_RUN_PATH, "logs/SingletonValidator.log")
OUTPUT_PATH = os.path.join(COMMON_PATH, "output/")
