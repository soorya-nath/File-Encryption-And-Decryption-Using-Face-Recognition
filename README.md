# File Encryption and Decryption Using Facial Recognition

## 📌 Project Overview  
This project is a secure file encryption and decryption system that uses facial recognition for user authentication, ensuring personalized data protection.

## 🔧 Tools  
- **SHA-256:** Secure hashing for password and data integrity.  
- **CNN (Convolutional Neural Network):** Accurate face recognition for user authentication.  
- **OpenCV:** Real-time face detection and recognition.  
- **RSA:** Robust asymmetric encryption and decryption for file security.  

## ✅ Key Features  
- **Secure File Protection:** Advanced file encryption and decryption using facial recognition for user-specific access.  
- **Robust Authentication:** Face recognition using CNN and OpenCV for precise user verification.  
- **Strong Encryption:** SHA-256 for secure hashing and RSA for data encryption and decryption.  
- **Enhanced Accuracy:** Deep learning techniques to boost user identification, minimizing false positives.  

## 🚀 How It Works  
1. **User Authentication:** Users authenticate via face recognition (captured using OpenCV).  
2. **Encryption:** The file is encrypted using RSA, ensuring secure data storage.  
3. **Decryption:** Only authenticated users (verified by face recognition) can decrypt the file.  
4. **Security:** SHA-256 is used for secure hashing and data integrity.

## 🛠️ Installation and Setup  
1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/File-Encryption-Face-Recognition.git
   cd File-Encryption-Face-Recognition
##Install the required dependencies:
    pip install opencv-python-headless numpy cryptography
##Run the application:
python main.py
📌 Usage
   1.Launch the application.
   2.Register your face for authentication.
   3.Choose the file you want to encrypt.
   4.Authenticate using your face to decrypt the file.
