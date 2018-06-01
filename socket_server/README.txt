# Server

xxx@machine-learn01 ~/a/m/socket_server> python ml_server.py
Predicted: not cancer.
Predicted: not cancer.
Predicted: not cancer.
Predicted: cancer.
Predicted: not cancer.
Predicted: not cancer.
Predicted: not cancer.

# Client

webuser@machine-learn01 ~/a/m/socket_server> python ml_client.py
b'not cancer.'
b'not cancer.'
b'not cancer.'
b'cancer.'
b'not cancer.'
b'not cancer.'
b'not cancer.'
^CTraceback (most recent call last):
  File "ml_client.py", line 15, in <module>
    time.sleep(1)
KeyboardInterrupt
