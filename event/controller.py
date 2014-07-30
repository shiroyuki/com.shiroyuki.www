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

@renderer('event.view')
class AttWeddingCodeFactoryEvent(Controller):
    def get(self):
        """
            the 1st character indicates events for close family members and represents with the character U.
            the 2nd character indicates events for friends and represents with the character B.
            the 3rd character indicates events for VIP and elders and represents with the character Q.
            the 4th character indicates events for colleagues and represents with the character C.
            the 5th character indicates events for relatives and represents with the character R.
        """
        code_book = [
            ('u', 'close family members'),
            ('b', 'friends'),
            ('q', 'VIP'),
            ('c', 'colleagues'),
            ('r', 'relatives'),
        ]
        self.render('att-wedding-code-factory.html', code_book = code_book)
