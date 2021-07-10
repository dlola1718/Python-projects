from web3 import Web3

from flask import Flask, jsonify, request
from flask.helpers import total_seconds

import requests

import pandas as pd
import hashlib



#Smart Contract related code
# Connect to local Ganche and check if it is connected. 
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
print(w3.isConnected())

# The following abi and bytecode are received after the compiling the smart contract. You can it using "CompileSolInPython.py" file
abi = [
	{
		"constant": 'true',
		"inputs": [
			{
				"name": "fileName",
				"type": "string"
			}
		],
		"name": "retrieve",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": 'false',
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": 'false',
		"inputs": [
			{
				"name": "fileName",
				"type": "string"
			},
			{
				"name": "hashOfFile",
				"type": "string"
			}
		],
		"name": "storeHash",
		"outputs": [],
		"payable": 'false',
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": 'true',
		"inputs": [],
		"name": "showAllFileNames",
		"outputs": [
			{
				"name": "",
				"type": "string[]"
			}
		],
		"payable": 'false',
		"stateMutability": "view",
		"type": "function"
	}
]


# Both of the parties sharing data should have the same smart contract address, so that they view the same on-chain data.  
# Reading the contract address from text file. It is saved in text file so that every file gets the same contract address.
f = open("contractAddress.txt", "r")
contract_address = f.read()

# Use the deployed_contract to access functions of the smart contract
deployed_contract = w3.eth.contract(address=contract_address, abi=abi)



def hash_the_excel(excelFilePath):
    excelFileName = str(excelFilePath)
    #This will read all of the sheets of the excel file
    df = pd.concat(pd.read_excel(excelFileName, sheet_name=None), ignore_index=True)
    df = str(df)

    excelFileHash = hashlib.sha256(df.encode()).hexdigest()

    return(excelFileHash)


#To Upload the hash of the file to BC
def uploadFileHashToBC(fileName):
    deployed_contract.functions.storeHash(fileName,hash_the_excel(fileName)).transact({'from':w3.eth.accounts[0]})


# To check all files stored on the chain
def showBCFileNames():
    result = deployed_contract.functions.showAllFileNames().call()
    return result

def retrieveFileHashFromBC(fileName):
    result = deployed_contract.functions.retrieve(fileName).call()
    return result


def send_excelFileToCompanyB(fileName):
    uploadFileHashToBC(fileName) # Upload the file hash to BC first
    url = "http://127.0.0.1:5000/sendFile"  # URL of the company
    files = {'file': open(f'{fileName}', 'rb')}
    r = requests.post(url, files=files) # send the file to the other company
    r.text
    print(r.text)
