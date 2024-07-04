# Terminal Guide
**GUI is in development and will be finished soon!**

```
from launcher import *

add_variables([["*1", "*2", "*3"]])
delete_variable("*7")
start_bot([["*4", "*4", "*5", "*6"], ["response_command", "time", "Current date is {date_var()}, {time_var()}", "Say the current date and time"]])
```


### (*1) - Imports

Here you enter the imports that are needed to create the variable

### (*2) - Variable name

Here you write what the variable should be called

### (*3) - Calculations

Here you write how to calculate the variable, e.g.: 1 + 1

### (*4) - Discord command type

The command type is passed here (currently there is only "response_command") Examples are in the 2nd list!

### (*5) - Slash name

Here you write how the command should be called, i.e. "hello" for /hello as a command

### (*6) Returned response

The text that is returned comes in here (with variables, but they are in {}, -> No formated String)

### (*7) - Slash command description

The command description goes here

### (*8) 

The variable name comes in here, the variable that is to be deleted 

**Additional information: Token is read automatically from TOKEN.txt**
