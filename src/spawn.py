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
    
    
    # Run each spawn
    for name in Object.keys(Game.spawns):
        spawn = Game.spawns[name]
        if not spawn.spawning:
            # Get the number of our creeps in the room.
            creep_types = ["harvester", "upgrader", "builder"]
            Memory.amount = {}
            for role in creep_types:
                Memory.amount.role = 0
            for name in Object.keys(Game.creeps):
                creep = Game.creeps[name]
                role = creep.memory.role
                Memory.amount.role. += 1
            
            creeps_definions = [{"parts": [WORK, CARRY, MOVE], "minEnergy": 200}, 
                                {"parts": [WORK, CARRY, MOVE, MOVE], "minEnergy": 250},
                                {"parts": [WORK, CARRY, MOVE, MOVE], "minEnergy": 250}]

            for i in range(len(creep_types)):
                creep_type = creep_types[i]
                print(f"Energy available: {spawn.room.energyAvailable}, Creep Type: {Memory.amount.creep_type}, Min Energy: {creeps_definions[i]["minEnergy"]}")
                if Memory.amount.creep_type <= 0 and spawn.room.energyAvailable >= creeps_definions[i]["minEnergy"]:
                    print(f"Trying to spawn first {creep_type}")
                    spawn.createCreep(creeps_definions[i]["parts"], f"{role}{Game.time}", {"role":creep_type, "filling": True})
                    Memory.amount[creep_type] += 1
                    
            for i in range(len(creep_types)):
                creep_type = creep_types[i]
                current_controller_lvl = StructureController.level
                min_amount_creeps = creeps_amount[current_controller_lvl][creep_type]
                print(f"Number of {creep_type}: {Memory.amount.creep_type}")
                if Memory.amount.creep_type <= min_amount_creeps and spawn.room.energyAvailable >= creeps_definions[i]["minEnergy"]:
                    spawn.createCreep(creeps_definions[i]["parts"], f"{role}{Game.time}", {"role":creep_type, "filling": True})
                    Memory.amount[creep_type] += 1
            else:
                # If we have all minimum creeps and have enough energy spawn default creep
                if spawn.room.energyAvailable >= 300: 
                    spawn.createCreep(creeps_definions[1]["parts"], f"Upgrader{Game.time}", {"role":"upgrader", "filling": True})
                    Memory.amount["upgrader"] += 1
            
            