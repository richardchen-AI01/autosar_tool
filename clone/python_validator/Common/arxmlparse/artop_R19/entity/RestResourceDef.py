# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RestResourceDef.py
from .Identifiable import Identifiable

class RestResourceDef(Identifiable):

    def __init__(self):
        super().__init__()
        from .RestElementDef import RestElementDef
        from .RestAbstractEndpoint import RestAbstractEndpoint
        from .RestSystemTriggeredEvent import RestSystemTriggeredEvent
        self._artop_element = []
        self._artop_endpoint = []
        self._artop_resource = []
        self._artop_systemTriggeredEvent = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_element': '"REST-ELEMENT-DEF"', 
         '_artop_endpoint': '"REST-ABSTRACT-ENDPOINT"', 
         '_artop_resource': '"REST-RESOURCE-DEF"', 
         '_artop_systemTriggeredEvent': '"REST-SYSTEM-TRIGGERED-EVENT"'})

    @property
    def elements_RestElementDef(self):
        return self._artop_element

    @property
    def endpoints_RestAbstractEndpoint(self):
        return self._artop_endpoint

    @property
    def resources_RestResourceDef(self):
        return self._artop_resource

    @property
    def systemTriggeredEvents_RestSystemTriggeredEvent(self):
        return self._artop_systemTriggeredEvent
