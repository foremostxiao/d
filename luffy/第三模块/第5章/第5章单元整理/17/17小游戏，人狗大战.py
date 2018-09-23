class Animal:
    def __init__(self,name,life_value,aggressivity):
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value
    def attack(self,enemy):
        enemy.life_value -= self.aggressivity
        print(f"{self.name},进攻了{enemy.name},敌方剩余生命值{enemy.life_value}")

class People(Animal):
    camp = '正方'
    def attack(self,enemy):
        super().attack(enemy)

class Dog(Animal):
    camp = '反方'

if __name__ == '__main__':
    print('--人狗大战游戏----')
    print('----请创建2个人和3条狗进行游戏---')

    peo = People('aa',100,20)
    peo2 = People('bb',120,20)
    dog = Dog('keke',100,20)
    dog2 =Dog('duole',120,15)
    dog3 = Dog('hashi',150,10)

    peo.attack(dog)