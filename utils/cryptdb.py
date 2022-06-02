from pathlib import Path
import os
import sys
sys.path.append(os.path.join(Path().resolve().parent, 'src', 'chunkcrypt'))
from cryptchunk import encrypt_file, decrypt_file

def_ch_sz = 1024

while True:
    encrt_mode = input('Please specify if \"encrypt\" or \"decrypt\", input the same keyword: ')
    if encrt_mode != 'encrypt' and encrt_mode != 'decrypt':
        print(f'{encrt_mode} is not a valid encryption mode')
        continue
    encrt_key = None
    if encrt_mode == 'encrypt':
        conf_ch_sz = input(f'Specify a reading chunck size or just press \"ENTER\" to use the default chunk size of {def_ch_sz}: ')
        if conf_ch_sz:
            try:
                def_ch_sz = int(conf_ch_sz)
            except:
                print('Invalid chunck size, please try again')
        encrt_key = input('Please input the encryption key or just press \"ENTER\" key to generate own key: ')
        encrt_key = None if not encrt_key else encrt_key
    else:
        while True:
            encrt_key = input('Please input the encryption key: ')
            if not encrt_key:
                print('Please input a encryption key:')
                continue
            break
    while True:
        db_path = input('Please input the database path: ')
        if not os.path.exists(db_path):
            print('Database doesn\'t exist')
            continue
        out_path = input('Please input the output path and file name: ')
        if os.path.exists(out_path):
            print(f'This output filename or directory \"{out_path}\" is exists')
            continue
        break
    if encrt_mode == 'decrypt':
        out_path = out_path if out_path.find('.db') > -1 else out_path + '.db'
    break

if encrt_mode == 'encrypt':
    used_key = encrypt_file(encrt_key, db_path, out_path, def_ch_sz)
    print(f'Encryption key used: {used_key}')
else:
    decrypt_file(encrt_key, db_path, out_path)



# https://e1.pcloud.link/publink/show?code=XZ6TQRZLicYE61mShbKKkVKerT6KS4wi1Hy
# https://mega.nz/file/IAk30QiY#CP_r12xT5j2op05F5NUAbsrQx9JDtq-yrNFSKSmBYZ8
# https://archive.org/download/w3_20220529/w3.encdb
