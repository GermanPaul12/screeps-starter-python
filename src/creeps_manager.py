from defs import *
import harvester
import upgrader
import builder

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def manage():
    """
    Manages all existing creeps
    """

    # Run each creep
    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]
        role = creep.memory.role
        # if creep is still spawning skip him
        if creep.spawning: continue
        if creep.ticksToLive == 1: 
            creep.say("☠️Dying")
            Memory.amount.role -= 1
        # Run creep depending on role
        if not role: creep.memory.role = "harvester"
        if role == "harvester": harvester.run(creep)
        if role == "upgrader": upgrader.run(creep)
        if role == "builder": builder.run(creep)

