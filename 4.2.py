class Bird(object):
    def chirp(self,sound):

        print(sound)

    def set_color(self,color):

        self.color = color

summer = Bird()

summer.set_color("Yellow")

print(summer.color)

class Bird(object):

    def _init_(self,sound):

        self.sound = sound

        print("my sound is:")

    def chirp(self):

        print(self.sound)

summer = Bird("ji")

summer.chirp()