#!/usr/bin/env python3
from Crypto.Util.number import long_to_bytes, inverse
import owiener

# Valores iniciales
N = 0x8da7d2ec7bf9b322a539afb9962d4d2ebeb3e3d449d709b80a51dc680a14c87ffa863edfc7b5a2a542a0fa610febe2d967b58ae714c46a6eccb44cd5c90d1cf5e271224aa3367e5a13305f2744e2e56059b17bf520c95d521d34fdad3b0c12e7821a3169aa900c711e6923ca1a26c71fc5ac8a9ff8c878164e2434c724b68b508a030f86211c1307b6f90c0cd489a27fdc5e6190f6193447e0441a49edde165cf6074994ea260a21ea1fc7e2dfb038df437f02b9ddb7b5244a9620c8eca858865e83bab3413135e76a54ee718f4e431c29d3cb6e353a75d74f831bed2cc7bdce553f25b617b3bdd9ef901e249e43545c91b0cd8798b27804d61926e317a2b745
e = 0x86d357db4e1b60a2e9f9f25e2db15204c820b6e8d8d04d29db168c890bc8a6c1e31b9316c9680174e128515a00256b775a1a8ccca9c6936f1b4c2298c03032cda4dd8eca1145828d31466bf56bfcf0c6a8b4a1b2fb27de7a57fae7430048d7590734b2f05b6443ad60d89606802409d2fa4c6767ad42bffae01a8ef1364418362e133fa7b2770af64a68ad50ad8d2bd5cebb99ceb13368fb31a6e7503e753f8638e21a96af1b6498c18578ba89b98d70fa482ad137d28fe701b4b77baa25d5e84c81b26ee9bddf8cbb51a071c60dd57714de379cd4bc14932809ba18524a0a18e4133665cfc46e2c4fcfbc28e0a0957e5513a7307c422b87a6182d0b6a074b4d
c = 0x6a2f2e401a54eeb5dab1e6d5d80e92a6ca189049e22844c825012b8f0578f95b269b19644c7c8af3d544840d380ed75fdf86844aa8976622fa0501eaec0e5a1a5ab09d3d1037e55501c4e270060470c9f4019ced6c4e67673843daf2fd71c64f3dd8939ae322f2b79d283b3382052d076ebe9bb50b0042f1f7dd7beadf0f5686926ade9fc8370283ead781a21896e7a878d99e77c3bb1f470401062c0e0327fd85da1cf12901635f1df310e8f8c7d87aff5a01dbbecd739cd8f36462060d0eb237af8d613e2d9cebb67d612bcfc353ef2cd44b7ac85e471287eb04ae9b388b66ea8eb32429ae96dba5da8206894fa8c58a7440a127fceb5717a2eaa3c29f25f7


d = owiener.attack(e, N)
pt = pow(int(c), d, int(N))

decrypted = long_to_bytes(pt)
print(decrypted)

# NOTA IMPORTANTE: Se supone que este reto se resuelve mediante el Ataque de Wiener