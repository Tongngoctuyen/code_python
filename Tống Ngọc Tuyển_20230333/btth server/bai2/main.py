import threading
import subprocess
import sys
import time

def run_server():
    subprocess.run([sys.executable, "tcpserver.py"])

def run_client():
    time.sleep(1)
    subprocess.run([sys.executable, "tcpclient.py"])

if __name__ == "__main__":
    t1 = threading.Thread(target=run_server)
    t2 = threading.Thread(target=run_client)

    t1.start()
    t2.start()

    t1.join()
    t2.join()