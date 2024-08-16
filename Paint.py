import tkinter as tk
import math
class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.master.geometry("500x500")
        self.master.resizable(False, False)
        self.penColour = 'black'
        self.penWidth = 1
        self.redValue = 0
        self.greenValue = 0
        self.blueValue = 0
        self.create_widgets()
    def create_widgets(self):
        #create
        #menu
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        root.config(menu=menubar)
        filemenu.add_command(label="color", command=self.color)
        filemenu.add_command(label="brush", command=self.brush)
        menubar.add_cascade(label="File", menu=filemenu)
        #canvas
        self.DrawCanvas = tk.Canvas( width= 500,height = 300,bg='#ffffff')
        self.DrawCanvas.grid(row = 0, column = 1)
        #buttons
        self.clearButton = tk.Button(self, text='clear', bg='red',command = self.clear)
        self.Pwidth = tk.Scale(self, command=self.ChangeW, from_=1, to=30)
        self.clearButton.grid(row = 0, column = 0)

        self.Pwidth.grid(row=10, column =0)
        
        #bind
        self.DrawCanvas.bind("<Button-1>",self.draw)
        self.DrawCanvas.bind("<ButtonRelease-1>",self.drawRelease)

    def draw(self,event):
        self.xCoor = event.x
        self.yCoor = event.y
        
    def drawRelease(self,event):
        self.xCoor1 = event.x
        self.yCoor1 = event.y
        #draw line
        self.DrawCanvas.create_line(self.xCoor,self.yCoor,self.xCoor1,self.yCoor1, fill=self.penColour, width=self.penWidth)
    def drawArcRelease(self,event):
        self.xCoor1 = event.x
        self.yCoor1 = event.y
        gradient=(self.yCoor1 - self.yCoor)/(self.xCoor1 - self.xCoor)
        if gradient < 0:
             angle = 180 +(math.degrees((math.atan(gradient))))
        else:
            angle = math.degrees((math.atan(gradient)))
        print(gradient)
        print(angle)                   
        #draw line
        self.DrawCanvas.create_arc(self.xCoor,self.yCoor,self.xCoor1,self.yCoor1, start=0,extent=angle,outline=self.penColour,width=self.penWidth)
    def ovalReleased(self,event):
        self.xCoor1 = event.x
        self.yCoor1 = event.y
        self.DrawCanvas.create_oval(self.xCoor,self.yCoor,self.xCoor1,self.yCoor1,outline=self.penColour, width=self.penWidth)
    def drawSquRelease(self,event):
        self.xCoor1 = event.x
        self.yCoor1 = event.y
        self.DrawCanvas.create_rectangle(self.xCoor,self.yCoor,self.xCoor1,self.yCoor1,outline=self.penColour, width=self.penWidth)
    def ChangeW(self,e):
        self.penWidth = e
    def clear(self):
        self.DrawCanvas.delete('all')
    def activate_paint(self,e):
        self.lastx =e.x
        self.lasty =e.y
        self.DrawCanvas.bind('<B1-Motion>', self.paint)
    def paint(self,e):
        self.x = e.x
        self.y = e.y
        self.DrawCanvas.create_line((self.lastx, self.lasty, self.x, self.y), fill=self.penColour, width=self.penWidth)
        self.lastx =e.x
        self.lasty =e.y
    def color(self):
         clWin = tk.Tk()
         clWin.master = self
         self.grid()
         clWin.geometry("400x100")
         clWin.resizable(False, False)
         self.create_clr_widgets(clWin)

    def create_clr_widgets(self, master):
        self.redButton = tk.Button(master,bg='#f01a21', command = self.SetRed, height=1,width=2)
        self.blueButton = tk.Button(master,bg='#3483e3', command = self.SetBlue, height=1,width=2)
        self.greenButton = tk.Button(master,bg='#0bbd23', command = self.SetGreen, height=1,width=2)
        self.blackButton = tk.Button(master,bg='#000000', command = self.SetBlack, height=1,width=2)
        self.yellowButton = tk.Button(master,bg='#fcee4c', command = self.SetYellow, height=1,width=2)
        self.orangeButton = tk.Button(master,bg='#f2a229', command = self.SetOrange, height=1,width=2)
        self.pinkButton = tk.Button(master,bg='#f79cff', command = self.SetPink, height=1,width=2)
        self.purpleButton = tk.Button(master,bg='#b375ff', command = self.SetPurple, height=1,width=2)
        self.whiteButton = tk.Button(master,bg='#ffffff', command = self.SetWhite, height=1,width=2)
        self.cyanButton = tk.Button(master,bg='#a1f0e8', command = self.SetCyan, height=1,width=2)
        self.brownButton = tk.Button(master,bg='#966c56', command = self.SetBrown, height=1,width=2)
        self.greyButton = tk.Button(master,bg='#adadad', command = self.SetGrey, height=1,width=2)
        self.redButton.grid(row = 0, column = 0)
        self.blueButton.grid(row = 0, column = 1)
        self.greenButton.grid(row = 0, column = 2)
        self.blackButton.grid(row = 0, column = 3)
        self.yellowButton.grid(row = 1, column = 0)
        self.orangeButton.grid(row = 1, column = 1)
        self.pinkButton.grid(row = 1, column = 2)
        self.purpleButton.grid(row = 1, column = 3)
        self.whiteButton.grid(row = 2, column = 0)
        self.brownButton.grid(row = 2, column = 1)
        self.cyanButton.grid(row = 2, column = 2)
        self.greyButton.grid(row = 2, column = 3)
    def brush(self):
         brWin = tk.Tk()
         brWin.master = self
         self.grid()
         brWin.geometry("400x100")
         brWin.resizable(False, False)
         self.create_br_widgets(brWin)
    def create_br_widgets(self, master):
        self.arcButton = tk.Button(master, text='arc', bg='red',command = self.SetArc)
        self.lineButton = tk.Button(master, text='line',bg='red', command = self.SetLine)
        self.ovalButton = tk.Button(master, text='oval',bg='red', command = self.SetOval)
        self.SquButton = tk.Button(master, text='Square',bg='red', command = self.SetSquare)
        self.brushButton = tk.Button(master, text='brush',bg='red', command = self.SetBrush)
        self.arcButton.grid(row = 0, column = 0)
        self.lineButton.grid(row = 0, column = 1)
        self.ovalButton.grid(row = 0, column = 2)
        self.SquButton.grid(row = 0, column = 3)
        self.brushButton.grid(row = 0, column = 4)
    ##SET COLOUR ##
    def SetRed(self):
        self.penColour = '#f01a21'
    def SetBlue(self):
        self.penColour = '#3483e3'
    def SetBlack(self):
        self.penColour = '#000000'
    def SetGreen(self):
        self.penColour = '#0bbd23'
    def SetOrange(self):
        self.penColour = '#f2a229'
    def SetPink(self):
        self.penColour = '#f79cff'
    def SetPurple(self):
        self.penColour = '#b375ff'
    def SetWhite(self):
        self.penColour = '#ffffff'
    def SetYellow(self):
        self.penColour = '#fcee4c'
    def SetGrey(self):
        self.penColour = '#adadad'
    def SetBrown(self):
        self.penColour = '#966c56'
    def SetCyan(self):
        self.penColour = '#a1f0e8'
    ## BINDINGS##
    def SetBrush(self):
        self.DrawCanvas.bind("<Button-1>",self.activate_paint)
        self.DrawCanvas.unbind("<ButtonRelease-1>")
    def SetSquare(self):
        self.DrawCanvas.bind("<Button-1>",self.draw)
        self.DrawCanvas.bind("<ButtonRelease-1>",self.drawSquRelease)
        self.DrawCanvas.unbind('<B1-Motion>')
    def SetArc(self):
        self.DrawCanvas.bind("<Button-1>",self.draw)
        self.DrawCanvas.bind("<ButtonRelease-1>",self.drawArcRelease)
        self.DrawCanvas.unbind('<B1-Motion>')
    def SetLine(self):
        self.DrawCanvas.bind("<Button-1>",self.draw)
        self.DrawCanvas.bind("<ButtonRelease-1>",self.drawRelease)
        self.DrawCanvas.unbind('<B1-Motion>')
    def SetOval(self):
        self.DrawCanvas.bind("<Button-1>",self.draw)
        self.DrawCanvas.bind("<ButtonRelease-1>",self.ovalReleased)
        self.DrawCanvas.unbind('<B1-Motion>')
root = tk.Tk()
Bluevar = tk.IntVar()
Redvar = tk.IntVar()
Greenvar = tk.IntVar()
app = Application(master = root)
app.mainloop()
