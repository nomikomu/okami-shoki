import pyglet as pygl
from pyglet.gl import *

win = pygl.window.Window()
label = pyglet.text.Label('DZA WARLDO',
                          font_name='Times New Roman',
                          font_size=36,
                          x=win.width//2,y=win.height//2,
                          anchor_x='center', anchor_y='center')
image = pyglet.resource.image('test.png')
@win.event
def on_key_press(symbol, modifiers):
  print 'key_pressed'
  #incl. pressed key name:
  #print 'key_pressed_{key}.format(symbol)
  #problem: can't get symbol this way ;(


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

pyglet.app.run()
