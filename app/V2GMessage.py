# from Socket import *
import socket, pickle
import time

LOCALHOST = '127.0.0.1'  # The server's hostname or IP address
LOCALPORT = 8080        # The port used by the server
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

#msg1 = SessionSetupReq('0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0','0x2, 0x0, 0x0, 0x0, 0x0, 0x1')

msg1 = SessionSetupReq('100000000','020001')    


time.sleep(2)

buffer1 = msg1.headerSessionId + msg1.evccid

time.sleep(2)
b = bytes(buffer1.encode('utf-8'))
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
    print('Sending Session Setup V2G Message!')
    time.sleep(2)
    s.sendall(b) #uffer.encode('utf-8'))
    #print('hex version: ',b)
    time.sleep(1)


    print('Sent Session Setup V2G Message!')
    data = s.recv(1024)
    
    print('Received from OpenV2G Server: ', repr(data))


# Then send the data above to the CANoe to get response...



#class SessionSetupRsp(V2GMessage):
#    def __init__(self,sessionId):
#        super().__init__(sessionId)
#        self.evccid = evccid
# tcp connections here ...



#class ServiceDiscoveryReq(V2GMessage):
    
#    def __init__(self,sessionId,evccid):
#        super().__init__(sessionId)
#        self.serviceScope = serviceScope
#        self.serviceCategory = serviceCategory

#print('V2G Message Details: ')
#msg1 = ServiceDiscoveryReq([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],20)


# tcp connections here ...


#class ServiceDetailReq(V2GMessage):
    
#    def __init__(self,sessionId,evccid):
#        super().__init__(sessionId)
#        self.serviceID = serviceID

#print('V2G Message Details: ')
#msg = ServiceDetailReq([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],20)





# class SessionSetupResp(V2GMessage):

#      def __init__(self,sessionId,responseCode,evseid,eVseTimestamp):

#         super().__init__(sessionId)

#         self.responseCode = responseCode
#         self.evseid = evseid
#         self.eVseTimestamp = eVseTimestamp

# msg1res = SessionSetupReq(data)




# send parameters over to Canoe


    # buffer(sessid,evid)

