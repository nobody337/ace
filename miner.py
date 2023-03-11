import time
import secrets
import hashlib
import base58
import requests

from colorama import init, Fore

init()

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

if __name__ == "__main__":
    mine_wallet()
