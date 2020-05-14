from random import random
import threading
import time

from sensor_module.sensor_module import SensorModuleNode
from sensor_module.sensor_line   import NodeLine

from data_packet import DataPacket

progress = 0
request_node = None
result = None
node_1_event = threading.Event()
data_packet = DataPacket()


# def background_calculation():

#     node_1 = SensorModuleNode()
#     node_2 = SensorModuleNode()

#     # when the calculation is done, the result is stored in a global variable
#     global result
#     result = 42
#     result_available.set()

#     # do some more work before exiting the thread
#     time.sleep(10)

def node_2_process():
    
    global request_node

    node_2 = SensorModuleNode()  
    node_2.set_node_id("1a2b3d")

    mode = 0

    while True:
        # Waiting for request
        if (mode == 0):
            print("Waiting for request on %s.." % node_2.get_node_id())

            if (request_node == node_2.get_node_id()):
                print("Request has been received on %s.." % node_2.get_node_id())
                mode += 1

        # Transmit send ACK
        elif (mode == 1):
            print("Sending ACK on %s.." % node_2.get_node_id())

        # Transmit data packet
        elif (mode == 2):
            print("Sending Data on %s.." % node_2.get_node_id())

        # Transmit end packet
        elif (mode == 3):
            print("Sending End packet on %s.." % node_2.get_node_id())

        # Receive end ack
        elif (mode == 4):
            print("Waiting for end ack on %s.." % node_2.get_node_id())

        else:
            print("Error with %s", node_2)

        time.sleep(1)

    node_2_event.set()

    # do some more work before exiting the thread
    time.sleep(10)

def node_1_process():
    
    global request_node

    node_1 = SensorModuleNode()  
    node_1.set_node_id("1a2b3c")

    mode = 0

    while True:
        # Waiting for request
        if (mode == 0):
            print("Waiting for request on %s.." % node_1.get_node_id())

            if (data_packet.request_id == node_1.get_node_id()):
                create_node_ack_packet(node_1.get_node_id())
                print("Request has been received on %s.." % node_1.get_node_id())
                mode += 1

        # Transmit send ACK
        elif (mode == 1):
            print("Sending ACK on %s.." % node_1.get_node_id())

        # Transmit data packet
        elif (mode == 2):
            print("Sending Data on %s.." % node_1.get_node_id())

        # Transmit end packet
        elif (mode == 3):
            print("Sending End packet on %s.." % node_1.get_node_id())

        # Receive end ack
        elif (mode == 4):
            print("Waiting for end ack on %s.." % node_1.get_node_id())

        else:
            print("Error with %s", node_1)

        time.sleep(1)

    node_1_event.set()

    # do some more work before exiting the thread
    time.sleep(10)

def request(node_id):

def main():
    global request_node

    thread_1 = threading.Thread(target=node_1_process)
    thread_1.start()

    thread_2 = threading.Thread(target=node_2_process)
    thread_2.start()

    while True:
        time.sleep(4)
        data_packet.create_hub_request_packet("1a2b3c")
        time.sleep(4)
        request_node = "1a2b3d"
        time.sleep(4)

    # wait here for the result to be available before continuing
    while not node_1_event.wait(timeout=5):
        print('\r{}% done...'.format(progress), end='', flush=True)


if __name__ == '__main__':
    main()