# -*- coding: utf-8 -*-
from tori.controller           import Controller
from tori.decorator.controller import renderer

class Visibility(object):
    friend = 'friend'
    honour = 'honour'
    family = 'family'
    guest  = 'guest'

class Information(object):
    def __init__(self, summary, location, start_at, *guest_types):
        self.summary  = summary
        self.location = location
        self.start_at = start_at
        self.guest_types = guest_types

@renderer('event.view')
class AttWeddingEvent(Controller):
    def get(self):
        self.render('att-wedding.html', sequence = self.__sequence(), visibility = self.__visibility())

    def __visibility(self):
        for key in dir(Visibility):
            if key[0] == '_':
                continue

            yield getattr(Visibility, key)

    def __sequence(self):
        return [
            Information(
                'Engagement Ceremony',
                'TBD',
                '0700',
                Visibility.family,
                Visibility.friend
            ),
            Information(
                'Family Introduction',
                'The Noppornpitak',
                '1200',
                Visibility.family
            ),
            Information(
                'Wedding Ceremony',
                'TBD',
                '1300',
                Visibility.family,
                Visibility.honour,
                Visibility.friend,
                Visibility.guest
            ),
            Information(
                'Wedding Party',
                'TBD',
                '1330',
                Visibility.family,
                Visibility.honour,
                Visibility.guest
            ),
            Information(
                'Wedding Party',
                'TBD',
                '1900',
                Visibility.friend
            )
        ]