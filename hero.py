import os
class ability(object):

    def __init__(self,**kwargs):

        if 'name' in kwargs:
            self.name = kwargs['name']
        else:
            self.name = None

        if 'description' in kwargs:
            self.description = kwargs['description']
        else:
            self.description = {}

        self._static = False

    def freeze(self):
        self._static = True

    def unfreeze(self):
        self._static = False

    def isFrozen(self):
        return self._static

class hero(object):

    def __init__(self,**kwargs):
        """
        Initialize hero
        """

        #Initialize null identifiers
        if 'name' in kwargs:
            self.name = kwargs['name']
        else:
            self.name = None
        self._id = None
        self.icon = None


        #Initialize all valid abilities to None
        self.lmbAbility = ability()
        self.rmbAbility = ability()
        self.qAbility = ability()
        self.eAbility = ability()
        self.rAbility = ability()


    def setAbility(self,tag,ability):

        if hasattr(self,tag+'Ability'):
            if not getattr(self,tag+'Ability').isFrozen():
                setattr(self,tag+'Ability',ability)
            else:
                print("WARNING: Ability "+tag+"Ability for hero "+self.name+" is frozen and cannot be changed!\n")
        else:
            raise KeyError("Ability type "+tag+" not recognised! \n")


    def getAbility(self,tag):

        try:
            return getattr(self,tag+'Ability')
        except AttributeError:
            print("Ability type "+tag+" not recognised! Returning None. \n")
            return None


def test_hero_init():

    test_hero = hero(name='test')
    print(test_hero.name)

def test_set_ability():
    test_hero = hero(name='test_hero')
    test_ability = ability(name='test_ability')
    print(test_hero.name)
    print(test_ability.name)
    print(test_hero.lmbAbility.name)
    test_hero.setAbility('lmb',test_ability)
    print(test_hero.lmbAbility.name)









def get_current_hero_register(root_path):
    import csv
    N_heroes = 0
    register = {}
    names = []
    with open(os.path.join(root_path, 'curent_hero_list.csv'),'rU') as f:

        reader = csv.reader(f)
        head = reader.next() #Skip first row
        ability_tags = head[1:]
        for row in reader:

            name = row[0]
            abilities = row[1:]
            names.append(name)
            this_hero = hero(name=name)
            for i in range(5):
                this_ability = ability(name=abilities[i])
                this_hero.setAbility(ability_tags[i].lower(),this_ability)

            register[this_hero.name] = this_hero
            N_heroes += 1

    return N_heroes,register,names





if __name__=='__main__':

    test_hero_init()
    test_set_ability()
    N,hero_register = get_current_hero_register('')
    print(N)
    print(hero_register)

    for hero in hero_register:
        print(hero)
        print(hero_register[hero].lmbAbility.name,hero_register[hero].lmbAbility.description)
    