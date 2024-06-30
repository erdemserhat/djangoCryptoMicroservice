# Secure Encryption System

## Project Overview
This project aims to provide a more secure and effortless approach to encrypting user data compared to traditional methods. Encryption operations are carried out on a separate server, independent of the main server, and unique encryption configurations are created for each user.

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
