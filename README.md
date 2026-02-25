# Public Key Encryption — Diffie-Hellman Key Exchange

## 📹 Demo Video
Watch a full walkthrough of this project here:
[https://www.loom.com/share/73477dc7e3f04dd1878a0962ea895bc6](https://www.loom.com/share/73477dc7e3f04dd1878a0962ea895bc6)

---

## Overview
This project demonstrates a **Diffie-Hellman (DH) key exchange** between two parties, **Alice** and **Bob**, communicating over the local network (`localhost`). The Diffie-Hellman protocol allows two parties to securely establish a shared secret over an insecure channel, without ever transmitting the secret itself.

---

## How It Works

1. **Public parameters** are chosen: a large prime `p = 2q + 1` (where `q` is also prime) and a generator `g = 2`.
2. **Alice** (client):
   - Generates a private random integer `x` in the range `[1, q-1]`.
   - Computes `gx = g^x mod p` (her public value).
   - Connects to Bob and sends the public parameters `(p, q, g, gx)`.
   - Receives Bob's public value `gy` and computes the shared secret: `shared_secret = gy^x mod p`.
3. **Bob** (server):
   - Waits for a connection from Alice and receives the public parameters.
   - Generates a private random integer `y` in the range `[1, q-1]`.
   - Computes `gy = g^y mod p` (his public value).
   - Computes the shared secret: `shared_secret = gx^y mod p`.
   - Sends `gy` back to Alice.
4. Both parties now hold the **same shared secret** (`g^(xy) mod p`), which can be used as a symmetric encryption key.

---

## Files
| File | Description |
|---|---|
| `alice final code.py` | Alice's script — acts as the **client**, initiates the key exchange |
| `bob final code.py` | Bob's script — acts as the **server**, waits for Alice's connection |

---

## Requirements
- Python 3.6 or higher
- No external libraries required (uses only built-in `socket`, `json`, and `random` modules)

---

## Running the Project

Open **two separate terminal windows**.

### Terminal 1 — Start Bob (server) first:
```bash
python3 "bob final code.py"
```
Bob will start listening on `localhost:4321` and wait for Alice to connect.

### Terminal 2 — Start Alice (client):
```bash
python3 "alice final code.py"
```
Alice will connect to Bob, perform the key exchange, and both will print the same shared secret.

### Expected Output
Both terminals should print the same value, confirming the key exchange succeeded:
```
Shared secret: <large integer>
```

---

## Security Note
This implementation uses a 256-bit safe prime (`p = 2q + 1`), making the discrete logarithm problem computationally infeasible to brute-force. The security of the Diffie-Hellman exchange relies on this hardness assumption.
