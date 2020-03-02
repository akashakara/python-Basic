import os
ping = os.system('ping www.bcetdgp.ac.in')
if ping==0:
  print('up')
else:
  print('down')