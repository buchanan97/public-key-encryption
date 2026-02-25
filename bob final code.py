import socket
import json
import random

################################################
# Bob acts as server and waits for connections #
################################################

# Do not change this function
def wait_and_get_socket():
    port = 4321
    host = 'localhost'
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind((host, port))
    serversocket.listen(1)
    (clientsocket, address) = serversocket.accept()
    print(f"Running Diffie-Hellman key exchange protocol with {str(address)}")
    return clientsocket

# Do not change this function
def send(gy, client_socket):
    encoded_data = json.dumps({'gy': gy})
    client_socket.send(encoded_data.encode('ascii'))

# Do not change this function
def receive(client_socket):
    data = client_socket.recv(1024)
    return json.loads(data)

def generate_y(q):
    y = random.randint(1, q-1)
    return y

def compute_g_y_mod_p(g, y, p):
    gy = pow(g, y, p)
    return gy

def compute_shared_secret(gx, y, p):
    shared_secret = pow(gx, y, p)
    return shared_secret

def exchange_shared_secret():
    s = wait_and_get_socket()
    # Receive public parameters from Alice
    data = receive(s)
    q = data['q']
    p = data['p']
    g = data['g']
    gx = data['gx']

# Generate y and compute gy
    y = generate_y(q)
    gy = compute_g_y_mod_p(g, y, p)
    # Compute shared secret
# Change the parameters with the correct ones
    shared_secret = compute_shared_secret(gx, y, p)
    print(f"Shared secret: {shared_secret}")

# Now send what is missing to Alice, so that she can complete the protocol
# Change the first parameter with the correct one
    send(gy, s)
    s.close()

if __name__ == "__main__":
    exchange_shared_secret()