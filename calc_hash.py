import sys
import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256=hashlib.sha256()

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
'''
with open(sys.argv[2], 'rb') as f:
        lines=f.readlines()
        for line in lines:
            if line.startswith("SHA256"):
                sha=line.split(": ").strip()
                if sha==sha256.hexdigest():
                    print("SHA256 hashes are equal")
                else:
                    print("SHA256 hashes are NOT equal")
'''                    

'''
def get_digest(file_path):
    h = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()
'''
