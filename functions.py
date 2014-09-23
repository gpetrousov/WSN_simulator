import global_vars
import classes
from time import ctime

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



def check_if_node_is_beyond_grid_and_take_a_step():
    """Checks if the node is about to leave the grid of motes.
    If the node is still in the grid, takes a step.
    If node is on the edge of the grid, return True to indicate it.
    OUTPUT: 
        True == the node is about to step out of the grid
        False == the node is still in the grid
    """
    #update node position
    if global_vars.NODES_ARRAY[0].heading == 'E':
        if global_vars.NODES_ARRAY[0].current_col < (len(global_vars.MOTES_ARRAY[0]) - 1):
            #if you are still in the grid of the motes
            global_vars.NODES_ARRAY[0].current_col += 1
        else:
            #you are out of the grid
            return True

    elif global_vars.NODES_ARRAY[0].heading == 'W':
        if global_vars.NODES_ARRAY[0].current_col > 0:
            global_vars.NODES_ARRAY[0].current_col -= 1
        else:
            #you are out of the grid
            return True

    elif global_vars.NODES_ARRAY[0].heading == 'N':
        if global_vars.NODES_ARRAY[0].current_row > 0:
            global_vars.NODES_ARRAY[0].current_row -= 1
        else:
            #you are out of the grid
            return True

    elif global_vars.NODES_ARRAY[0].heading == 'S':
        if global_vars.NODES_ARRAY[0].current_row < (len(global_vars.MOTES_ARRAY) - 1):
            global_vars.NODES_ARRAY[0].current_row += 1
        else:
            #you are out of the grid
            return True
    return False #the node is still in the grid after the step



def write_simulation_results_to_file():
    print '#############  SIMULATION COMPLETED  ###############'
    print '####################################################'
    print '#############   SIMULATION RESULTS   ###############'
    print '####################################################'

    #create the results file
    results_file = open(global_vars.RESULTS_FILE_NAME, 'a')
    results_file.write('Wireless sensors network simulator\n') #program
    results_file.write('author: Ioannis Petrousov\nemail: petrousov@gmail.com\n\n') #affiliation
    results_file.write(ctime()) #type the date
    results_file.write('\n####################################################\n')
    results_file.write('\t   #############   SIMULATION RESULTS   ###############\n')
    results_file.write('####################################################\n')
    results_file.write('\nSimulation time: %d seconds\n\n'%global_vars.SIM_TIME)

    ###### write the number of packets sent by motes ######
    results_file.write('DATA PACKETS SENT BY MOTES\n\t')
    for q in xrange(len(global_vars.MOTES_ARRAY[0])):
        results_file.write('%d\t'%q) #type the columns
    results_file.write('\n')
    row_number = 0
    for _r_ in global_vars.MOTES_ARRAY:  #for each row
        if row_number > 0:
            results_file.write('\n')
        results_file.write('%d\t'%row_number) #type the row number
        row_number += 1
        for e in _r_: #for each element of row
            results_file.write('%d\t'%e.packets_sent) #type the data

    results_file.write('\n')

    ###### write the number of packets received by motes ######
    results_file.write('\n\nDATA PACKETS RECEIVED BY MOTES\n\t')
    for q in xrange(len(global_vars.MOTES_ARRAY[0])):
        results_file.write('%d\t'%q) #type the columns
    results_file.write('\n')
    row_number = 0
    for _r_ in global_vars.MOTES_ARRAY:  #for each row
        if row_number > 0:
            results_file.write('\n')
        results_file.write('%d\t'%row_number) #type the row number
        row_number += 1
        for e in _r_: #for each element of row
            results_file.write('%d\t'%e.packets_received) #type the data

    results_file.write('\n')
    
    ###### write node log #####
    results_file.write('\n\nEnters\tTime\t\t\t\tHeading\tRC\n')
    for _l_ in global_vars.NODES_ARRAY[0].log: #each line of log
        for log_data in _l_:
            results_file.write('%s\t'%log_data)
        if len(global_vars.NODES_ARRAY[0].log[-1]) != 4:
            results_file.write('\t%s\n'%global_vars.NODES_ARRAY[0].packets_received)
        else:
            results_file.write('\n')

    results_file.write('\n')

    ###### write total packets sent/forwarded
    total_packets_sent = 0
    results_file.write('\nTotal packets sent/forwarded ')
    for _i_ in global_vars.MOTES_ARRAY:
        for e in _i_:
            total_packets_sent += e.packets_sent
    results_file.write('%s'%total_packets_sent)


    results_file.close()
    return
