# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DdsEventQosProps.py
from .DdsQosProps import DdsQosProps

class DdsEventQosProps(DdsQosProps):

    def __init__(self):
        super().__init__()
        from .ServiceEventDeployment import ServiceEventDeployment
        self._artop_eventRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_eventRef": "SERVICE-EVENT-DEPLOYMENT"})

    @property
    def ref_event_(self):
        return self._artop_eventRef

    @property
    def event_(self):
        if self._artop_eventRef is not None:
            if hasattr(self._artop_eventRef, "uuid"):
                return self._artop_eventRef.uuid
        return
