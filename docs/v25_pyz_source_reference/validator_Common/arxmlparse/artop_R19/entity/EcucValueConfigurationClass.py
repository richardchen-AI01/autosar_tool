# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucValueConfigurationClass.py
from .EcucAbstractConfigurationClass import EcucAbstractConfigurationClass

class EcucValueConfigurationClass(EcucAbstractConfigurationClass):

    def __init__(self):
        super().__init__()
        from .EcucCommonAttributes import EcucCommonAttributes
        self._artop_ecucCommonAttributes = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ecucCommonAttributes": "ECUC-COMMON-ATTRIBUTES"})

    @property
    def ref_ecucCommonAttributes_(self):
        return self._artop_ecucCommonAttributes

    @property
    def ecucCommonAttributes_(self):
        if self._artop_ecucCommonAttributes is not None:
            if hasattr(self._artop_ecucCommonAttributes, "uuid"):
                return self._artop_ecucCommonAttributes.uuid
        return
