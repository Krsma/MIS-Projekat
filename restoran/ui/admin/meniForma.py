import tkinter
from tkinter import ttk, TOP, BOTTOM, LEFT, RIGHT, BOTH
from tkinter import filedialog, simpledialog, messagebox
from tkinter import scrolledtext

class NewMealUI():
    def __init__(self):
        self.app = tkinter.Tk()
        self.app.geometry("900x300")
        self.ingredients = []
        
        self.leftFrame= tkinter.Frame(self.app)
        self.entryFrame = tkinter.Frame(self.leftFrame)
        
        self.entryLabel = tkinter.Label(self.entryFrame, text="Meal Name")
        self.entryLabel.pack(side=LEFT)
        self.createMealButton=tkinter.Button(self.entryFrame, text="Create the meal", command= lambda : self.createMeal())
        self.createMealButton.pack(side=RIGHT)
        self.appendOfficialDoc=tkinter.Button(self.entryFrame, text="Attach the official document", command= lambda : self.createMeal())
        self.appendOfficialDoc.pack(side=RIGHT)
        self.nameEntry = tkinter.Entry(self.entryFrame)
        self.nameEntry.pack(side=RIGHT)
        self.entryFrame.pack(side=TOP)
        self.entryFrame.pack(side=TOP)
        self.tutorial = scrolledtext.ScrolledText(self.leftFrame, width=70,height=60)
        self.tutorial.pack(side=BOTTOM)
        self.leftFrame.pack(side=LEFT)


        self.rightFrame = tkinter.Frame(self.app)
        self.ingredientsList = tkinter.Listbox(self.rightFrame, width=50, height=60)
        self.addNewIng = tkinter.Button(self.rightFrame, text="Add new ingredient", command= lambda : self.addIngredient())
        self.addNewIng.pack(side=TOP)
        self.ingredientsList.pack(side=TOP)
        self.rightFrame.pack(side=RIGHT)
    def createMeal(self):
        meal = {}
        meal["instruction"] = self.tutorial.get("1.0","end")
        meal["ingredients"] = self.ingredients
        print(meal)
    def addIngredient(self):
        dialog = NewIngredientForm(self.app)
        ingredient = dialog.ingredient
        self.ingredients.append(ingredient)
        self.ingredientsList.insert("end",f"{ingredient['name']} : {ingredient['amount']}")
class NewIngredientForm(tkinter.simpledialog.Dialog):
    def __init__(self, parent):
        self.ingredient = {}
        super().__init__(parent)

    def body(self, frame):
        # print(type(frame)) # tkinter.Frame
        self.nameFrame = tkinter.Frame(frame)
        self.ingredientNameLabel = tkinter.Label(self.nameFrame, text="Ingredient name")
        self.ingredientEntry = tkinter.Entry(self.nameFrame)
        self.ingredientAmountLabel = tkinter.Label(self.nameFrame, text="Amount")
        self.ingredientAmountEntry = tkinter.Entry(self.nameFrame)
        self.ingredientNameLabel.grid(row=1,column=1)
        self.ingredientEntry.grid(row=1,column=2)
        self.ingredientAmountLabel.grid(row=1,column=3)
        self.ingredientAmountEntry.grid(row=1,column=4)

        self.nameFrame.pack()
        return frame

    def ok_pressed(self):
        # TODO: allow the user to leave out data
        self.ingredient["name"] = self.ingredientEntry.get()
        self.ingredient["amount"] = self.ingredientAmountEntry.get()

        self.destroy()

    def cancel_pressed(self):
        # print("cancel")
        self.destroy()


    def buttonbox(self):
        self.ok_button = tkinter.Button(self, text='OK', width=5, command=self.ok_pressed)
        self.ok_button.pack(side="left")
        cancel_button = tkinter.Button(self, text='Cancel', width=5, command=self.cancel_pressed)
        cancel_button.pack(side="right")
        self.bind("<Return>", lambda event: self.ok_pressed())
        self.bind("<Escape>", lambda event: self.cancel_pressed())

def run():
    app = NewMealUI()
    # app.addNewOrder("Pljeska", 2)
    #app.newTicket(2, [{"name": "Omlet", "ammount": 1},{"name": "Brusketo", "ammount": 2},{"name": "Sendvic", "ammount": 4}])
    app.app.mainloop()
if __name__ == "__main__":
    run()