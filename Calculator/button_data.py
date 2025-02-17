#The new button_data information for the assignment is this one, which was already in the file, I just changed the name to button_data.
#We just change the name of the library, so it fits the main code on "TheReckoner.py"

button_data = [
    {"row": 1, "col": 0, "value": '('}, 
    {"row": 1, "col": 1, "value": ')'}, 
    {"row": 1, "col": 2, "value": 'AC'}, 
    {"row": 1, "col": 3, "value": '←'}, 

    {"row": 2, "col": 0, "value": '7'}, 
    {"row": 2, "col": 1, "value": '8'}, 
    {"row": 2, "col": 2, "value": '9'}, 
    {"row": 2, "col": 3, "value": '/'}, 

    {"row": 3, "col": 0, "value": '4'}, 
    {"row": 3, "col": 1, "value": '5'}, 
    {"row": 3, "col": 2, "value": '6'}, 
    {"row": 3, "col": 3, "value": '*'}, 

    {"row": 4, "col": 0, "value": '1'}, 
    {"row": 4, "col": 1, "value": '2'}, 
    {"row": 4, "col": 2, "value": '3'}, 
    {"row": 4, "col": 3, "value": '-'}, 

    {"row": 5, "col": 0, "value": '0'}, 
    {"row": 5, "col": 1, "value": '.'}, 
    {"row": 5, "col": 2, "value": ' '}, 
    {"row": 5, "col": 3, "value": '+'}, 
    
    {"row": 6, "col": 0, "columnspan": 2, "value": '=',}, 
    {"row": 6, "col": 2, "value": '**'}, 
    {"row": 6, "col": 3, "value": '%'}, 
    #Added the "%" function on row 6
    #Added the columnspan for the "=" button to spread across multiple columns
]