#!/usr/bin/env python3
"""Decrypt iSoft V25.10 .class files (XOR 0x21) inside a jar.

Usage: decrypt_isoft_jar.py <input.jar> <output_dir>
Result: output_dir/ contains all jar entries; .class files have been XOR-decoded
to standard CAFEBABE classes that javap/CFR can read.
"""
import sys, os, zipfile, shutil

def decrypt_class(b: bytes) -> bytes:
    return bytes(x ^ 0x21 for x in b)

def main():
    src, dst = sys.argv[1], sys.argv[2]
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    n_class = n_other = 0
    with zipfile.ZipFile(src) as z:
        for name in z.namelist():
            if name.endswith('/'):
                continue
            data = z.read(name)
            if name.endswith('.class'):
                # Sanity: detect already-decrypted (CAFEBABE) and skip XOR
                if not (data[:4] == b'\xca\xfe\xba\xbe'):
                    data = decrypt_class(data)
                n_class += 1
            else:
                n_other += 1
            out = os.path.join(dst, name)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, 'wb') as f:
                f.write(data)
    print(f"decoded {n_class} .class + {n_other} other files into {dst}")

if __name__ == '__main__':
    main()
