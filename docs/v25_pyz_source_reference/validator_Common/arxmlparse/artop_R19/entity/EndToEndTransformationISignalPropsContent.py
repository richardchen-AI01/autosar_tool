# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EndToEndTransformationISignalPropsContent.py
from .TransformationISignalPropsContent import TransformationISignalPropsContent

class EndToEndTransformationISignalPropsContent(TransformationISignalPropsContent):

    def __init__(self):
        super().__init__()
        self._artop_dataId = None
        self._artop_dataLength = None
        self._artop_maxDataLength = None
        self._artop_minDataLength = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def dataId_(self):
        return self._artop_dataId

    @property
    def dataLength_(self):
        return self._artop_dataLength

    @property
    def maxDataLength_(self):
        return self._artop_maxDataLength

    @property
    def minDataLength_(self):
        return self._artop_minDataLength
