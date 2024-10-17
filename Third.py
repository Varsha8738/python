#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "Uday", age = 20)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("Uday",20)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("Uday",20)


print(txt1)
print(txt2)
print(txt3)
-->OUTPUT
My name is Uday, I'm 20
My name is Uday, I'm 20
My name is Uday, I'm 20

