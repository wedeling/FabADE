# FabSim3 Commands Python API
#
# This file maps command-line instructions for FabSim3 to Python functions.
# NOTE: No effort is made to map output back to FabSim, as this complicates
# the implementation greatly.
#
# This file can be included in any code base. 
# It has no dependencies, but does require a working FabSim3 installation.

import os

def fabsim(command, arguments, machine = 'localhost'):
    """
    Generic function for running any FabSim3 command.
    """
    print('Executing', "fabsim {} {}:{}".format(machine, command, arguments))
    os.system("fabsim {} {}:{}".format(machine, command, arguments))

def run_uq_ensemble(campaign_dir, script_name, machine='localhost', skip = 0, **args):
    """
    Launches a UQ ensemble.
    """
    sim_ID = campaign_dir.split('/')[-1]
    arguments = "{},campaign_dir={},script_name={},skip={}".format(sim_ID, campaign_dir, script_name, skip)
    fabsim("run_uq_ensemble", arguments, machine=machine)
    
def get_uq_samples(campaign_dir, machine = 'localhost'):
    """
    Retrieves results from UQ ensemble
    """
    sim_ID = campaign_dir.split('/')[-1]
    arguments = "{},campaign_dir={}".format(sim_ID, campaign_dir)
    fabsim("get_uq_samples", arguments, machine=machine)