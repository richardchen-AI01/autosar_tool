# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DelegationSwConnector.py
from .SwConnector import SwConnector

class DelegationSwConnector(SwConnector):

    def __init__(self):
        super().__init__()
        from .PortInCompositionTypeInstanceRef import PortInCompositionTypeInstanceRef
        from .PortPrototype import PortPrototype
        self._artop_innerPortIref = None
        self._artop_outerPortRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_innerPortIref':"PORT-IN-COMPOSITION-TYPE-INSTANCE-REF-IREF", 
         '_artop_outerPortRef':"PORT-PROTOTYPE"})

    @property
    def ref_innerPort_(self):
        return self._artop_innerPortIref

    @property
    def innerPort_(self):
        if self._artop_innerPortIref is not None:
            if hasattr(self._artop_innerPortIref, "uuid"):
                return self._artop_innerPortIref.uuid
        return

    @property
    def ref_outerPort_(self):
        return self._artop_outerPortRef

    @property
    def outerPort_(self):
        if self._artop_outerPortRef is not None:
            if hasattr(self._artop_outerPortRef, "uuid"):
                return self._artop_outerPortRef.uuid
        return
