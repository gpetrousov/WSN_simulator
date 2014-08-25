import global_vars
import classes

#### Functions ####

def initialize_motes():
    """Create the mote objects and append them to MOTES_ARRAY"""
    for i in xrange(10):
        global_vars.MOTES_ARRAY.append([])
        for j in xrange(100):
            #create motes
            global_vars.MOTES_ARRAY[i].append(classes.Mote(';%s;%s'%(i,j), i, j))
            #print 'Created mote %s ' %(MOTES_ARRAY[i].moteID)
    return

def initialize_channels():
    """Create the channel objects"""
    global_vars.CHANNEL_ARRAY.append(classes.Channel(0))
    return


def initialize_nodes():
    """Create the node objects"""
    global_vars.NODES_ARRAY.append(classes.Node())
    return



def check_if_channel_available():
    """Check is a channel is available and returns True of False."""
    pass




def initialize_event_list():
    """Initialize the global_vars.EVENT_LIST with the initial values for the events, times and mote-node IDs"""

    #put event
    global_vars.EVENT_LIST[0] = [0] * 1000

    #put time
    global_vars.EVENT_LIST[1] = [0] * 1000

    #put ID
    for i in xrange(10):
        for j in xrange(100):
            global_vars.EVENT_LIST[2].append(global_vars.MOTES_ARRAY[i][j].moteID)

    #Termination event
    global_vars.EVENT_LIST[0].append(10)
    global_vars.EVENT_LIST[1].append(global_vars.SIM_TIME)
    global_vars.EVENT_LIST[2].append(-1)
    return



def calculate_transmission_delay(packet_size):
    """Calculates the transmission delay by which the channel will be occupied. This function works for 10 bit addressing.
    INPUT: size of the packet to send in bytes
    OUTPUT: transmission time in seconds
    """
    transmission_delay = (global_vars.HEADER_SIZE + packet_size) * (32 / 1000000.0)
    return transmission_delay




def sortrows(lista, row_number):
    """
    Sort all the rows of the given list according to a given row.
    Emulates the functionality of matlabs sortrows() function.
    Input: list, row number, based on which the sorting will be made
    Output: sorted list
    Did not wanted to use numpy.
    """
    lista = zip(*lista) #make list of tupples
    lista.sort(key = lambda x: x[row_number]) #set the row to which you want to sort the list
    lista = zip(*lista) #make a list of lists
    lista[0] = list(lista[0])
    lista[1] = list(lista[1])
    lista[2] = list(lista[2])
    return lista

