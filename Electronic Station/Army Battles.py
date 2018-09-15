class Army():
	def __init__(self):
		self.health = 0
		self.attack = 0
		self.num = 0

	def add_units(self, x, num):
		self.health = x().health
		self.attack = x().attack
		self.num = num


class Battle:
	def fight(self, first_army, second_army):
		x2 = y2 = 0
		while first_army.num > 0 and second_army.num > 0:
			x1 = first_army.health if x2 == 0 else x2
			y1 = second_army.health if y2 == 0 else y2
			while True:
				y1 -= first_army.attack
				
				if y1 <= 0:
					x2 = x1
					y2 = 0
					second_army.num -= 1
					break
				x1 -= second_army.attack
				if x1 <= 0:
					y2 = y1
					x2 = 0
					first_army.num -= 1
					break

		return True if first_army.num else False

class Warrior:
	def __init__(self):
		self.health = 50
		self.attack = 5
		self.is_alive = True

class Knight(Warrior):
	def __init__(self):
		super().__init__()
		self.attack = 7

def fight(first, second):
	while True:
		second.health -= first.attack
		if second.health <= 0:
			second.is_alive = False
			return True

		first.health -= second.attack
		if first.health <= 0:
			first.is_alive = False
			return False

army1 = Army()
army1.add_units(Knight, 3)

army2 = Army()
army2.add_units(Warrior, 3)

army3 = Army()
army3.add_units(Warrior, 30)
army3.add_units(Knight, 5)
print(army3.num)

army4 = Army()
army4.add_units(Warrior, 30)

battle = Battle()
print(battle.fight(army1, army2))
print(battle.fight(army3, army4))