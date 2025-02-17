#Name: Chingizkhan Nurbolatov Yankolov
#Date: 5th February 2025
#Description: Raspberry Pi Activity 3 -> Calculator GUI

#Import libraries
from tkinter import *
from button_data import button_data

#Constants
WIDTH = 400
HEIGHT = 650

#The GUI
class MainGUI(Frame):

    def __init__(self, parent):
        super().__init__(parent, bg = "white")
        self.setupGUI()
        self.clear = False #Check if we have to clear the display after a new number is put

    def setupGUI(self):
        
        #The top display
        self.display = Label(
            self,
            text = "",
            anchor = E,
            bg = "white",
            fg = "black",
            height = 1,
            font = ("Arial", 50)
            )
        self.display.grid(row = 0, column = 0, columnspan = 4, sticky = NSEW)

        #Configure the grid
        for row in range(6):
            Grid.rowconfigure(self, row, weight = 1)
        for col in range(4):
            Grid.columnconfigure(self, col, weight = 1)

        for button in button_data:
            self.make_button(
                button["row"],  #Option: button.get("row")
                button["col"],
                button["value"],
                button.get("columnspan", 1) #Set the columnspan value, to use it on the "=" button. Set the default to 1 (rest of buttons)
                )

        self.pack(fill = BOTH, expand = 1)
        
    def make_button(self, row, col, value, columnspan = 1): #Add columnspan
        bg_color = "#dddddd"
        if value == "=":
            bg_color = "blue"

        if value in ['(', ')', 'AC', '+', '-', '*', '/']:
            bg_color = "#999999"
        
        button = Button(
            self,
            text = value,
            font = ("Arial", 30),
            fg = "black",
            bg = bg_color,
            borderwidth = 0,
            highlightthickness = 0,
            width = 5,
            activebackground = "white",
            command = lambda: self.process(value)
        )

        #Adjust and add the columnspan value
        button.grid(row = row, column = col, columnspan = columnspan, sticky = NSEW)

    def process(self, button):
        """
        parameter 'button' represents the value on the button
        example: '=' to evaluate, '+' for addition
        """
        if self.clear == True and button not in ["=", "AC", "←"]:
            #This will clear the display in case of a result or error.
            self.display["text"] = ""
            self.clear = False #By default I set it to false, so it does not clear the display.
            #However, whenever I get a result/Error it will be set to true, so the dispay can be cleared.
        
        if button == "AC":
            #Clear the display
            self.display["text"] = ""
        elif button == "←":
            #Clear the right character in the display
            self.display["text"] = self.display["text"][:-1]
        elif len(self.display["text"]) >= 14 and button not in ["=", "AC", "←"]:
            #Here, we limit the display to 14 characters
            pass
        elif button == "=":
            #Evaluate the expression
            expr = self.display["text"]
            try:
                result = str(eval(expr))
                if len(result) > 14:
                    #Check the amount of number in the result
                    self.display["text"] = result[:11] + "..."
                else:
                    self.display["text"] = result
                self.clear = True #Set it to true, so the display get cleared
            except:
                self.display["text"] = "ERROR"
                self.clear = True #Set it to true also, so the display get cleared
        else:
            #Append the button value to the display
            self.display["text"] += button

#Main
window = Tk()
window.title("The Reckoner")
window.geometry(f"{WIDTH}x{HEIGHT}")

p = MainGUI(window)
window.mainloop()