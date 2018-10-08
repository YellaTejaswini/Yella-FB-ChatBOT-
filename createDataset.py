#Updated from and content and removed received and send and just assigned combined =df and in step 70 changed combinedDictionary.iteritems() to items()


import pandas as pd
import numpy as np
import os
import re
from datetime import datetime

personName = input('Enter your full name: ')
whatsAppData = input('Do you have whatsAppData to parse through (y/n)?')

def getWhatsAppData():
        df = pd.read_csv('_chat.txt_structured.csv')
        print(1)
        responseDictionary = dict()
        print(2)
        
        #print(df[df['From']])
        #receivedMessages = df[df['From'] != personName]
        print(3)
        
        #print(receivedMessages)
        #sentMessages = df[df['From'] == personName]
        #combined = pd.concat([sentMessages, receivedMessages])
        combined=df
        otherPersonsMessage, myMessage = "",""
        firstMessage = True
        for index, row in combined.iterrows():
            if (row['From'] != personName):
                if myMessage and otherPersonsMessage:
                    otherPersonsMessage = cleanMessage(otherPersonsMessage)
                    myMessage = cleanMessage(myMessage)
                    responseDictionary[otherPersonsMessage.rstrip()] = myMessage.rstrip()
                    otherPersonsMessage, myMessage = "",""
                otherPersonsMessage = otherPersonsMessage + str(row['message']) + " "
            else:
                if (firstMessage):
                    firstMessage = False
                    # Don't include if I am the person initiating the convo
                    continue
                myMessage = myMessage + str(row['message']) + " "
        print(responseDictionary)
        return responseDictionary



def cleanMessage(message):
	# Remove new lines within message
	cleanedMessage = message.replace('\n',' ').lower()
	# Deal with some weird tokens
	cleanedMessage = cleanedMessage.replace("\xc2\xa0", "")
	# Remove punctuation
	cleanedMessage = re.sub('([.,!?])','', cleanedMessage)
	# Remove multiple spaces in message
	cleanedMessage = re.sub(' +',' ', cleanedMessage)
	return cleanedMessage

combinedDictionary = {}

if (whatsAppData == 'y'):
        print ('Getting whatsApp Data')
        combinedDictionary.update(getWhatsAppData())
print ('Total len of dictionary', len(combinedDictionary))

print ('Saving conversation data dictionary')
np.save('conversationDictionary.npy', combinedDictionary)

conversationFile = open('conversationData.txt', 'w')
for key,value in combinedDictionary.items():


		
   	conversationFile.write(key.strip() + value.strip())