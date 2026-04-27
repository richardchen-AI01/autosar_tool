# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FileInfoComment.py
from .ARObject import ARObject

class FileInfoComment(ARObject):

    def __init__(self):
        super().__init__()
        from .AUTOSAR import AUTOSAR
        from .Sdg import Sdg
        self._artop_autosar = None
        self._artop_sdg = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_autosar':"AUTOSAR", 
         '_artop_sdg':"SDG"})

    @property
    def ref_aUTOSAR_(self):
        return self._artop_autosar

    @property
    def aUTOSAR_(self):
        if self._artop_autosar is not None:
            if hasattr(self._artop_autosar, "uuid"):
                return self._artop_autosar.uuid
        return

    @property
    def sdgs_Sdg(self):
        return self._artop_sdg
