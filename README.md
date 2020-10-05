This is a Python library for decoding the Victron Energy VE.Direct text protocol used in their range of MPPT solar charge controllers and battery monitors.

The test directory contains a set of live recordings of the serial port data sent by the 3 devices that I own.

* SmartSolar MPPT 100/20 running firmware version 1.39
* BlueSolar MPPT 75/15 running firmware version 1.23
* BVM 702 battery monitor running firmware version 3.08

These recordings can be fed to the Vedirect decoder using a pair of virtual serial ports. To create a pair of virtual serial ports issue the following command:
```
$ socat -d -d PTY,raw,echo=0,link=/tmp/vmodem0 PTY,raw,echo=0,link=/tmp/vmodem1
```
This will create 2 virtual serials ports connected to each other. Anything sent to /tmp/vmodem0 will be echoed to /tmp/vmodem1 and vice versa.

Attach the decoder to /tmp/vmodem1
```
python3 examples/vedirect_print.py --port /tmp/vmodem1
```

Feed the recording over to /tmp/vmodem0
```
$ cat test/bvm702.dump > /tmp/vmodem0
```
There is no 1 second delay between the packets as there is with the real hardware. The above commands will flood the terminal with all of the data at once.

To simulate the behaviour of the Victron devices you can use ``awk``:

```
awk '/PID/{}; {print}; /Checksum/{system("sleep 1") };' test/bluesolar_1.23.dump > /tmp/vmodem0
```
