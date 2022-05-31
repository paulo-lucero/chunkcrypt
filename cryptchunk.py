def encrypt_file(fer_obj, in_path, out_path, def_ch=1024):
    with open(in_path, 'rb') as in_file, open(out_path, 'ab') as out_file:
        while rd_chk := in_file.read(def_ch):
            enc_chk = fer_obj.encrypt(rd_chk)
            ar_enc = len(enc_chk).to_bytes(4, 'big')
            out_file.write(ar_enc)
            out_file.write(enc_chk)

def decrypt_file(fer_obj, in_path, out_path):
    with open(in_path, 'rb') as in_file, open(out_path, 'ab') as out_file:
        while ar_enc := in_file.read(4):
            lengt_enc = int.from_bytes(ar_enc, 'big')
            dec_chk = fer_obj.decrypt(in_file.read(lengt_enc))
            out_file.write(dec_chk)
