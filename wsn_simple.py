"""Event driven simulation for a wireless sensor network.
Properties:
    - The area is 10km^2
    - The network consists of 1000 motes-sensors, cloud A
    - The motes a uniformly spread
    - One node (Cloud B) enters the area and croses it at a given speed
    - Once the node enters the area, it starts receiving data from the motes
    - The network reorganizes as the node croses the area
    - Time is measured in seconds
    """

__author__ = "Giannis Petrousov"
__copyright__ = "Copyright 2014"
__credits__ = ["Giannis Petrousov"]
__license__ = "The MIT License"
__maintainer__ = "Giannis Petrousov"
__email__ = "petrousov@gmail"
__status__ = "early alpha"



#### Global variables ####
MOTES_ARRAY = [] #contains all the mote objects

EVENT_LIST = []
#2D array                       [columns]
#           --------------------------...
#           |event name        | | | |...
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



#### Classes ####
class Node():
    """Class for the node"""
    def __init__(self):
        self.locationX = -1
        self.locationY = -1
        self.channel = Channel(str(1001))



class Mote():
    """Class for the mote sensors"""
    def __init__(self, moteID, row, column):
        self.moteID = 'mote%s' % moteID
        self.locationR =  int(row) #row in the MOTES_ARRAY
        self.locationC =  int(column) #column in the MOTES_ARRAY

        #real coordinates of the mote
        #Index location : upper left corner
        self.positionX = (self.locationC +1) * 100
        self.positionY = (self.locationR + 1) * 100

        self.neighbors = [] #lookup table
        self.parent = str() #where the mote forwards it's data
        self.channel = Channel(moteID)



class Channel():
    """Class for the channels in the network"""
    def __init__(self, channelID):
        self.channelID = 'channel%s' % channelID
        self.occupied = False






#### Functions ####
def initialize_motes():
    """Create the mote objects and append them to the MOTES_ARRAY"""
    for i in xrange(10):
        MOTES_ARRAY.append([])
        for j in xrange(100):
            #create motes
            MOTES_ARRAY[i].append(Mote('%s%s'%(i,j), i, j))
            #print 'Created mote %s ' %(MOTES_ARRAY[i].moteID)

def initialize_lookup_tables():




def initialize_event_list():
    """Initialize the EVENT_LIST with the initial values for the events, times and mote-node IDs"""
    #first row
    for event_name in xrange(1000):
        EVENT_LIST.append()
    for event_time in xrange(1000):
        pass
    for mote_id int xrange(1000):
        pass
    


def wsn_main():
    pass








########### INIT ###########
if __name__ == '__main__':
    initialize_motes()
    node = Node()

    #debug statements
    """ 
    for i in xrange(10):
        for j in xrange(100):
            print '%s, location: %d,%d, coordinates: %d,%d' %(MOTES_ARRAY[i][j].moteID, MOTES_ARRAY[i][j].locationR, MOTES_ARRAY[i][j].locationC, MOTES_ARRAY[i][j].positionY, MOTES_ARRAY[i][j].positionX)
            print ' '

    print 'initialized node and channel %s' % node.channel.channelID 
    """
