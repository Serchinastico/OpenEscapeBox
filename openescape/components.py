class Component(object):
	pass

class ButtonComponent(Component):
	def __init__(self, device, input_pin):
		self.__device = device
		self.__input_pin = input_pin

	def was_pressed(self):
		return False
