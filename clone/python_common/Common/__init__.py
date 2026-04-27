"""Common framework (replaces V25.10 ORIENTAISBswGen.exe's Common/*.pyd).

V25.10 把这一批 helper 用 Cython 编成 Windows native DLL（.pyd），不可反编。
我们这里用纯 Python 重写，参考 docs §15 的 reverse-engineering 结论 +
ORIENTAISBswVal.exe/data/Bsw/MemIf/MemIfRules.py 里的调用现场。

D1 只写 MemIf 实际用到的 5 个: BswBase / Public / CodeGenerator / Context / J2Filters
其余 8 个先 stub, D6 补齐。
"""
