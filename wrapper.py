"""Simulator wrapper"""

import global_vars
import wsn_main
import sys


if __name__ == "__main__":

    if len(sys.argv) > 6:
        global_vars.SIM_TIME = int(sys.argv[1])
        global_vars.NUMBER_OF_MOTES = int(sys.argv[2])
        global_vars.NUMBER_OF_NODES = int(sys.argv[3])
        global_vars.DATA_PACKET_SIZE = int(sys.argv[4])
        global_vars.ECHO_PACKET_SIZE = int(sys.argv[5])
        global_vars.DATA_INTERVAL_TIME = int(sys.argv[6])
        global_vars.PRESENCE_ENTRY_INTERVAL = int(sys.argv[7])
        global_vars.NODE_SPEED = int(sys.argv[8])
        global_vars.BANDWIDTH = int(sys.argv[9])
        global_vars.RESULTS_FILE_NAME = sys.argv[10]
        global_vars.HEADER_SIZE = int(sys.argv[11])
        global_vars.RN = int(sys.argv[12])

    wsn_main.wsn_main()
