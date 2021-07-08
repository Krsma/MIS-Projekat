import restoran.ui.kitchen.kitchenForm
import restoran.ui.admin.meniForma
import restoran.ui.admin.statsForma
import tkinter
from tkinter import ttk, TOP, BOTTOM, LEFT, RIGHT, BOTH

if __name__ == "__main__":
    #restoran.ui.kitchen.kitchenForm.run()
    app = tkinter.Tk()
    Button1 = tkinter.Button(app, text="Run kitchen form", command = restoran.ui.kitchen.kitchenForm.run)
    Button1.pack(side=LEFT)
    Button2 = tkinter.Button(app, text="Run stats form", command = restoran.ui.admin.statsForma.run)
    Button2.pack(side=LEFT)
    Button3 = tkinter.Button(app, text="Run meni form", command = restoran.ui.admin.meniForma.run)
    Button3.pack(side=LEFT)
    app.mainloop()