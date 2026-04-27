# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayFifoRange.py
from .ARObject import ARObject

class FlexrayFifoRange(ARObject):

    def __init__(self):
        super().__init__()
        from .FlexrayFifoConfiguration import FlexrayFifoConfiguration
        self._artop_rangeMax = None
        self._artop_rangeMin = None
        self._artop_flexrayFifoConfiguration = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_flexrayFifoConfiguration": "FLEXRAY-FIFO-CONFIGURATION"})

    @property
    def rangeMax_(self):
        if self._artop_rangeMax:
            return int(self._artop_rangeMax)
        return self._artop_rangeMax

    @property
    def rangeMin_(self):
        if self._artop_rangeMin:
            return int(self._artop_rangeMin)
        return self._artop_rangeMin

    @property
    def ref_flexrayFifoConfiguration_(self):
        return self._artop_flexrayFifoConfiguration

    @property
    def flexrayFifoConfiguration_(self):
        if self._artop_flexrayFifoConfiguration is not None:
            if hasattr(self._artop_flexrayFifoConfiguration, "uuid"):
                return self._artop_flexrayFifoConfiguration.uuid
        return
