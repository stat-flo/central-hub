from sensor_module.sensor_module import SensorModuleNode

class NodeLine:
    #TODO: 
    def __init__(self):
        pass

class CentralHub:
    def __init__(self):
        self.node_set = {}
        self.db_cache = {}
        self.num_nodes = 0

    #TODO: No data has been received from this node
    def error_node(self, node):
        pass

    #TODO: Iterates through the list of nodes and reads
    #      the data from those nodes
    def cycle_nodes(self, node_list):
        pass

    #TODO: Reads the data from the input node
    def read_node(self, node):
        pass

    #TODO: Pushes data from node to the database
    def push_to_database(self, node):
        pass

    #TODO: Adds a node to the set
    def add_node(self, node):
        self.node_set[node.get_name()] = node
        self.num_nodes += 1

    #TODO: Removes a node from a set
    def remove_node(self, node):
        try:
            self.node_set.pop(node.get_name())
            self.num_nodes -= 1

        except:
            print("Error: Removing Node %s" % node.get_name())

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

if __name__ == "__main__":
    hub = CentralHub()
    node = SensorModuleNode()

    node.set_name("1f3b79")

    hub.add_node(node)

    hub.display_nodes()

    hub.remove_node(node)

    hub.display_nodes()