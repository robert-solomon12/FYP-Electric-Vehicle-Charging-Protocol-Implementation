# from Socket import *
import socket
import time

LOCALHOST = '127.0.0.1'  # The server's hostname or IP address
LOCALPORT = 8080       # The port used by the server
GLOBALHOST = 'fe80::292f:2eda:aa83:cf63'  # The server's hostname or IP address
GLOBALPORT1 = 15118 
GLOBALPORT2 = 15443

        # s.connect((HOST, PORT,0,3)) parameters to be used ...
        
        
        #print('initialized Session ID in superclass')

#class SupportedAppProtocolReq():
    
    #def __init__():
      #  self.protocolNamespace = protocolNamespace
      #  self.versionNumberMajor = versionNumberMajor
      #  self.versionNumberMinor = versionNumberMinor
      #  self.priority = priority
        
        # tcp connections here ...
            
#print('Supported App Protocol Handshake Details: ')


# Superclass

# Subclass SessionSetupReq

# class SECCDiscovery():
#     
#     msg = [0x01,0xFE,0x90,0x00,0x00,0x00,0x00,0x02,0x10,00]
#     
#     buffer = bytes(msg)
#     time.sleep(2)
# 
#     print ("Target IPv6 Address:", GLOBALHOST)
#     print ("Target UDP Port:", GLOBALPORT1)
# 
#     sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) # UDP
#     time.sleep(1)
# 
#     print('V2G Message Details: ')
# 
#     time.sleep(1)
#     
#     print ("1. Sending SECC Discovery Req. Message: ", msg)
#     sock.sendto(buffer, (GLOBALHOST, GLOBALPORT1,0,0));
# 
#   #  time.sleep(2)
# 
#     while True:
#         
#         data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#         print ("received message from CANoe EVSE: ", data)



class V2GMessage:
    
    def __init__(self,headerSessionId):
                
        self.headerSessionId = headerSessionId
        
class SessionSetupReq(V2GMessage):
    
    def __init__(self,headerSessionId,evccid):
        super().__init__(headerSessionId)
        self.evccid = evccid
        
print('V2G Message Details: ')

msg1 = SessionSetupReq([0x01,0x00,0x00, 0x00,0x00,0x00,0x00,0x00,0x00],[0x02,0x00,0x00,0x00,0x00,0x01])

#msg1 = SessionSetupReq('100000000','020001')    


time.sleep(2)

buffer1 = msg1.headerSessionId + msg1.evccid

time.sleep(2)
b = bytes(buffer1)
print('Header SessionId: ',msg1.headerSessionId,'EVCCID: ',msg1.evccid)
print('bytes: ',b)
#print('hex format: ' b.hex())
print('Length of bytestring: ',len(b))
print('Type of bytestring: ',type(b))
time.sleep(1)

#print(int(0x8E))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('.........')
    time.sleep(1)
    print('.........')
    time.sleep(1)
    print('.........')
    time.sleep(1)
    s.connect((LOCALHOST, LOCALPORT))
    print('Connected to V2G Server!')
    time.sleep(1)
    print('Sending Session Setup Message to OpenV2G!')
    time.sleep(1)
    s.sendall(b) 
    time.sleep(2)
    
    data1 = s.recv(1024)
    
    print('Received from OpenV2G Server: ', repr(data1))
    print('Length of data rec.: ',len(data1))
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) # TCP
    sock.connect((GLOBALHOST, GLOBALPORT2, 0, 3))
    print("Connected to CANoe");
    time.sleep(2)
    print("Sending Session Setup Message to CANoe..");
    
    bufferSessSetup = bytes(data1)
    sock.sendall(bufferSessSetup)
    
    print ("-----")
    print ("-----")
    print ("-----")
    
    while True:
        data, addr = sock.recvfrom(2048) # buffer size is 1024 bytes
        
        print ("received message from CANoe EVSE: ", data)
    
    #time.sleep(2)
    #s.close()