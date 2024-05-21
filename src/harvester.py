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
    Runs a creep as a generic harvester.
    :param creep: The creep to run
    """
    energy.get(creep)
    
    # Get a random new target.
    target = _(creep.room.find(FIND_STRUCTURES)) \
        .filter(lambda s: ((s.structureType == STRUCTURE_SPAWN or s.structureType == STRUCTURE_EXTENSION)
                            and s.energy < s.energyCapacity) or s.structureType == STRUCTURE_CONTROLLER) \
        .sample()
    creep.memory.target = target.id
    energy.give(creep, target, 1, "harvester")
