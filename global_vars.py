from classes import Channel
#### Global variables ####

MOTES_ARRAY = [] #contains all the mote objects

CCA_TIME = 0.0000128 # cca takes 0.128ms

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

SIM_TIME = 100000 #user input, maximum simulation time

CHANNEL_ARRAY = []#contains all the available channels, max 16 for 802.15.4

NODES_ARRAY = []#contains all the nodes that will enter the motes area

HEADER_SIZE = 8 #bytes. Header size for 10 bits addressing.

NODE_SPEED = 1 #meters per second

#current cloud A gateway
GATEWAY_ROW = -1
GATEWAY_COL = -1
