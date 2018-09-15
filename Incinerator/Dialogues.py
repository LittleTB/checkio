# 抽象中介者类
class AbstractChat:
	# 中介者管理的同事列表
	_objects = {}

	# 增加一个要被管理的同事
	def add_colleague(self, name, colleague):
		self._colleagues[name] = colleague
		colleague.set_mediator(self)

	# 中介者最重要的事件方法，处理多个同事对象之间的关系
	def execute(self, method, args):
		pass

# 人类
class Human:
	def send(self,message):
		return message

# 机器人类
class Robot:
	def send(self,message):
		return message

class Chat:
	def connect_human(self,name):