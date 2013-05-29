import pyglet as pygl
from pyglet.gl import *

win = pygl.window.Window()
@win.event
def on_draw():
  glClear(GL_COLOR_BUFFER_BIT)
  glBegin(GL_POINTS)
  glVertex2i(50,50)
  glVertex2i(75,100)
  glVertex2i(100,150)
  glEnd()

pyglet.app.run()
