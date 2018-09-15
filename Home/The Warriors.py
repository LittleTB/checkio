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

chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()

print(fight(chuck, bruce)) # True
print(fight(dave, carl)) # False
print(chuck.is_alive) # True
print(bruce.is_alive) # False
print(carl.is_alive) # True
print(dave.is_alive) #False