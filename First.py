# Python program to demonstrate
# string slicing
String = 'SASICSE' #0123456
# Using slice constructor
s1 = slice(3) #sas
s2 = slice(1, 10, 2)
s3 = slice(-1, -12, -2)
print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])
-->OUTPUT
String slicing
SAS
AIS
ECSS
