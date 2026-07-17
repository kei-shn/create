class Data:
    def __init__(self, pet, name, birthday, address, favsong, motivation, support, nickname):
        self.pet = pet
        self.name = name
        self.birthday = birthday
        self.address = address
        self.favsong = favsong
        self.motivation = motivation
        self.support = support
        self.nickname = nickname
        
    def display_info(self):
        
        print("=" * 75)
        print(" ༶•┈┈⛧┈♛ MY TIME TO SHINE ♛┈⛧┈┈•༶ ")
        print("=" * 75)
        
        print()
        print("     What I am???    ")
        print(f"      {self.pet}     ") 
        
        print()
        print("      My Identity    ")
        print(f" Name       : {self.name} ")
        
        print()
        print("       Codename      ")
        print(f" Nickname   : {self.nickname} ")
        
        print()
        print("   When I was born?  ")
        print(f" Birthday   : {self.birthday} ")
        
        print()
        print("   Where do I live?  ")
        print(f" Address    : {self.address} ")
        
        print()
        print("     ♡🎧  |◁   II   ▷|  ↺      ")
        print(f" Favsong    : {self.favsong} ")
        
        print()
        print("   What makes me motivate?   ")
        print(f" Motivation : {self.motivation} ")
        
        print()
        print("   Support? like Healer or Tank??   ")
        print(f" Support    : {self.support} ")
        
        print("=" * 75)
        print("     WAIT FOR THE RIGHT TIME (≧∇≦)/   ")
        print("=" * 75)
        
        
MyProfile = Data(
    "🐶 🐶 🐶",
    "Dominic Valencia",
    "08/05/2006",
    "Brgy. Tagbac Sur, Oton, Iloilo",
    "Musika by Doniela, FAKE IT by IZNA",
    "I want to graduate and help my family finance and travel to Japan because it is my dream destination. ",
    "To learn more about new programming language and how can i create my own project with new programming language. ",
    "Dom"
)  

MyProfile.display_info()
