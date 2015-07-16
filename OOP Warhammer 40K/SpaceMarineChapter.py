import random

class Space_Marine():
    """
    Space_Marine is the Base class.
    __init__ input(self,name):
    sets up all the required Variables:
    Name,Chapter,Speciality,Characteristics,Exp,HP,SKills,TalentTraits,Fate,Movement.

    Methods to set all the Values:
    CharacteristicCalc,MovementCalc,FateCalc,HPCalc
    """

    def __init__(self, Name):
        self.Name = Name
        self.Chapter = ""
        self.Speciality = ""
        self.Characteristics = {'WS': 0,'BS': 0,'S': 0,'T': 0,'AG': 0,
                                'INT': 0,'PER': 0,'WP': 0,'FEL': 0}
        self.Exp = 1000
        self.HP = 0
        self.Skills = []
        self.TalentTraits = []
        self.Fate = 0
        self.Movement = []

        #Running Methods to Generate the Players Chars, Movement, Fate, HP
        self.CharacteristicCalc()
        self.FateCalc()
        self.HPCalc()
        self.MovementCalc()
        self.SkillSetUp()
        self.TalentTraitsSetUp()



    def __str__(self):
        return ("\n\nThis is {} of the Space Marine Chapter, {}.\nThey are a {}".format(self.Name, self.Chapter, self.Speciality))


    def SkillSetUp(self):

        SpaceMarineSkills = {}
        
        SpaceMarineSkills.update({'Basic':['Barter(Fel)','Carous(T)','Charm(Fel)','Commander(Fel)',
                            'Contortionist(Ag)','Deceive(Fel)','Disguise(Fel)','Dodge(Ag)','Evaluate(**Int)',
                            'Gamble(Int)','Inquiry(Fel)','Intimidate(S)','Logic(Int)','Scrutiny(Per)','Search(Per)',
                            'Swim(S)']})
                            
        SpaceMarineSkills.update({'Trained':['Awareness(Per)',{'Ciphers(Int)': 'Chapter Runes'},'Climb(S)',
                                {'Common Lore(Int)':['Adeptus Astartes','DeathWatch','Imperium','War']},
                                'Concealment(Ag)',{'Drive(Ag)':['Ground Vehicles']},
                                {'Forbidden Lore(Int)':['Xenos']},'Literacy(Int)',
                                {'Speaking Language(Int)':['High Gothic','Low Gothic']},{'Tactics(Int)':['']},'Tracking(Int)']})

        SpaceMarineSkills.update({'+10%':[]})

        SpaceMarineSkills.update({'+20%':[]})

        self.Skills = SpaceMarineSkills



    def TalentTraitsSetUp(self):
        """
        Sets Up Talents & Traits of the Space Marine.

        IF
        Space Wolf Chapter Character it will add addition talent HeightenedSenses["Smell"]
        ELSE
        TalentTraits is Generic SpaceMarineTalents
        """
        SpaceMarineTalents = ['Ambidextrous', 'Astartes Weapon Training', 'Bulging Biceps', {'HeightenedSenses': ['Hearing', 'Sight']},
        'Killing Strike', 'Nerves of Steel', 'Quick Draw', {'Resistance': ['Psychic Powers']}, 'True Grit', 'Unarmed Master',
        {'UnnaturalStrength': 2}, {'UnnaturalToughness': 2}]

        if self.Chapter == "Space Wolves":
          self.TalentTraits['HeightenedSenses'] = SpaceMarineTalents['HeightenedSenses'].extend(['Smell'])
        else:
          self.TalentTraits = SpaceMarineTalents



    def MovementCalc(self):
        """
        Calculates Movement Distances
        Movement Table Ref DeathWatch Core RuleBook Page 27
        """
        if self.Characteristics['AG'] <= 10:
          self.Movement = {'half':0.5, 'full':1, 'charge':2, 'run':3}
        else:
          AbilityBonus = self.Characteristics['AG']/10
          AbilityBonus = int(AbilityBonus)
          self.Movement = {'half':AbilityBonus, 'full':AbilityBonus*2 ,'charge':AbilityBonus*3 ,'run':AbilityBonus*6}

    def FateCalc(self):
        """
        Calculates the Fate Points.
        Random Integer from 1 - 10.
        Table ({1-7 Roll Value: 3 Fate Points},{8-9: 4},{10: 5})
        """
        FateRoll = random.randint(1,10)

        if FateRoll == 10:
          self.Fate = 5
        elif FateRoll > 7:
          self.Fate = 4
        else:
          self.Fate = 3

    def HPCalc(self):
        """
        Calculates the HP based off of the roll 1d5 + 18
        """
        HPRoll = random.randint(1,5)
        self.HP = 18 + HPRoll

    def CharacteristicCalc(self,Option = ''):
        """
        Loops through self.Characteristics generatings the percentage.
        Equal is 30 + 2d10 per each Characteristic.
        """

        for Char in self.Characteristics:
          CharacteristicRoll = random.randint(1,10) + random.randint(1,10)
          self.Characteristics[Char] = 30 + CharacteristicRoll
        print("WS: {}\nBS: {}\nS: {}\nT: {}\nAg: {}\nInt: {}\nPer: {}\nWP: {}\nFel: {}\n".format(
                self.Characteristics['WS'],self.Characteristics['BS'],self.Characteristics['S'],self.Characteristics['T'],
                self.Characteristics['AG'],self.Characteristics['INT'],self.Characteristics['PER'],
                self.Characteristics['WP'],self.Characteristics['FEL']))
        ReRoll = input("Re-Roll One Characteric or None\n\nType Characteric as shown above or None")
        ReRoll.upper()
        if ReRoll == 'NONE' or ReRoll == '':
            print("No Re-Roll Selected")
        # NEED TO MAKE A CHECK THAT IT IS A LEGIT CHARACTERISTIC ELSE GO THROUGH LOOP AGAIN
        elif ReRoll ==









class Blood_Angels (Space_Marine):

    def __init__(self, *args, **kwargs):
        Space_Marine.__init__(self, *args)
        self.Chapter = "Blood Angels"
        self.SkillSetUp()
        self.TalentTraitsSetUp()
        self.Characteristics['WS'] += 5
        self.Characteristics['AG'] += 5

class Black_Templars (Space_Marine):

    def __init__(self, *args, **kwargs):
        Space_Marine.__init__(self, *args)
        self.Chapter = "Black Templars"
        self.SkillSetUp()
        self.TalentTraitsSetUp()
        self.Characteristics['WS'] += 5
        self.Characteristics['WP'] += 5

class Dark_Angels (Space_Marine):

    def __init__(self, *args, **kwargs):
        Space_Marine.__init__(self, *args)
        self.Chapter = "Dark Angels"
        self.SkillSetUp()
        self.TalentTraitsSetUp()
        self.Characteristics['BS'] += 5
        self.Characteristics['INT'] += 5

class Storm_Wardens (Space_Marine):

    def __init__(self, *args, **kwargs):
        Space_Marine.__init__(self, *args)
        self.Chapter = "Storm Wardens"
        self.SkillSetUp()
        self.TalentTraitsSetUp()
        self.Characteristics['S'] += 5
        self.HP += 2

class Space_Wolves(Space_Marine):

    def __init__(self, *args, **kwargs):
        Space_Marine.__init__(self, *args)
        self.Chapter = "Space Wolves"
        self.SkillSetUp()
        self.TalentTraitsSetUp()
        self.Characteristics['WS'] += 5
        self.Characteristics['FEL'] += 5
        self.Skills = "Counter Attack"

#TO UPDATE DUE TO SELECTION CHOICE OF Characteristics
# class Ultramarines(Space_Marine):
#
#  def __init__(self, *args, **kwargs):
#     Space_Marine.__init__(self, *args)
#     self.Chapter = "Ultramarines"
#     self.Characteristics[] += 5
#     self.Characteristics[] += 5
