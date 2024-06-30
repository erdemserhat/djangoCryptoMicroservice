# CaaS ( Crypto as a Service )

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

## Endpoints

### `/encrypt`

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
  "apiKey": "your_api_key",
  "userUUID": "123e4567-e89b-12d3-a456-426614174000",
  "sensitiveData": "this is some sensitive data"
}


**Example Respond:**

{
    "encrypted_data": "35db2f10e244a19686cf929071a80ac7029ad03cff2b7aebff4bac148c7dd32f64cf96c0b4122eb61f4ced1bba6672c1"
}

