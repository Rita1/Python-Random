class Baby:
    babies_made = 0

    def __new__(cls, *args, **kw):
        cls.babies_made = cls.babies_made + 1
        my_baby = super(Baby, cls).__new__(cls)
        return my_baby

    def __init__(self, name, is_male):
        self.name = name
        self.is_male = is_male

class AboutBabies:
    tify = Baby("Tify", False)
    tutu = Baby("Tutu", False)

ab = AboutBabies()
print(ab.tify.name)
print(ab.tutu.babies_made)