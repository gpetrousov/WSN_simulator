import global_vars
import functions
import random

###events###

"""
0 = Take random time
1 = Perform CCA-Clear Channel Assesment
2 = Send echo
3 = Send package
4 = update lookup tables
5 = random node entry
6 = node takes a step
7 = node sends Presence Entry
8 = propagate the new gateway of cloud A
10 = Termination event
"""


######
#    #
#    #
#    #
#    #
######
def assign_random_wait_time():
    """Event 0: perform random delay and after random delay perform CCA.
    0 : (2^BE - 1) * 0.320 ms
    where BE starts at RN and increments each time (up to max value of 5) 
    through the loop until step 3 is cleared
    """
    current_time  = global_vars.EVENT_LIST[1][0]

    global_vars.EVENT_LIST[0].append(1)#CCA event
###############         FUTURE WORK        ###################
########fix the timing function if you want##################     
######add more complexity                 ##################
    global_vars.EVENT_LIST[1].append(current_time + random.random())#random time
#########but for now                                 #############
###########let random() do the work for us            ############
###############have to add BE for each mote in the class ########
    global_vars.EVENT_LIST[2].append(global_vars.EVENT_LIST[2][0])#ID

    return

   ##
  ###
 ####
#####
   ##
   ##
########
def cca():
    """The mote checks if the channel is clear to send data.
    This operation lasts 0.000128 seconds.
    If the channel is clear after 0.000128 seconds, mote will send it's data.
    Otherwise random delay will be performed and the CCA again."""
    current_time  = global_vars.EVENT_LIST[1][0]

    if (current_time + global_vars.CCA_TIME) > global_vars.CHANNEL_ARRAY[0].release_time:
        #channel is released by that time
        #mote takes the channel
        global_vars.EVENT_LIST[1].append(current_time + global_vars.CCA_TIME)
        global_vars.EVENT_LIST[2].append(global_vars.EVENT_LIST[2][0])

        mote_row = int( global_vars.EVENT_LIST[2][0].split(';')[1] )
        mote_col = int( global_vars.EVENT_LIST[2][0].split(';')[2] ) 
        if global_vars.MOTES_ARRAY[ mote_row ][ mote_col ].payload == True:
            #mote has payload ready
            #schedule the send package event
            global_vars.EVENT_LIST[0].append(3)

        elif global_vars.MOTES_ARRAY[ mote_row ][ mote_col ].echo == True:
            #mote has echo ready
            #schedule echo event
            global_vars.EVENT_LIST[0].append(2)

    else:
        #channel will not be free
        #schedule cca again after random time
        global_vars.EVENT_LIST[0].append(0)
        global_vars.EVENT_LIST[1].append(current_time)
        global_vars.EVENT_LIST[2].append(global_vars.EVENT_LIST[2][0])
    return




#######
     ##
     ##
     ##
#######
##
##
##
#######
def echo():
    """Updates the channel release time according to the time it takes to transmit 1 Byte. Schedules the update lookup tables event (4) to update the neighboring motes."""
    current_time  = global_vars.EVENT_LIST[1][0]
    global_vars.CHANNEL_ARRAY[0].release_time = current_time + functions.calculate_transmission_delay(1)

######
####Let's see hwo this goes.
###Event 4 might be useless to pefrorm.
##
    #global_vars.EVENT_LIST[0].append(4)
    #global_vars.EVENT_LIST[1].append(global_vars.CHANNEL_ARRAY[0].release_time)
    #global_vars.EVENT_LIST[2].append(global_vars.EVENT_LIST[2][0])
    return


########
      ##
      ##
      ##
########
      ##
      ##
      ##
########
def send_payload():
    return





###########################
####################  USELESS EVENTS BELOW

#    #
#    # 
#    #
######
     #
     #
     #
#######                             #######
######Perhaps we can skip this event######
#####                               #######
##################################################
def update_lookup_tables():
    """This is a supplementary event for the echo event.
    This event updates the lookup tables of a maximum 8 neighbor motes.
    """
    sender_row = int( global_vars.EVENT_LIST[2][0].split()[1] )
    sender_col = int( global_vars.EVENT_LIST[2][0].split()[2] ) 
    #update neighbors
    return
##########################################################




######
##
##
##
######
    ##
    ##
    ##
######
def random_node_entry():
    """This event will assign to the node random entry coordinates.
    These coordinates are row and column of the MOTES_ARRAY."""
    current_time  = global_vars.EVENT_LIST[1][0]
    entry_side = random.randint(0,3)
    if entry_side == 0:
        #the node will enter from west
        entry_row = random.randint(0,len(global_vars.MOTES_ARRAY)-1)
        global_vars.NODES_ARRAY[0].heading = 'E'
        global_vars.NODES_ARRAY[0].current_row = entry_row
        global_vars.NODES_ARRAY[0].current_col = 0
    elif entry_side == 1:
        #node will enter from north
        entry_col = random.randint(0, len(global_vars.MOTES_ARRAY[0])-1)
        global_vars.NODES_ARRAY[0].heading = 'S'
        global_vars.NODES_ARRAY[0].current_row = 0
        global_vars.NODES_ARRAY[0].current_col = entry_col
    elif entry_side == 2:
        #node will enter from east
        entry_row = random.randint(0,len(global_vars.MOTES_ARRAY)-1)
        global_vars.NODES_ARRAY[0].heading = 'W'
        global_vars.NODES_ARRAY[0].current_row = entry_row
        global_vars.NODES_ARRAY[0].current_col = len(global_vars.MOTES_ARRAY[0])-1
    elif entry_side == 3:
        #node will enter from south
        entry_col = random.randint(0, len(global_vars.MOTES_ARRAY[0])-1)
        global_vars.NODES_ARRAY[0].heading = 'N'
        global_vars.NODES_ARRAY[0].current_row = entry_col
        global_vars.NODES_ARRAY[0].current_col = len(global_vars.MOTES_ARRAY)-1
    else:
        print "Error in random entry point"
        sys.exit(-1)

###schedule presence entry event####
    global_vars.EVENT_LIST[0].append(6)
    global_vars.EVENT_LIST[1].append(current_time)
    global_vars.EVENT_LIST[2].append('node0')

###schedule node step event###
    global_vars.EVENT_LIST[0].append(7)
    global_vars.EVENT_LIST[1].append(100.0 / global_vars.NODE_SPEED)
    global_vars.EVENT_LIST[2].append('node0')

###reschedule random node entry event###
    global_vars.EVENT_LIST[0].append(5)
    #just a random re-entry time
    global_vars.EVENT_LIST[1].append((1000.0 / global_vars.NODE_SPEED) + random.random())    
    global_vars.EVENT_LIST[2].append('node0')

    return



######
#
#
######
#    #
#    #
######

def presence_entry():
    """The node sends presence entry packet to inform the surrounding motes about his presence
    in the area. The motes must react accordingly to update their gateways."""
    current_time  = global_vars.EVENT_LIST[1][0]
    cur_node_row = global_vars.NODES_ARRAY[0].current_row
    cur_node_col = global_vars.NODES_ARRAY[0].current_col
    
    #delete previous gateway
    try:
        if global_vars.NODES_ARRAY[0].heading == 'E':
            global_vars.MOTES_ARRAY[cur_node_row][cur_node_col-1].gateway = False

        elif global_vars.NODES_ARRAY[0].heading == 'W':
            global_vars.MOTES_ARRAY[cur_node_row][cur_node_col+1].gateway = False

        elif global_vars.NODES_ARRAY[0].heading == 'N':
            global_vars.MOTES_ARRAY[cur_node_row+1][cur_node_col].gateway = False

        elif global_vars.NODES_ARRAY[0].heading == 'S':
            global_vars.MOTES_ARRAY[cur_node_row-1][cur_node_col-1].gateway = False
    except:
        #in case there is no previous mote gateway
        pass

    #set current gateway
    global_vars.MOTES_ARRAY[cur_node_row][cur_node_col].gateway = True
    global_vars.GATEWAY_ROW = cur_node_row
    global_vars.GATEWAY_COL = cur_node_col

    #schedule motes path to gateway update
    for i in xrange(10):
        for j in xrange(100):
            global_vars.EVENT_LIST[0].append(8)
            global_vars.EVENT_LIST[1].append(current_time)
            global_vars.EVENT_LIST[2].append('mote;%s;%s'%(i,j))
#####################
    
    #reschedule presence entry
    #global_vars.EVENT_LIST[0].append(6)
    #global_vars.EVENT_LIST[1].append()
    return



######
     #
     #
     #
     #
     #
def node_step():
    """This event is called every time the node goes more than 100 meters from the nearest mote.
    Once the node is more than 100m from the closest mote, mote gateways have to change."""
    current_time  = global_vars.EVENT_LIST[1][0]

    #update node position
    if global_vars.NODES_ARRAY[0].heading == 'E':
        global_vars.NODES_ARRAY[0].current_col += 1

    elif global_vars.NODES_ARRAY[0].heading == 'W':
        global_vars.NODES_ARRAY[0].current_col -= 1

    elif global_vars.NODES_ARRAY[0].heading == 'N':
        global_vars.NODES_ARRAY[0].current_row -= 1

    elif global_vars.NODES_ARRAY[0].heading == 'S':
        global_vars.NODES_ARRAY[0].current_row += 1

    #schedule presenece entry at the same time
    global_vars.EVENT_LIST[0].append(6)
    global_vars.EVENT_LIST[1].append(current_time)
    global_vars.EVENT_LIST[2].append('node0')

    #schedule update gateway
##########this needs to be done for all motes
    global_vars.EVENT_LIST[0].append(8)
    global_vars.EVENT_LIST[1].append(100.0 / global_vars.NODE_SPEED)
    global_vars.EVENT_LIST[2].append('node0')

    #schedule self
    global_vars.EVENT_LIST[0].append(7)
    global_vars.EVENT_LIST[1].append(100.0 / global_vars.NODE_SPEED)
    global_vars.EVENT_LIST[2].append('node0')
    return



######
#    #
#    #
######
#    #
#    #
######
def propagate_new_gateway():
    """Propagetes the cloud A gateway change and updates the parent child relationship.
    Uses the manhatan heuristic to find the shortest path to the gateway."""
    mote_i = int(global_vars.EVENT_LIST[2][0].split()[1])
    mote_j = int(global_vars.EVENT_LIST[2][0].split()[2])

    #check if this is the gateway
    if global_vars.MOTES_ARRAY[mote_i][mote_j].gateway == False:
        distance_to_gateway = 10000

        try:#check if the West mote is closer to gateway
            if abs( (global_vars.MOTES_ARRAY[mote_i][mote_j - 1].locationR + global_vars.MOTES_ARRAY[mote_i][mote_j].locationC) - (global_vars.GATEWAY_ROW + global_vars.GATEWAY_COL) ) < distance_to_gateway:
                #update gawteway
                global_vars.MOTES_ARRAY[mote_i][mote_j].parent = 'mote;%d;%d'(mote_i, mote_j-1)
        except:
                #out of bounds
            pass

        try:#check if the NW mote is closer to gateway
            if abs( (global_vars.MOTES_ARRAY[mote_i-1][mote_j - 1].locationR + global_vars.MOTES_ARRAY[mote_i][mote_j].locationC) - (global_vars.GATEWAY_ROW + global_vars.GATEWAY_COL) ) < distance_to_gateway:
                #update gawteway
                global_vars.MOTES_ARRAY[mote_i][mote_j].parent = 'mote;%d;%d'(mote_i-1, mote_j-1)
        except:
                #out of bounds
            pass

        try:#check if the North mote is closer to gateway
            if abs( (global_vars.MOTES_ARRAY[mote_i-1][mote_j].locationR + global_vars.MOTES_ARRAY[mote_i][mote_j].locationC) - (global_vars.GATEWAY_ROW + global_vars.GATEWAY_COL) ) < distance_to_gateway:
                #update gawteway
                global_vars.MOTES_ARRAY[mote_i][mote_j].parent = 'mote;%d;%d'(mote_i-1, mote_j)
        except:
                #out of bounds
            pass

        try:#check if the NE mote is closer to gateway
            if abs( (global_vars.MOTES_ARRAY[mote_i-1][mote_j+1].locationR + global_vars.MOTES_ARRAY[mote_i][mote_j].locationC) - (global_vars.GATEWAY_ROW + global_vars.GATEWAY_COL) ) < distance_to_gateway:
                #update gawteway
                global_vars.MOTES_ARRAY[mote_i][mote_j].parent = 'mote;%d;%d'(mote_i-1, mote_j+1)
        except:
                #out of bounds
            pass
        
        try:#check if the East mote is closer to gateway
            if abs( (global_vars.MOTES_ARRAY[mote_i][mote_j+1].locationR + global_vars.MOTES_ARRAY[mote_i][mote_j].locationC) - (global_vars.GATEWAY_ROW + global_vars.GATEWAY_COL) ) < distance_to_gateway:
                #update gawteway
                global_vars.MOTES_ARRAY[mote_i][mote_j].parent = 'mote;%d;%d'(mote_i, mote_j+1)
        except:
                #out of bounds
            pass

        try:#check if the SE mote is closer to gateway
            if abs( (global_vars.MOTES_ARRAY[mote_i+1][mote_j+1].locationR + global_vars.MOTES_ARRAY[mote_i][mote_j].locationC) - (global_vars.GATEWAY_ROW + global_vars.GATEWAY_COL) ) < distance_to_gateway:
                #update gawteway
                global_vars.MOTES_ARRAY[mote_i][mote_j].parent = 'mote;%d;%d'(mote_i+1, mote_j+1)
        except:
                #out of bounds
            pass

        try:#check if the South mote is closer to gateway
            if abs( (global_vars.MOTES_ARRAY[mote_i+1][mote_j].locationR + global_vars.MOTES_ARRAY[mote_i][mote_j].locationC) - (global_vars.GATEWAY_ROW + global_vars.GATEWAY_COL) ) < distance_to_gateway:
                #update gawteway
                global_vars.MOTES_ARRAY[mote_i][mote_j].parent = 'mote;%d;%d'(mote_i+1, mote_j)
        except:
                #out of bounds
            pass

        try:#check if the SW mote is closer to gateway
            if abs( (global_vars.MOTES_ARRAY[mote_i+1][mote_j-1].locationR + global_vars.MOTES_ARRAY[mote_i][mote_j].locationC) - (global_vars.GATEWAY_ROW + global_vars.GATEWAY_COL) ) < distance_to_gateway:
                #update gawteway
                global_vars.MOTES_ARRAY[mote_i][mote_j].parent = 'mote;%d;%d'(mote_i+1, mote_j-1)
        except:
                #out of bounds
            pass
    #gateway updated done
    return
