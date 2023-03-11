from miner import Miner
from termcolor import colored
import threading
import time

class BitcoinWalletGenerator:
    def __init__(self):
        self.balance = 0
        self.found = False
        self.stop_event = threading.Event()
        self.miners = []

    def generate_wallet(self):
        while not self.stop_event.is_set():
            miner = Miner()
            self.miners.append(miner)
            miner.start()

            time.sleep(0.1)

            for miner in self.miners:
                if miner.found:
                    self.found = True
                    self.stop()

            self.miners = [miner for miner in self.miners if not miner.finished]

    def start(self):
        print("Starting wallet generation...")

        self.generate_wallet()

        print("Stopping wallet generation...")

        for miner in self.miners:
            miner.stop()

        self.miners = []

    def stop(self):
        self.stop_event.set()

        for miner in self.miners:
            miner.stop()

        self.miners = []

    def get_results(self):
        if self.found:
            valid_result = colored(f"Balance: {self.balance} | [✅] FOUND! {self.miners[-1].wallet} | Priv: {self.miners[-1].priv}", "green")
            return valid_result
        else:
            return "No wallets found."
