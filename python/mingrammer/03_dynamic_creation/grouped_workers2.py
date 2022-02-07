#!/usr/bin/env python3
#
# grouped workers on AWS from external data (faked)
#
# usage:
#   ./grouped_workers2.py

import random

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


# let's pretend this function actually loads from an external file
def load_data(filename):
    print(f"Loading configuration file '{filename}'.")
    # please ignore the code - I'm just trying to create a variable
    # number of worker nodes to simulate a dynamic environment
    data = {
        "workers": [],
    }
    count = random.randrange(1,5)
    print("Generating", count, "workers")
    for idx in range(1, count+1):
        data["workers"].append(f"worker{idx}")
        #                      ^------------^
        # can't use 'EC2(<workername>) here since Diagram() has not been set up yet
    return data


def make_diagram(data):
    with Diagram("Grouped Workers", show=False, direction="TB"):
        lb = ELB("lb")
        # -------------------------------------------------------
        # create an EC2() object for each worker
        workers = []
        for worker in data["workers"]:
            workers.append(EC2(worker))
        # -------------------------------------------------------
        rds = RDS("events")
        
        lb >> workers >> rds


if __name__ == "__main__":
    data = load_data("data/my_solution.cfg")
    make_diagram(data)
