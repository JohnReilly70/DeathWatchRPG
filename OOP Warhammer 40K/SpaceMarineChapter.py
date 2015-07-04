import random

class Space_Marine():



  
  def __init__(self, name):
    self.name = name
    self.Chapter = ""
    self.Speciality = ""
    self.Characteristics = {'WS': 0,'BS': 0,'S': 0,'T': 0,'AG': 0,
                            'INT': 0,'PER': 0,'WP': 0,'FEL': 0}
    self.exp = 1000
    self.HP = 0
    self.skills = []
    self.TalentTraits = []
    self.Fate = 0
    self.Movement = []

    #Running Methods to Generate the Players Chars, Movement, Fate, HP
    self.CharacteristicCalc()
    self.MovementCalc()
    self.FateCalc()
    self.HPCalc()
    
  def __str__(self):
    return ("\n\nThis is " + self.name + " of the Space Marine Chapter, " + self.Chapter + ".\n"
            + "They are a " + self.Speciality)

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
    
    HPRoll = random.randint(1,5)
    self.HP = 18 + HPRoll

  def CharacteristicCalc(self):
    for Char in self.Characteristics:     
      CharacteristicRoll = random.randint(1,10) + random.randint(1,10)
      self.Characteristics[Char] = 30 + CharacteristicRoll
      


  
    
    

class Blood_Angels (Space_Marine):
  
  def __init__(self, *args, **kwargs):
    Space_Marine.__init__(self, *args)
    self.Chapter = "Blood Angels"
    self.Characteristics['WS'] += 5
    self.Characteristics['AG'] += 5

class Black_Templars (Space_Marine):

  def __init__(self, *args, **kwargs):
    Space_Marine.__init__(self, *args)
    self.Chapter = "Black Templars"
    self.Characteristics['WS'] += 5
    self.Characteristics['WP'] += 5

class Dark_Angels (Space_Marine):

  def __init__(self, *args, **kwargs):
    Space_Marine.__init__(self, *args)
    self.Chapter = "Dark Angels"
    self.Characteristics['BS'] += 5
    self.Characteristics['INT'] += 5

class Storm_Wardens (Space_Marine):

  def __init__(self, *args, **kwargs):
    Space_Marine.__init__(self, *args)
    self.Chapter = "Storm Wardens"
    self.Characteristics['S'] += 5
    self.HP += 2

class Space_Wolves(Space_Marine):

 def __init__(self, *args, **kwargs):
    Space_Marine.__init__(self, *args)
    self.Chapter = "Space Wolves"
    self.Characteristics['WS'] += 5
    self.Characteristics['FEL'] += 5
    self.skills = "Counter Attack"
