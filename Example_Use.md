# Terminal Guide
GUI is in development and will be finished soon!

```
from launcher import *

add_variables([["*1", "*2", "*3"]])
delete_variable("*7")
start_bot([["*4", "*4", "*5", "*6"], ["response_command", "time", "Current date is {date_var()}, {time_var()}", "Say the current date and time"]])

```

*1 Here you enter the imports that are needed to create the variable
*2 Here you write what the variable should be called
*3 GHere you write how to calculate the variable, e.g.: 1 + 1

*4 The command type is passed here (currently there is only "response_command") Examples are in the 2nd list!
*5 Here you write how the command should be called, i.e. "hello" for /hello as a command
*5 The text that is returned comes in here (with variables, but they are in {}, -> No formated String)
*6 The command description goes here

*7 The variable name comes in here, the variable that is to be deleted 

Additional information: Token is read automatically from TOKEN.txt
