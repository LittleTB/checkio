class state:
	def call(self,con):
		pass
class green(state):
	def call(self,con):
		con.changeState(red())

class red(state):
	def call(self,con):
		con.changeState(blue())

class blue(state):
	def call(self,con):
		con.changeState(yellow())

class yellow(state):
	def call(self,con):
		con.changeState(green())

class Context:
	def __init__(self,state):
		self.state=state
	def call(self):
		self.state.call(self)
	def changeState(self,state):
		self.state=state

if __name__=="__main__":
	Green = green()
	context = Context(Green)
	for i in range(0, 3):
		print(context.state)
		context.call()
