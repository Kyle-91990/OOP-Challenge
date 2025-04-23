from pet import Pet

def main():
    # Create a new pet
    my_pet = Pet("Buddy", "Corgi")
    
    # Test basic functionalities
    print("Welcome to Virtual Pet Simulator! 🐾")
    print(my_pet.get_status())
    
    print("\nFeeding pet...")
    print(my_pet.eat())
    
    print("\nPlaying with pet...")
    print(my_pet.play())
    
    print("\nPet sleeping...")
    print(my_pet.sleep())
    
    print("\nTraining pet...")
    print(my_pet.train("sit"))
    print(my_pet.train("roll over"))
    print(my_pet.train("high five"))
    
    print("\nPlaying more...")
    print(my_pet.play())
    print(my_pet.play())
    
    print("\nShowing tricks...")
    print(my_pet.show_tricks())
    
    print("\nFinal status:")
    print(my_pet.get_status())

if __name__ == "__main__":
    main()
