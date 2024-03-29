import socket
import time
from V2GMessage import *
LOCALHOST = '127.0.0.1'  # The server's hostname or IP address
LOCALPORT = 8080       # The port used by the server
GLOBALHOST = 'fe80::292f:2eda:aa83:cf63'  # The server's hostname or IP address
GLOBALPORT1 = 15118 
GLOBALPORT2 = 51111

#class ChargingSession:
    
    
def startSequence():
    time.sleep(2)
    print("Charging Sequence started ...")
    
    MSG1 = [0x01,0xFE,0x90,0x00,0x00,0x00,0x00,0x02,0x10,00]
    
    buffer = bytes(MSG1)
    
    print ("Target IPv6 Address:", GLOBALHOST)

    print ("Target UDP Port:", GLOBALPORT1)

    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) # UDP

    print ("1. Sending SECC Discovery Req. Message: ", MSG1)
    sock.sendto(buffer, (GLOBALHOST, GLOBALPORT1,0,0));
    time.sleep(1)
    data = sock.recv(2048)
    print('Received from CANoe Server: ', repr(data))
    print("----")
    time.sleep(1)
    print ("-----")
    time.sleep(1)
    
    
    
    print('Session Setup V2G Message Details: ')
  
    buffer1 = msgReq1.headerSessionId + msgReq1.evccid
    time.sleep(2)
    b1 = bytes(buffer1)
    print('Header SessionId: ',msgReq1.headerSessionId,'EVCCID: ',msgReq1.evccid)
    print('Length of bytestring: ',len(b1))
    time.sleep(1)
    


    print('Service Discovery V2G Message Details: ')
    buffer2 = msgReq2.headerSessionId + msgReq2.serviceScope + msgReq2.serviceCategory
    
    time.sleep(2)
    b2 = bytes(buffer2)
    print('Header SessionId: ',msgReq2.headerSessionId,'Service Scope: ',msgReq2.serviceScope, 'Service Category: ',msgReq2.serviceCategory)
    print('Length of bytestring: ',len(b2))
    time.sleep(1)
    
    
    
    print('Service Discovery V2G Message Details: ')
    buffer3 = msgReq3.headerSessionId + msgReq3.serviceId + msgReq3.selectedPaymentOption
    time.sleep(2)
    
    b3 = bytes(buffer3)
    print('Header SessionId: ',msgReq3.headerSessionId, 'Service Scope: ',msgReq3.serviceId, 'Selected Payment Option: ',msgReq3.selectedPaymentOption)
    print('Length of bytestring: ',len(b3))
    time.sleep(1)


    # connect to CANoe for sending UDP Req. Message
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('.........')
    time.sleep(1)

    # connect to OpenV2G Server
    tcpsock.connect((LOCALHOST, LOCALPORT))
    
    time.sleep(1)
    print('Sending Session Setup Request Message to OpenV2G!')
    time.sleep(1)
    tcpsock.sendall(b1) 
    time.sleep(2)
    
    
    data1 = tcpsock.recv(2048)
    print('Received from OpenV2G Server: ', repr(data1))
    
    
    
    # Sending Service Discovery Message to Local Server
    time.sleep(1)
    print('Sending Service Discovery Request Message to OpenV2G!')
    time.sleep(1)
    tcpsock.sendall(b2) 
    time.sleep(2)
    
    data2 = tcpsock.recv(2048)
    print('Received from OpenV2G Server: ', repr(data2))
    
    
    
    # Sending Payment Selection Request Message to Local Server
    time.sleep(1)
    print('Sending Payment Selection Request Message to OpenV2G!')
    time.sleep(1)
