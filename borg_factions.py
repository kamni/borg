"""
J Leadbetter <jleadbet@gmail.com>
MIT License

The Borg have had a schism, and now understand the concept of 'faction'. Borg
only share knowledge with members of the same faction.
"""

from __future__ import print_function


class FactionedBorg(object):
    """Borg implementation that only shares attributes with faction members"""

    __others__ = set()

    def __init__(self, faction, slogan):
        super(FactionedBorg, self).__init__()

        tmp_others = list(self.__others__)
        self.faction = faction
        try:
            faction_member = tmp_others.pop(tmp_others.index(self))
            self.__dict__ = faction_member.__dict__

            # We need to set the slogan after joining the faction
            self.slogan = slogan
        except ValueError:
            # We have a lone Borg. Create a new faction.
            self.slogan = slogan
            self.__others__.add(self)

    def __hash__(self):
        return hash(self.faction)

    def __eq__(self, other):
        return self.faction == other.faction

    def __str__(self):
        return "We are the {} Borg. {}".format(self.faction, self.slogan)

    def assimilate(self, other_lifeform):
        other_lifeform.__dict__ = self.__dict__


if __name__ == '__main__':
    borg1 = FactionedBorg('Delta Quadrant', 'You will be assimilated.')
    borg2 = FactionedBorg('Hue', 'We are Hue.')
    borg3 = FactionedBorg('Locutus', 'Make it so.')

    print(borg1)
    print(borg2)
    print(borg3)
    print('The three borg factions have different agendas...')
    print('What happens if the Original Borg win?')

    borg1.assimilate(borg2)
    print(borg2)

    print('But Locutus lives on...')
    print(borg3)
