# simple-hash-checksum
Just another simple hash checksum MD5, SHA1, SHA256  
https://stackoverflow.com/questions/22058048/hashing-a-file-in-python  
Example:  
>python calc_hash.py  
Usage: python.exe calc_hash.py [file_to_be_hashed]  
Or usage python.exe calc_hash.py [file_to_be_hashed] [file_with_checksum_to_compare_with]

>python calc_hash.py calc_hash.py - creates file calc_hash.py_hash.txt with checksums  

>python calc_hash.py calc_hash.py calc_hash.py_hash.txt  
MD5: 666b71f47b12c67e40a5af79ae143a2a  
SHA1: 2aea9420a63264e1bdca3af8cc7e7ad305b308c1  
SHA256: 747a14d45eb0867f96845cd0bf16206a6016914be43700319e95be59f1aa0487  
sha: 747a14d45eb0867f96845cd0bf16206a6016914be43700319e95be59f1aa0487  
SHA256 hashes are equal
