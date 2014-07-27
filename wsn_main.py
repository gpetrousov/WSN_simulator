"""Event driven simulation for a wireless sensor network.
Properties:
    - The area is 10km^2
    - The network consists of 1000 motes-sensors, cloud A
    - The motes a uniformly spread
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
__status__ = "early alpha"






def wsn_main():
    """Main function that loops over the event list and calls the events themselves"""

###########################################
    while True:
        if global_vars.EVENT_LIST[0][0] == 0:
            #delay by random time
            pass

        if global_vars.EVENT_LIST[0][0] == 1:
            #send echo
            pass

        if global_vars.EVENT_LIST[0][0] == 2:
            #send package
            pass





        if global_vars.EVENT_LIST[0] == 10:
            #terminate
            pass

        #passed event must be deleted
        for x in global_vars.EVENT_LIST:
            del x[0]
        #sort the the event list
        #dont fucking worry about the simulation time now
        global_vars.EVENT_LIST = functions.sortrows(global_vars.EVENT_LIST, 1)

    #pass
###############################################
    return




########### INIT ###########
if __name__ == '__main__':

    functions.initialize_motes()
    functions.initialize_nodes()
    functions.initialize_channels()
    functions.initialize_event_list()

    #debug statements
    """ 
    for i in xrange(10):
        for j in xrange(100):
            print '%s, location: %d,%d, coordinates: %d,%d' %(MOTES_ARRAY[i][j].moteID, MOTES_ARRAY[i][j].locationR, MOTES_ARRAY[i][j].locationC, MOTES_ARRAY[i][j].positionY, MOTES_ARRAY[i][j].positionX)
            print ' '

    print 'initialized node and channel %s' % node.channel.channelID 
    """

    wsn_main()
