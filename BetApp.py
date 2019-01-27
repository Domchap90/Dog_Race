import tkinter as tk 
import tkinter.messagebox
from tkinter import font, Label, Entry, Radiobutton, Listbox, Button
import re

intro_txt = 'Welcome to the Betting Parlour! Each Bettor starts with £50 to bet. Minimum bet on each race is £5, Max bet is £15. Odds are Double or nothing.\n Have fun!'

class Guy:
    def __init__(self, bettorname, cash, mybet):
        self.bettorname = bettorname
        self.cash = 50
        self.mybet = self.Bet()

    class Bet():
        def __init__(self, betnum, dognum):
            self.dognum = dognum
            self.betnum = betnum


class BetApp():
    def __init__(self,master,n,d,b):
        self.master = master
        self.n = tk.StringVar()
        self.d = tk.IntVar(value=None) 
        self.b = tk.IntVar()
        txt_font = font.Font(family = 'Times new roman', size = 18, weight = 'bold')
        self.intro = Label(master, text = intro_txt, bg = 'light blue', fg ='red', font = txt_font).grid(row = 0, column = 0, columnspan = 8, sticky= 'W')
        self.select()

        master.title('Betting Parlour') 
        master.configure(bg = 'light blue')

        self.betbut = Button(master,text = 'Bet', command = self.PlaceBet).grid(row =4, column = 1)
        self.description = Label(master, text = 'pounds on dog number ',width = 18, bg = 'light blue').grid(row = 4, column = 3)

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
        self.b = tk.IntVar(value=self.amount_options[self.ind])
        

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
        self.d = tk.IntVar(value=self.dog_options[self.index])
        
    def select(self):
        self.Bettors = ['Bill', 'Ted', 'Joe']
        for i, bettor in enumerate(self.Bettors, 1):
            bettor = Guy(bettor,True, True)
            self.selector = Radiobutton(self.master,text = bettor + ' has £' + bettor.cash, variable = self.n, value = bettor, command = self.selbet, bg = 'light blue').grid(row = i, column = 0)

    def selbet(self): 
            #get name from radio button and use in Label
        self.bettor = self.n.get()
        self.current_bettor = Label(self.master, text = self.bettor ,width = 5, bg = 'light blue')
        self.current_bettor.grid(row = 4, column = 0)
        
        

    def PlaceBet(self):

        self.betnumber = self.b.get()
        self.dognumber = self.d.get()
        betlabel = self.bettor + ' has bet £' + str(self.betnumber) + ' on dog number ' + str(self.dognumber) + '.'
        #if self.n != None and self.b != None and self.d != None:
        if self.bettor == 'Bill' and self.betnumber !=0 and self.dognumber !=0:
            B1 = Bet(self.bettor, self.betnumber, self.dognumber)
            b1 = Label(self.master, text = betlabel, bg = 'light blue',).grid(row = 1, column = 1)

        elif self.bettor == 'Ted' and self.betnumber !=0 and self.dognumber !=0:
            B2 = Bet(self.bettor, self.betnumber, self.dognumber)
            b2 = Label(self.master, text = betlabel, bg = 'light blue',).grid(row = 2, column = 1)

        elif self.bettor == 'Joe' and self.betnumber != 0 and self.dognumber !=0:#condition type(self.betnum) is not type(float)?
            B3 = Bet(self.bettor, self.betnumber, self.dognumber)
            b3 = Label(self.master, text = betlabel, bg = 'light blue',).grid(row = 3, column = 1)

        else:
            tk.messagebox.showerror('Incomplete fields','Please make sure you have selected all appropriate fields before placing your bet!')
    
    def Startrace(self):
        SRbutton = Button(master,text = 'Start Race!', command = self.Go)

    #def Go():
        #if b1 == True and b2 == True and b3 == True:
            #start race
        #else:
         #   print('Please ensure all bets are placed before starting the race.')

    def Racetrack():
        photo = PhotoImage(file = '')

            
root = tk.Tk()
App = BetApp(root, None, None, None)
App.betamount()
App.chosedog()

root.mainloop() 
