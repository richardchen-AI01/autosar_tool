# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventVfb.py
from .TimingDescriptionEvent import TimingDescriptionEvent

class TDEventVfb(TimingDescriptionEvent):

    def __init__(self):
        super().__init__()
        from .ComponentInCompositionInstanceRef import ComponentInCompositionInstanceRef
        self._artop_componentIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_componentIref": "COMPONENT-IN-COMPOSITION-INSTANCE-REF-IREF"})

    @property
    def ref_component_(self):
        return self._artop_componentIref

    @property
    def component_(self):
        if self._artop_componentIref is not None:
            if hasattr(self._artop_componentIref, "uuid"):
                return self._artop_componentIref.uuid
        return
