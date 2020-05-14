import time
import random

from sensor_module.sensor_module import SensorModuleNode
from sensor_module.sensor_line   import NodeLine

class CentralHub:
    def __init__(self):
        self.node_set = {}
        self.line_set = {}
        self.db_cache = {}
        self.num_nodes = 0
        self.num_lines = 0
        self.node_line_id = 0

    #TODO: Send the request packet to the desired node
    def transmit_request(self, node_id):
        flag = 1

        # while ()

    def line_calibration(self, node1, node2, node_line):     
        node1_data = []
        node2_data = []
        
        # Start the timer
        start = time.time()

        # Run for 600 seconds (10 minutes)
        run_time = 15

        while(time.time() - start < run_time + 1):        
            print(time.time() - start)  

            node1.set_node_data(random.randint(6500, 8000))
            node2.set_node_data(random.randint(6500, 8000))

            node1_data.append(node1.get_node_data())
            node2_data.append(node2.get_node_data())

            time.sleep(5)

        node_line.set_node_1_avg(self.calculate_avg_time(node1_data))
        node_line.set_node_2_avg(self.calculate_avg_time(node2_data))

        node1.set_max_sample(max(node1_data))
        node2.set_max_sample(max(node2_data))

        node1.set_min_sample(min(node1_data))
        node2.set_min_sample(min(node2_data))

        self.display_nodes()

    def initialize_node_line(self, node_line, node1, node2):
        line_id = node_line.generate_node_line_id()

        while (str(line_id) in self.line_set):
            line_id = node_line.generate_node_line_id()

        self.line_set[str(line_id)] = node_line

        node_line.set_node_pairs(node1, node2)
        self.num_lines += 1

    def calculate_avg_time(self, node_data_set):
        return sum(node_data_set) // len(node_data_set) 

    #TODO: No data has been received from this node
    def error_node(self, node):
        pass

    # Iterates through the list of nodes and reads
    # the data from those nodes
    def cycle_nodes(self):
        print("\nCycle Nodes:")
        for line in self.line_set:
            print("Reading from Nodeline %s" % self.line_set[line].get_node_line_id())
            print("\nSending request to Node %s" % self.line_set[line].get_node_pairs()[0].get_node_id())
            time.sleep(2)
            print("Waiting on the recipient ack from Node %s" % self.line_set[line].get_node_pairs()[0].get_node_id())
            time.sleep(2)
            print("Ack received from Node %s!" % self.line_set[line].get_node_pairs()[0].get_node_id())
            time.sleep(2)
            print("Waiting for data packet from Node %s" % self.line_set[line].get_node_pairs()[0].get_node_id())
            time.sleep(2)
            print("Receiving data packet from Node %s" % self.line_set[line].get_node_pairs()[0].get_node_id())
            time.sleep(2)
            print("Receiving end packet from Node %s" % self.line_set[line].get_node_pairs()[0].get_node_id())
            time.sleep(2)
            print("Sending end packet ack to Node %s" % self.line_set[line].get_node_pairs()[0].get_node_id())
            time.sleep(2)

            print("\n\nSending request to Node %s" % self.line_set[line].get_node_pairs()[1].get_node_id())
            time.sleep(2)
            print("Waiting on the recipient ack from Node %s" % self.line_set[line].get_node_pairs()[1].get_node_id())
            time.sleep(2)
            print("Ack received from Node %s!" % self.line_set[line].get_node_pairs()[1].get_node_id())
            time.sleep(2)
            print("Waiting for data packet from Node %s" % self.line_set[line].get_node_pairs()[1].get_node_id())
            time.sleep(2)
            print("Receiving data packet from Node %s" % self.line_set[line].get_node_pairs()[1].get_node_id())
            time.sleep(2)
            print("Receiving end packet from Node %s" % self.line_set[line].get_node_pairs()[1].get_node_id())
            time.sleep(2)
            print("Sending end packet ack to Node %s" % self.line_set[line].get_node_pairs()[1].get_node_id())
            time.sleep(2)

            #print(self.line_set[line])

    #TODO: Pushes data from node to the database
    def push_to_database(self, node_id):
        pass

    # Adds a node to the set
    def add_node(self, node):
        self.node_set[node.get_node_id()] = node
        self.num_nodes += 1

    # Removes a node from a set
    def remove_node(self, node):
        try:
            self.node_set.pop(node.get_node_id())
            self.num_nodes -= 1

        except:
            print("Error: Removing Node %s" % node.get_node_id())

    #TODO: An error has occured when loading to the database
    #      and the node data has been stored in a cache
    def error_database(self, node):
        pass

    def display_nodes(self):
        if self.num_nodes <= 0:
            print("Node list is empty.")
            return 

        node_num = 1

        for node in self.node_set:
            print("Node %s: " % int(node_num), flush=True, end="")
            print(self.node_set[node])
            node_num += 1

    def display_lines(self):
        if self.num_lines <= 0:
            print("Node list is empty.")
            return 

        line_num = 1

        for line in self.line_set:
            print("Line %s: " % int(line_num), flush=True, end="")
            print(self.line_set[line])
            line_num += 1

if __name__ == "__main__":
    hub = CentralHub()

    node_1 = SensorModuleNode()
    node_2 = SensorModuleNode()

    node_line = NodeLine()
    node_line.set_node_line_id("000001")

    node_1.set_node_id("1f3b79")
    node_2.set_node_id("1f3b56")

    hub.add_node(node_1)
    hub.display_nodes()

    hub.add_node(node_2)
    hub.display_nodes()

    hub.initialize_node_line(node_line, node_1, node_2)
    hub.line_calibration(node_1, node_2, node_line)
 
    hub.display_lines()
    hub.cycle_nodes()

    hub.remove_node(node_2)
    hub.display_nodes()

    hub.remove_node(node_1)
    hub.display_nodes()