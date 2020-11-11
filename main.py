from classes.game import Person, bcolors


magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 12, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]
player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

# print(player.generate_damage())
# print(player.generate_spell_damage(0))
# print(player.generate_spell_damage(1))

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("========================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())

    enemy_choice = 1
    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print("Enemy attacks for", enemy_damage, "Player HP", player.get_hp())