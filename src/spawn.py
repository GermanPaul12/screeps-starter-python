from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def spawn_creeps():
    """_summary_
    Takes energy in room and spawns necessary creeps for current
    controller level
    """
    creep_parts = {"MOVE":50, 
                "WORK":100, 
                "CARRY":50,
                "ATTACK":80,
                "RANGED_ATTACK":150,
                "HEAL":250,
                "CLAIM":600,
                "TOUGH":10,
                }
    
    creeps_amount = {0: {"harvester":3, "upgrader":5, "default":"upgrader" },
              1: {"harvester":3, "upgrader":5, "builder":5, "default":"upgrader" },
              2: {"harvester":3, "upgrader":3, "builder":3, "repairer":3, "default":"upgrader" },
              3: {"harvester":3, "upgrader":3, "builder":3, "repairer":3, "default":"upgrader" },
              4: {"harvester":3, "upgrader":3, "builder":3, "repairer":3, "miner":2, "default":"upgrader" },
              5: {"harvester":3, "upgrader":3, "builder":3, "repairer":3, "miner":2, "default":"upgrader" },
              6: {"harvester":3, "upgrader":3, "builder":3, "repairer":3, "miner":2, "default":"upgrader" },
    }
    current_controller_lvl = StructureController.level
    
    # Run each spawn
    for name in Object.keys(Game.spawns):
        spawn = Game.spawns[name]
        if not spawn.spawning:
            # Get the number of our creeps in the room.
            num_harvesters = _.sum(Game.creeps, lambda c: c.pos.roomName == spawn.pos.roomName and c.memory.role == "harvester")
            num_upgraders = _.sum(Game.creeps, lambda c: c.pos.roomName == spawn.pos.roomName and c.memory.role == "upgrader")
            num_builders = _.sum(Game.creeps, lambda c: c.pos.roomName == spawn.pos.roomName and c.memory.role == "builder")
            num_creeps = [num_harvesters, num_upgraders, num_builders]
            creep_types = ["harvester", "upgrader", "builder"]
            creeps_definions = [{"parts": [WORK, WORK, CARRY, MOVE], "minEnergy": 300, "memory":{"role":role, "filling": True}}, {"parts": [WORK, CARRY, CARRY, MOVE, MOVE], "minEnergy": 300, "memory":{"role":role, "full": False}},
                                {"parts": [WORK, CARRY, CARRY, MOVE, MOVE], "minEnergy": 300, "memory":{"role":role, "filling": True}}]
            # If there are no creeps, spawn one creep of each type once energy is at 300 or more
            for ind,creep_type_amnt in enumerate(num_creeps):
                creep_type = creeps_definions[ind]
                role = creep_types[ind]
                if creep_type_amnt <= 0 and spawn.room.energyAvailable >= creep_type["minEnergy"]:
                    spawn.createCreep(creep_type["parts"], f"{role}{Game.time}", creep_type["memory"])
            # If we have one creep of each type and energy is available spawn more
            for ind,creep_type_amnt in enumerate(num_creeps):
                creep_type = creeps_definions[ind]
                role = creep_types[ind]
                min_amount_creeps = creeps_amount[current_controller_lvl][role]
                if creep_type_amnt <= min_amount_creeps and spawn.room.energyAvailable >= creep_type["minEnergy"]:
                    spawn.createCreep(creep_type["parts"], f"{role}{Game.time}", creep_type["memory"])
            # If we have all minimum creeps and have enough energy spawn default creep
            if spawn.room.energyAvailable >= creep_type["minEnergy"]: spawn.createCreep(creeps_definions[1]["parts"], f"Upgrader{Game.time}", creep_type["memory"])   
  