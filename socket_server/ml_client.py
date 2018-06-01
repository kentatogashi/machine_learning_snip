import socket, pickle
from sklearn.datasets import load_breast_cancer
import time
df = load_breast_cancer()
x = df.data

for i in x:
    serialized = pickle.dumps(i)
    client = socket.socket()
    client.connect(('localhost', 33333))
    client.send(serialized)
    res = client.recv(4096)
    print(res)
    client.close()
    time.sleep(1)
