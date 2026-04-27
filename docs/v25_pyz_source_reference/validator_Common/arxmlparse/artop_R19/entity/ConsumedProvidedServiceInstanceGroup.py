# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ConsumedProvidedServiceInstanceGroup.py
from .FibexElement import FibexElement

class ConsumedProvidedServiceInstanceGroup(FibexElement):

    def __init__(self):
        super().__init__()
        from .ConsumedServiceInstanceRefConditional import ConsumedServiceInstanceRefConditional
        from .ProvidedServiceInstanceRefConditional import ProvidedServiceInstanceRefConditional
        self._artop_consumedServiceInstance = []
        self._artop_providedServiceInstance = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_consumedServiceInstance':"CONSUMED-SERVICE-INSTANCE-REF-CONDITIONAL", 
         '_artop_providedServiceInstance':"PROVIDED-SERVICE-INSTANCE-REF-CONDITIONAL"})

    @property
    def consumedServiceInstances_ConsumedServiceInstanceRefConditional(self):
        return self._artop_consumedServiceInstance

    @property
    def providedServiceInstances_ProvidedServiceInstanceRefConditional(self):
        return self._artop_providedServiceInstance
