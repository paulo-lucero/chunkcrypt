from pathlib import Path
import os
import sys
sys.path.append(os.path.join(Path().resolve().parent, 'src', 'chunkcrypt'))
from cryptchunk import downl_decrypt

while True:
    file_url = input('Please input the url: ')
    if not file_url:
        print('Please input a url')
        continue
    title_name = input('Please input the Title or Name or any short description: ')
    if not file_url:
        print('Please input a Title or Name or any short description')
        continue
    out_file = input('Please input the output path and filename: ')
    if os.path.exists(out_file):
        print(f'\"{out_file}\" File or directory already exists')
        continue
    enc_key = input('Please input the encryption key: ')
    if not enc_key:
        print('Please input a encryption key')
        continue
    break

downl_decrypt(file_url, out_file, enc_key, False, ' - ', '', title_name)

# https://archive.org/download/tw3lvlg0-0-2/tw3lvlg0-0-2.encdb
# https://archive.org/download/tw3pages/tw3pages.encdb
