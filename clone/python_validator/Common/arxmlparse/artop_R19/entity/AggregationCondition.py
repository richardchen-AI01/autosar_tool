# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AggregationCondition.py
from .AttributeCondition import AttributeCondition

class AggregationCondition(AttributeCondition):

    def __init__(self):
        super().__init__()
        from .AggregationTailoring import AggregationTailoring
        self._artop_aggregationRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_aggregationRef": "AGGREGATION-TAILORING"})

    @property
    def ref_aggregation_(self):
        return self._artop_aggregationRef

    @property
    def aggregation_(self):
        if self._artop_aggregationRef is not None:
            if hasattr(self._artop_aggregationRef, "uuid"):
                return self._artop_aggregationRef.uuid
        return
