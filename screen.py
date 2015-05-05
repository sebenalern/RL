import pyglet

window = pyglet.window.Window()


class Screen:

	arr = []

	def __init__(self):
		global window
		self.char_size = 18
		self.width = 20
		self.height = 20
		window.height = self.height*self.char_size+5
		window.width = self.width*self.char_size

		for y in range(self.height):
			for x in range(self.width):
				label = pyglet.text.Label("#",
                      font_name='Courier',
                      font_size=self.char_size,
                      x=x*self.char_size, y=y*self.char_size,
                      anchor_x='left', anchor_y='bottom')
				self.arr.append(label)

	def set_char(self,char,x,y):
		self.arr[y*self.width+x].text = char

	def clear_chars(self):
		for label in self.arr:
			label.text = " "

screen = Screen()
for y in range(5):
	for x in range(5):
		screen.set_char("L",x,y)

@window.event
def on_draw():
	window.clear()
	global screen
	print("Test")
	for label in screen.arr:
		label.draw()

pyglet.app.run()

	