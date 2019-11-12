class Orange:
    def setWeight(self,aWeight):
        self.weight=aWeight
    def setOrchard(self, anOrchard):
        self.orchard = anOrchard
    def pick(self, aBasket):
        self.basket=aBasket
        #aBasket.listOfOranges.append(self)
        aBasket.addOrange(self)


class Basket:
    def initBasket(self):
        self.listOfOranges=[]
    def addOrange(self, anOrange):
       self.listOfOranges.append(anOrange)

    def printWeightOfOranges(self,minWeight=0):
        # listOfWeight=[]
        # for el in self.listOfOranges:
        #     if el.weight>=minWeight:
        #         listOfWeight.append(el.weight)
        #

        listOfWeight= [el.weight for el in self.listOfOranges if el.weight>=minWeight]
        print(listOfWeight)
        