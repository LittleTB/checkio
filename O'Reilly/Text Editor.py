class Text():
	def __init__(self,text):
		self.text = text

	def write(self,cur_text):
		self.text += cur_text

	def set_font(self,font):

	def show(self,font):
		print('['+font+']'+self.text+'['+font+']')

	def restore(self):
		self.text.save()

class SaveText():
	def __init__(self):

	def save_text(self):

	def get_version(self):