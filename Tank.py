import random

class Tank():
    """
   Template of tanks
   """

    def __init__(self, model, speed, min_damage, max_damage, health, breach, armor):
        self.model = model
        self.speed = speed
        self.health = health
        self.damage = random.randint(min_damage, max_damage)
        self.armor = armor
        self.breach = breach

    def print_info(self):
        print(
            self.model + " имеет скорость " + self.speed + "км/ч " + "его hp - " + str(self.health) + "и урон " + str(
                self.damage))

    def health_down(self, enemy_damage):
        self.health -= enemy_damage  # self.health = self.health - enemy_damage
        print(
            "\n" + self.model + ": " + "Командир, по нам попали, у нас осталось " + str(self.health) + " единиц здоровья")

    def shot(self, enemy):
        if enemy.health <= 0:
            print("Экипаж танка " + enemy.model + "уничтожен")

        if self.breach <= enemy.armor:
                print("Броню противника не пробить")

        else:
            enemy.health_down(self.damage)
            print("\n" + self.model + ": " + "Точно в цель! У противника " + enemy.model + " осталось " + str(
                enemy.health) + " здоровья")
            print(self.damage)


tank1 = Tank("t-34", "30", 10, 50, 100, 40, 50)
tank2 = Tank("Tank", "100", 20, 50, 120, 30, 60)
tank2.shot(tank1)