import random

p = int(input("Enter a prime number (17, 19, 23, etc): "))
q = int(input("Enter another prime number (Not one you entered above): "))

def is_prime(n):
	d = 2
	if n == 1:
		return False	
	while n % d != 0:
		d += 1
	return True


phi = (p-1) * (q-1)
e = random.randrange(1, phi)

def gcd(e,phi):

	while e!=0 and phi!=0:
		if e > phi:
			e = e % phi
		else:
			phi = phi % e
	return (e+phi)

def ext_gcd(e, phi):
    if phi == 0:
        return e, 1, 0
    else:
        d, x, y = ext_gcd(phi, e % phi)
        return d, y, x - y * (e // phi)
    # (e*y)+ (x - y * (e // phi) ) = d

def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.

    >>> multiplicative_inverse(7, 40)
    23
    """
    d = ext_gcd(e, phi)
    res = d[1] % phi
    return res

def generate_keypair(p, q):
	if not (is_prime(p) and is_prime(q)):
		raise ValueError('Both numbers must be prime.')
	elif p == q:
		raise ValueError('p and q cannot be equal')
	n = p * q
	phi = (p - 1) * (q - 1)
	g = 0
	while g != 1:
		e = random.randrange(1, phi)
		g = gcd(e, phi)
	d = multiplicative_inverse(e, phi)
	return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)

	
if __name__ == '__main__':
	print("RSA Encrypter/ Decrypter")
	print("Generating your public/private keypairs now . . .")
	public, private = generate_keypair(p, q)
	print("Your public key is ", public, " and your private key is ", private)
	message = input("Enter a message to encrypt with your private key: ")
	encrypted_msg = encrypt(private, message)
	print("Your encrypted message is: ")
	print(''.join(map(lambda x: str(x), encrypted_msg)))
	print("Decrypting message with public key ", public, " . . .")
	print("Your message is:")
	print(decrypt(public, encrypted_msg))
