import sys

sharedPrime = int(input("Enter the prime Number :"))    # p
sharedBase = int(input("Enter the primitive root :"))      # g
 
def isNotPrime(possible):
    i = 2
    while i*i <= possible:
        if (possible % i) == 0:
            return True
        i = i + 1
    return False

def primRoots(theNum):
    if isNotPrime(theNum):
        raise ValueError("Sorry, the number must be prime.")
    o = 1
    roots = []
    r = 2
    while r < theNum:
        k = pow(r, o, theNum)
        while (k > 1):
            o = o + 1
            k = (k * r) % theNum
        if o == (theNum - 1):
            roots.append(r)
        o = 1
        r = r + 1
    return roots

all=primRoots(sharedPrime)
print(all)

if sharedBase in all:
	aliceSecret = int(input("Enter the Alice's Secret key :"))    # a
	bobSecret = int(input("Enter the Bob's Secret key :"))      # b
	# Begin
	print( "Publicly Shared Variables:")
	print( "\nPublicly Shared Prime: " , sharedPrime )
	print( "\nPublicly Shared Base:  " , sharedBase )
 
	# Alice Sends Bob A = g^a mod p
	A = (sharedBase**aliceSecret) % sharedPrime
	print( "\nAlice Sends Over Public Channel: " , A )
 
	# Bob Sends Alice B = g^b mod p
	B = (sharedBase ** bobSecret) % sharedPrime
	print("\nBob Sends Over Public Channel: ", B )
 
	print( "\n------------\n" )
	print( "Privately Calculated Shared Secret:" )
	# Alice Computes Shared Secret: s = B^a mod p
	aliceSharedSecret = (B ** aliceSecret) % sharedPrime
	print( "    Alice Shared Secret: ", aliceSharedSecret )
 
	# Bob Computes Shared Secret: s = A^b mod p
	bobSharedSecret = (A**bobSecret) % sharedPrime
	print( "    Bob Shared Secret: ", bobSharedSecret )
else:
	print("Here ", sharedBase ," is not primitive root of ", sharedPrime)

