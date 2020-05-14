import random

class NodeLine:
    def __init__(self):
        self.node_line_id = None
        self.node_1 = None
        self.node_2 = None
        self.node_1_avg = None
        self.node_2_avg = None

    def set_node_pairs(self, node1, node2):
        self.node2 = node2
        self.node1 = node1

    def get_node_pairs(self):
        return self.node1, self.node2

    def set_node_1_avg(self, avg):
        self.node_1_avg = avg

    def set_node_2_avg(self, avg):
        self.node_2_avg = avg

    def generate_node_line_id(self):
        return random.randint(0, 4294967296)

    def get_node_line_id(self):
        return self.node_line_id

    def set_node_line_id(self, id):
        self.node_line_id = id

    def __repr__(self):
        return "Line ID: %s | Node1: %s | Node2: %s | Node1 Avg: %s | Node2 Avg: %s" %\
            (str(self.node_line_id), self.node1, self. node2, str(self.node_1_avg), str(self.node_2_avg))