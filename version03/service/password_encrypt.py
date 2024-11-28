from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):

        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_password(self, password: str) -> str:
      
        encrypted_password = self.cipher.encrypt(password.encode())
        return encrypted_password.decode()  

    def decrypt_password(self, encrypted_password: str) -> str:
       
        decrypted_password = self.cipher.decrypt(encrypted_password.encode())
        return decrypted_password.decode()  

    def get_key(self) -> bytes:

        return self.key
