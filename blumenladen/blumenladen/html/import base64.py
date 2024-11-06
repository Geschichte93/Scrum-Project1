import base64

# Given Base64 encoded string
ciphertext = "5dXaiu4FdLn8spHb1qHpG8dfhVjaA8BK1xUeJYDYKwv1gjfT"

# Decode using Base64
decoded_bytes = base64.b64decode(ciphertext)
decoded_string = decoded_bytes.decode('utf-8', errors='ignore')

# Print the result
print(decoded_string)
