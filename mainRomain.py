from character import *
from ennemy import *

michel = character()
gobelin = ennemy(damage = 30)

michel.presentation()

while gobelin.life and michel.life:
    gobelin.dealDamage(michel)
    michel.dealDamage(gobelin)
  