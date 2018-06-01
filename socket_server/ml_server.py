import socket
import pickle
import warnings
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')

class Model:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.clf = LogisticRegression()
        self.clf.fit(self.X, self.y)

    def predict(self, X_test):
        return self.clf.predict(X_test)

    def __call__(self):
        if self.X is not None or self.y is not None:
            print('accuracy_score: {}'.format(accuracy_score(self.X, self.y)))


def main(model):
    host = 'localhost'
    port = 33333
    while True:
        s_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_soc.bind((host, port))
        s_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        s_soc.listen(128)
        c_soc, (c_addr, c_port) = s_soc.accept()
        while True:
            try:
                recv_data = c_soc.recv(4096)
            except OSError:
                break

            if len(recv_data) == 0:
                break

            test_data = pickle.loads(recv_data)
            predicted = model.predict(test_data)
            if predicted[0] == 0:
                mes = 'not cancer.'
            else:
                mes = 'cancer.'
            print('Predicted: {}'.format(mes))
            sent = mes.encode('utf-8')
            while True:
                sent_len = c_soc.send(sent)
                if sent_len == len(sent):
                    break
                sent = sent[sent_len:]
        c_soc.close()
        s_soc.close()


if __name__ == '__main__':
    df = load_breast_cancer()
    X, y = df.data, df.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    model = Model(X_train, y_train)
    main(model)
