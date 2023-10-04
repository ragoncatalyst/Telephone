import json
import random

class Character:
    def __init__(self, name, health, attack_power, skills):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.skills = skills

    def attack(self, other):
        other.health -= self.attack_power

    def use_skill(self, skill_name, other):
        if skill_name in self.skills:
            other.health -= self.skills[skill_name]
        else:
            print(f'{self.name} does not know the skill {skill_name}!')

class Pet:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

class Game:
    def __init__(self, player, enemy, player_pets):
        self.player = player
        self.enemy = enemy
        self.player_pets = player_pets

    def print_status(self):
        print('----------------------')
        print(f'⛑️ 玩家：{self.player.name}，生命值：{self.player.health}')
        print(f'⛑️ 敌人：{self.enemy.name}，生命值：{self.enemy.health}')
        print(f'⛑️ 宠物：{", ".join([pet.name for pet in self.player_pets])}')
        print('----------------------')

    def start(self):
        while self.player.health > 0 and self.enemy.health > 0:
            print()
            self.print_status()
            target = random.choice([self.player] + self.player_pets)
            self.enemy.attack(target)
            # https://emojipedia.org/
            print(f'💀 > 敌人[{self.enemy.name}]开始攻击')
            print(f'攻击：[{self.enemy.name}] 攻击了 [{target.name}]!')
            print(f'🥷 > 玩家[{self.player.name}]开始攻击')
            skills = list(self.player.skills.keys())
            for i, skill in enumerate(skills, 1):
                print(f'  [{i}] {skill}')
            skill_choice = -1
            while skill_choice < 1 or skill_choice > len(skills):
                print('  选择一个技能[1, 2, ...]：')
                skill_choice = int(input())
            self.player.use_skill(skills[skill_choice - 1], self.enemy)
            print(f'🗡️ 攻击：[{self.player.name}] 使用 [{skills[skill_choice - 1]}] 攻击了 [{self.enemy.name}]!')

        if self.player.health <= 0:
            print(f'🏁🏁🏁 游戏结束！[{self.player.name}]你输了。')
        else:
            print(f'✨✨✨ 游戏结束！[{self.player.name}]你赢了。')

def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)

config = load_config('config.json')

player = Character(config['player']['name'], config['player']['health'], config['player']['attack_power'], config['player']['skills'])
enemy = Character(config['enemy']['name'], config['enemy']['health'], config['enemy']['attack_power'], config['enemy']['skills'])
player_pets = [Pet(pet['name'], pet['health'], pet['attack_power']) for pet in config['player']['pets']]

game = Game(player, enemy, player_pets)
game.start()
