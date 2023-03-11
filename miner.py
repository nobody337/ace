import threading
import time
from hashlib import sha256
from base58 import b58encode_check
from bitcoinrpc.authproxy import AuthServiceProxy
from termcolor import colored

class Miner(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.daemon = True
        self.finished = False
        self.found = False
        self.balance = 0
        self.wallet = ""
        self.priv = ""

    def run(self):
        while not self.finished and not self.found:
            seed = str(time.time() * 1000).encode('utf-8')
            priv = sha256(seed).hexdigest()
            pub = b58encode_check(bytes.fromhex("80" + priv))
            wallet = b58encode_check(bytes.fromhex("00" + pub))
            try:
                rpc_connection = AuthServiceProxy("http://127.0.0.1:8332", timeout=10)
                balance = rpc_connection.getbalance(wallet.decode("utf-8"))
                self.balance = balance
                self.wallet = wallet.decode("utf-8")
                self.priv = priv
                self.found = True
            except:
                pass

    def stop(self):
        self.finished = True
