# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanControllerConfigurationRequirements.py
from .AbstractCanCommunicationControllerAttributes import AbstractCanCommunicationControllerAttributes

class CanControllerConfigurationRequirements(AbstractCanCommunicationControllerAttributes):

    def __init__(self):
        super().__init__()
        self._artop_maxNumberOfTimeQuantaPerBit = None
        self._artop_maxSamplePoint = None
        self._artop_maxSyncJumpWidth = None
        self._artop_minNumberOfTimeQuantaPerBit = None
        self._artop_minSamplePoint = None
        self._artop_minSyncJumpWidth = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def maxNumberOfTimeQuantaPerBit_(self):
        if self._artop_maxNumberOfTimeQuantaPerBit:
            return int(self._artop_maxNumberOfTimeQuantaPerBit)
        return self._artop_maxNumberOfTimeQuantaPerBit

    @property
    def maxSamplePoint_(self):
        if self._artop_maxSamplePoint:
            return float(self._artop_maxSamplePoint)
        return self._artop_maxSamplePoint

    @property
    def maxSyncJumpWidth_(self):
        if self._artop_maxSyncJumpWidth:
            return float(self._artop_maxSyncJumpWidth)
        return self._artop_maxSyncJumpWidth

    @property
    def minNumberOfTimeQuantaPerBit_(self):
        if self._artop_minNumberOfTimeQuantaPerBit:
            return int(self._artop_minNumberOfTimeQuantaPerBit)
        return self._artop_minNumberOfTimeQuantaPerBit

    @property
    def minSamplePoint_(self):
        if self._artop_minSamplePoint:
            return float(self._artop_minSamplePoint)
        return self._artop_minSamplePoint

    @property
    def minSyncJumpWidth_(self):
        if self._artop_minSyncJumpWidth:
            return float(self._artop_minSyncJumpWidth)
        return self._artop_minSyncJumpWidth
