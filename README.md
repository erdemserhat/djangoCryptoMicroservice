# 🔐 CaaS (Crypto as a Service)

<div align="center">
  <img src="https://img.shields.io/badge/CaaS-Crypto%20as%20a%20Service-blue?style=for-the-badge&logo=lock" alt="CaaS Crypto Service" />
  <br/>
  <h1>🔐 CaaS - Advanced Encryption Microservice</h1>
  <p><em>Revolutionary UUID-based encryption with unique salt and algorithm per user</em></p>
</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)](https://python.org/)
[![Django](https://img.shields.io/badge/Django-4.0+-green?style=flat-square&logo=django)](https://djangoproject.com/)
[![Microservice](https://img.shields.io/badge/Architecture-Microservice-orange?style=flat-square)](https://microservices.io/)
[![Security](https://img.shields.io/badge/Security-Enterprise%20Grade-red?style=flat-square&logo=shield)](https://owasp.org/)
[![Encryption](https://img.shields.io/badge/Encryption-UUID%20Based-purple?style=flat-square)](https://en.wikipedia.org/wiki/Encryption)

</div>

---

## 🎯 Project Overview

CaaS represents a **revolutionary approach** to user data encryption, breaking away from traditional single-salt, single-algorithm methods. Our innovative system uses **unique salt values and encryption algorithms** based on each user's UUID, ensuring maximum security and randomness.

### 🚀 **Innovation Highlights**

- **🔐 Unique Encryption per User**: Each user gets their own salt and encryption algorithm
- **🆔 UUID-Based Configuration**: Deterministic yet unique encryption based on UUID
- **🏗️ Microservice Architecture**: Independent encryption server for separation of concerns
- **🛡️ Maximum Security**: Even if database is compromised, each row uses different encryption

---

## 🏗️ Architecture Overview

<div align="center">
  <img src="https://img.shields.io/badge/Architecture-Microservice%20Design-blue?style=for-the-badge" alt="Microservice Architecture" />
  <img src="https://img.shields.io/badge/Security-UUID%20Based%20Encryption-green?style=for-the-badge" alt="UUID Encryption" />
  <img src="https://img.shields.io/badge/Pattern-Separation%20of%20Concerns-purple?style=for-the-badge" alt="SoC Pattern" />
</div>

### 🎯 **Core Principles**

<table>
  <tr>
    <td align="center" width="250">
      <b>🔐 Unique Encryption</b><br/>
      <small>Different salt and algorithm per user</small>
    </td>
    <td align="center" width="250">
      <b>🆔 UUID-Based</b><br/>
      <small>Deterministic configuration from UUID</small>
    </td>
    <td align="center" width="250">
      <b>🏗️ Microservice</b><br/>
      <small>Independent encryption server</small>
    </td>
  </tr>
  <tr>
    <td align="center" width="250">
      <b>🛡️ Maximum Security</b><br/>
      <small>Even compromised DB remains secure</small>
    </td>
    <td align="center" width="250">
      <b>⚡ High Performance</b><br/>
      <small>Optimized encryption operations</small>
    </td>
    <td align="center" width="250">
      <b>🔧 Easy Integration</b><br/>
      <small>Simple API for developers</small>
    </td>
  </tr>
</table>

---

## 🏛️ System Architecture

<div align="center">
  <h3>🔐 CaaS Encryption Flow</h3>
</div>

```
🔐 CaaS ENCRYPTION ARCHITECTURE TREE
├── 🏢 MAIN SERVER (Business Logic)
│   ├── 📡 API Gateway
│   │   ├── Request Validation
│   │   ├── Authentication
│   │   └── Rate Limiting
│   ├── 💼 Business Services
│   │   ├── User Management
│   │   ├── Data Processing
│   │   └── Business Logic
│   └── 🗄️ Database Layer
│       ├── User Data
│       ├── Encrypted Data
│       └── Configuration
│
├── 🔐 ENCRYPTION MICROSERVICE
│   ├── 🎲 Cipher Pool
│   │   ├── blake2b
│   │   ├── sha256
│   │   ├── md5
│   │   └── (various algorithms)
│   ├── 🧂 Salt Pool
│   │   ├── 8 characters
│   │   ├── 16 characters
│   │   ├── 32 characters
│   │   └── 64 characters
│   ├── 🆔 UUID Processor
│   │   ├── UUID Parsing
│   │   ├── Algorithm Selection
│   │   └── Salt Selection
│   └── 🔒 Encryption Engine
│       ├── Data Encryption
│       ├── Hash Generation
│       └── Response Formatting
│
└── 🔗 COMMUNICATION LAYER
    ├── 🔐 Secure Protocols
    │   ├── HTTPS/TLS
    │   ├── API Authentication
    │   └── Request Validation
    └── 📡 API Endpoints
        ├── POST /encrypt
        ├── POST /decrypt
        └── GET /health

🔄 ENCRYPTION FLOW:
User Data → Main Server → Encryption Service → Encrypted Data → Database
     ↓              ↓              ↓              ↓              ↓
Validation    UUID Processing   Algorithm    Secure Storage   Retrieval
```

---

## 🎬 Presentation Video

https://github.com/erdemserhat/djangoCryptoMicroservice/assets/116950260/452801ed-40e6-44d2-82c1-787e2ed32a76



## Features
- **Independent Encryption Server**: Encryption operations are performed on a server independent of the main server.
- **Unique Encryption**: Different salt and encryption algorithms are used for each user.
- **UUID-Based Configuration**: Unique encryption configurations are created using UUIDs.

## Technical Details
- **Cipher Pool**: A pool containing various encryption algorithms, such as blake2b, sha256, md5, etc.
- **Salt Pool**: A pool containing salt values of different lengths (8, 16, 32, 64 characters, etc.).
- **Service**: The folder where the API service logic is implemented.
- **Routes**: Endpoints for encryption operations.

## Encryption Process
1. **Data Flow**: User data is sent to the main server, which then forwards it to the encryption server.
2. **UUID Usage**: A unique salt and encryption algorithm are selected based on the user's UUID.
3. **Encryption**: The data is encrypted using the selected configuration.
4. **Returning Encrypted Data**: The encrypted data is sent back to the main server and securely stored.

## Security and Performance
- **Security**: Communication between the main server and the encryption server is secured using secure protocols. The independent encryption server adds an extra layer of security against attacks.
- **Performance**: The performance of the encryption server can affect the overall speed and efficiency of the system. Therefore, it is crucial to ensure that the encryption server has sufficient performance and scalability.




📡 API Endpoints

### 📌 `/encrypt`

**Method:** `POST`

**Description:**
This endpoint handles encryption requests by processing sensitive data, user UUID, and an API key. It uses the provided UUID to determine the encryption and salt methods from predefined pools and returns the encrypted data as a response.

**Request Body:**
- `apiKey`: The API key for authentication.
- `userUUID`: The unique identifier for the user.
- `sensitiveData`: The data that needs to be encrypted.

**Response:**
- On success: Returns the encrypted data.
- On failure: Returns an error message if the request is not a POST request or if there is an issue with the encryption process.

**Example Request:**
```json
{
    "apiKey": "example_api_key",
    "userUUID": "4dbcbcfe-4800-40a8-badf-c26b73af230c",
    "sensitiveData": "example sensitive data"
}
```

**Example Respond:**
```json

{
    "encrypted_data": "35db2f10e244a19686cf929071a80ac7029ad03cff2b7aebff4bac148c7dd32f64cf96c0b4122eb61f4ced1bba6672c1"
}
```
