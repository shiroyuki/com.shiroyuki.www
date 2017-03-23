from tori.db.entity import entity
from tori.db.mapper import link, AssociationType as t, CascadingType as c

@link(
    target      = 'cis.model.Sequence',
    mapped_by   = 'current_sequence',
    association = t.ONE_TO_ONE
)
@link(
    target      = 'cis.model.Sequence',
    mapped_by   = 'last_sequence',
    association = t.ONE_TO_ONE
)
@link(
    target      = 'cis.model.Automation',
    mapped_by   = 'automation',
    association = t.MANY_TO_ONE
)
@entity
class Job(object):
    def __init__(self, trigger, automation, created=None, updated=None,
                 started=None, finished=None, pid=None, completed_sequence=0,
                 current_sequence=None, last_sequence=None):
        self.automation = automation
        self.trigger = trigger
        self.created = created
        self.updated = updated
        self.started = started
        self.finished = finished
        self.pid = pid
        self.completed_sequence = completed_sequence
        self.current_sequence   = current_sequence
        self.last_sequence      = last_sequence