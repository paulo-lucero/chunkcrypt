from cryptchunk import encrypt_file, decrypt_file
import os

def_ch_sz = 1024

while True:
    encrt_key = input('Please input the encryption key: ')
    encrt_mode = input('Please specify if \"encrypt\" or \"decrypt\", input the same keyword: ')
    if encrt_mode == 'encrypt':
        conf_ch_sz = input(f'Specify a reading chunck size or input \"ok\" to use the default chunk size of {def_ch_sz} :')
        if conf_ch_sz.lower() != 'ok':
            try:
                def_ch_sz = int(conf_ch_sz)
            except:
                print('Invalid chunck size, please try again')
    if encrt_mode != 'encrypt' and encrt_mode != 'decrypt':
        print(f'{encrt_mode} is not a valid encryption mode')
        continue
    db_path = input('Please input the database path: ')
    if not os.path.exists(db_path):
        print('Database doesn\'t exist')
        continue
    out_path = input('Please input the output path and file name: ')
    if os.path.exists(out_path):
        print(f'This output filename or directory \"{out_path}\" is exists')
        continue
    if encrt_mode == 'decrypt':
        out_path = out_path if out_path.find('.db') > -1 else out_path + '.db'
    break

if encrt_mode == 'encrypt':
    encrypt_file(encrt_key, db_path, out_path, def_ch_sz)
else:
    decrypt_file(encrt_key, db_path, out_path)



# https://e1.pcloud.link/publink/show?code=XZ6TQRZLicYE61mShbKKkVKerT6KS4wi1Hy
# https://mega.nz/file/IAk30QiY#CP_r12xT5j2op05F5NUAbsrQx9JDtq-yrNFSKSmBYZ8
# https://archive.org/download/w3_20220529/w3.encdb
