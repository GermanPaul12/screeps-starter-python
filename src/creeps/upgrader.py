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
    if creep.memory.filling:
        harvester.run(creep)
    else:
        # If we have a saved target, use it
        if creep.memory.target:
            target = Game.getObjectById(creep.memory.target)
        else:
            # Get a random new target.
            target = creep.room.controller
            creep.memory.target = target.id

        # If we are targeting a spawn or extension, we need to be directly next to it - otherwise, we can be 3 away.
        if target:
            is_close = creep.pos.isNearTo(target)
        else:
            is_close = creep.pos.inRangeTo(target, 3)


        code = creep.upgradeController(target)
        
        if is_close:
            if code == OK or code == ERR_FULL:
                creep.say('⚡ tranfer')
                del creep.memory.target
            elif code == ERR_NOT_IN_RANGE or not creep.pos.inRangeTo(target, 2):
                creep.say('🚶‍♂️ move') 
                creep.moveTo(target, '#4800FF')
            elif code == ERR_NOT_OWNER:
                print(f"{creep} lost in {creep.room}")  
            elif code == ERR_NO_BODYPART:
                creep.say("☠️ suicide")
                creep.suicide()         
        else:
            creep.say('🚶‍♂️ move')
            creep.moveTo(target, '#4800FF')   

