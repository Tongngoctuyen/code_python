import multiprocessing
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_server():
    os.system(f"python \"{BASE_DIR}\\server_main.py\"")

def run_client():
    os.system(f"python \"{BASE_DIR}\\client_main.py\"")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_server)
    p2 = multiprocessing.Process(target=run_client)

    p1.start()
    p2.start()

    p1.join()
    p2.join()