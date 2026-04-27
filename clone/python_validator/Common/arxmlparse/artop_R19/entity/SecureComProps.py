# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SecureComProps.py
from .Identifiable import Identifiable

class SecureComProps(Identifiable):

    def __init__(self):
        super().__init__()
        from .SecureComPropsSet import SecureComPropsSet
        self._artop_secureComPropsSet = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_secureComPropsSet": "SECURE-COM-PROPS-SET"})

    @property
    def ref_secureComPropsSet_(self):
        return self._artop_secureComPropsSet

    @property
    def secureComPropsSet_(self):
        if self._artop_secureComPropsSet is not None:
            if hasattr(self._artop_secureComPropsSet, "uuid"):
                return self._artop_secureComPropsSet.uuid
        return
