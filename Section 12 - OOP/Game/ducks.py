class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee, this is fun")
        elif self.ratio ==1:
            print("This is hard work, but i'm flying")
        else:
            print("I think ill just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle,Waddle,Waddle,")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack, Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle,Waddle, I waddle too")

    def swim(self):
        print("Come on in, it's a bit chilly here")

    def quack(self):
        print("Are you 'avin' a larf? I'm penguin!")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    # percy=Penguin()
    # test_duck(percy)