#!/usr/bin/env python3


# Binary number
def Binary_Number(Number):
	return Number
VarX=3
VarX=bin(VarX)[2:]
print(VarX)


VarY=input("Number: ")
VarY=int(VarY)
print(f"Binary: {bin(VarY)[2:]}")


Namaku="Ruben Leonardo Sigalingging"
print(f"Nama Saya: {Namaku}")
print(f"Hasil 0:3 ~> {Namaku[0:3]}")
print(f"Hasil 1:3 ~> {Namaku[1:3]}")
print(f"Hasil 2:3 ~> {Namaku[2:3]}")
print(f"Hasil 3: ~> {Namaku[3:]}")