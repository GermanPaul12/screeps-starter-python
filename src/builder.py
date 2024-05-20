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
    target = creep.pos.findClosestByRange(FIND_MY_CONSTRUCTION_SITES)
    energy.give(creep, target, 3)