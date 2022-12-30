class Superli(list):
    def __init__(self, *args):
        self.li = [*args]

    def __len__(self):
        return 1000


li1 = Superli(1, 2, 3, 5)
print(len(li1))
print(li1.append(2))
print(li1)


# len

# append

# get
