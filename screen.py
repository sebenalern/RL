import pyglet

window = pyglet.window.Window()


class Screen:

	chars = []

	def __init__(self):
		global window
		self.char_height = 36
		self.char_width = 36
		self.width = 10*self.char_width
		self.height = 10*self.char_height
		window.height = self.height
		window.width = self.width

	def draw_char(self,char,x,y):
		label = pyglet.text.Label(char,
                      font_name='Times New Roman',
                      font_size=36,
                      x=x*self.char_width, y=y*self.char_height,
                      anchor_x='center', anchor_y='center')
		self.chars.append(label)

screen = Screen()
screen.draw_char("L",2,2)

@window.event
def on_draw():
	window.clear()
	global screen
	print("Test")
	for c in screen.chars:
		c.draw()

pyglet.app.run()

	