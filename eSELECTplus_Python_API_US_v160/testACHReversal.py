import time
import USmpgClasses


host = "esplusqa.moneris.com"
store_id = "monusqa002"
api_token = "qatoken"

order_id = "test_python-1410466581.69"
txn_number = "3-0_10"

ach = USmpgClasses.ACHReversal (order_id, txn_number)

req = USmpgClasses.mpgHttpsPost(host, store_id, api_token, ach)
req.postRequest()
resp = req.getResponse()

print ("ReceiptId: " + resp.getReceiptId()) 
print ("ReferenceNum: " + resp.getReferenceNum()) 
print ("ResponseCode: " + resp.getResponseCode()) 
print ("AuthCode: " + resp.getAuthCode()) 
print ("TransTime: " + resp.getTransTime()) 
print ("TransDate: " + resp.getTransDate()) 
print ("TransType: " + resp.getTransType()) 
print ("Complete: " + resp.getComplete()) 
print ("Message: " + resp.getMessage()) 
print ("TransAmount: " + resp.getTransAmount()) 
print ("CardType: " + resp.getCardType()) 
print ("TransID: " + resp.getTransID()) 
print ("TimedOut: " + resp.getTimedOut()) 
print ("BankTotals: " + resp.getBankTotals()) 
print ("Ticket: " + resp.getTicket()) 
print ("AvsResultCode: " + resp.getAvsResultCode())
print ("CvdResultCode: " + resp.getCvdResultCode())
#print ("\n\nStatus Check:")
#req.postStatus()
#resp = req.getResponse()
#print ("Status Code: " + resp.getStatusCode()) 
#print ("Status Message: " + resp.getStatusMessage()) 

