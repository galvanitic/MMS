#  Author:    Rodolfo J. Galván Martinez
#  Created:   07.08.2020
#  License:   MIT
#  (c) Copyright by Rodolfo J. Galván Martinez.
#  Using Python^3.7.7 64-bit compiler & pip3

# Just importing some secret sauce here
from galvanite import auth
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from openpyxl import load_workbook
# Identifying ourselves
client = Client(auth["account_sid"], auth["auth_token"])

# Our message class :)
class Message:
  def __init__(self, firstName, recipientNum):
    self.senderNum = auth["pelotonU_phone"]
    self.message = "Hi, {firstName}! Janet with PelotonU. I hope you are well! I wanted to let you know we are continuing to enroll student into our college programs. If now is a good time for you to continue with the enrollment process I would love to chat with you about next steps! Looking forward to talking with you soon!"
    self.firstName = firstName
    self.recipientNum = recipientNum
  
  def sendText(self):
    try:
      message = client.messages \
          .create(
              body=self.message.format(firstName=self.firstName),
              from_= self.senderNum,
              to=self.recipientNum,
          )
      print('Message sent to {rcpnt} successfully! => {id}'.format(rcpnt = self.firstName, id=message.sid))
    except TwilioRestException as e:
      print('Something is wrong with {rcpnt}\'s number, {nmbr}. Skipping it!'.format(rcpnt=self.firstName, nmbr=self.recipientNum))
      print('Error: {err}'.format(err=e))

      
def main():
  #Let's load up our excel doc & grab the correct sheet
  doc = load_workbook("contacts.xlsx")
  sheet = doc["Initial Call"]

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