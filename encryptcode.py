# encrypt.py
import cv2
import os

# Read the image
img = cv2.imread("mypic.jpg")  # Replace with the correct image path

# Get the secret message and passcode from the user
msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Create encoding dictionary
d = {chr(i): i for i in range(255)}

# Encode message into image
n, m, z = 0, 0, 0
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save encrypted image
cv2.imwrite("encryptedImage.jpg", img)

# Save passcode to a file
with open("passcode.txt", "w") as f:
    f.write(password)

print("Encryption Complete. Image saved as encryptedImage.jpg")
