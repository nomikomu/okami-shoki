import pyglet as pygl
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
"""
  TODO:
    Config -->
      __init__ - screnn setting
      get_gl_atrributes - conditions
      is_complete - conditions

"""

class Config:
  def __init__(self,scrnn_x=600,scrnn_y=400,depth=24):
    
    on_resize(self.scrnn_x,self.scrnn_y)
    depth_size(self.depth)

  def get_gl_atrributes():
    return self
  def is_complete():
    return self

def get_platform():
  platform = pyglet.window.get_platform()
  display = platform.get_default_display()

"""
   Main varibles to use
    win    ->  name for obj creating window
    lablel ->  'DZA WARLDO' text; formating, placement
    image  ->  reading image file
    music  ->  reading music file
"""
win = pygl.window.Window()
label = pyglet.text.Label('DZA WARLDO',
                          font_name='Times New Roman',
                          font_size=36,
                          x=win.width//2,y=win.height//2,
                          anchor_x='center', anchor_y='center')
image = pygl.resource.image('test.png')
music = pygl.resource.media('test_battlelolis.mp3')

# Input for window > key, mouse etc.
@win.event
def on_key_press(symbol, modifiers):
  print 'key_pressed'
  #incl. pressed key name:
  #print 'key_pressed_{key}.format(symbol)
  #problem: can't get symbol this way ;(
  if symbol == key.A:
    print '--A_key_press'
  elif symbol == key.LEFT:
    print '--LEFT_key_press'
  elif symbol == key.ENTER:
    print '--ENTER_key_press'

@win.event
def on_mouse_press(x,y,button,modifiers):
  if button == mouse.LEFT:
    print 'LMB_press'
  if button == mouse.RIGHT:
    print 'RMB_press'
    win.push_handlers(pyglet.window.event.WindowEventLogger())

# Printing to window
@win.event
def on_draw():

  get_platform()
  glClear(GL_COLOR_BUFFER_BIT)
  image.blit(win.width//2-84,275)
  glBegin(GL_POINTS)
  glVertex2i(50,50)
  glVertex2i(75,100)
  glVertex2i(100,150)
  glEnd()
  label.draw()
  
music.play()
pyglet.app.run()


