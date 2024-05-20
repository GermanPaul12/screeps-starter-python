from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def get(creep, source=None):
    """
    Get's energy from source
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
        # If we have a saved source, use it
        if not source:
            # Get a random new source and save it
            source = _.sample(creep.room.find(FIND_SOURCES))
            creep.memory.source = source.id

        # If we're near the source, harvest it - otherwise, move to it.
        if creep.pos.isNearTo(source):
            result = creep.harvest(source)
            creep.say("🔋 charge")
            if result != OK:
                print("[{}] Unknown result from creep.harvest({}): {}".format(creep.name, source, result))
        else:
            creep.moveTo(source)
            creep.say("🚶‍♂️ move")

def give(creep, target=creep.room.controller, range=0):
    """
    Gives energy to target
    """
    creep.memory.target = target
    if target.energyCapacity:
        is_close = creep.pos.isNearTo(target)
    else:
        is_close = creep.pos.inRangeTo(target, 3)

    if is_close:
        # If we are targeting a spawn or extension, transfer energy. Otherwise, use upgradeController on it.
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
    else:
        creep.moveTo(target)
