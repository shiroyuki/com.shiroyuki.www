from tori.db.entity import entity

@entity
class Automation(object):
    def __init__(self, name):
        self.name = name