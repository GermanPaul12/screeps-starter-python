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
        # if creep is still spawning skip him
        if creep.spawning: continue
        if creep.ticksToLive == 1: creep.say("☠️Dying")
        # Run creep depending on role
        if not creep.memory.role: creep.memory.role = "harvester"
        if creep.memory.role == "harvester": harvester.run(creep)
        if creep.memory.role == "upgrader": upgrader.run(creep)
        if creep.memory.role == "builder": builder.run(creep)

