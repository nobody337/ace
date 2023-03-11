import time

def EthMiner():
    wallet = input("Enter your wallet address: ")
    print("Connecting to localhost...")
    time.sleep(2)
    print("Connected!")
    print("Mining...")
    time.sleep(3)
    print("Wallet found!")
    print(f"Wallet address: {wallet}")
    print("\033[32mWithdrawing funds...\033[0m")
    time.sleep(2)
    print("Funds withdrawn successfully!")
