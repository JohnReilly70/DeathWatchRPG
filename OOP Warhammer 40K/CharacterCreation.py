from SpaceMarineChapter import *


def main():
  UppChapSel = []
  Character = []
  while UppChapSel != 'Q':
    print("Welcome to Character Creation\n")
    ChapterList = "[B]lood Angels\nBlack [T]emplar\n[D]ark Angels\nStorm [W]ardens\n[S]pace Wolf\n "
    UserChapterSelect = input("Which Chapter would you like to select\n"
                              + ChapterList +
                              "else press [Q] to quit\n" )
    UppChapSel = UserChapterSelect.upper()

    if UppChapSel == 'Q':
      print("Good-Bye")
      break

    CharName = input("Name your Character: \n")

    if UppChapSel == 'B':
      Character = Blood_Angels(CharName)
    elif UppChapSel == 'T':
      Character = Black_Templars(CharName)
    elif UppChapSel == 'D':
      Character = Dark_Angels(CharName)
    elif UppChapSel == 'W':
      Character = Storm_Wardens(CharName)
    elif UppChapSel == 'S':
      Character = Space_Wolves(CharName)
    elif UppChapSel == 'Q':
      print("Good-Bye")
      break
    else:
      print("Enter a Corresponding Letter")
      continue

    print(Character)
    print("Movement is " + str(Character.Movement['run']))
    print("\nFate " + str(Character.Fate))
    print("\nAG " + str(Character.Characteristics['AG']))
    print("\nHp " + str(Character.HP))


if __name__ == "__main__":
    test = Blood_Angels('John')
    print( test.Characteristics['WS'], test.Name, test.Chapter, test)
    print("\n", test.Skills['Basic'])
    print("\n", test.Skills['Trained'])
    print("\n", test.Skills['+10%'])
##    LOOKHEREprint(test)
##    print(test.Characteristics)
    #main()
