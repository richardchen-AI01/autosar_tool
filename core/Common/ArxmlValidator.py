"""ArxmlValidator — V25.10 Common/ArxmlValidator.py (validator side).

Reverse-engineered from validator's pyz_source. The base validator framework
that holds rule metadata (`dict_message`) and orchestrates rule execution.

<Module>ArxmlValidator subclass implements `runRules`. Used as:

    class MemIfArxmlValidator(ArxmlValidator):
        def __init__(self):
            super().__init__()
            super().createMessageData(dir_module)
        def runRules(self, changeTargetDefPath):
            ruleR23 = RuleBSWMemIfR23()
            super().execute_method(ruleR23, changeTargetDefPath)

D1 STATUS: minimal — load JSON message file, hold dict, expose execute_method
that calls all @RuleHandler-decorated functions on `ruleR23`.
"""
from __future__ import annotations
import json
import os
from typing import Any, Dict, List

#: Class-level message store, populated by createMessageData
dict_message: Dict[str, Any] = {}


class ArxmlValidator:
    """Base class for per-module ECUC validators."""

    def __init__(self) -> None:
        self.moduleName = type(self).__name__.replace('ArxmlValidator', '')
        self._results: List[Any] = []

    def createMessageData(self, dir_module: str) -> None:
        """Load <Module>Messages.json from dir_module and merge into dict_message."""
        json_files = [f for f in os.listdir(dir_module) if f.endswith('Messages.json')]
        for jf in json_files:
            path = os.path.join(dir_module, jf)
            with open(path, 'r', encoding='utf-8') as f:
                items = json.load(f)
            for item in items:
                if item.get('active', False):
                    dict_message[item['key']] = item

    def execute_method(self, rule_obj: Any, change_target_def_path: str = '') -> None:
        """Run every @RuleHandler-decorated method on rule_obj, collect results.

        D1 stub: ignores change_target_def_path (M2 will use to filter).
        """
        for attr in dir(rule_obj):
            if attr.startswith('_'):
                continue
            method = getattr(rule_obj, attr)
            if not callable(method):
                continue
            # @RuleHandler-decorated methods are wrapped with functools.wraps,
            # so name still starts with Rule_ when set up properly
            if not attr.startswith('Rule_'):
                continue
            try:
                result = method()
            except Exception as e:
                print(f'  [WARN] rule {attr} raised: {type(e).__name__}: {e}')
                continue
            if result:
                for tup in result:
                    self._results.append((attr, tup))
                    rec = dict_message.get(attr, {})
                    target_uri = tup[0] if len(tup) > 0 else '?'
                    msg_args = tup[1] if len(tup) > 1 else []
                    template = rec.get('message', '<no message>')
                    msg = template.format(*msg_args)
                    print(f'  [{rec.get("level","?")}] {attr}: {msg}  @ {target_uri}')

    def get_results(self) -> List[Any]:
        return self._results
