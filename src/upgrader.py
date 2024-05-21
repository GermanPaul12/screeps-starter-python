from defs import *
import energy

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
    energy.get(creep)
    if creep.memory.target:
        target = Game.getObjectById(creep.memory.target)
    else:
        # Get a random new target.
        target = creep.room.controller
        creep.memory.target = target.id    

    energy.give(creep, target, 3, "upgrader")