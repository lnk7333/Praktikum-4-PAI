from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import gmpy2

# --- 1. Key Generation for RSA ---
p = getPrime(1024) # 1024-bit prime for RSA modulus
q = getPrime(1024) # 1024-bit prime for RSA modulus

# --- 2. Key Generation for Diffie-Hellman (DH) Parameters ---
p_dh = getPrime(2048) # 2048-bit prime modulus for DH key exchange
g = getPrime(512)    # 512-bit prime generator for DH
a = getPrime(512)    # 512-bit prime (Alice's private key)
b = getPrime(512)    # 512-bit prime (Bob's private key)

def generate_public_int(g, a, p):
    # !!! FLAWED IMPLEMENTATION !!!
    # This should be modular exponentiation: pow(g, a, p) or g**a % p
    # The code uses the bitwise XOR operator '^' instead of '**' (exponentiation).
    # This calculates (g XOR a) % p, which is cryptographically insecure.
    return g ^ a % p

def generate_shared_secret(A, b, p):
    # !!! FLAWED IMPLEMENTATION !!!
    # This should be modular exponentiation: pow(A, b, p) or A**b % p
    # The code uses the bitwise XOR operator '^' instead of '**' (exponentiation).
    # This calculates (A XOR b) % p, which is cryptographically insecure.
    return A ^ b % p

# --- 3. Cryptographic Operations ---

n = p * q           # RSA Modulus (n = p * q, size 2048 bits)
e = 3               # RSA Public Exponent (very small, typically 'low-exponent' security risk)
flag = SECRET      # Placeholder for the secret flag (e.g., a byte string)
flag_int = bytes_to_long(flag) # Convert the flag bytes to an integer

# Calculate Public Keys using the FLAWED DH function:
A = generate_public_int(g,a,p_dh) # A = (g XOR a) % p_dh
B = generate_public_int(g,b,p_dh) # B = (g XOR b) % p_dh

# Calculate Shared Secret using the FLAWED DH function:
shared_int = generate_shared_secret(A, b, p_dh) # shared_int = (A XOR b) % p_dh
# NOTE: Due to the XOR flaw, 'a' and 'b' can be easily recovered,
# making 'shared_int' predictable from public values (g, A, B, p_dh).

# Mask the flag using the shared secret:
flag2 = flag_int ^ shared_int # Intermediate value (flag XOR shared_secret)

# Encrypt the masked flag using RSA:
# c = (flag2 ^ e) mod n
c = pow(flag2, e, n)

# Print the public parameters for the challenge
print(f"e = {e}")
print(f"n = {n}")
print(f"c = {c}")
print(f"p_dh = {p_dh}")
print(f"g = {g}")
print(f"A = {A}")
print(f"B = {B}")