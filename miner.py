import time
import secrets
import hashlib
import base58
import requests
import os

from colorama import init, Fore

init()

print(Fore.YELLOW + """

  _____________________________________________
|                                             |
|                                             |
|          Connecting, please wait...         |
|             made by ctx#6239                |
|                                             |
|_____________________________________________|

""")
time.sleep(3.31)
os.system('clear')
print(Fore.BLUE + """

_____________________________________________________
|                                                   |
|                                                   |
|               CONNECTED SUCCESSFULLY!             |
|                                                   |
|___________________________________________________|

""")
time.sleep(1)
os.system('clear')
print(Fore.YELLOW + """

 _____________________________________________
|                                             |
|                                             |
|     Trying to connect to LocalHost...       |
|                                             |
|_____________________________________________|

"""
)
time.sleep(4.20)
os.system('clear')
print(Fore.GREEN + """

+--------------------------------------------------+
|                                                  |
|                                                  |
|                                                  |
|                                                  |
|                    CONNECTED!                    |
|                                                  |
|                                                  |
|                                                  |
|                                                  |
+--------------------------------------------------+

""")
os.system('clear')
time.sleep(1)
print(Fore.BLUE + "Starting Mining Process please be patient!")
time.sleep(4.20)
os.system('clear')
print(Fore.BLUE + "MINING PROCESS STARTED")
os.system('clear')
VALID_PAIR = Fore.GREEN + "Balance: {balance} | [✅] FOUND! {wallet} | Priv: {priv}"
INVALID_PAIR = Fore.RED + "Balance: {balance} | [X] Trying! {wallet} | Priv: {priv}"

def generate_private_key():
    """Generate a new private key."""
    while True:
        private_key = hex(secrets.randbits(256))[2:]
        if len(private_key) == 64:
            return private_key

def private_key_to_public_key(private_key):
    """Convert a private key to a public key."""
    private_key_bytes = bytes.fromhex(private_key)
    public_key_bytes = hashlib.sha256(private_key_bytes).digest()
    return public_key_bytes.hex()

def public_key_to_wallet_address(public_key):
    """Convert a public key to a wallet address."""
    public_key_bytes = bytes.fromhex(public_key)
    hash_bytes = hashlib.new('ripemd160', public_key_bytes).digest()
    return base58.b58encode_check(b'\x00' + hash_bytes).decode()

def get_wallet_balance(wallet_address):
    """Get the balance of a wallet address."""
    try:
        response = requests.get(f"https://blockchain.info/q/addressbalance/{wallet_address}")
        if response.status_code == 200:
            balance = int(response.text)
            return balance
        else:
            return None
    except:
        return None

def mine_wallet():
    """Mine a new wallet."""
    while True:
        private_key = generate_private_key()
        public_key = private_key_to_public_key(private_key)
        wallet_address = public_key_to_wallet_address(public_key)
        balance = get_wallet_balance(wallet_address)

        if balance is not None:
            print(VALID_PAIR.format(balance=balance, wallet=wallet_address, priv=private_key))
            break
        else:
            print(INVALID_PAIR.format(balance=balance, wallet=wallet_address, priv=private_key))
while True:
  if __name__ == "__main__":
    mine_wallet()
