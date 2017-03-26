import sys
import RPi.GPIO as GPIO
from ST_VL6180X import VL6180X
from time import sleep
GPIO.setmode(GPIO.BCM)


"""-- Setup --"""
debug = False
if len(sys.argv) > 1:
    if sys.argv[1] == "debug":  # sys.argv[0] is the filename
        debug = True

# setup ToF ranging/ALS sensor
tof_address = 0x29
#init lib with address and turn on debug
tof_sensor = VL6180X(address=tof_address, debug=debug)


class SensorArray:
    def __init__ (self):
        self.get_sensors()
        self.get_sensor_address()
        
        #set gpio pin addresses
        self.s0 = 4
        self.s1 = 5
        self.s2 = 6
        self.s3 = 7
        
        # build a tuple that represents the byte address on the HP4067 multiplexer
        self.ch0 =(0,0,0,0)
        self.ch1 =(1,0,0,0)
        self.ch2 =(0,1,0,0)
        self.ch3 =(1,1,0,0)
        self.ch4 =(0,0,1,0)
        self.ch5 =(1,0,1,0)
        self.ch6 =(0,1,1,0)
        self.ch7 =(1,1,1,0)
        self.ch8 =(0,0,0,1)
        self.ch9 =(1,0,0,1)
        self.ch10 =(0,1,0,1)
        self.ch11 =(1,1,0,1)
        self.ch12 =(0,0,1,1)
        self.ch13 =(1,0,1,1)
        self.ch14 =(0,1,1,1)
        self.ch15 =(1,1,1,1)
        
        # build a tuple of tuples of binary address
        self.muxChannel = (self.ch0,self.ch1,self.ch2,self.ch3,self.ch4,self.ch5,self.ch6,self.ch7,self.ch8,self.ch9,self.ch10,self.ch11,self.ch12,self.ch13,self.ch14,self.ch15)
        
        #build a tuple of the GPIO Board pin Addresses
        self.controlPin = (self.s0,self.s1,self.s2,self.s3)
        
        #  set initial values to 1
        self.setpins = (GPIO.output(self.s0,1),GPIO.output(self.s1,1),GPIO.output(self.s2,1),GPIO.output(self.s3,1))
        
        # 
        self.pinstate = (GPIO.input(self.s0),GPIO.input(self.s1),GPIO.input(self.s2),GPIO.input(self.s3))
        
        # print("set pins to 1",pinstate)
    def get_sensors(self):
        print ("got sensor data")
    def get_sensor_address(self):
        print ("set sensor address")
    def read_mux(self, channel):
        
        GPIO.setup(channel,GPIO.OUT)
        print(muxChannel[channel])
        
    def write_mux_location(self, readChannel):
        muxValue = muxChannel[readChannel]
        
        print("muxValue",muxValue)
        for m in range(4):
            GPIO.output(controlPin[m],muxValue[m])
            print("controlpin {}, muxChannel {}".format(controlPin[m], muxValue[m]))
    def read_signal(self, sdaChannel):
        GPIO.input()
    
    
    
    
def main():
        sensor = SensorArray()
        sensor.get_sensors()
        #sensor.read_mux(15)
        sensor.write_mux_location(1)
        print ("Measured distance is : {} mm".format(tof_sensor.get_distance()))
        #print ("Measured light level is : {} lux".format(tof_sensor.get_ambient_light(20))
        

        
if __name__ == "__main__": main()  

              