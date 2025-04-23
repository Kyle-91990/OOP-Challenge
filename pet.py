class Pet:
    def __init__(self, name, pet_type="Dog"):
        self.name = name
        self.type = pet_type
        self.hunger = 50
        self.energy = 100
        self.happiness = 50
        self.tricks = []
        self.mood = "😊"
        
    def get_status(self):
        self._update_mood()
        return f"{self.name} the {self.type}\n" \
               f"Mood: {self.mood}\n" \
               f"Hunger: {'🍖' * (self.hunger // 20)}\n" \
               f"Energy: {'⚡' * (self.energy // 20)}\n" \
               f"Happiness: {'❤️' * (self.happiness // 20)}"
    
    def eat(self):
        self.hunger = max(0, self.hunger - 30)
        self.energy = min(100, self.energy + 10)
        return f"{self.name} is eating... nom nom 🍽️"
    
    def play(self):
        if self.energy < 20:
            return f"{self.name} is too tired to play... 😴"
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 20)
        self.hunger = min(100, self.hunger + 10)
        return f"{self.name} is playing... woo! 🎾"
    
    def sleep(self):
        self.energy = 100
        self.hunger = min(100, self.hunger + 20)
        return f"{self.name} is sleeping... zzz 💤"
    
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(100, self.happiness + 10)
            self.energy = max(0, self.energy - 15)
            return f"{self.name} learned {trick}! 🌟"
        return f"{self.name} already knows {trick} 📚"
    
    def show_tricks(self):
        if not self.tricks:
            return f"{self.name} doesn't know any tricks yet 😢"
        return f"{self.name}'s tricks: " + ", ".join(self.tricks) + " 🎯"
    
    def _update_mood(self):
        if self.happiness > 80:
            self.mood = "🤩"
        elif self.hunger > 80:
            self.mood = "😫"
        elif self.energy < 20:
            self.mood = "😴"
        else:
            self.mood = "😊"
