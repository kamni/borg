"""
J Leadbetter <j@jleadbetter.com>
MIT License

How can we make the Borg assimilate people in a thread-safe manner?
"""

import random
import threading
import time


class ThreadSafeBorg:
    """
    Borg class that safely assimilates people at the same time.

    The Borg keep track of which individuals they've assimilated and how many
    individuals they've assimilated. Two Borgs can't assimilate the same
    person twice.

    This is a Highlander Borg...there can be only one.
    """

    _shared_state = {'borg': True}
    _assimilation_lock = threading.Lock()

    def __init__(self):
        self.__dict__ = ThreadSafeBorg._shared_state

        with self._assimilation_lock:
            if not hasattr(self, 'assimilation_count'):
                self.assimilation_count = 0
            if not hasattr(self, 'assimilation_list'):
                self.assimilation_list = []

    def __str__(self):
        return "We are the Borg."

    def is_borg(self):
        return True

    @classmethod
    def assimilate(cls, other_lifeforms):
        """Completely assimilate other lifeform"""

        for lifeform in other_lifeforms:
            with cls._assimilation_lock:
                try:
                    # Don't assimilate someone who is already a Borg
                    lifeform.borg
                except AttributeError:
                    lifeform_str = str(lifeform)
                    cls._shared_state['assimilation_count'] += 1
                    cls._shared_state['assimilation_list'].append(
                        lifeform_str,
                    )
                    lifeform.__dict__ = cls._shared_state
                    # It takes time to assimilate an individual
                    time.sleep(random.uniform(0, 1))
                    print(f'Successfully assimilated {lifeform_str}')

    def report_assimilated(self):
        """Print a verification report of who was assimilated"""
        print(f'Number assimilated: {self.assimilation_count}')
        for lifeform in self.assimilation_list:
            print(lifeform)


class FederationOfficer:
    """A class that exists solely to be assimilated by the Borg"""

    def __init__(self, name, rank, ship):
        self.name = name
        self.rank = rank
        self.ship = ship

    def __str__(self):
        return f'{self.rank} {self.name} of the {self.ship}'


if __name__ == '__main__':
    uss_voyager = [
        FederationOfficer('Janeway', 'Captain', 'USS Voyager'),
        FederationOfficer('Kim', 'Ensign', 'USS Voyager'),
        FederationOfficer('Paris', 'Lieutenant', 'USS Voyager'),
        FederationOfficer('Tuvok', 'Chief Tactical Officer', 'USS Voyager'),
    ]
    borg = [
        ThreadSafeBorg(),
        ThreadSafeBorg(),
        ThreadSafeBorg(),
    ]
    print('The USS Voyager:')
    for crew_member in uss_voyager:
        print(crew_member)

    print((
        '\nUnfortunately, they encounter the Borg....'
        'Will any escape their clutches?'
    ))
    for drone in borg:
        crew_members = [random.choice(uss_voyager) for i in range(3)]
        thread = threading.Thread(
            target=ThreadSafeBorg.assimilate,
            args=(crew_members,),
        )
        thread.start()
        thread.join()

    print("\nLet's see who survived, according to the Borg!")
    for idx, drone in enumerate(borg):
        print(f'Drone {idx + 1} says:')
        drone.report_assimilated()

    print("\nWho's left?")
    count = 0
    for crew_member in uss_voyager:
        if not hasattr(crew_member, 'borg'):
            count += 1
            print(f'Survived: {crew_member}')
    if not count:
        print('No one survived...')
