import socket

addrs = [('fe80::292f:2eda:aa83:cf63%wlan0', 15118),            
         ('fe80::292f:2eda:aa83:cf63%wlan0', 15443)]    
for addr in addrs:
  print('Original addr: {}'.format(addr))
  for res in socket.getaddrinfo(addr[0], addr[1], socket.AF_INET6,
                                socket.SOCK_STREAM, socket.SOL_TCP):
      af, socktype, proto, canonname, sa = res
      print('Full addr:     {}'.format(sa))
  print('')
