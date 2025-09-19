import time
import random
import threading
import requests

pool_servers = [
    "http://159.89.182.1:8080/submit",
    "http://51.15.73.163:3333/submit",
    "http://167.99.233.123:4444/submit"
]

def generate_hash():
    return ''.join(random.choices('abcdef0123456789', k=64))

def submit_share(hash_result, pool_url):
    wallet = os.getenv('WALLET')
    try:
        payload = {
            "wallet": wallet,
            "share": hash_result
        }
        requests.post(pool_url, data=payload, timeout=2)
    except Exception:
        pass

def miner_thread(thread_id):
    pool_url = random.choice(pool_servers)
    print(f"[Thread {thread_id}] Connected to pool: {pool_url} | Mining to wallet: {wallet}")
    while True:
        hash_result = generate_hash()
        submit_share(hash_result, pool_url)
        print(f"[Thread {thread_id}] Hash: {hash_result}")
        time.sleep(random.uniform(0.01, 0.1))

def main():
    threads = []
    num_threads = 4
    for i in range(num_threads):
        t = threading.Thread(target=miner_thread, args=(i,))
        t.daemon = True
        t.start()
        threads.append(t)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Miner stopped.")

          
if __name__ == "__main__":
    
    main()
