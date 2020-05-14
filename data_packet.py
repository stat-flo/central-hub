class DataPacket:
    def __init__(self):
        self.flag = None
        self.checksum = None
        self.node_data = None
        self.time = None

        self.send_id = None
        self.request_id = None

    def reset_packet(self):
        self.flag = None
        self.checksum = None
        self.node_data = None
        self.time = None

        self.send_id = None
        self.request_id = None        

    def create_hub_request_packet(self, request_id):
        self.reset_packet()

        self.flag = 1
        self.request_id = request_id
        self.checksum = 5

    def create_node_ack_packet(self, send_id):
        self.reset_packet()

        self.flag = 2
        self.send_id = send_id
        self.checksum = 5

    def create_node_data_packet(self, send_id, data, time):
        self.reset_packet()

        self.flag = 3
        self.send_id = send_id
        self.node_data = data
        self.time = time
        self.checksum = 11

    def create_node_end_packet(self, send_id):
        self.reset_packet()

        self.flag = 4
        self.send_id = send_id
        self.checksum = 5

    def create_hub_ack_end_packet(self, request_id):
        self.reset_packet()

        self.flag = 5
        self.request_id = request_id
        self.checksum = 5