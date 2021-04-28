# from Socket import *

class SupportedAppReq():
    
    def __init__(self,protocolNamespace,versionNumberMajor,versionNumberMinor,schemaID,priority):
        self.protocolNamespace = protocolNamespace
        self.versionNumberMajor = versionNumberMajor
        self.versionNumberMinor = versionNumberMinor
        self.schemaID = schemaID
        self.priority = priority

msgReq = SupportedAppReq(['urn:iso:15118:2:2013:MsgDef'],[0x02],[0x00],[0x00],[0x02])


class V2GMessage:
    
    def __init__(self,headerSessionId):
        self.headerSessionId = headerSessionId
        
        
class SessionSetupReq(V2GMessage):
    
    def __init__(self,headerSessionId,evccid):
        super().__init__(headerSessionId)
        self.evccid = evccid

msgReq1 = SessionSetupReq([0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],[0x02,0x00,0x00,0x00,0x00,0x01])



class SessionSetupRes(V2GMessage):
    
    def __init__(self,headerSessionId,responseCode,evseId,evseTimestamp):
        super().__init__(headerSessionId)
        self.responseCode = responseCode
        self.evseId = evseId
        self.evseTimestamp = evseTimestamp
          
        
class ServiceDiscoveryReq(V2GMessage):
    
    def __init__(self,headerSessionId,serviceScope,serviceCategory):
        super().__init__(headerSessionId)
        self.serviceScope = serviceScope
        self.serviceCategory = serviceCategory
msgReq2 = ServiceDiscoveryReq([0x02,0x29,0x63,0xB6,0x70,0x00,0xCD,0x4A,0x7B],[0x77,0x77,0x77,0x2e,0x76,0x65,0x63,0x74,0x6f,0x72,0x2e,0x63,0x6f,0x6d],[0x45,0x56,0x43,0x68,0x61,0x72,0x67,0x69,0x6e,0x67])


class ServiceDiscoveryRes(V2GMessage):
    
    def __init__(self,headerSessionId,responseCode,paymentOption):
        super().__init__(headerSessionId)
        self.responseCode = responseCode
        self.paymentOption = paymentOption
       
       
       
class PaymentServiceSelectionReq(V2GMessage):
    
    def __init__(self,headerSessionId,serviceId,selectedPaymentOption):
        super().__init__(headerSessionId)
        self.serviceId = serviceId
        self.selectedPaymentOption = selectedPaymentOption
msgReq3 = PaymentServiceSelectionReq([0x03,0x29,0x63,0xB6,0x70,0x00,0xCD,0x4A,0x7B],[0x01],['Contract'])


class PaymentServiceSelectionRes(V2GMessage):
    
    def __init__(self,headerSessionId,responseCode):
        super().__init__(headerSessionId)
        self.serviceID = serviceID
        self.responseCode = responseCode
        
        
class PaymentDetailsReq(V2GMessage):
    
    def __init__(self,headerSessionId,eMAID,contractSignatureCertChain):
        super().__init__(headerSessionId)
        self.eMAID = eMAID
        self.contractSignatureCertChain = contractSignatureCertChain
#msgReq4 = PaymentServiceSeletionReq([0x04,0x29,0x63,0xB6,0x70,0x00,0xCD,0x4A,0x7B],['DE8AX1A2B3C4D59'],[])



class PaymentDetailsRes(V2GMessage):
    
    def __init__(self,headerSessionId,responseCode):
        super().__init__(headerSessionId)
        self.serviceID = serviceID
        self.responseCode = responseCode
        
        

class ServiceDetailReq(V2GMessage):

    def __init__(self,headerSessionId,serviceId):
        super().__init__(headerSessionId)
        self.serviceId = serviceId
#msgReq5 = ServiceDetailReq([0x02,0x29,0x63,0xB6,0x70,0x00,0xCD,0x4A,0x7B],[],[]) 

        
class ServiceDetailRes(V2GMessage):

    def __init__(self,headerSessionId,serviceScope,serviceCategory):
        super().__init__(headerSessionId)
        self.serviceId = serviceId
        
        

class SessionStopReq(V2GMessage):
    
    def __init__(self,headerSessionId,chargingSession):
        super().__init__(headerSessionId)
        self.chargingSession = chargingSession
msg6 = SessionStopReq([0x05,0x29,0x63,0xB6,0x70,0x00,0xCD,0x4A,0x7B],['Terminate'])


class SessionStopRes(V2GMessage):
    
    def __init__(self,headerSessionId,responseCode):
        super().__init__(headerSessionId)
        self.responseCode = responseCode