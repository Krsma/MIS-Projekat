import tkinter
from tkinter import ttk, TOP, BOTTOM, LEFT, RIGHT, BOTH, W
from tkinter import filedialog, simpledialog, messagebox
from tkinter import scrolledtext
import json
import matplotlib.pyplot as plt

statistika = [
    {"item" : "Omlet", "boughtNo" : 54, "profitMargin" : 48},
    {"item" : "Tost", "boughtNo" : 24, "profitMargin" : 120},
    {"item" : "Biftek", "boughtNo" : 4, "profitMargin" : 364},
    {"item" : "Palacinke", "boughtNo" : 34, "profitMargin" : 220},
    {"item" : "Tortilje", "boughtNo" : 28, "profitMargin" : 150},
    {"item" : "Cezar salata", "boughtNo" : 24, "profitMargin" : 350}
]


class StatsForm():
    def __init__(self):
        self.app = tkinter.Tk()
        #self.app.geometry("300x300")
        self.stats = statistika

        self.statsList = tkinter.Listbox(self.app, width=50)
        for item in self.stats:
            self.statsList.insert("end",f"Item {item['item']} : Purchased {item['boughtNo']} times : Profit margin {item['profitMargin']}")

        graphFrame = tkinter.Frame(self.app)
        buttonFrame = tkinter.Frame(self.app)
        self.pictureFrame = tkinter.Frame(graphFrame)
        self.profitButton = tkinter.Button(buttonFrame, text='View profit data', width=25, command = lambda: self.showProfitData())
        self.profitButton.pack(side=LEFT)
        self.purchaseButton = tkinter.Button(buttonFrame, text='View purchasing data', width=25, command = lambda: self.showPurchasingData())
        self.purchaseButton.pack(side=LEFT)
        #self.profitButton = tkinter.Button(buttonFrame, text='View profit data', width=25)
        #self.profitButton.pack(side=LEFT)

        self.statsList.pack(side=BOTTOM)
        #graphFrame.pack(side=RIGHT)
        buttonFrame.pack(side=TOP)
    def showProfitData(self):
        profitWindow(self.app, self.stats)
    def showPurchasingData(self):
        purchasingWindow(self.app, self.stats)

class profitWindow():
    def __init__(self, parent, stats):
        super().__init__()
        #print("Usao")
        self.window = tkinter.Toplevel(parent)
        self.window.geometry("300x300")
        sortLambda = lambda x : x["boughtNo"]*x["profitMargin"]
        self.stats = sorted(stats, key = sortLambda, reverse = True)
        self.statsList = tkinter.Listbox(self.window, width = 40)
        index = 0
        self.statsList.insert('end', "Sorted list of most profitable items ")
        self.statsList.insert('end', "--------------------------------------")
        for item in self.stats:
            index+=1
            self.statsList.insert("end",f"Item {index}: {item['item']} :  Profit {item['boughtNo']*item['profitMargin']}")

        self.profitButton = tkinter.Button(self.window, text='Show as graph', width=25, command = lambda: self.generatePlot())
        self.profitButton.pack(side=BOTTOM)
        self.statsList.pack(side=TOP)
        self.window.mainloop()
    def generatePlot(self):
        labels = [x["item"] for x in self.stats]
        values = [x["boughtNo"]*x["profitMargin"] for x in self.stats]

        # # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        # sizes = [15, 30, 45, 10]
        #explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

class purchasingWindow():
    def __init__(self, parent, stats):
        super().__init__()
        #print("Usao")
        self.window = tkinter.Toplevel(parent)
        self.window.geometry("300x300")
        sortLambda = lambda x : x["boughtNo"]
        self.stats = sorted(stats, key = sortLambda, reverse = True)
        self.statsList = tkinter.Listbox(self.window, width = 40)
        index = 0
        for item in self.stats:
            index+=1
            self.statsList.insert("end",f"Item {index}: {item['item']} :  Purchased {item['boughtNo']} times")

        self.profitButton = tkinter.Button(self.window, text='Show as graph', width=25, command = lambda: self.generatePlot())
        self.profitButton.pack(side=BOTTOM)
        self.statsList.pack(side=TOP)
        self.window.mainloop()
    def generatePlot(self):
        labels = [x["item"] for x in self.stats]
        values = [x["boughtNo"] for x in self.stats]

        # # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        # sizes = [15, 30, 45, 10]
        #explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

def run():
    app = StatsForm()
    # app.addNewOrder("Pljeska", 2)
    #app.newTicket(2, [{"name": "Omlet", "ammount": 1},{"name": "Brusketo", "ammount": 2},{"name": "Sendvic", "ammount": 4}])
    app.app.mainloop()
if __name__ == "__main__":
    run()