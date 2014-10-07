from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import time
import profile 
import os,sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
from ctypes import *  
dll = cdll.LoadLibrary(dirname+"/DllTest.dll")  
def init():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	gluOrtho2D(-5, 5, 0, 10)
	
def Cal():
	print "PyLoop - Begin at "+str(time.time())
	x = 0
	y = 0
	List = []
	for  i in xrange (1000000):
		rand = random.random()
		glVertex2f(x, y)
		
		if (rand < 0.83):
			newx = (0.85 * x) + (0.04 * y)
			newy = (-0.04 * x) + (0.85 * y) + 1.6
			x = newx
			y = newy
		elif (rand < 0.91):
			newx = (0.2 * x) - (0.26 * y)
			newy = (0.23 * x) + (0.22 * y) + 1.6
			x = newx
			y = newy
		elif (rand<0.99):
			newx = (-0.15 * x) + (0.28 * y)
			newy = (0.26 * x) + (0.24 * y) + 0.44
			x = newx
			y = newy
		else:
			x = 0
			y = 0.16*y
	List.append((x,y))
	print "PyLoop - End at "+str(time.time())
	return List

 
def cb(a,b):
	glVertex2f(a,b)
	return 0
 
 
def drawFunc():
	print "\nMain - Begin at "+str(time.time())
	glClear(GL_COLOR_BUFFER_BIT)
	x = 0
	y = 0
	glPointSize(1.0)
	glBegin(GL_POINTS)
	glColor3f(1.0, 0.0, 0.0)
	Len = 1000000
	#Lis = (c_double*(Len*2))()
	'''
	print "Dll - Begin at "+str(time.time())
	res = dll.Lo(c_int(1000000) , glVertex2f)
	print "Dll - End at "+str(time.time())
	'''
	'''
	print "Lis - Begin at "+str(time.time())
	Lis = list(Lis)
	print "Lis - End at "+str(time.time())
	while Lis:
		glVertex2f(Lis.pop(), Lis.pop())
		#print Lis[2*i], Lis[2*i+1]
	'''
	#libtest = cdll.dll_py
	CMPFUNC = CFUNCTYPE(c_int ,c_double, c_double) 
	_callback = CMPFUNC(cb)
	a = dll.Lo
	a.restype = None
	print "Dll - Begin at "+str(time.time())
	a(c_int(1000000),_callback)
	print "Dll - End at "+str(time.time())
	
	glEnd()
	print "Main - End at "+str(time.time())
	glFlush()
def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGBA|GLUT_SINGLE)
	glutInitWindowSize(400, 400)
	glutCreateWindow("Sencond")
	init() 
	glutDisplayFunc(drawFunc)
	
	glutMainLoop()
	
main()