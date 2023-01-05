"""
J Leadbetter <j@jleadbetter.com>
MIT License

Typically children of Borg classes still maintain their parents' attributes,
so inheritance isn't very useful in the Borg pattern. In this exploration,
we'll show that it's possible to have Borg classes that share a class base
without sharing attributes.
"""


class TotalBorgOldGen:
    """
    Variation on the FactionedBorg that uses class to determine uniqueness.

    Child classes of this will not share the parent's dictionary, unlike in
    traditional Borg classes.
    """

    __others__ = set()

    def __init__(self, objective=None):
        tmp_others = list(self.__others__)
        try:
            other_borg = tmp_others.pop(tmp_others.index(self))
            self.__dict__ = other_borg.__dict__

            # Set the objective after joining the collective
            self.objective = objective or self.objective
        except ValueError:
            # This is the first of a new Borg child class
            self.objective = objective
            self.__others__.add(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__

    def __hash__(self):
        return hash(self.__class__.__name__)

    def __str__(self):
        return "We are the Borg."

    def assimilate(self, other_lifeform):
        """Completely assimilate other lifeform, but take any attributes"""

        self_attrs = dir(self)
        for attr in dir(other_lifeform):
            # ignore dunderscore attributes
            if not (attr.startswith('__') or attr in self_attrs):
                setattr(self, attr, getattr(other_lifeform, attr))

        for attr in self_attrs:
            try:
                setattr(other_lifeform, attr, getattr(self, attr))
            except AttributeError:
                # some dunderscore methods can't be copied, so ignore
                pass

        other_lifeform.__dict__ = self.__dict__


class TotalBorgNextGen(TotalBorgOldGen):
    """A new generation of Borg, with their own collective memory"""

    pass


class FederationOfficer:
    """A class that exists solely to be assimilated by the Borg"""

    def __init__(self, name, rank, ship):
        self.name = name
        self.rank = rank
        self.ship = ship

    def __str__(self):
        return "{}, {} of the {}".format(self.name, self.rank, self.ship)

    def mission(self):
        return "To boldly go where no one has gone before."


if __name__ == '__main__':

    starfleet_officer1 = FederationOfficer(
        'Kathryn Janeway', 'Captain', 'USS Voyager'
    )

    print(starfleet_officer1)
    print("Janeway's Mission: {}".format(starfleet_officer1.mission()))

    borg1 = TotalBorgOldGen('You will be assimilated.')
    borg2 = TotalBorgNextGen('We must assimilate.')
    borg3 = TotalBorgNextGen()

    print('Old Borg: {}'.format(borg1))
    print('First new Borg: {}'.format(borg2))
    print('Second new Borg: {}'.format(borg3))
    print('Old Borg objective: {}'.format(borg1.objective))
    print('First new Borg objective: {}'.format(borg2.objective))
    print('Second new Borg objective: {}'.format(borg3.objective))
    try:
        borg1.mission()
    except AttributeError:
        print('Old Borg has no mission.')
    try:
        borg2.mission()
    except AttributeError:
        print('First new Borg has no mission.')
    try:
        borg3.mission()
    except AttributeError:
        print('Second new Borg has no mission.')

    print('If one of the new Borg had assimilated Janeway...')
    print('Then both Janeway and both the new Borg would change.')

    borg2.assimilate(starfleet_officer1)

    print('Janeway: {}'.format(starfleet_officer1))
    print('First new Borg: {}'.format(borg2))
    print('Second new Borg: {}'.format(borg3))
    print("Janeway's mission: {}".format(starfleet_officer1.mission()))
    print("First new Borg's mission: {}".format(borg2.mission()))
    print("Second new Borg's mission: {}".format(borg3.mission()))
    print("Janeway's objective: {}".format(starfleet_officer1.objective))
    print('First new Borg objective: {}'.format(borg2.objective))
    print('Second new Borg objective: {}'.format(borg3.objective))

    print('But the old Borg remain unaffected.')
    print('Old Borg: {}'.format(borg1))
    print('Old Borg objective: {}'.format(borg1.objective))
    try:
        borg1.mission()
    except AttributeError:
        print('Old Borg has no mission.')
