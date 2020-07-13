# MMS
  Author:    Rodolfo J. Galván Martinez  
  Created:   07.08.2020  
  License:   MIT  
  (c) Copyright by Rodolfo J. Galván Martinez  
  Using Python^3.7.7 64-bit compiler & pip3
  
This project is intended to be used for PelotonU in order to send out a mass text message campaign to previously interested students.

> Using Twillio  
> Using openpyxl
---
Example Excel sheet layout:
| fname    | lname     | phone      | last_text | textable? |
|----------|-----------|------------|-----------|-----------|
| Santiago | Fernández | 8268028048 |           | TRUE      |
| Alma     | Cortés    | 4848085496 |           | TRUE      |
| Laura    | Polanco   | 3196928249 |           | FALSE     |

_Please note: all names & phone numbers listed above were randomly generated to serve as an example. Also, the only columns that the script reads at the moment are the columns lables "fname" and "phone"; all other columns are still required to be there even if they have empty values._
