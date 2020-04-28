class SensorModuleNode:
    def __init__(self):
        self.name = ""

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def __repr__(self):
        return "Name: %s" % self.name
        