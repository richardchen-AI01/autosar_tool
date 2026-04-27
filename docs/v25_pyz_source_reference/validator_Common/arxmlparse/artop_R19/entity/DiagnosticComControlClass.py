# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticComControlClass.py
from .DiagnosticServiceClass import DiagnosticServiceClass

class DiagnosticComControlClass(DiagnosticServiceClass):

    def __init__(self):
        super().__init__()
        from .CommunicationCluster import CommunicationCluster
        from .DiagnosticComControlSpecificChannel import DiagnosticComControlSpecificChannel
        from .DiagnosticComControlSubNodeChannel import DiagnosticComControlSubNodeChannel
        self._artop_allChannelsRef = []
        self._artop_specificChannel = []
        self._artop_subNodeChannel = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_allChannelsRef':"COMMUNICATION-CLUSTER", 
         '_artop_specificChannel':"DIAGNOSTIC-COM-CONTROL-SPECIFIC-CHANNEL", 
         '_artop_subNodeChannel':"DIAGNOSTIC-COM-CONTROL-SUB-NODE-CHANNEL"})

    @property
    def ref_allChannels_(self):
        return self._artop_allChannelsRef

    @property
    def allChannels_(self):
        return self._artop_allChannelsRef

    @property
    def specificChannels_DiagnosticComControlSpecificChannel(self):
        return self._artop_specificChannel

    @property
    def subNodeChannels_DiagnosticComControlSubNodeChannel(self):
        return self._artop_subNodeChannel
