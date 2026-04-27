# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApApplicationErrorSet.py
from .UploadablePackageElement import UploadablePackageElement

class ApApplicationErrorSet(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .ApApplicationError import ApApplicationError
        self._artop_apApplicationErrorRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_apApplicationErrorRef": "AP-APPLICATION-ERROR"})

    @property
    def ref_apApplicationErrors_(self):
        return self._artop_apApplicationErrorRef

    @property
    def apApplicationErrors_(self):
        return self._artop_apApplicationErrorRef
