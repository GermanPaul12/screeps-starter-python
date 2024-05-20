from defs import *
import harvester

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def run(creep):
    """
    Runs a creep as a generic upgrader.
    :param creep: The creep to run
    """

    # If we're full, stop filling up and remove the saved source
    if creep.memory.filling and _.sum(creep.carry) >= creep.carryCapacity:
        creep.memory.filling = False
        del creep.memory.source
    # If we're empty, start filling again and remove the saved target
    elif not creep.memory.filling and creep.carry.energy <= 0:
        creep.memory.filling = True
        del creep.memory.target

    if creep.memory.filling:
        harvester.run(creep)
    else:
        target = creep.pos.findClosestByRange(FIND_MY_CONSTRUCTION_SITES)
        is_close = creep.pos.inRangeTo(target, 3)

        code = creep.build(target)
        
        if is_close:
            if code == OK or code == ERR_FULL:
                creep.emote('🏗️ build')
                del creep.memory.target
            elif code == ERR_NOT_IN_RANGE:
                creep.emote('🚶‍♂️ move') 
                creep.moveTo(target, '#4800FF')
            elif code == ERR_NOT_OWNER:
                print(f"{creep} lost in {creep.room}")  
            elif code == ERR_NO_BODYPART:
                creep.emote("☠️ suicide")
                creep.suicide()         
        else:
            creep.emote('🚶‍♂️ move')
            creep.moveTo(target, '#4800FF')   