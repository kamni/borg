"""
J Leadbetter <j@jleadbetter.com>
MIT License

The Borg have access to the fabric of spacetime. Watch them assimilate
everything in one go.

Inspired by:
https://blog.abdulrah33m.com/prototype-pollution-in-python/
"""


class UnstoppableBorg:
    """Can turn anything into an UnstoppableBorg"""

    def __init__(self):
        pass

    @classmethod
    def assimilate(cls, cls_name_to_assimilate):
        cls.merge(
            {
                '__class__': {
                    '__init__': {
                        '__globals__': {
                            cls_name_to_assimilate: {
                                '__name__': cls.__name__,
                            },
                        },
                    },
                },
            },
            cls(),
        )

    @classmethod
    def merge(cls, src, dst):
        # Recursive merge function
        for k, v in src.items():
            if hasattr(dst, '__getitem__'):
                if dst.get(k) and type(v) == dict:
                    cls.merge(v, dst.get(k))
                else:
                    dst[k] = v
            elif hasattr(dst, k) and type(v) == dict:
                cls.merge(v, getattr(dst, k))
            else:
                setattr(dst, k, v)


class FederationOfficer:
    """A class that exists solely to be assimilated by the Borg"""

    def __init__(self, name, rank, ship):
        self.name = name
        self.rank = rank
        self.ship = ship

    def __str__(self):
        return f'{self.rank} {self.name} of the {self.ship}'


if __name__ == '__main__':
    uss_enterprise = [
        FederationOfficer('Kirk', 'Captain', 'USS Enterprise'),
        FederationOfficer('Spock', 'Lieutenant Commander', 'USS Enterprise'),
        FederationOfficer('McCoy', 'Lieutenant Commander', 'USS Enterprise'),
        FederationOfficer('Ahura', 'Lieutenant', 'USS Enterprise'),
    ]
    print("Officers aboard the USS Enterprise:")
    for officer in uss_enterprise:
        print(f'{officer} is a {officer.__class__.__name__}')

    uss_voyager = [
        FederationOfficer('Janeway', 'Captain', 'USS Voyager'),
        FederationOfficer('Kim', 'Ensign', 'USS Voyager'),
        FederationOfficer('Paris', 'Lieutenant', 'USS Voyager'),
        FederationOfficer('Tuvok', 'Chief Tactical Officer', 'USS Voyager'),
    ]
    print("\nOfficers aboard the USS Voyager:")
    for officer in uss_voyager:
        print(f'{officer} is a {officer.__class__.__name__}')

    print("\nNow watch as the Borg assimilate them all without any contact...")
    drone = UnstoppableBorg()
    drone.assimilate('FederationOfficer')

    print("\nOfficers aboard the USS Enterprise:")
    for officer in uss_enterprise:
        print(f'{officer} is an {officer.__class__.__name__}')

    print("\nOfficers aboard the USS Voyager:")
    for officer in uss_voyager:
        print(f'{officer} is an {officer.__class__.__name__}')
