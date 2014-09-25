"""Event driven simulation for a wireless sensor network.
Properties:
    - The area is 10km^2
    - The network consists of 1000 motes-sensors, cloud A
    - The motes are uniformly spread
    - One node (Cloud B) enters the area and croses it at a given speed
    - Once the node enters the area, it starts receiving data from the motes
    - The network reorganizes as the node croses the area
    - Time is measured in seconds
For more details see the readme file.
    """

import global_vars
import classes
import functions
import events

__author__ = "Giannis Petrousov"
__copyright__ = "Copyright 2014"
__credits__ = ["Giannis Petrousov"]
__license__ = "The MIT License"
__maintainer__ = "Giannis Petrousov"
__email__ = "petrousov@gmail"
__status__ = "beta"






def wsn_main():
    """Main function that loops over the event list and calls the events themselves"""

    functions.initialize_motes()
    functions.initialize_nodes()
    functions.initialize_channels()
    functions.initialize_event_list()

###########################ECHO-MEETING STEP###################################
    echoed_nodes = 0

    while echoed_nodes < 1000:
    #Initially take some time for the motes to meet eachother and populate lookup tables
    #Reschedule delay and cca until echoed
        current_time = global_vars.EVENT_LIST[1][0]
        if global_vars.EVENT_LIST[0][0] == 0:
            #0 = Take random time
            events.assign_random_wait_time()
            #pass
        if global_vars.EVENT_LIST[0][0] == 1:
            #1 = Perform CCA-Clear Channel Assesment
            events.cca()
        if global_vars.EVENT_LIST[0][0] == 2:
            #2 = Send echo
            events.echo()
            echoed_nodes += 1
        #passed event must be deleted
        for x in global_vars.EVENT_LIST:
            del x[0]
        #sort the the event list
        #dont fucking worry about the simulation time now
        global_vars.EVENT_LIST = functions.sortrows(global_vars.EVENT_LIST, 1)
        #global_vars.EVENT_LIST[0] = list(global_vars.EVENT_LIST[0])
        #global_vars.EVENT_LIST[1] = list(global_vars.EVENT_LIST[1])
        #global_vars.EVENT_LIST[2] = list(global_vars.EVENT_LIST[2])
            #pass
#When the loop above finishes, all motes know their neigbors == lookup tables updated
###############################################################################

#node enters here
    global_vars.EVENT_LIST[0].append(5)
    global_vars.EVENT_LIST[1].append(current_time)
    global_vars.EVENT_LIST[2].append('node0')
    global_vars.EVENT_LIST = functions.sortrows(global_vars.EVENT_LIST, 1)

####################### DEBUG TILL HERE ; ALL GOOD ##############


###########################################
    while True:
        current_time = global_vars.EVENT_LIST[1][0] #for debugging purposes
        print current_time
        if global_vars.EVENT_LIST[0][0] == 0:
            #delay by random time
            events.assign_random_wait_time()

        if global_vars.EVENT_LIST[0][0] == 1:
            events.cca()

        if global_vars.EVENT_LIST[0][0] == 2:
            events.echo()

        if global_vars.EVENT_LIST[0][0] == 3:
            events.send_payload()

        if global_vars.EVENT_LIST[0][0] == 4:
            events.update_lookup_tables()

        if global_vars.EVENT_LIST[0][0] == 5:
            events.random_node_entry()

        if global_vars.EVENT_LIST[0][0] == 6:
            events.presence_entry()

        if global_vars.EVENT_LIST[0][0] == 7:
            events.node_step()

        if global_vars.EVENT_LIST[0][0] == 8:
            events.propagate_new_gateway()

        if global_vars.EVENT_LIST[0][0] == 9:
            events.forward_payload()

        if global_vars.EVENT_LIST[0][0] == 10:
            #terminate
            break

        #passed event must be deleted
        for x in global_vars.EVENT_LIST:
            del x[0]
        #sort the the event list
        #dont fucking worry about the simulation time now
        global_vars.EVENT_LIST = functions.sortrows(global_vars.EVENT_LIST, 1)

    #pass
###############################################
    functions.write_simulation_results_to_file()
    return
