# By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class.
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        return "deleted"

    def __call__(self):
        return ('yes??')

    def __getitem__(self, i):
        return self.my_dict[i]

    def __bytes__(self):
        return len(self)

    def __dir__(self):
        return ('__Str___, __len__, __call__, etc')

    def __bool__(self):
        if len(self) > 5:
            return True
        else:
            return False


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
print(action_figure.__bytes__())
print(action_figure.__dir__())
print(action_figure.__bool__())
print(action_figure == False)
