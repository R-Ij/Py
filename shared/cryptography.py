import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from shared import common, make_log
import traceback


class Crypt:
    def __init__(self):
        self.path = '../pem/'
        self.s = 'Hello Python World!'
        pem_list = common.file_list(dir=self.path, extension='.pem')
        if not pem_list:
            self.__make_key()
        self.private_key, self.public_key = self.__read_key()

    def __make_key(self):
        """
        秘密鍵/公開鍵の生成

        Notes:
            Private
        """
        # 秘密鍵の生成
        private_key = RSA.generate(2048)
        with open(self.path + 'private.pem', 'w') as f:
            tmp = private_key.export_key().decode('utf-8')
            f.write(tmp)

        # 秘密鍵から公開鍵を生成
        public_key = private_key.publickey()
        with open(self.path + 'receiver.pem', 'w') as f:
            tmp = public_key.export_key().decode('utf-8')
            f.write(tmp)

    def __read_key(self):
        """
        秘密鍵/公開鍵の読み込み

        Returns:
            RsaKey: private_key(秘密鍵), public_key(公開鍵)

        Notes:
            Private
        """
        # ファイルからキーを読み込む
        with open(self.path + 'private.pem', 'rb') as f:
            private_pem = f.read()
            private_key = RSA.import_key(private_pem)

        with open(self.path + 'receiver.pem', 'rb') as f:
            public_pem = f.read()
            public_key = RSA.import_key(public_pem)

        return private_key, public_key

    def encryption(self):
        """
        文字列を暗号化する

        Returns:
            bytes: ciphertext(暗号化された文字列)
        """
        cipher_rsa = PKCS1_OAEP.new(self.public_key)
        ciphertext = cipher_rsa.encrypt(self.s.encode())
        return ciphertext

    def composite(self, enc_name):
        """
        ファイルに出力した暗号を復号する

        Args:
            enc_name (str): 暗号ファイル名

        Returns:
            str: s(復号された文字列)
        """
        with open(self.path + enc_name + '_encrypt.dat', 'br') as f:
            ciphertext = f.read()
        decipher_rsa = PKCS1_OAEP.new(self.private_key)
        s = decipher_rsa.decrypt(ciphertext).decode('utf-8')
        return s

    def make_crypt(self, enc_name):
        """
        文字列を暗号化してファイルに出力

        Args:
            enc_name (str): 暗号ファイル名

        """
        # 暗号化
        encrypt = self.encryption()

        with open(self.path + enc_name + '_encrypt.dat', 'bw') as f:
            f.write(encrypt)


def main(msg=None):

    path = os.path.dirname(__file__)
    write_log = make_log.Log(path)

    try:
        write_log.debug_log('START')

        crypt = Crypt()
        if msg:
            crypt.s = msg
        # crypt.make_crypt('pytest')
        s = crypt.composite('pytest')
        #
        # write_log.debug_log(s)

    except Exception as e:
        write_log.error_log(str(e))
        err_list = traceback.format_exc().split('\n')
        for err in err_list:
            write_log.error_log(err)
        return False

    write_log.debug_log('OK')
    return True


if __name__ == '__main__':
    main('I love you...')
