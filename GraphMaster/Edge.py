class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __eq__(self, other):
        if not isinstance(other, Edge):
            return False
        return self.source == other.source and self.destination == other.destination

    def __hash__(self):
        return hash(self.source) + hash(self.destination)

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination
