# 🚀 Mobile Computing

---

# 📡 1. CDMA Simulation (Walsh Matrix and SNR Calculation)

### 📄 Overview

In this project, we simulate a **basic CDMA (Code Division Multiple Access)** system using **Walsh matrices** for spreading codes.

We simulate:
- Encoding and transmitting messages.
- Adding Gaussian noise.
- Decoding messages and calculating **SNR** (Signal to Noise Ratio).

### 📑 Key Features

- **Walsh Matrix** based orthogonal code generation.
- **Noise** introduced through Gaussian distribution.
- **SNR**, Signal Power, and Noise Power calculated per user.

### 🛠 How It Works

1. **Walsh Codes** are generated using recursion.
2. **Message Bits** are multiplied with the corresponding Walsh code.
3. **Noise** is added to simulate real-world conditions.
4. **Correlation** is used to decode the bits at the receiver.
5. **SNR Calculation** is performed per bit and averaged.

### 🔍 Important Code Parts

```python
def walshmatrix(n):
    if n == 1:
        return np.array([[1, 1], [1, -1]])
    else:
        W = walshmatrix(n-1)
        return np.vstack((np.hstack((W, W)), np.hstack((W, -W))))
```

---

# 📶 2. BPSK BER Simulation in AWGN and Rayleigh Channels

### 📄 Overview

This project analyzes the performance of **BPSK modulation** over:
- **AWGN Channel**
- **Rayleigh Fading Channel**

We compare **theoretical BER** with **simulated BER**.

### 📑 Key Features

- **1 million bits** simulated.
- BER curves plotted for both AWGN and Rayleigh environments.
- Theoretical vs. Simulated performance comparison.

### 📈 Results

- `awgn.png` → BER plot for AWGN
- `ray.png` → BER plot for Rayleigh

### 🛠 Important Code Parts

```python
ber_theory_awgn = 0.5 * erfc(np.sqrt(10 ** (EbN0_dB_range / 10)))
ber_theory_rayleigh = 0.5 * (1 - np.sqrt(10 ** (EbN0_dB_range / (1 + 10 ** (EbN0_dB_range / 10)))))
```

### 📊 BER Graph

The project saves and plots BER performance graphs.

---

# 📁 3. TCP File Transfer using Python (Client-Server)

### 📄 Overview

A simple **TCP Client-Server** model to transfer files securely over a socket connection.

### 🛠 How It Works

- **Server** listens on a port and accepts a file upload.
- **Client** connects and sends a file in chunks.

### 🖧 Code Summary

**Server Side:**
```python
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(5)
```

**Client Side:**
```python
def send_file(server_host, server_port, file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
```

### 📜 TCP/OSI Layer Mapping

| OSI Layer | TCP/IP Layer | Action |
|-----------|--------------|--------|
| Application | Application | File read/write |
| Transport | Transport | TCP Socket (Connection-oriented) |
| Network | Internet | IP Addressing |
| Data Link | Network Access | Ethernet/Wi-Fi Transmission |
| Physical | Network Access | Electrical signals or Radio |

✅ This project follows all TCP/IP and OSI layers correctly.

---

# 🌐 4. DHCP Configuration on Cisco Router

---

## 📡 Network Topology


- **Gi0/0** → LAN 1 → `192.168.1.0/24`
- **Gi0/1** → LAN 2 → `192.168.2.0/24`
- **Gi0/2** → LAN 3 → `192.168.3.0/24`

---

## 📖 Project Overview

We configured a **Cisco 2911 Router** to act as a **DHCP Server**, dynamically assigning IPs to different networks.

✅ Provides IP address  
✅ Default gateway  
✅ DNS server configuration

---

## 🛠 Configuration Steps

**Interface Setup:**
```plaintext
interface gigabitEthernet 0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
```
(Similar setup for `0/1` and `0/2`.)

**DHCP Pools:**
```plaintext
ip dhcp pool MYLAN1
 network 192.168.1.0 255.255.255.0
 default-router 192.168.1.1
 dns-server 8.8.8.8
```
(Similar for MYLAN2 and MYLAN3.)

**Exclude Router IPs:**
```plaintext
ip dhcp excluded-address 192.168.1.1
ip dhcp excluded-address 192.168.2.1
ip dhcp excluded-address 192.168.3.1
```

---

## 🧠 DORA Process (DHCP Working)

| Step  | Description |
|------|-------------|
| **Discover** | Client broadcasts to find DHCP server |
| **Offer** | DHCP server offers an IP address |
| **Request** | Client requests offered IP |
| **Acknowledgement** | DHCP server confirms and finalizes lease |

✅ Ensures dynamic and conflict-free IP address allocation.

---

## 🛜 TCP/IP and OSI Model Layer Mapping for DHCP

| OSI Layer | TCP/IP Layer | DHCP Action |
|-----------|--------------|-------------|
| Layer 7 - Application | Application | DHCP messaging |
| Layer 6 - Presentation | Application | Data formatting |
| Layer 5 - Session | Application | DHCP session maintenance |
| Layer 4 - Transport | Transport | UDP on Port 67/68 |
| Layer 3 - Network | Internet | IP Address management |
| Layer 2 - Data Link | Network Access | MAC addressing |
| Layer 1 - Physical | Network Access | Physical transmission |

---

# 📢 Conclusion

Across these four projects:
- We **simulated communication systems** (CDMA, BPSK BER).
- We **built basic network services** (TCP File Transfer).
- We **configured real-world network infrastructure** (Router DHCP).

✅ Real-world concepts like **SNR**, **BER**, **TCP/IP**, **OSI Model**, and **DORA** were applied hands-on!

---

# 🚀 End of Combined Projects
