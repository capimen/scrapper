class ProductScraped:

    def __init__(self,productId, url, commerceName, priceClass, priceTag, nameClass, nameTag, commerceId, productCommerceDetailId ):
        self.productId = productId
        self.productName = None
        self.url = url
        self.commerceName = commerceName
        self.priceClass = priceClass
        self.priceTag = priceTag
        self.nameClass = nameClass
        self.nameTag = nameTag
        self.commerceId = commerceId
        self.productCommerceDetailId = productCommerceDetailId
        self.valor = "null"

    def formatValor(self):
        self.valor = self.valor.replace("$", "").strip();
        self.valor = self.valor.replace(".", "").strip();
