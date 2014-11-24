#!/usr/bin/env python
#-*- coding:utf-8 -*-
import LIS,sys,os



try:
	from tkinter import *
except ImportError:  #Python 2.x
	PythonVersion = 2
	from Tkinter import *
	from tkFont import Font
	from ttk import *
	#Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
	from tkMessageBox import *
	#Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
	#import tkFileDialog
	#import tkSimpleDialog
else:  #Python 3.x
	PythonVersion = 3
	from tkinter.font import Font
	from tkinter.ttk import *
	from tkinter.messagebox import *
	#import tkinter.filedialog as tkFileDialog
	#import tkinter.simpledialog as tkSimpleDialog	#askstring()

class Application_ui(Frame):
	#这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master.title('Form1')
		self.master.geometry('416x388')
		self.createWidgets()

	def createWidgets(self):
		self.top = self.winfo_toplevel()

		self.style = Style()

		self.Text1Var = StringVar(value='')
		self.Text1 = Text(self.top, font=('宋体',9))
		self.Text1.place(relx=0., rely=0., relwidth=1.002, relheight=1.013)


class Application(Application_ui):
	#这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
	def __init__(self, master=None):
		
		Application_ui.__init__(self, master)
		try:
			F = open(S,"r")
		except:
			raise error
		#self.Text1.delete(1.0,END)
		for eachline in F:
			self.Text1.insert(END, eachline.decode("GBK","Ignore").encode("UTF-8"))
		F.close()

if __name__ == "__main__":
	RES = LIS.Listen()
	Book = RES[1][-1]
	Type = RES[1][:-2]
	Path = os.path.split(os.path.realpath(__file__))[0]
	global S
	S = Path+"\\ANS\\Book_"+Book+"\\"+Type+"\\"+RES[0]+".txt"
	top = Tk()
	top.wm_attributes('-topmost',1)
	Application(top).mainloop()