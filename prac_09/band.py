"""Band class for CP1404"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty members list"""
        self.name = name
        self.members = []

    def __repr__(self):
        """Return a string representation of a Band"""
        print("Str")
        return f"{self.name} ({str(self.members)})"

    def add(self, member):
        """Add another member to the band's members"""
        self.members.append(member)

    def __iter__(self):
        return self

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        for member in self.members:
            if member.instruments:
                print(f"{member.name} is playing: {member.instruments[0]}")
            if not member.instruments:
                print(f"{member.name} needs an instrument!")
