import random
from print_speed import print_medium as pm 
from print_speed import print_slow as ps
from abc import ABC, abstractmethod


class Enemy: #cogs
    valid_levels = range(1, 13)
    max_health_by_level = {
            1: 7,
            2: 12,
            3: 16,
            4: 25,
            5: 37,
            6: 42,
            7: 69,
            8: 79,
            9: 94,
            10: 105,
            11: 120,
            12: 135
        }
    
    def __init__(self, level):
        self.health = self.max_health_by_level[level]
        self.attacks = []
        self.level = int(level)
        self.is_soaked = False
        self.soak_delay = False
        self.soak_duration = 0
        
    
    @property
    def cog_class(self):
        parent_class = self.__class__.__bases__[0]
        return parent_class.__name__ if parent_class != Enemy else self.__class__.__name__
    
    @classmethod
    def get_all_subclasses(cls):
        all_subclasses = []

        direct_subclasses = cls.__subclasses__()

        while direct_subclasses:
            subclass = direct_subclasses.pop()
            all_subclasses.append(subclass)
            direct_subclasses.extend(subclass.__subclasses__())

        return all_subclasses
        
    def apply_soak_effect(self, duration):
        self.is_soaked = True
        self.soak_duration = duration
        self.soak_delay = True
        
    def choose_random_attack(self):
        chosen_attack = random.choice(self.attacks)
        attack_name = chosen_attack ["name"]
        attack_damage = chosen_attack["damage"]
        hit_chance = chosen_attack["hit_chance"]
        
        
        return attack_name, attack_damage, hit_chance

    def attack(self): #this is the boolean that dictates whether the attack misses or not
        attack_name, attack_damage, hit_chance = self.choose_random_attack()
    
        if random.random() < hit_chance:
            return attack_name, attack_damage, True
        else:
            return attack_name, 0, False

class Bossbot(Enemy, ABC):
   
    cog_class="Bossbot"
    def __init__(self,level):
        super().__init__(level)
        
class Lawbot(Enemy, ABC):
    
    cog_class="Lawbot"
    def __init__(self,level):
        super().__init__(level)
        
class Cashbot(Enemy, ABC):
    
    cog_class="Cashbot"
    def __init__(self,level):
        super().__init__(level)
        
class Sellbot(Enemy, ABC):
   
    cog_class="Sellbot"
    def __init__(self,level):
        super().__init__(level)


                    
class Flunky(Bossbot):####any time you add new cog, need to populate the class list at the bottom.
    valid_levels = range(1, 6)
    type_name="Flunky"
    max_damage_by_level = {
        1: {"Clip on Tie": 1, "Pound key": 2, "Shred": 3},
        2: {"Clip on Tie": 2, "Pound key": 3, "Shred": 4},
        3: {"Clip on Tie": 2, "Pound key": 4, "Shred": 5},
        4: {"Clip on Tie": 3, "Pound key": 5, "Shred": 6},
        5: {"Clip on Tie": 3, "Pound key": 6, "Shred": 7} 
    }
    def __init__(self, level=None, area=None):

        super().__init__(level)
        self.setup_attacks(level)
        
   
    def setup_attacks(self, level): 
        self.attacks = []
        for attack_name, damage in self.max_damage_by_level[level].items():
            attack = {
                "name": attack_name, 
                "damage": damage,
                "hit_chance": 0.9 if attack_name == "Clip on Tie" else 0.8 if attack_name == "Pound key" else 0.65, 
                "phrases": [
                    "I think I'll tie you up.",
                    "No tie, no service.",
                    "Try this on for size."
                ] if attack_name == "Clip on Tie" else [
                    "Ring-a-ling - it's for you!",
                    "O.K. Toon, it's the pound for you.",
                    "Time to return some calls."
                ] if attack_name == "Pound key" else [
                    "I'm gonna shred you apart!",
                    "It's time for a document shredding party!",
                    "My shredder's ready to roll!"
                ]
            }
            self.attacks.append(attack)
            
        self.begin_battle_phrases = [
            "You've wandered into my territory.",
            "Prepare to face the Flunky!",
            "You won't escape my clutches!"
        ]

class Pencil_pusher(Bossbot):
    valid_levels = range(2, 7)
    type_name="Pencil Pusher"
    max_damage_by_level = {
            2: {"Fountain Pen": 2, "Write Off": 3, "Fill With Lead": 4},
            3: {"Fountain Pen": 2, "Write Off": 4, "Fill With Lead": 5},
            4: {"Fountain Pen": 3, "Write Off": 5, "Fill With Lead": 6},
            5: {"Fountain Pen": 3, "Write Off": 6, "Fill With Lead": 7},
            6: {"Fountain Pen": 4, "Write Off": 6, "Fill With Lead": 8} 
        }
    
    def __init__(self, level=None, area=None):
        
            
        super().__init__(level)
        self.setup_attacks(level)
        
    def setup_attacks(self, level):
        self.attacks = []
        for attack_name, damage in self.max_damage_by_level[level].items():
            attack = {
                "name": attack_name, 
                "damage": damage,
                "hit_chance": 0.9 if attack_name == "Fountain Pen" else 0.8 if attack_name == "Write Off" else 0.65, 
                "phrases": [
                    "Can you read my writing?.",
                    "Be prepared for some permanent damage.",
                    "You should change.",
                    "You're going to need a good dry cleaner.",
                    "Let's ink this deal.",
                    "Don't you hate when this happens?",
                    "I call this the plume of doom.",
                    "This fountain pen has such a nice font.",
                    "Here, I'll use my pen.",
                    "This is going to leave a stain.",
                    "There's a blot on your performance."
                ] if attack_name == "Fountain Pen" else [
                    "Time to balance the books.",
                    "Let me increase your losses.",
                    "You’re about to suffer some losses.",
                    "Let’s make the best of a bad deal.",
                    "I’ll shuffle your accounts around.",
                    "You must account for your losses.",
                    "I'm looking for some dividends.",
                    "This won't look good on your books.",
                    "You can forget about a bonus.",
                    "This is going to hurt your bottom line."
                ] if attack_name == "Write Off" else [
                    "Take that!",
                    "Take a memo on this!",
                    "Say hello to my little friend!"
                ]
            }
            self.attacks.append(attack)
            
        self.begin_battle_phrases = [
        "Careful, Toon. You can be easily erased.",
            "I'm No.2!",
            "So you want to push your luck?",
            "Careful, I may leave a mark."
        ]

class Yesman(Bossbot):
    valid_levels = range(3, 8)
    type_name="Yesman"
    max_damage_by_level = {
            3: {"Razzle Dazzle": 2, "Rubber Stamp": 4, "Tee Off": 5},
            4: {"Razzle Dazzle": 3, "Rubber Stamp": 5, "Tee Off": 6},
            5: {"Razzle Dazzle": 3, "Rubber Stamp": 6, "Tee Off": 7},
            6: {"Razzle Dazzle": 4, "Rubber Stamp": 6, "Tee Off": 8},
            7: {"Razzle Dazzle": 5, "Rubber Stamp": 7, "Tee Off": 9} 
        }
    def __init__(self, level=None, area=None):
        
        
        super().__init__(level)
        self.setup_attacks(level)
        
    def setup_attacks(self, level):
        self.attacks = []
        for attack_name, damage in self.max_damage_by_level[level].items():
            attack = {
                "name": attack_name, 
                "damage": damage,
                "hit_chance": 0.9 if attack_name == "Razzle Dazzle" else 0.8 if attack_name == "Rubber Stamp" else 0.65, 
                "phrases": [
                    "Read my lips.",
                    "How about these choppers?",
                    "Aren't I charming?",
                    "I'm going to wow you.",
                    "My dentist does excellent work.",
                    "Blinding aren't they?",
                    "Hard to believe these aren't real.",
                    "Shocking, aren't they?",
                    "I'm going to cap this off.",
                    "I floss after every meal.",
                    "Say Cheese!'"
                ] if attack_name == "Razzle Dazzle" else [
                    
                    "I always make a good impression.",
                    "It's important to apply firm and even pressure.",
                    "A perfect imprint every time.",
                    "I want to stamp you out.",
                    "You must be RETURNED TO SENDER.",
                    "You've been CANCELLED.",
                    "You have a PRIORITY delivery.",
                    "I'll make sure you RECEIVED my message.",
                    "You're not going anywhere - you have POSTAGE DUE.",
                    "I'll need a response ASAP."
                ] if attack_name == "Rubber Stamp" else [
                    
                    "You're not up to par.",
                    "Fore!",
                    "I'm getting teed off.",
                    "Caddie, I'll need my driver!",
                    "Just try and avoid this hazard.",
                    "Swing!",
                    "This is a sure hole in one.",
                    "You're in my fairway.",
                    "Notice my grip.",
                    "Watch the birdie!",
                    "Keep your eye on the ball!",
                    "Mind if I play through?'"
                ]
            }
            self.attacks.append(attack)
            
        self.begin_battle_phrases = [
            "You need some positive enforcement.",
            "I haven't been wrong yet.",
            "Want to meet? I say yes, anytime.",
            "I won't take no for an answer.",
            "I'll be sure to end this on a positive note.",
            "I'm positive you're not going to like this.",
            "I'm confirming our meeting time.",
            "I don't know the meaning of no."
        ]
        
class Micromanager(Bossbot):
    valid_levels = range(4, 9)
    type_name="Micromanager"
    max_damage_by_level = {
            
            4: {"Finger Wag": 3, "Buzz Word": 5, "Demotion": 6},
            5: {"Finger Wag": 3, "Buzz Word": 6, "Demotion": 7},
            6: {"Finger Wag": 4, "Buzz Word": 6, "Demotion": 8},
            7: {"Finger Wag": 4, "Buzz Word": 7, "Demotion": 9},
            8: {"Finger Wag": 5, "Buzz Word": 8, "Demotion": 10} 
        }
    
    def __init__(self, level=None, area=None):
        
    
        super().__init__(level)
        self.setup_attacks(level)
        
    def setup_attacks(self, level):
        self.attacks = []
        for attack_name, damage in self.max_damage_by_level[level].items():
            attack = {
                "name": attack_name, 
                "damage": damage,
                "hit_chance": 0.9 if attack_name == "Finger Wag" else 0.8 if attack_name == "Buzz Word" else 0.65, 
                "phrases": [
                    "Don't make me come over there.",
                    "We've been through this before.",
                    "I'm tired of repeating myself.",
                    "Now see here Toon.",
                    "Don't make me laugh.",
                    "I believe we've been over this.",
                    "I have told you a thousand times.",
                    "I think it's time you pay attention.",
                    "You have no respect for us Cogs.",
                    "Blah, Blah, Blah, Blah, Blah.",
                    "Am I going to have to separate you?",
                    "Don't make me stop this meeting."     
                ] if attack_name == "Finger Wag" else [
                    "Pardon me if I drone on.",
                    "You should B more careful.",
                    "See if you can dodge this swarm.",
                    "Careful, you’re about to get stung.",
                    "Can you catch on to this?",
                    "See if you can hum this Toon.",
                    "I'll 'B' perfectly clear.",
                    "Let me put in a good word for you.",
                    "Looks like you have a bad case of hives.",
                    "Have you heard the latest?"
                ] if attack_name == "Buzz Word" else [
                    "You're moving down the corporate ladder.",
                    "I'm sending you back to the Mail Room.",
                    "You're not going anywhere.",
                    "Time to turn in your nameplate.",
                    "You're in a dead end position.",
                    "This will go on your permanent record.",
                    "You're going down, clown."
                ]
            }
            self.attacks.append(attack)
            
        
        
        self.begin_battle_phrases = [
            "I'm going to get into your business!",
            "Sometimes big hurts come in small packages.",
            "No job is too small for me.",
            "I want the job done right, so I'll do it myself.",
            "You need someone to manage your assets.",
            "Oh good, a project.",
            "I could probably manage things better than my boss.",
            "Well, you've managed to find me.",
            "I think you need some managing.",
            "I'll take care of you in no time.",
            "I'm watching every move you make.",
            "Are you sure you want to do this?",
            "We're going to do this my way.",
            "I'm going to be breathing down your neck.",
            "I can be very intimidating.",
            "I've been searching for my growth spurt."
        ]
        
class Big_Cheese(Bossbot):
    valid_levels = range(8, 13)
    type_name="Big Cheese"
    max_damage_by_level = {
        8: {"Tee Off": 4, "Cigar Smoke": 5, "Power Trip": 8},
        9: {"Tee Off": 6, "Cigar Smoke": 7, "Power Trip": 10},
        10: {"Tee Off": 8, "Cigar Smoke": 9, "Power Trip": 12},
        11: {"Tee Off": 10, "Cigar Smoke": 11, "Power Trip": 14},
        12: {"Tee Off": 12, "Cigar Smoke": 13, "Power Trip": 16} 
    }
    def __init__(self, level=None, area=None):
        
        
        
        super().__init__(level)
        self.setup_attacks(level)
        
   
    def setup_attacks(self, level): 
        self.attacks = []
        for attack_name, damage in self.max_damage_by_level[level].items():
            attack = {
                "name": attack_name, 
                "damage": damage,
                "hit_chance": 0.75 if attack_name == "Tee Off" else 0.8 if attack_name == "Cigar Smoke" else 0.65, 
                "phrases": [
                    "I'm getting teed off.",
                    "Just try and avoid this hazard.",
                    "Fore!",
                    "Caddie, I'll need my driver!",
                    "Notice my grip.",
                    "Mind if I play through?",
                    "Watch the birdie!",
                    "Swing!",
                    "You're not up to par.",
                    "You're in my fairway.",
                    "Keep your eye on the ball!" 
                ] if attack_name == "Tee Off" else [
                    
                    "Another day, another dollar spent.",
                    "You can't even escape my secondhand smoke.",
                    "I always have the occasional cigar.",
                    "Take a breath of this.",
                    "Smoking is a dirty habit.",
                    "I'll quit tomorrow, I swear.",
                    "Gentlemen.",
                    "I need a good smoke.",
                    "These fumes are toxic.",
                    "It's a good day for me to have a smoke."
                ] if attack_name == "Cigar Smoke" else [
                    
                    "You look a little tripped up.",
                    "Sorry to trip you up there!",
                    "Power corrupts, especially in my hands!",
                    "Did you have a nice trip?",
                    "How was your trip?",
                    "Who's got the power now?",
                    "Now you see who's in power!",
                    "Nice trip, I guess I'll see you next fall.",
                    "Pack your bags, we're taking a little trip.",
                    "I am much more powerful than you.",
                    "You can't fight the power."
                ]
            }
            self.attacks.append(attack)
            
        
        
        self.begin_battle_phrases = [
            "I'm going to make Mozzarella outta ya.",
            "I've been told I'm very strong.",
            "You can call me Jack.",
            "Watch it, Toon. I can assign your expiration date.",
            "Ending you will be a Breeze.",
            "Watch out, I'm Gouda get ya.",
            "I'm swissly surprised you came to someone my level.",
            "Are you sure? I can be a real Muenster at times.",
            "Let's cut the cheesy lines and get down to business.",
            "Don't you think I've aged well?",
            "Stepping up the ladder? I'm a whiz at this game.",
            "Finally. I was afraid you were stringing me along.",
            "A Toon, you say? Teleme more.",
            "Grate timing, I was just about to send in my Flunkies.",
            "I hope I'm not too sharp for you."
        ]        
class Bottom_Feeder(Lawbot):
    valid_levels = range(1, 6)
    type_name="Bottom Feeder"
    max_damage_by_level = {
            1: {"Pick Pocket": 1, "Rubber Stamp": 2, "Shred": 3},
            2: {"Pick Pocket": 2, "Rubber Stamp": 3, "Shred": 4},
            3: {"Pick Pocket": 2, "Rubber Stamp": 4, "Shred": 5},
            4: {"Pick Pocket": 3, "Rubber Stamp": 5, "Shred": 6},
            5: {"Pick Pocket": 3, "Rubber Stamp": 6, "Shred": 7}   
        }
    def __init__(self, level=None, area=None):
        
        
        super().__init__(level)
        self.setup_attacks(level)
        
    def setup_attacks(self, level):
        self.attacks = []
        for attack_name, damage in self.max_damage_by_level[level].items():
            attack = {
                "name": attack_name, 
                "damage": damage,
                "hit_chance": 0.9 if attack_name == "Pick Pocket" else 0.8 if attack_name == "Rubber Stamp" else 0.65, 
                "phrases": [
                    "Let me check your valuables.",
                    "Hey, what's that over there?",
                    "Like taking candy from a baby.",
                    "What a steal.",
                    "I'll hold this for you.",
                    "Watch my hands at all times.",
                    "The hand is quicker than the eye.",
                    "There's nothing up my sleeve.",
                    "The management is not responsible for lost items.",
                    "Finder's keepers.",
                    "You'll never see it coming.",
                    "One for me, none for you.",
                    "Don't mind if I do.",
                    "You won't be needing this..."
                ] if attack_name == "Pick Pocket" else [
                    
                    "I always make a good impression.",
                    "It's important to apply firm and even pressure.",
                    "A perfect imprint every time.",
                    "I want to stamp you out.",
                    "You must be RETURNED TO SENDER.",
                    "You've been CANCELLED.",
                    "You have a PRIORITY delivery.",
                    "I'll make sure you RECEIVED my message.",
                    "You're not going anywhere - you have POSTAGE DUE.",
                    "I'll need a response ASAP."
                ] if attack_name == "Rubber Stamp" else [
                    
                    "I'm gonna shred you apart!",
                    "It's time for a document shredding party!",
                    "My shredder's ready to roll!"
                ]
            }
            self.attacks.append(attack)
            
        
        
        self.begin_battle_phrases = [
            "Oh goody, lunch time.",
            "I'm ready to feast!",
            "I'm a sucker for Toons.",
            "Let's talk about the bottom line.",
            "You'll find my talents are bottomless.",
            "I'd love to have you for lunch.",
            "I'd like some feedback on my performance.",
            "Perfect timing, I need a quick bite.",
            "Looks like you've hit rock bottom.",
            "Good, I need a little pick-me-up."
        ]
        
class Cold_Caller(Sellbot):
    valid_levels = range(1, 6)
    type_name="Cold Caller"
    max_damage_by_level = {
        1: {"Freeze Assets": 1, "Pound key": 2, "Hot Air": 3},
        2: {"Freeze Assets": 1, "Pound key": 2, "Hot Air": 4},
        3: {"Freeze Assets": 1, "Pound key": 3, "Hot Air": 6},
        4: {"Freeze Assets": 1, "Pound key": 4, "Hot Air": 8},
        5: {"Freeze Assets": 1, "Pound key": 5, "Hot Air": 10} 
    }
    def __init__(self, level=None, area=None):
        
        
        
        super().__init__(level)
        self.setup_attacks(level)
        

    def setup_attacks(self, level): 
        self.attacks = []
        for attack_name, damage in self.max_damage_by_level[level].items():
            attack = {
                "name": attack_name, 
                "damage": damage,
                "hit_chance": 0.9 if attack_name == "Freeze Assets" else 0.8 if attack_name == "Pound key" else 0.65, 
                "phrases": [
                    "Your assets are mine.",
                    "Do you feel a draft?",
                    "Hope you don't have plans.",
                    "This should keep you on ice.",
                    "There's a chill in the air.",
                    "Winter is coming early this year.",
                    "Are you feeling a little blue?",
                    "Let me crystallize my plan.",
                    "You're going to take this hard.",
                    "This should cause freezer burn.",
                    "I hope you like cold cuts.",
                    "I'm very cold blooded."
                ] if attack_name == "Freeze Assets" else [
                    
                    "Time to return some calls.",
                    "I'd like to make a collect call.",
                    "Ring-a-ling - it's for you!",
                    "I've been wanting to drop a pound or two.",
                    "I have a lot of clout.",
                    "This may cause a slight pounding sensation.",
                    "I'll just punch in this number.",
                    "Let me call up a little surprise.",
                    "I'll ring you up.",
                    "O.K. Toon, it's the pound for you."
                ] if attack_name == "Pound key" else [
                    
                    "We're having a heated discussion.",
                    "You're experiencing a heat wave.",
                    "I've reached my boiling point.",
                    "This should cause some wind burn.",
                    "I hate to grill you, but...",
                    "Always remember, where there's smoke, there's fire.",
                    "You're looking a little burned out.",
                    "Another meeting up in smoke.",
                    "Guess it's time to add fuel to the fire.",
                    "Let me kindle a working relationship.",
                    "I have some glowing remarks for you.",
                    "Air Raid!!!"
                ]
            }
            self.attacks.append(attack)
            
        self.begin_battle_phrases = [
            "Boy, did you get your wires crossed.",
            "I was hoping you'd answer my call.",
            "You rang?",
            "I'm going to cause a ringing sensation.",
            "This call is going to cost you.",
            "You've got big trouble on the line.",
            "Surprised to hear from me?",
            "Are you ready to accept my charges?",
            "This caller always collects.",
            "I'm one smooth operator.",
            "Hold the phone -- I'm here.",
            "Have you been waiting for my call?",
            "I always make my calls direct."
        ]
    
class Short_Change(Cashbot):
    valid_levels = range(1, 6)
    type_name="Short Change"
    max_damage_by_level = {
        1: {"Clip on Tie": 1, "Pick Pocket": 2, "Bounce Check": 3},
        2: {"Clip on Tie": 1, "Pick Pocket": 2, "Bounce Check": 5},
        3: {"Clip on Tie": 2, "Pick Pocket": 3, "Bounce Check": 7},
        4: {"Clip on Tie": 2, "Pick Pocket": 4, "Bounce Check": 9},
        5: {"Clip on Tie": 3, "Pick Pocket": 6, "Bounce Check": 11} 
    }
    def __init__(self, level=None, area=None):
        
        super().__init__(level)
        self.setup_attacks(level)
        
    def setup_attacks(self, level): 
        self.attacks = []
        for attack_name, damage in self.max_damage_by_level[level].items():
            attack = {
                "name": attack_name, 
                "damage": damage,
                "hit_chance": 0.9 if attack_name == "Clip on Tie" else 0.8 if attack_name == "Pick Pocket" else 0.65, 
                "phrases": [
                    "Better dress for our meeting.",
                    "You can't go OUT without your tie.",
                    "The best dressed Cogs wear them.",
                    "Try this on for size.",
                    "You should dress for success.",
                    "No tie, no service.",
                    "Do you need help putting this on?",
                    "Nothing says powerful like a good tie.",
                    "Let's see if this fits.",
                    "This is going to choke you up.",
                    "You'll want to dress up before you go OUT.",
                    "I think I'll tie you up."
                ] if attack_name == "Clip on Tie" else [
                    
                    "Let me check your valuables.",
                    "Hey, what's that over there?",
                    "Like taking candy from a baby.",
                    "What a steal.",
                    "I'll hold this for you.",
                    "Watch my hands at all times.",
                    "The hand is quicker than the eye.",
                    "There's nothing up my sleeve.",
                    "The management is not responsible for lost items.",
                    "Finder's keepers.",
                    "You'll never see it coming.",
                    "One for me, none for you.",
                    "Don't mind if I do.",
                    "You won't be needing this..."
                ] if attack_name == "Pick Pocket" else [
                    
                    "Ah, too bad, you're funless.",
                    "You have a payment due.",
                    "I believe this check is yours.",
                    "You owed me for this.",
                    "I'm collecting on this debt.",
                    "This check isn't going to be tender.",
                    "You're going to be charged for this.",
                    "Check this out.",
                    "This is going to cost you.",
                    "I'd like to cash this in.",
                    "I'm just going to kick this back to you.",
                    "This is one sour note.",
                    "I'm deducting a service charge."
                ]
            }
            self.attacks.append(attack)
            
        self.begin_battle_phrases = [
            "I'll be with you shortly.",
            "I'll make short work of you.",
            "You're about to have money trouble.",
            "I think you've been shorted.",
            "Let's make this a short stop.",
            "You're about to be overcharged.",
            "I have a short temper for Toons.",
            "I think you've come up short.",
            "This will be a short-term assignment.",
            "I'm going to Short Change you.",
            "You'll soon experience a shortfall."
        ]


def get_random_cog(area):
    MAX_RETRIES = 1000
    #print("All subclasses:", Enemy.get_all_subclasses()) #for debugging
    area_data = {
        "Loopy Lane": {
            "valid_range": range(1, 6),
            "level_probs": {1: 0.1, 2: 0.1, 3: 0.2, 4: 0.3, 5: 0.3},
            "class_probs": {"Sellbot": 0.1, "Cashbot": 0.1, "Lawbot": 0.1, "Bossbot":.7}
        },
        "Silly Street": {
            "valid_range": range(1, 6),
            "level_probs": {1: 0.3, 2: 0.375, 3: 0.2, 4: 0.1, 5: 0.025},
            "class_probs": {"Sellbot": 0.25, "Cashbot": 0.25, "Lawbot": 0.25,"Bossbot":.25}
        }
    }

    # Extract relevant data for the given area
    data = area_data.get(area)
    if not data:
        return None
    
    valid_range = data["valid_range"]
    level_probs = data["level_probs"]
    class_probs = data["class_probs"]

    enemy_subclasses = Enemy.get_all_subclasses()
    exclude_classes = [Sellbot, Cashbot, Lawbot, Bossbot]    #making the list choose actual cogs and not the parent class
    valid_cogs = [cog for cog in enemy_subclasses if set(cog.valid_levels).intersection(valid_range)and cog not in exclude_classes]
    
    #print(f"Valid cogs for {area}: {valid_cogs}")
    
    for _ in range(MAX_RETRIES):
            selected_class = random.choices(
                population=list(class_probs.keys()),
                weights=list(class_probs.values()),
                k=1
            )[0]

            selected_level = random.choices(
                population=list(level_probs.keys()),
                weights=list(level_probs.values()),
                k=1
            )[0]

            matching_cogs = [cog for cog in valid_cogs if cog.cog_class == selected_class and selected_level in cog.valid_levels]
            
            if matching_cogs:
                SelectedCog = random.choice(matching_cogs)
                return SelectedCog(level=selected_level)

        # If no matching cog was found after all retries
    print("Failed to find a matching cog after maximum retries!")
    return None
    


