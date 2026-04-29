#!/usr/bin/env python3
"""tools/decrypt-isoft.py — 解 iSoft 加密 .class 文件

iSoft V25.10 把 OSGi bundle 里所有 .class 文件做了**单字节 XOR 0x21** 处理，
导致标准 javap / CFR / Procyon 报 'Bad magic number'（首 4 字节是 eb df 9b 9f
而非 ca fe ba be）。

ADR 0006 当时主动放弃这条路（保守法律姿态）；用户在 v0.1 研究 demo 阶段
明确选择 走 B 路径——解密后**仅作架构参考**，不直接复制代码。

法律边界：
  - 你必须是 ORIENTAIS V25.10 的合法持有者
  - 解密后的源码 / 字节码**不入 git**（tools/_decompile/ + 相关 dir 已在 .gitignore）
  - 写自己实现时**只参考结构**，变量名/注释/类名都重写
  - v0.3 商业化必须放弃所有 B 路径产物，重做 clean-room

用法：
  python3 tools/decrypt-isoft.py <input.jar> [<input2.jar> ...]
  → 在每个输入旁边产出 <name>.decrypted.jar
"""
import sys
import zipfile
import os

CLEAN_MAGIC = bytes([0xCA, 0xFE, 0xBA, 0xBE])
ENCRYPTED_MAGIC = bytes([0xEB, 0xDF, 0x9B, 0x9F])
XOR_KEY = 0x21


def decrypt_class_bytes(data: bytes) -> bytes:
    """XOR 每个字节 0x21；如果首 4 字节已经是 ca fe ba be 说明这个 class
    没加密（jar 里有时混装），直接返回原文。"""
    if len(data) < 4:
        return data
    if data[:4] == CLEAN_MAGIC:
        return data
    if data[:4] != ENCRYPTED_MAGIC:
        # Unknown magic — leave alone
        return data
    return bytes(b ^ XOR_KEY for b in data)


def decrypt_jar(in_path: str, out_path: str) -> tuple[int, int]:
    """返回 (decrypted_class_count, total_files)"""
    decrypted = 0
    total = 0
    with zipfile.ZipFile(in_path, 'r') as zin:
        with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zout:
            for name in zin.namelist():
                total += 1
                data = zin.read(name)
                if name.endswith('.class'):
                    new_data = decrypt_class_bytes(data)
                    if new_data is not data:
                        decrypted += 1
                    data = new_data
                zout.writestr(name, data)
    return decrypted, total


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)

    for in_path in sys.argv[1:]:
        if not os.path.isfile(in_path):
            print(f"[SKIP] not a file: {in_path}", file=sys.stderr)
            continue
        base, ext = os.path.splitext(in_path)
        out_path = base + ".decrypted" + ext
        decrypted, total = decrypt_jar(in_path, out_path)
        print(f"[OK]   {in_path}")
        print(f"       → {out_path}")
        print(f"       decrypted {decrypted}/{total} entries")


if __name__ == '__main__':
    main()
