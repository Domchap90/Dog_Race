import tkinter as tk 
import tkinter.messagebox
import PIL.Image, PIL.ImageTk
import random as rnd
import sys
from tkinter import Grid
import time
from tkinter import font, Label, Entry, Radiobutton, Listbox, Button, Canvas

import re

intro_txt = 'Welcome to the Betting Parlour! Each Bettor starts with £50 to bet. Minimum bet on each race is £5, Max bet is £15. Odds are Double or nothing.\n Have fun!'

class Guy():
    def __init__(self, bettorname, betnum, dognum, cash = 50):
        self.bettorname = bettorname
        self.betnum = betnum
        self.dognum = dognum
        self.cash = cash 

class Dog():
    def __init__(self, dogobj, posx, posy):
        self.dogobj = dogobj
        self.posx = posx
        self.posy = posy

class BetApp():
    def __init__(self,master):
        self.master = master
        for x in range(5): 
            Grid.rowconfigure(master, x, weight = 1)
        for y in range(5):
            Grid.columnconfigure(master, y, weight = 1)
        self.n = tk.StringVar()
        self.dn = tk.IntVar() 
        self.bn = tk.IntVar() 
        txt_font = font.Font(family = 'Times new roman', size = 18, weight = 'bold')
        self.intro = Label(self.master, text = intro_txt, bg = 'light blue', fg ='red', font = txt_font).grid(row = 0, column = 0, columnspan = 8, sticky= 'W')
        self.B1 = Guy(0,0,0)
        self.B2 = Guy(0,0,0)
        self.B3 = Guy(0,0,0)
        self.Guys_dict = {}
        self.Gclass_list = [self.B1,self.B2,self.B3]
        self.timesbet = [0,0,0]
        self.select()

        master.title('Betting Parlour') 
        master.configure(bg = 'light blue')
        
        self.fieldsfilled = [i == 0 for i in range(3)] #allowing condition to be set for StartRace button to be activated. (Only upon all bets being submitted)
        Button(master,text = 'Bet', command = self.PlaceBet).grid(row =4, column = 1)
        Label(master, text = 'pounds on dog number ',width = 18, bg = 'light blue').grid(row = 4, column = 3)

    def betamount(self):
        self.amount_options = [i for i in range(5,16)]
        self.current_amount = Listbox(self.master, width = 3, bg = 'DeepSkyBlue2', relief = tk.SUNKEN, exportselection = 0)
        self.current_amount.grid(row = 4, column = 2)

        for a in range(len(self.amount_options)):
            self.current_amount.insert(a, self.amount_options[a])
        self.current_amount.bind('<<ListboxSelect>>', self.getbet)


    def getbet(self, event):
        self.tuple = self.current_amount.curselection()
        self.ind = self.tuple[0]
        self.bn = tk.IntVar(value = self.amount_options[self.ind])

    def chosedog(self):
        self.dog_options = [i+1 for i in range(4)]
        self.current_dog = Listbox(self.master, width = 3, bg = 'DeepSkyBlue2',relief = tk.SUNKEN,exportselection = 0)
        self.current_dog.grid(row = 4, column = 4)

        for a in range(len(self.dog_options)):
            self.current_dog.insert(a, self.dog_options[a])
        self.current_dog.bind('<<ListboxSelect>>', self.getdog)


    def getdog(self, event):
        self.tuple = self.current_dog.curselection()
        self.index = self.tuple[0]
        self.dn = tk.IntVar(value=self.dog_options[self.index])

    def select(self):
        self.Bettors = ['Bill', 'Ted', 'Joe']
        for i, bettor in enumerate(self.Bettors, 1):                                  
            self.Guys_dict[self.Gclass_list[i-1]] = Guy(bettor, True, True)#reading 
            self.selector = Radiobutton(self.master,text = bettor + ' has £' + str(self.Gclass_list[i-1].cash), variable = self.n, value = bettor   , command = self.selbet, bg = 'light blue').grid(row = i, column = 0)
            

    def selbet(self): 
            #get name from radio button and use in Label
        Guy.bettorname = self.n.get()
        self.current_bettor = Label(self.master, text = Guy.bettorname ,width = 5, bg = 'light blue')
        self.current_bettor.grid(row = 4, column = 0)
        
        

    def PlaceBet(self): 
        betnum = self.bn.get()
        dognum = self.dn.get()
        bettorname = self.n.get()
        #cash = 
        betlabel = bettorname + ' has bet £' + str(betnum) + ' on dog number ' + str(dognum) + '.'
        
        if bettorname == 'Bill' and betnum != 0 and dognum != 0:
            self.Gclass_list[0] = Guy(bettorname, betnum, dognum)
            self.Lab1 = Label(self.master, text = betlabel, bg = 'light blue',)
            self.Lab1.grid(row = 1, column = 1)
            self.fieldsfilled[0] = 1
            self.timesbet[0] += 1
            return self.fieldsfilled

        elif bettorname == 'Ted' and betnum != 0 and dognum != 0:
            self.Gclass_list[1] = Guy(bettorname, betnum, dognum)
            self.Lab2 = Label(self.master, text = betlabel, bg = 'light blue',)
            self.Lab2.grid(row = 2, column = 1)
            self.fieldsfilled[1] = 1
            self.timesbet[1] += 1
            return self.fieldsfilled

        elif bettorname == 'Joe' and betnum != 0 and dognum != 0:#condition type(self.betnum) is not type(float)?
            self.Gclass_list[2] = Guy(bettorname, betnum, dognum)
            self.Lab3 = Label(self.master, text = betlabel, bg = 'light blue',)
            self.Lab3.grid(row = 3, column = 1)
            self.fieldsfilled[2] = 1
            self.timesbet[2] += 1
            return self.fieldsfilled

        else:
            tk.messagebox.showerror('Incomplete fields','Please make sure you have selected all appropriate fields before placing your bet!')
        
    
    def Startrace(self):
        self.SRbutton = Button(self.master,text = 'Start Race!', command = self.Go)
        self.SRbutton.grid(row = 5, column = 1 )

    def Go(self):
        if self.fieldsfilled == [1,1,1] :
            self.dogs_move()
        else:
            tk.messagebox.showerror('Incomplete Bets','Please ensure all bets are placed before starting the race.')

    def Racetrack(self):
        self.track = Canvas(self.master, width = 1000, height = 500)
        self.track.grid(row = 5, column = 0)
        
        self.a = self.track.create_line(0,500,1000,500)
        self.b = self.track.create_line(0,375, 1000, 375)
        self.c = self.track.create_line(0,250,1000,250) 
        self.d = self.track.create_line(0,125,1000,125)     
        self.e = self.track.create_line(0,0,1000,0)   

        self.A = self.track.create_line(0,0,0,500)
        self.B = self.track.create_line(900, 0, 900, 500)
        self.C = self.track.create_line( 1000, 0, 1000, 500)  

        fl = PIL.Image.open('C:\\Users\\domch\\Downloads\\finish_line.png')
        fl = fl.resize((125,125))
        self.finish_line = PIL.ImageTk.PhotoImage(fl)
        k = [62,187,312,437]
        for j in k:
            self.track.create_image((937,j),image= self.finish_line)

    def dog_pic(self):
        image = PIL.Image.open('C:\\Users\\domch\\Downloads\\droopy_dog.jpg')
        image = image.resize((100,100))
        self.dog_image = PIL.ImageTk.PhotoImage(image)

        self.l = [50,190,310,440] # y coordinate
        self.dog_canvasobj = ['one','two','three','four']
        self.dog_class = ['One','Two','Three','Four']
        self.class_dict = {}
        for (i, k) in zip(self.l, range(4)):
            self.dog_canvasobj[k] = self.track.create_image((50,i), image= self.dog_image) # coordinates becomes attribute of function
            self.class_dict[self.dog_class[k]] = Dog(self.dog_canvasobj[k],self.track.coords(self.dog_canvasobj[k])[0],self.track.coords(self.dog_canvasobj[k])[1])
            
    def dogs_move(self):
        while self.class_dict[self.dog_class[0]].posx < 925 and self.class_dict[self.dog_class[1]].posx < 925 and self.class_dict[self.dog_class[2]].posx < 925 and self.class_dict[self.dog_class[3]].posx < 925:
            for key in dict.keys(self.class_dict):
                move_x = rnd.randint(50,100)
                self.class_dict[key].posx += move_x
                self.track.move(self.class_dict[key].dogobj,move_x,0)
            self.winner_is()
            self.track.update()
            self.track.after(200)

    def winner_is(self):
        self.winner_dict = {}
        for k in range(4):
            self.winner_dict[self.dog_class[k]] = self.dog_options[k]
        for l in dict.keys(self.class_dict):
            if self.class_dict[l].posx >= 925:
                tk.messagebox.showinfo('Race Finished!', 'The winner is Dog '+ l)
                self.winner = self.winner_dict[l]
                self.payout()
                break
            else:
                continue

    def payout(self):
        for clss in self.Gclass_list:
            if clss.dognum == self.winner:
                clss.cash = clss.betnum + clss.cash
            else:
                clss.cash = clss.cash - clss.betnum
        self.select()

    def resettor(self):
        self.Rbutton = Button(self.master,text = 'Reset', command = self.reset)
        self.Rbutton.grid(row = 5, column = 2)

    def reset(self):
        L = [self.Lab1,self.Lab2,self.Lab3]
        
        for z in range (4):
            doggy = self.class_dict[self.dog_class[z]]
            current_x = doggy.posx
            resetx = 50 - current_x
            self.track.move(doggy.dogobj,resetx,0)
            doggy.posx = 50
        #clear bet labels
        
        for l in L:
            n = 0
            while n < max(self.timesbet):
                l.grid_remove()
                n += 1
                print(n)

    def Quit(self):
        quit = Button(self.master, text = 'Quit', command = self.Checkquit)
        quit.grid(row = 5, column = 3)

    def Checkquit(self):
        check = tk.messagebox.askyesno("Exit App", "Are you sure you want to quit?")
        if check == True:
            self.master.destroy()
        else:
            None

root = tk.Tk()

App = BetApp(root)
App.betamount()
App.chosedog()  
App.Racetrack()
App.dog_pic()

App.Startrace()
App.resettor()
App.Quit()

root.mainloop() 