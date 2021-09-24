class Computer:
    def __init__(self, id, ip, increaseBand):
        self.id = id
        self.ip = ip
        self.increaseBand = increaseBand

    def __repr__(self):
        return "id=%s ip=%s increaseBand=%s" % (self.id, self.ip, self.increaseBand)

class Resource:
    def __init__(self, id, name, size, unit):
        self.id = id
        self.name = name
        self.size = size
        self.unit = unit

    def __repr__(self):
        return "id=%s name=%s size=%s unit=%s" % (self.id, self.name, self.size, self.unit)
