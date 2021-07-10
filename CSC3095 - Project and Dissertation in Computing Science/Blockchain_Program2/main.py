#Main file - e.g ( File Sender )
import os

print('Deploying the smart contract on the Blockchain (BC).....')

import contractAddressGenerator

# This python file is the sender. The code inside this file is used for sending the file to companyA and adding the hash of the excel file on the Blockchain

import toSendFile   


while True:
    d1a = input ("Select: \n1) Send Excel File to company B. \n2) Retreive hash of Excel File from Blockchain \n3) Show All Filenames stored on Blockchain \n4) Exit \n Your option: ")
    '''
   
    # check if d1a is equal to one of the strings, specified in the list
    if d1a in ['1', '2', '3','4']:
        # if it was equal - break from the while loop
        break
    '''


    # process the input
    if d1a == "1": 
        fileName = input('Enter the fileName:  ')
        toSendFile.send_excelFileToCompanyB(fileName)


    elif d1a == "2": 
        fileName = input('Enter the fileName to get its hash from the Blockchain BC:  ')
        result = toSendFile.retrieveFileHashFromBC(fileName)
        print (f"Hash of the file is {fileName} = ", result)

    elif d1a == "3":
        file_names = toSendFile.showBCFileNames()
        print('Name of all files on Blockchain BC: ',file_names)

    elif d1a == "4":
        print('Exiting...')
        break
