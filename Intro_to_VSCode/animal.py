class Animal:
    
    def __init__(self, type, sound) -> None:
        self.type = type
        self.sound = sound
        self.x = 3
    
    def make_sound(self):
        return f"The {self.type} makes a sound {self.sound}"
    
    def x(self):
        print("Hello")
        
    