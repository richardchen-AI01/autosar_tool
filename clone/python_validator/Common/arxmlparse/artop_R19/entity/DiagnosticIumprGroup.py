# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticIumprGroup.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticIumprGroup(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .NameTokenValueVariationPoint import NameTokenValueVariationPoint
        from .DiagnosticIumpr import DiagnosticIumpr
        self._artop_groupIdentifier = None
        self._artop_iumprRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_groupIdentifier':"NAME-TOKEN-VALUE-VARIATION-POINT", 
         '_artop_iumprRef':"DIAGNOSTIC-IUMPR"})

    @property
    def ref_groupIdentifier_(self):
        return self._artop_groupIdentifier

    @property
    def groupIdentifier_(self):
        if self._artop_groupIdentifier is not None:
            if hasattr(self._artop_groupIdentifier, "uuid"):
                return self._artop_groupIdentifier.uuid
        return

    @property
    def ref_iumprs_(self):
        return self._artop_iumprRef

    @property
    def iumprs_(self):
        return self._artop_iumprRef
