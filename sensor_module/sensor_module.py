class SensorModuleNode:
    def __init__(self):
        self.node_id = ""
        self.node_line_id = ""
        self.nodal_data = None
        self.node_max = None
        self.node_min = None
        self.last_read_time = None
        self.dedicated_time = None

    def set_dedicated_time(self, set_time):
        self.dedicated_time = set_time

    def get_dedicated_time(self):
        return self.dedicated_time

    def get_last_read_time(self):
        return self.last_read_time

    def set_last_read_time(self, read_time):
        self.last_read_time = read_time

    def get_node_id(self):
        return self.node_id

    def set_node_id(self, node_id):
        self.node_id = node_id

    def get_node_line_id(self):
        return self.node_line_id

    def set_node_line_id(self, id):
        self.node_line_id = id

    def get_node_data(self):
        return self.nodal_data

    def set_node_data(self, data):
        self.nodal_data = data

    def set_max_sample(self, data):
        self.node_max = data

    def set_min_sample(self, data):
        self.node_min = data

    def get_max_sample(self, data):
        return self.node_max

    def get_min_sample(self, data):
        return self.node_min

    def __repr__(self):
        return "Node ID: %s | Data: %s | Threshold Min: %s | Threshold Max: %s" %\
            (self.node_id, self.nodal_data, self. node_min, self.node_max)