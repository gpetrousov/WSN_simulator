#### Global variables ####

MOTES_ARRAY = [] #contains all the mote objects

EVENT_LIST = [[],[],[]]
#2D array                       [columns]
#           --------------------------...
#           |event name - ID   | | | |...
#  [rows]   |time              | | | |...
#           |#moteID or nodeID | | | |...
#           --------------------------...

NUMBER_OF_MOTES = 1000
NUMBER_OF_NODES = 1
BANDWIDTH = 250 * 1024 #bps

#packet sizes#
ACK_PACKET_SIZE = 1 #bytes; confirmation package
DATA_PACKET_SIZE = 4 #bytes
ECHO_PACKET_SIZE = 1 #bytes; "Hello neighbor, add me to your lookup table"

#time intervals#
DATA_INTERVAL_TIME = 60 #seconds, every 60 seconds motes will generate data
PRESENCE_ENTRY_INTERVAL = 6 #seconds, every 6 seconds node will emmit presence entry packet

RN = 0 #is default 0; it is a user-settable parameter for random delay on the XBee 802.15.4

SIM_TIME = 0 #user input, maximum simulation time
