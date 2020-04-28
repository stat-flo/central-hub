

class CentralHub:
    def __init__(self):
        pass

    #TODO: Takes the voltage data from the node pressure (in uV)
    #      module and calculates the pressure in PSI
    def calculate_pressure(self, node_voltage):
        pass

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