import socket
import threading
import queue


# ip_list = queue.Queue()
ip = '192.168.1.1'
port_list = queue.Queue()

# for i in range(1, 255):
#     ip = f'192.168.1.{i}'
#     ip_list.put(ip)


for i in range(21, 1001):
    port_list.put(i)


def scan():
    while not port_list.empty():
        port = port_list.get()
        # ip_address = ip_list.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((ip, port))
                print(f"[{ip}] port {port} is open!")
            except:
                pass

        port_list.task_done()


for i in range(30):
    thread = threading.Thread(target=scan, daemon=True)
    thread.start()


port_list.join()

print("Finished")
