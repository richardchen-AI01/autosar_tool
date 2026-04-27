"""Constant — stub (D6 will fill from V25.10 Common/Constant.pyd).

Reverse-engineered key strings: LOG_FILE, COMMON_PATH, PROJ_ROOT, CONFIG_FOLDER,
TEMPLATE_FILELIST. ArxmlValidator references OUTPUT_PATH from this module.
"""
import os

OUTPUT_PATH = os.environ.get('AUTOSAR_OUTPUT_PATH', 'output')
LOG_FILE = os.environ.get('AUTOSAR_LOG_FILE', 'generator.log')
TEMPLATE_FILELIST = 'FilesList.jinja'
