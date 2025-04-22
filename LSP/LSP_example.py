class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        return "Flying"

class Ostrich(Bird):
    def run(self):
        return "Running fast!"

def let_bird_fly(bird: FlyingBird):
    print(bird.fly())

let_bird_fly(FlyingBird())
