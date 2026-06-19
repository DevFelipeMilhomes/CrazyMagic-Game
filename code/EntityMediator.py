
from code.Const import DISTANCE_ATTACK, ENTITY_DAMAGE, DAMAGE_FRAME
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_player_distance_enemy(ent1: Entity, ent2: Entity):
        valid_interaction = False
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        if isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            difference_distances = abs(ent1.rect.centerx - ent2.rect.centerx)
            if difference_distances < 1000:
                if isinstance(ent2, Enemy):
                    if not ent2.is_dead and ent2.health >0:
                        if difference_distances <= DISTANCE_ATTACK[ent2.name]:
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

                        if ent2.name in ('Boss1', 'Boss2', 'Boss3'):
                            ent2.active_bar_health = True
                if isinstance(ent1, Enemy):
                    if not ent1.is_dead and ent1.health>0:
                        if difference_distances <= DISTANCE_ATTACK[ent1.name]:
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
                            if ent1.name in ('Boss1', 'Boss2', 'Boss3'):
                                ent1.active_bar_health = True
            else:
                if isinstance(ent2, Enemy):
                    ent2.is_idle = True
                    ent2.act = False
                if isinstance(ent1, Enemy):
                    ent1.is_idle = True
                    ent1.act = False

    @staticmethod
    def verify_distance_entity(entity_list:list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_player_distance_enemy(entity1, entity2)
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def __verify_collision_entity(entity1: Entity, entity2: Entity):
        valid_interaction = False
        if isinstance(entity1, Enemy) and isinstance(entity2, Player):
            valid_interaction = True
        elif isinstance(entity1, Player) and isinstance(entity2, Enemy):
            valid_interaction = True

        if valid_interaction:
            if (entity1.rect.right >= entity2.rect.left and
                    entity1.rect.left <= entity2.rect.right and
                    entity1.rect.bottom >= entity2.rect.top and
                    entity1.rect.top <= entity2.rect.bottom):
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

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if not ent.is_dead:
                    ent.is_dead = True
                    ent.is_hurt = False
                    ent.is_attack1 = False
                    ent.is_idle = False
                    ent.act = False
                else:
                    entity_list.remove(ent)
