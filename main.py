import random
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

#Create black magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

#Create white magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

#Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]

player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},
                {"item": grenade, "quantity": 15}]

#Instatiation People
player1 = Person("Valos:", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Nick :", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Robot:", 3089, 174, 288, 34, player_spells, player_items)
enemy = Person("Magus:", 11200, 701, 525, 25, [], [])

players = [player1, player2, player3]

# print(player.generate_damage())
# print(player.generate_spell_damage(0))
# print(player.generate_spell_damage(1))

running = True
i = 0


print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("========================")

    print("\n\n")
    print("NAME                 HP                                      MP")
    for player in players:
        player.get_stats()
    print("\n")

    enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage.")

        if index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            #print("magic_choice = " + str(magic_choice))

            # if the user typed 0 go back to the upper menu
            if magic_choice == -1:
                #print("the user typed 0 go back to the upper menu")
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()


            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg) + " HP" + bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

        if index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1
            # if the user typed 0 go back to the upper menu
            if item_choice == -1:
                #print("the user typed 0 go back to the upper menu")
                continue

            item = player_items[item_choice]["item"]
            if  player_items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "None left..." + bcolors.ENDC)
                continue

            player_items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop) + " HP", bcolors.ENDC)
            elif item.type == "elixer":
                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)



    enemy_choice = 1
    enemy_damage = enemy.generate_damage()
    target = random.randint(0, 2)
    players[target].take_damage(enemy_damage)
    print("\nEnemy attacks " + players[target].name + "for", enemy_damage, "points of damage.")

    # print("-------------------------")
    # print("Enemy HP (Hit Points):", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You enemy has defited you!" + bcolors.ENDC)
        running = False
