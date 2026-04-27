# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SynchronizedSlaveTimeBase.py
from .TimeBaseResource import TimeBaseResource

class SynchronizedSlaveTimeBase(TimeBaseResource):

    def __init__(self):
        super().__init__()
        from .GlobalTimeSlave import GlobalTimeSlave
        self._artop_networkTimeSlaveRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_networkTimeSlaveRef": "GLOBAL-TIME-SLAVE"})

    @property
    def ref_networkTimeSlave_(self):
        return self._artop_networkTimeSlaveRef

    @property
    def networkTimeSlave_(self):
        if self._artop_networkTimeSlaveRef is not None:
            if hasattr(self._artop_networkTimeSlaveRef, "uuid"):
                return self._artop_networkTimeSlaveRef.uuid
        return
