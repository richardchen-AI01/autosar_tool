# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DltArgument.py
from .Identifiable import Identifiable

class DltArgument(Identifiable):

    def __init__(self):
        super().__init__()
        from .DltMessage import DltMessage
        from .SwDataDefProps import SwDataDefProps
        self._artop_dltMessage = None
        self._artop_networkRepresentation = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dltMessage':"DLT-MESSAGE", 
         '_artop_networkRepresentation':"SW-DATA-DEF-PROPS"})

    @property
    def ref_dltMessage_(self):
        return self._artop_dltMessage

    @property
    def dltMessage_(self):
        if self._artop_dltMessage is not None:
            if hasattr(self._artop_dltMessage, "uuid"):
                return self._artop_dltMessage.uuid
        return

    @property
    def ref_networkRepresentation_(self):
        return self._artop_networkRepresentation

    @property
    def networkRepresentation_(self):
        if self._artop_networkRepresentation is not None:
            if hasattr(self._artop_networkRepresentation, "uuid"):
                return self._artop_networkRepresentation.uuid
        return
