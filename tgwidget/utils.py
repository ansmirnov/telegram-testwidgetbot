import hashlib
import hmac
import os


class HashCheck:
    def __init__(self, data, secret):
        self.hash = data['hash']
        self.secret_key = hashlib.sha256(secret).digest()
        self.data = {}
        for k, v in data.items():
            if k != 'hash':
                self.data[k] = v

    def data_check_string(self):
        a = sorted(self.data.items())
        res = '\n'.join(map(lambda x: '='.join(x), a))
        return res

    def calc_hash(self):
        msg = bytearray(self.data_check_string(), 'utf-8')
        res = hmac.new(self.secret_key, msg=msg, digestmod=hashlib.sha256).hexdigest()
        return res
    
    def check_hash(self):
        return self.calc_hash() == self.hash
        
