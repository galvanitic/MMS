#  Author:    Rodolfo J. Galván Martinez
#  Created:   07.08.2020
#  License:   MIT
#  (c) Copyright by Rodolfo J. Galván Martinez.
#  Using Python^3.7.7 64-bit compiler & pip3

# Just importing some secret sauce here
from galvanite import auth
from twilio.rest import Client
from openpyxl import load_workbook
# Identifying ourselves
client = Client(auth["account_sid"], auth["auth_token"])

# Our message class :)
class Message:
  def __init__(self, firstName, recipientNum):
    self.senderNum = auth["pelotonU_phone"]
    self.message = "Hey {firstName}, this is just a test from PelotonU. All is well if you get this :)"
    self.firstName = firstName
    self.recipientNum = recipientNum
  
  def sendText(self):
    message = client.messages \
        .create(
            body=self.message.format(firstName=self.firstName),
            from_= self.senderNum,
            to=self.recipientNum,
        )
    print('Message sent to {rcpnt} successfully! => {id}'.format(rcpnt = self.firstName, id=message.sid))

def main():
  #Let's load up our excel doc & grab the correct sheet
  doc = load_workbook("contacts.xlsx")
  sheet = doc["toTextContacts"]

  #Now iterating over all of our contacts in the excel sheet
  headerDelta = 0
  for name in sheet['A']:
    if headerDelta > 0:
      newMessage = Message(name.value, sheet['C{i}'.format(i=headerDelta+1)].value)
      newMessage.sendText()
      headerDelta+=1
    else:
      headerDelta+=1

main()