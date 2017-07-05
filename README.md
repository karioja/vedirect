Using the vedirect class.

```
$ python vedirect.py --port /dev/vmodem1 
{'LOAD': 'ON', 'H19': '0', 'VPV': '0', 'ERR': '0', 'FW': '112', 'I': '0', 'H21': '0', 'PID': '0xA042', 'H20': '0', 'H23': '0', 'H22': '0', 'SER#': 'HQ1411?????', 'V': '12740', 'CS': '0', 'PPV': '0'}

{'LOAD': 'ON', 'H19': '0', 'VPV': '0', 'ERR': '0', 'FW': '112', 'I': '0', 'H21': '0', 'PID': '0xA042', 'H20': '0', 'H23': '0', 'H22': '0', 'SER#': 'HQ1411?????', 'V': '12740', 'CS': '0', 'PPV': '0'}

{'LOAD': 'ON', 'H19': '0', 'VPV': '0', 'ERR': '0', 'FW': '112', 'I': '0', 'H21': '0', 'PID': '0xA042', 'H20': '0', 'H23': '0', 'H22': '0', 'SER#': 'HQ1411?????', 'V': '12740', 'CS': '0', 'PPV': '0'}
```

Using the vedirectsim simulator.

Create a pair of virtual serial ports which transfer data between each other.

```
$ socat -d -d PTY,raw,echo=0,link=/tmp/vmodem0 PTY,raw,echo=0,link=/tmp/vmodem1
```

Connect vedirect.py to /tmp/vmodem1 and vedirectsim.py to /tmp/vmodem0 or use a live recording from test/mppt.dump

```
$ cat test/mppt.dump > /dev/vmodem0
```