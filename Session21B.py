import hashlib

password = input("Enter your password:")
print("password is", password)

password = password.encode('utf-8')

password_encrypted = hashlib.sha256(password).hexdigest()
print("encrypted password is",password_encrypted)