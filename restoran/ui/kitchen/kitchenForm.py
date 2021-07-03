import tkinter
from tkinter import ttk, TOP, BOTTOM, LEFT, RIGHT, BOTH, W
from tkinter import filedialog, simpledialog, messagebox
from tkinter import scrolledtext
import json
from restoran.io import io
class OrderUI():
    def __init__(self, parent, name, ammount):
        self.block = tkinter.Frame(parent,borderwidth = 1)
        self.parent=parent
        self.name = name
        self.mainLabel = tkinter.Label(self.block, width=15,text=f" {name}  x{ammount}", anchor='w')
        self.mainLabel.grid(row=0,column=0, sticky=W)


        self.confirm = tkinter.Button(self.block, text="DONE",command = lambda: self.block.pack_forget())
        self.confirm.grid(row=0,column=1)


        self.tutorial = tkinter.Button(self.block, text="Details", command = lambda : self.showDetails())
        self.tutorial.grid(row=0,column=2)
        # lambda za otvaranje uputsva preko


        self.block.pack(side=BOTTOM,fill=BOTH)

    def showDetails(self):
        detailsWIndow(self.parent, self.name)

class TicketUI():
    def __init__(self, parent, table, orders):
        self.ticket = tkinter.Frame(parent, highlightbackground="black", highlightthickness=1, padx=3, pady=3)
        self.block = tkinter.Frame(self.ticket, highlightbackground="black", highlightthickness=1)
        self.header = tkinter.Frame(self.ticket)
        self.confirm = tkinter.Button(self.header, text="DONE",command = lambda: self.ticket.pack_forget())
        self.confirm.pack(side=RIGHT,fill=BOTH)
        self.tableNo = tkinter.Label(self.header, text=f"Table {table} order")
        self.tableNo.pack(side=LEFT,fill=BOTH)

        self.header.pack(side=TOP,fill=BOTH)
        self.block.pack(side=TOP,fill=BOTH)
        self.ticket.pack(side=TOP,fill=BOTH)
        for order in orders:
            OrderUI(self.block, order["name"], order["ammount"])
class detailsWIndow():
    def __init__(self, parent, mealName):
        super().__init__()
        self.window = tkinter.Toplevel(parent)
        #self.window.geometry("1000x500")

        self.normativ = tkinter.Frame(self.window)
        # generisi vrednost
        

        self.tutorial = tkinter.Frame(self.window)
        mealData = io.loadMealData(mealName)
        # with open(f"../../resources/mealData/{mealName}.json", 'r') as f:
        #     mealData = json.load(f)
        print(mealData)    
        self.ingredientsList = tkinter.Listbox(self.normativ, width=40, height=20)
        for ingredient in mealData["ingredients"]:  
            self.ingredientsList.insert("end",f"{ingredient['name']} : {ingredient['amount']}")

        self.instructions = scrolledtext.ScrolledText(self.tutorial, width=40,height=20)
        self.instructions.insert('end', mealData["instructions"])


        if "docsName" in mealData:
            self.docsButton = tkinter.Button(self.tutorial, width=0, text=f"Show full documentation", command= lambda : io.openDocs(mealData["docsName"]))
            self.docsButton.pack(side=BOTTOM)
        self.instructions.pack(side=TOP)
        self.ingredientsList.pack(side=BOTTOM)
        self.normativ.pack(side=LEFT)
        self.tutorial.pack(side=RIGHT)

        self.window.mainloop()


    # def showPreviewSheet(self, sheetKey):
    #     self.textPanel.delete(1.0, "end")
    #     self.textPanel.insert("end", self.previewData[sheetKey])
    #     #self.textPanel.see("start")
    # def generatePreviewButtons(self, keys):
    #     buttonBuilder = lambda key: tkinter.Button(self.buttonPanel, width=0, text=f"Show {key}", command= lambda : self.showPreviewSheet(key))
    #     for key in keys:
    #         btn = buttonBuilder(key)
    #         btn.pack(side=LEFT)

class Kitchen():
    def __init__(self):
        self.app = tkinter.Tk()

        self.orders = tkinter.Frame(self.app)

        self.orders.pack(side=BOTTOM,fill=BOTH)

    # def addNewOrder(self, orderName, orderAmmount):
    #     order = OrderUI(self.orders, orderName, orderAmmount)
    #     # order.pack(side=BOTTOM)
    #     print(f"Added new {order}")

    def newTicket(self, table, orders):
        TicketUI(self.orders, table, orders)
def run():
    app = Kitchen()
    # app.addNewOrder("Pljeska", 2)
    app.newTicket(2, [{"name": "Omlet", "ammount": 1},{"name": "Brusketi", "ammount": 2},{"name": "Sendvic", "ammount": 4}])
    app.newTicket(3, [{"name": "Rizoto", "ammount": 1},{"name": "Musli", "ammount": 1},{"name": "Palacinke", "ammount": 2}])
    app.newTicket(8, [{"name": "Omlet", "ammount": 1}])
    app.newTicket(1, [{"name": "Rizoto", "ammount": 1},{"name": "Tost", "ammount": 1},{"name": "Brusketi", "ammount": 2}])
    app.newTicket(4, [{"name": "Pasta", "ammount": 1},{"name": "Palacinke", "ammount": 2}])
    app.newTicket("Dostava 1", [{"name": "Brusketi", "ammount": 3}])
    app.newTicket("Dostava 2", [{"name": "Rizoto", "ammount": 1},{"name": "Musli", "ammount": 1},{"name": "Palacinke", "ammount": 2}])

    app.app.mainloop()
if __name__ == "__main__":
    run()