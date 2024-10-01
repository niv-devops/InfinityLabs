# Approved by: Arin

import pytest # Use 'python3 -m pytest' command to run tests
from time import sleep
from oop_WS.ex3 import Cloud_Utility

TIME = 6

@pytest.fixture
def setup_cloud_utility():
    return Cloud_Utility()

def test_create_machine(setup_cloud_utility):
    cloud_utility = setup_cloud_utility

    machine_type1 = cloud_utility.create_machine(1)
    assert machine_type1 == 0, "First machine created should get ID num of 0."
    assert cloud_utility.machines[machine_type1].cost == 2, "Type 1 machine's cost should be initialized to 2."

    machine_type2 = cloud_utility.create_machine(2)
    assert machine_type2 == 1, "Second machine created should get ID num of 1."
    assert cloud_utility.machines[machine_type2].cost == 5, "Type 2 machine's cost should be initialized to 5."

def test_start_machine(setup_cloud_utility):
    cloud_utility = setup_cloud_utility
    machine = cloud_utility.create_machine(1)
    cloud_utility.start_machine(machine)
    assert cloud_utility.machines[machine].is_active, "is_active should return true after stating machine."

def test_stop_machine(setup_cloud_utility):
    cloud_utility = setup_cloud_utility
    machine = cloud_utility.create_machine(1)
    cloud_utility.start_machine(machine)
    cloud_utility.stop_machine(machine)
    assert not cloud_utility.machines[machine].is_active, "is_active should return false after stopping machine."

def test_get_cost_total(setup_cloud_utility):
    cloud_utility = setup_cloud_utility

    machine_type1 = cloud_utility.create_machine(1)
    machine_type2 = cloud_utility.create_machine(2)

    cloud_utility.start_machine(machine_type1)
    cloud_utility.start_machine(machine_type2)
    sleep(TIME)
    cloud_utility.stop_machine(machine_type1)
    cloud_utility.stop_machine(machine_type2)

    cost1 = cloud_utility.machines[machine_type1].get_cost()
    cost2 = cloud_utility.machines[machine_type2].get_cost()
    assert cloud_utility.cost_per_machine(machine_type1) == cost1, "Current cost per machine should be equal to machine.get_cost."
    assert cloud_utility.cost_per_machine(machine_type2) == cost2, "Current cost per machine should be equal to machine.get_cost."
    assert cloud_utility.total_cost() == cost1 + cost2, "Total cost should match sum of all machines current cost."