# decrypt.py
import cv2

# Read the encrypted image
img = cv2.imread("encryptedImage.jpg")

# Read stored passcode
try:
    with open("passcode.txt", "r") as f:
        stored_password = f.read().strip()
except FileNotFoundError:
    print("Passcode file not found. Decryption failed.")
    exit()

# Read passcode from user
pas = input("Enter passcode for Decryption: ")

if pas == stored_password:
    c = {i: chr(i) for i in range(255)}
    message = ""
    n, m, z = 0, 0, 0
    
    while True:
        try:
            char = c[img[n, m, z]]
            if char == '\x00':  # Stop when reaching null character
                break
            message += char
        except KeyError:
            break
        except IndexError:
            break
        n += 1
        m += 1
        z = (z + 1) % 3
    
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
