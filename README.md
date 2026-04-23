# DHmessenger
# 🔐 Diffie–Hellman Encrypted Messaging Prototype

## 📌 Overview

This project is a **Python-based encrypted messaging prototype** that demonstrates how the Diffie–Hellman (DH) key exchange can be used to establish a shared secret between two parties over an insecure network.

Once the shared key is established, it is used to derive a symmetric encryption key for secure message exchange.

---

## 🎯 Objective

The primary goal of this project is to:

* Understand the **Diffie–Hellman key exchange**
* Apply it in a **practical client–server communication setup**
* Explore how shared secrets can be used for **symmetric encryption**

This is a **learning-focused implementation**, not a production-ready secure messaging system.

---

## ⚙️ Features

* 🔑 Diffie–Hellman key exchange
* 🔐 Shared secret derivation
* 🧪 AES-GCM based encryption (authenticated encryption)
* 💬 Simple client-server messaging over sockets
* 🧱 Object-Oriented design

---

## 🧠 How It Works

1. **Key Exchange**

   * Client and server generate DH key pairs
   * Public keys are exchanged over the network
   * A shared secret is computed independently by both parties

2. **Key Derivation**

   * The shared secret is passed through HKDF to produce a symmetric key

3. **Secure Communication**

   * Messages are encrypted using AES-GCM
   * Each message uses a unique nonce
   * Encrypted data is transmitted over a TCP socket

---

## 📁 Project Structure

```
project/
│
├── client.py
├── server.py
├── dh.py
├── secure_channel.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Start the server

```
python server.py
```

### 3. Start the client

```
python client.py
```

---

## ⚠️ Security Disclaimer

This project is intended **for educational purposes only**.

* ❌ No authentication is implemented
* ❌ Vulnerable to **Man-in-the-Middle (MITM) attacks**
* ❌ Does not verify the identity of communicating parties

An attacker could intercept and replace public keys during the Diffie–Hellman exchange without detection.

---

## 🔮 Future Improvements

* Add **authentication** (digital signatures or certificates)
* Prevent MITM attacks
* Use standardized DH parameters (e.g., RFC-defined groups)
* Implement Perfect Forward Secrecy (ephemeral DH)
* Add a GUI interface
* Support multiple clients

---

## 🧾 Requirements

```
cryptography>=42.0.0
```

---

## 📚 Concepts Covered

* Diffie–Hellman Key Exchange
* Symmetric Encryption (AES-GCM)
* Key Derivation Functions (HKDF)
* Client–Server Networking (Sockets)

---

## 📌 Notes

This implementation focuses on clarity and learning rather than completeness or security hardening. It is a stepping stone toward understanding how real-world protocols like TLS work internally.

---

## 📜 License

This project is open-source and available under the MIT License.

