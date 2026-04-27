# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipEventProps.py
from .ARObject import ARObject

class SomeipEventProps(ARObject):

    def __init__(self):
        super().__init__()
        from .ProvidedSomeipServiceInstance import ProvidedSomeipServiceInstance
        from .SomeipCollectionProps import SomeipCollectionProps
        from .SomeipEventDeployment import SomeipEventDeployment
        self._artop_providedSomeipServiceInstance = None
        self._artop_collectionProps = None
        self._artop_eventRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_providedSomeipServiceInstance':"PROVIDED-SOMEIP-SERVICE-INSTANCE", 
         '_artop_collectionProps':"SOMEIP-COLLECTION-PROPS", 
         '_artop_eventRef':"SOMEIP-EVENT-DEPLOYMENT"})

    @property
    def ref_providedSomeipServiceInstance_(self):
        return self._artop_providedSomeipServiceInstance

    @property
    def providedSomeipServiceInstance_(self):
        if self._artop_providedSomeipServiceInstance is not None:
            if hasattr(self._artop_providedSomeipServiceInstance, "uuid"):
                return self._artop_providedSomeipServiceInstance.uuid
        return

    @property
    def ref_collectionProps_(self):
        return self._artop_collectionProps

    @property
    def collectionProps_(self):
        if self._artop_collectionProps is not None:
            if hasattr(self._artop_collectionProps, "uuid"):
                return self._artop_collectionProps.uuid
        return

    @property
    def ref_event_(self):
        return self._artop_eventRef

    @property
    def event_(self):
        if self._artop_eventRef is not None:
            if hasattr(self._artop_eventRef, "uuid"):
                return self._artop_eventRef.uuid
        return
