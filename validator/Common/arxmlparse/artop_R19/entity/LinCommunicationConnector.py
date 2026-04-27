# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinCommunicationConnector.py
from .CommunicationConnector import CommunicationConnector

class LinCommunicationConnector(CommunicationConnector):

    def __init__(self):
        super().__init__()
        from .LinConfigurableFrame import LinConfigurableFrame
        from .LinOrderedConfigurableFrame import LinOrderedConfigurableFrame
        self._artop_initialNad = None
        self._artop_linConfigurableFrame = []
        self._artop_linOrderedConfigurableFrame = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_linConfigurableFrame':"LIN-CONFIGURABLE-FRAME", 
         '_artop_linOrderedConfigurableFrame':"LIN-ORDERED-CONFIGURABLE-FRAME"})

    @property
    def initialNad_(self):
        if self._artop_initialNad:
            return int(self._artop_initialNad)
        return self._artop_initialNad

    @property
    def linConfigurableFrames_LinConfigurableFrame(self):
        return self._artop_linConfigurableFrame

    @property
    def linOrderedConfigurableFrames_LinOrderedConfigurableFrame(self):
        return self._artop_linOrderedConfigurableFrame
