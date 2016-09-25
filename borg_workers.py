"""
J Leadbetter <jleadbet@gmail.com>
MIT License

An exploration of multiple levels of shared attributes. In this case, the
WorkerBorg retains both shared attributes with the collective and shared
attributes with its unit. It also knows its own number within the unit.
"""

from __future__ import print_function


class WorkerBorg(object):
    """
    Borg class with distinct shared attributes between collective and unit.

    An instance of this class maintains a record of its own identity within the
    unit (e.g., 'Fourth' of Twelve); a record of its unit and unit's mission
    that is shared among all members of the unit; and a shared overall memory
    with the collective.
    """

    __shared__ = {}
    __work_units__ = set()

    def __init__(self, number, of_total, unit, mission):
        self.number = number
        tmp_units = list(self.__work_units__)

        # We need to create this temporarily to avoid an AttributeError, even
        # if we're going to override it once the worker is assimilated
        self.__unit_shared__ = {'unit': unit}

        try:
            unit_member = tmp_units.pop(tmp_units.index(self))
            self.__unit_shared__ = unit_member.__unit_shared__

            # We need to set the mission and of_total after joining the unit
            # so everyone gets the update
            self.of_total = of_total
            self.mission = mission
        except ValueError:
            # First Borg in the unit
            self.of_total = of_total
            self.mission = mission
            self.__work_units__.add(self)

    def __hash__(self):
        return hash(self.unit)

    def __eq__(self, other):
        return self.unit == other.unit

    def __str__(self):
        return 'Borg {} of {}, {}'.format(self.number, self.of_total, self.unit)

    def __getattribute__(self, name):
        if name in ('of_total', 'unit', 'mission'):
            unit_memory = super(WorkerBorg, self).__getattribute__(
                '__unit_shared__'
            )
            return unit_memory[name]
        else:
            try:
                collective_memory = super(WorkerBorg, self).__getattribute__(
                    '__shared__'
                )
                return collective_memory[name]
            except (AttributeError, KeyError):
                # There are a few attributes that a WorkerBorg retains for
                # itself and don't come from the __shared__ attributes
                return super(WorkerBorg, self).__getattribute__(name)

    def __setattr__(self, name, value):
        if name in ('number', '__unit_shared__', '__shared__'):
            super(WorkerBorg, self).__setattr__(name, value)
        elif name in ('of_total', 'unit', 'mission'):
            self.__unit_shared__[name] = value
        else:
            self.__shared__[name] = value


class TertiaryAdjunctUnimatrix01(WorkerBorg):
    """WorkerBorg with mission: Assimilate the Bajorans"""

    def __init__(self, number, of_total):
        unit = 'Tertiary Adjunct of Unimatrix 01'
        mission = 'Assimilate the Bajorans.'
        super(TertiaryAdjunctUnimatrix01, self).__init__(
            number, of_total, unit, mission
        )


class QuarternaryAdjunctUnimatrix02(WorkerBorg):
    """WorkerBorg with mission: Assimilate the Ferengi"""

    def __init__(self, number, of_total):
        unit = 'Quarternary Adjunct of Unimatrix 02'
        mission = 'Assimilate the Ferengi.'
        super(QuarternaryAdjunctUnimatrix02, self).__init__(
            number, of_total, unit, mission
        )


if __name__ == '__main__':
    borg1 = TertiaryAdjunctUnimatrix01('Seven', 'Nine')
    borg1.slogan = 'We are Borg. Lower your shields and surrender your ships.'
    borg2 = TertiaryAdjunctUnimatrix01('Nine', 'Nine')

    print(borg1)
    print('The first Borg says: {}'.format(borg1.slogan))
    print(borg2)
    print('The second Borg also says: {}'.format(borg2.slogan))
    print('The first Borg still retains its identity: {}'.format(borg1))
    print('But they share the same mission:\n{}\n{}'.format(
        borg1.mission, borg2.mission
    ))

    borg3 = QuarternaryAdjunctUnimatrix02('First', 'Five')

    print(borg3)
    print('The third Borg also says: {}'.format(borg3.slogan))
    print('But its mission is: {}'.format(borg3.mission))
