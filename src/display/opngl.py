import pyglet as pygl
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
"""
  TODO:
    


"""

# class stuff here

"""
   Main varibles to display
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


