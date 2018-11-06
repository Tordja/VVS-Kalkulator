import Ventilasjonskalkulator as VK
from tkinter import *


class Kalkulatorvindu:

    def __init__(self, root):

        self.root = root

        self.entry_value = StringVar(root, value="")

        root.title("Kanalkalkulator")
        root.geometry("700x50")

        self.quitButton = Button(root, text="Quit")
        self.quitButton.bind("<Button-1>", self.quit)
        self.quitButton.pack(side=BOTTOM)

        self.entry_diameter = Entry(root)
        self.entry_diameter.pack(side=LEFT)

        self.entry_flow = Entry(root)
        self.entry_flow.pack(side=LEFT)

        self.calculateButton = Button(root, text="Calculate")
        self.calculateButton.bind("<Button-1>", self.run_calculation)
        self.calculateButton.pack(side=LEFT)

        self.speedEntry = Entry(root)
        self.speedEntry.pack(side=LEFT)

        self.pressureEntry = Entry(root)
        self.pressureEntry.pack(side=LEFT)

        self.turbulenceEntry = Entry(root)
        self.turbulenceEntry.pack(side=LEFT)

    def run_calculation(self, event):
        newduct = VK.RoundDuct(self.entry_flow.get(), self.entry_diameter.get())

        speed = newduct.flowcalc()
        pressure = newduct.pressureCalc()
        turbulence = newduct.returnTurbulent()

        self.speedEntry.delete(0, "end")
        self.speedEntry.insert(0, speed)

        self.pressureEntry.delete(0, "end")
        self.pressureEntry.insert(0, pressure)

        self.turbulenceEntry.delete(0, "end")
        self.turbulenceEntry.insert(0, turbulence)

    def quit(self, event):
        self.root.destroy()





