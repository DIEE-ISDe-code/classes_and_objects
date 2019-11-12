from basket_oranges import Basket, Orange

aBasket=Basket()
aBasket.initBasket()

orange1=Orange()
orange2=Orange()
orange3=Orange()

orange1.setWeight(1)
orange2.setWeight(2)
orange3.setWeight(3)

orange1.pick(aBasket)
orange2.pick(aBasket)
orange3.pick(aBasket)


aBasket.printWeightOfOranges(2)
aBasket.printWeightOfOranges()
