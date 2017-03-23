import os.path
from tori.db.entity import entity
from tori.db.mapper import link, AssociationType as t, CascadingType as c

@link(
    target      = 'cis.model.Automation',
    mapped_by   = 'automation',
    association = t.MANY_TO_ONE
)
@entity
class Sequence(object):
    def __init__(self, priority, script, automation):
        self.priority = priority
        self.script   = script
        self.automation = automation