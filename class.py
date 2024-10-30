class Brand:
    name = 'online shopping'
    def __init__(self,name):
        self.name = name
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
a = Brand("Shopsy")
a.setColor("blue")
print(a.getColor())
