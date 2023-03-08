class Product:

    def __init__(self, id, name, referencePrice, discount, categoryName):
        self.id = id
        self.name = name
        self.referencePrice = referencePrice
        self.discount = discount
        self.categoryName = categoryName

    def printInfo(self):
        print("----------------------------------------")
        print("----------- Product Info ---------------")
        print("i  = " + str(self.id))
        print("n  = " + self.name)
        print("c  = " + self.categoryName)
        print("r  = " + str(self.referencePrice))
        print("u  = " + str(self.discount))

