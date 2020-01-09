import sys
import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256=hashlib.sha256()

if len(sys.argv)==1:
    print("Usage: python.exe calc_hash.py [file_to_be_hashed]")
    print("Or usage python.exe calc_hash.py [file_to_be_hashed] [file_with_checksum_to_compare_with]")

if len(sys.argv)==2:
    with open(sys.argv[1], 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
            sha256.update(data)
    with open(sys.argv[1]+"_hash.txt","w") as f:
        print("MD5: {0}".format(md5.hexdigest()),file=f)
        print("SHA1: {0}".format(sha1.hexdigest()),file=f)
        print("SHA256: {0}".format(sha256.hexdigest()),file=f)
elif len(sys.argv)==3:
    with open(sys.argv[1], 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
            sha256.update(data)

    print("MD5: {0}".format(md5.hexdigest()))
    print("SHA1: {0}".format(sha1.hexdigest()))
    print("SHA256: {0}".format(sha256.hexdigest()))
    with open(sys.argv[2], 'r') as f:
        lines=f.readlines()
        for line in lines:
            if line.startswith("SHA256"):
                sha=line.split(": ")[1].strip()
                if sha.isupper():
                    sha=sha.lower()
                print(f"sha in hash-file: {sha}")
                if sha==sha256.hexdigest():
                    print("SHA256 hashes are equal")
                else:
                    print("SHA256 hashes are NOT equal")