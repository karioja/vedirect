`
karioja@karioja-virtual-machine:~/projects/vedirect$ sudo python vedirect.py 
{'LOAD': 'ON', 'H19': '0', 'VPV': '0', 'ERR': '0', 'FW': '112', 'I': '0', 'H21': '0', 'PID': '0xA042', 'H20': '0', 'H23': '0', 'H22': '0', 'SER#': 'HQ1411?????', 'V': '12740', 'CS': '0', 'PPV': '0'}

{'LOAD': 'ON', 'H19': '0', 'VPV': '0', 'ERR': '0', 'FW': '112', 'I': '0', 'H21': '0', 'PID': '0xA042', 'H20': '0', 'H23': '0', 'H22': '0', 'SER#': 'HQ1411?????', 'V': '12740', 'CS': '0', 'PPV': '0'}

{'LOAD': 'ON', 'H19': '0', 'VPV': '0', 'ERR': '0', 'FW': '112', 'I': '0', 'H21': '0', 'PID': '0xA042', 'H20': '0', 'H23': '0', 'H22': '0', 'SER#': 'HQ1411?????', 'V': '12740', 'CS': '0', 'PPV': '0'}

^CTraceback (most recent call last):
  File "vedirect.py", line 76, in <module>
    ve.read_data()
  File "vedirect.py", line 67, in read_data
    byte = self.ser.read(1)
  File "/usr/lib/python2.7/dist-packages/serial/serialposix.py", line 446, in read
    ready,_,_ = select.select([self.fd],[],[], self._timeout)
KeyboardInterrupt
`