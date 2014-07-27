import global_vars
from random import random

###events###

"""
0 = Take random time
1 = Perform CCA-Clear Channel Assesment
2 = Send echo
3 = Send package
10 = Termination event
"""


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
    global_vars.EVENT_LIST[1].append(current_time + random())#random time
#########but for now                                 #############
###########let random() do the work for us            ############
###############have to add BE for each mote in the class ########
    global_vars.EVENT_LIST[2].append(global_vars.EVENT_LIST[2][0])#ID

    return



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

        mote_row = int( global_vars.EVENT_LIST[2][0].split()[1] )
        mote_col = int( global_vars.EVENT_LIST[2][0].split()[2] ) 
        if global_vars.MOTES_ARRAY[ mote_row ][ mote_col ].payload == True:
            #mote has payload ready
            #schedule the send package event
            global_vars.EVENT_LIST[0].append(3)

        elif global_vars.MOTES_ARRAY[ mote_row ][ mote_col ].payload == True:
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



def echo():
    current_time  = global_vars.EVENT_LIST[1][0]
    global_vars.CHANNEL_ARRAY[0].
    return


def send_payload():
    return
