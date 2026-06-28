from code.Npc import Npc
from code.Potion import Potion
from code.ShotEnemy import ShotEnemy
from code.ShotPlayer import ShotPlayer
from code.Const import DISTANCE_ATTACK, ENTITY_DAMAGE, DAMAGE_FRAME, HEALTH_VARIABLE, ENERGY_VARIABLE
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
import random
import pygame as py


class EntityMediator:

    @staticmethod
    def __verify_player_distance_enemy(ent1: Entity, ent2: Entity, level_text_actual: int):
        valid_interaction = False
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        if isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True
        if isinstance(ent1, Player) and isinstance(ent2, Npc):
            valid_interaction = True
        if isinstance(ent1, Npc) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            difference_distances = abs(ent1.rect.centerx - ent2.rect.centerx)
            if difference_distances < 1000:
                if isinstance(ent2, Enemy):
                    if not ent2.is_dead and ent2.health > 0:
                        if difference_distances <= DISTANCE_ATTACK[ent2.name]:
                            if ent2.name in ('Boss1', 'Boss3'):
                                EntityMediator.__alter_boss_attack(ent2)
                            else:
                                ent2.is_attack1 = True
                            ent2.act = False
                        else:
                            ent2.is_attack1 = False
                            ent2.act = True
                        ent2.is_idle = False
                        ent2.act = True
                        if ent1.rect.centerx > ent2.rect.centerx:
                            ent2.direction = 'R'
                        if ent1.rect.centerx < ent2.rect.centerx:
                            ent2.direction = 'L'
                        if ent2.name in ('Boss1', 'Boss2_1','Boss2_2', 'Boss3'):
                            ent2.active_bar_health = True
                if isinstance(ent1, Enemy):
                    if not ent1.is_dead and ent1.health > 0:
                        if difference_distances <= DISTANCE_ATTACK[ent1.name]:
                            if ent1.name in ('Boss1', 'Boss3'):
                                EntityMediator.__alter_boss_attack(ent1)
                            else:
                                ent1.is_attack1 = True
                            ent1.act = False
                        else:
                            ent1.is_attack1 = False
                            ent1.act = True
                        ent1.is_idle = False
                        ent1.act = True
                        if ent2.rect.centerx > ent1.rect.centerx:
                            ent1.direction = 'R'
                        if ent2.rect.centerx < ent1.rect.centerx:
                            ent1.direction = 'L'
                        if ent1.name in ('Boss1', 'Boss2_1','Boss2_2', 'Boss3'):
                            ent1.active_bar_health = True

                if isinstance(ent1, Npc):
                    if difference_distances <= DISTANCE_ATTACK[ent1.name]:
                        if ent1.name == 'Player1' or ent1.name == 'Player2':
                            ent2.level_finish = True
                        else:
                            if not ent1.closed_speech:
                                ent1.is_talk = True

                if isinstance(ent2, Npc):
                    if difference_distances <= DISTANCE_ATTACK[ent2.name]:
                        if ent2.name == 'Player1' or ent2.name == 'Player2':
                            ent1.level_finish = True
                        else:
                            if not ent2.closed_speech:
                                ent2.is_talk = True

            else:
                if isinstance(ent2, Enemy):
                    ent2.is_idle = True
                    ent2.act = False
                if isinstance(ent1, Enemy):
                    ent1.is_idle = True
                    ent1.act = False

    @staticmethod
    def verify_distance_entity(level_text_actual: int, entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_player_distance_enemy(entity1, entity2, level_text_actual)
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def __verify_collision_entity(entity1: Entity, entity2: Entity):
        valid_interaction = False
        if isinstance(entity1, Enemy) and isinstance(entity2, Player):
            valid_interaction = True
        elif isinstance(entity1, Player) and isinstance(entity2, Enemy):
            valid_interaction = True
        elif isinstance(entity1, ShotPlayer) and isinstance(entity2, Enemy):
            valid_interaction = True
        elif isinstance(entity1, Enemy) and isinstance(entity2, ShotPlayer):
            valid_interaction = True
        elif isinstance(entity1, ShotEnemy) and isinstance(entity2, Player):
            valid_interaction = True
        elif isinstance(entity1, Player) and isinstance(entity2, ShotEnemy):
            valid_interaction = True
        elif isinstance(entity1, Player) and isinstance(entity2, Potion):
            valid_interaction = True
        elif isinstance(entity1, Potion) and isinstance(entity2, Player):
            valid_interaction = True


        if valid_interaction:
            if (entity1.rect.right >= entity2.rect.left and
                    entity1.rect.left <= entity2.rect.right and
                    entity1.rect.bottom >= entity2.rect.top and
                    entity1.rect.top <= entity2.rect.bottom):
                if isinstance(entity1, (Player, Enemy, ShotPlayer)) and isinstance(entity2,
                                                                                   (Player, Enemy, ShotPlayer)):
                    if entity1.attack1_dmg in DAMAGE_FRAME[entity1.name]['Attack1']:
                        entity2.health -= ENTITY_DAMAGE[entity1.name]['Attack1']
                        entity2.is_hurt = True

                    if entity2.attack1_dmg in DAMAGE_FRAME[entity2.name]['Attack1']:
                        entity1.health -= ENTITY_DAMAGE[entity2.name]['Attack1']
                        entity1.is_hurt = True

                    if entity1.attack2_dmg in DAMAGE_FRAME[entity1.name]['Attack2']:
                        entity2.health -= ENTITY_DAMAGE[entity1.name]['Attack2']
                        entity2.is_hurt = True

                    if entity2.attack2_dmg in DAMAGE_FRAME[entity2.name]['Attack2']:
                        entity1.health -= ENTITY_DAMAGE[entity2.name]['Attack2']
                        entity1.is_hurt = True

                    if entity1.attack3_dmg in DAMAGE_FRAME[entity1.name]['Attack3']:
                        entity2.health -= ENTITY_DAMAGE[entity1.name]['Attack3']
                        entity2.is_hurt = True

                    if entity2.attack3_dmg in DAMAGE_FRAME[entity2.name]['Attack3']:
                        entity1.health -= ENTITY_DAMAGE[entity2.name]['Attack3']
                        entity1.is_hurt = True

                if isinstance(entity1, ShotPlayer) and isinstance(entity2, Enemy):
                    entity2.health -= entity1.damage
                    if entity1.shot_attack_c:
                        entity1.shot_attack_c.stop()
                        entity1.shot_attack_c = None
                    entity1.health -= 1
                    entity2.is_hurt = True

                if isinstance(entity1, Enemy) and isinstance(entity2, ShotPlayer):
                    entity1.health -= entity2.damage
                    if entity2.shot_attack_c:
                        entity2.shot_attack_c.stop()
                        entity2.shot_attack_c = None
                    entity2.health -= 1
                    entity1.is_hurt = True

                if isinstance(entity1, ShotEnemy) and isinstance(entity2, Player):
                    entity2.health -= entity1.damage
                    if entity1.shot_attack_c:
                        entity1.shot_attack_c.stop()
                        entity1.shot_attack_c = None
                    entity1.health -= 1
                    entity2.is_hurt = True

                if isinstance(entity1, Player) and isinstance(entity2, ShotEnemy):
                    entity1.health -= entity2.damage
                    if entity2.shot_attack_c:
                        entity2.shot_attack_c.stop()
                        entity2.shot_attack_c = None
                    entity2.health -= 1
                    entity1.is_hurt = True

                if isinstance(entity1, Player) and isinstance(entity2, Potion):
                    if entity2.npc == 'Npc2':
                        entity1.active_attack2 = True
                        entity2.health = 0
                    if entity2.npc == 'Npc4':
                        entity1.active_shotAttack = True
                        entity2.health = 0
                    if entity2.npc == 'Npc3':
                        entity1.health = HEALTH_VARIABLE['Player']['2']
                        entity1.active_health2 = True
                        entity2.health = 0
                    if entity2.npc == 'Npc5':
                        entity1.health = HEALTH_VARIABLE['Player']['3']
                        entity1.active_health3 = True
                        entity2.health = 0
                    if entity2.npc == 'Npc6':
                        entity1.energy = ENERGY_VARIABLE['Player']['2']
                        entity1.active_energy2 = True
                        entity2.health = 0
                    if entity2.npc == 'Npc7':
                        entity1.active_attack3 = True
                        entity2.health = 0
                    if entity2.npc == 'Teleporter':
                        entity1.level_finish = True
                        entity2.health = 0

                if isinstance(entity1, Potion) and isinstance(entity2, Player):
                    if entity1.npc == 'Npc2':
                        entity2.active_attack2 = True
                        entity1.health = 0
                    if entity1.npc == 'Npc4':
                        entity2.active_shotAttack = True
                        entity1.health = 0
                    if entity1.npc == 'Npc3':
                        entity2.health = HEALTH_VARIABLE['Player']['2']
                        entity2.active_health2 = True
                        entity1.health = 0
                    if entity1.npc == 'Npc5':
                        entity2.health = HEALTH_VARIABLE['Player']['3']
                        entity2.active_health3 = True
                        entity1.health = 0
                    if entity1.npc == 'Npc6':
                        entity2.energy = ENERGY_VARIABLE['Player']['2']
                        entity2.active_energy2 = True
                        entity1.health = 0
                    if entity1.npc == 'Npc7':
                        entity2.active_attack3 = True
                        entity1.health = 0
                    if entity1.npc == 'Teleporter':
                        entity2.level_finish = True
                        entity1.health = 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Potion):
                    if ent.potion_c is None or not ent.potion_c.get_busy():
                        ent.potion_c = py.mixer.find_channel()
                        if ent.potion_c:
                            ent.potion_c.play(ent.potion_sound)
                if isinstance(ent, (ShotPlayer, ShotEnemy)):
                    entity_list.remove(ent)
                if not ent.is_dead:
                    if isinstance(ent, Potion):
                        ent.is_dead = True
                    ent.is_dead_frame = True
                    ent.is_hurt = False
                    ent.is_attack1 = False
                    if ent.name in ('Boss1', 'Boss3'):
                        ent.is_attack2 = False
                        ent.is_attack3 = False
                    ent.is_idle = False
                    ent.act = False
                else:
                    entity_list.remove(ent)

    @staticmethod
    def __alter_boss_attack(enemy: Enemy):
        attack = random.randint(1, 3)
        if attack == 1:
            if enemy.is_attack2 == True or enemy.is_attack3 == True:
                enemy.is_attack1 = False
            else:
                enemy.is_attack1 = True
        if attack == 2:
            if enemy.is_attack1 == True or enemy.is_attack3 == True:
                enemy.is_attack2 = False
            else:
                enemy.is_attack2 = True
        if attack == 3:
            if enemy.is_attack1 == True or enemy.is_attack2 == True:
                enemy.is_attack3 = False
            else:
                enemy.is_attack3 = True
