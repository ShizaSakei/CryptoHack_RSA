from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
e = 3
p = 752708788837165590355094155871
q = 986369682585281993933185289261

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

n = p * q
ct = 39207274348578481322317340648475596807303160111338236677373
pt = pow(ct, d, n)

decrypted = long_to_bytes(pt)
print(decrypted)