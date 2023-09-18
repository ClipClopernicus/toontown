import random
import Enemy
class Area:
    def __init__(self,name):
        self.name = name
        
class Street(Area):
    def __init__(self, name, cogs, cog_classes, buildings):
        super().__init__(name)
        self.cogs = cogs
        self.buildings = buildings
        self.cog_classes = cog_classes
    
    def spawn_random_cog(self):
        cog = Enemy.get_random_cog(self.name)
        self.cogs.append(cog)
        
    def display_choices(self): #displays the choices to fight cogs or enter buildings on a street
        choices = []
        for cog in self.cogs:
            choices.append(f"Fight the {cog.category} : {cog.type_name} (level {cog.level})")
        
        for building in self.buildings:
            choices.append(f"Enter the {building}")
    
        for i, choice in enumerate(choices):
            print(f"{i + 1}. {choice}")
            #display_choices(choices)
            print()
        
        return choices
    
        
class Playground(Area):
    def __init__(self, name, amenities):
        super().__init__(name)
        self.amenities = amenities # list of amenities availalbe in the playground    
    