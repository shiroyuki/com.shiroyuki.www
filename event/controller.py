# -*- coding: utf-8 -*-
from tori.controller           import Controller
from tori.decorator.controller import renderer

class Visibility(object):
    friend = 'friend'
    elder  = 'VIP'
    family = 'family member'

class Information(object):
    def __init__(self, summary, location, start_at, *guest_types):
        self.summary  = summary
        self.location = location
        self.start_at = start_at
        self.guest_types = guest_types

@renderer('event.view')
class AttWeddingEvent(Controller):
    def get(self):
        sequence = [
            Information(
                'Engagement Ceremony',
                'TBD',
                '0700',
                Visibility.family,
                Visibility.elder,
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
                Visibility.elder,
                Visibility.friend
            ),
            Information(
                'Wedding Party',
                'TBD',
                '1330',
                Visibility.family,
                Visibility.elder
            ),
            Information(
                'Wedding Party',
                'TBD',
                '1900',
                Visibility.friend
            )
        ]
        self.render('att-wedding.html', sequence = sequence, visibility = Visibility)