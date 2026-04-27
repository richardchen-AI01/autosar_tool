# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucChoiceContainerDef.py
from .EcucContainerDef import EcucContainerDef

class EcucChoiceContainerDef(EcucContainerDef):

    def __init__(self):
        super().__init__()
        from .EcucParamConfContainerDef import EcucParamConfContainerDef
        self._artop_choice = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_choice": "ECUC-PARAM-CONF-CONTAINER-DEF"})

    @property
    def choices_EcucParamConfContainerDef(self):
        return self._artop_choice
