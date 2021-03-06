import global_vars
import classes
import functions

#### Classes ####

class Node():
    """Class for the node"""
    def __init__(self):
        self.current_row = -1
        self.current_col = -1
        self.heading = ''
        #self.channel = Channel(str(1001))
        self.packets_sent = 0
        self.packets_received = 0
        self.log = []



class Mote():
    """
    Class for the mote sensors
    INPUT: mote identifier, it's row in MOTES_ARRAY, it's column in MOTES_ARRAY
    """
    def __init__(self, moteID, row, column):
        self.moteID = 'mote%s' % moteID
        self.locationR =  int(row) #row in the MOTES_ARRAY
        self.locationC =  int(column) #column in the MOTES_ARRAY
        self.payload = False #no payload to send
        self.echo = True #initially echo must be sent

        #real coordinates of the mote
        #Index location : upper left corner
        self.positionX = (self.locationC +1) * 100
        self.positionY = (self.locationR + 1) * 100

        self.gateway = False
        self.neighbors = [] #lookup table
        self.parent = str() #where the mote forwards it's data
        #self.channel = Channel(moteID)

        self.cca_once = 0                                        ## 
        #0: cca has not been set for this random node entry ##
        #1: cca has been set for this random node entry     ##

        self.packets_sent = 0
        self.packets_received = 0

class Channel():
    """Class for the channels in the network"""
    def __init__(self, channelID):
        self.channelID = 'channel%d' % channelID
        self.occupied = False
        self.release_time = 0


