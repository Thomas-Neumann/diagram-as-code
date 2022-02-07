#!/usr/bin/env python3
#
# grouped workers on AWS with different environments
#
# usage:
#   ./grouped_workers2.py dev
#   ./grouped_workers2.py prod

import sys

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

def make_diagram(environment):
    # -------------------------------------------------------
    # match diagram title to selected environment
    if environment == "dev":
        diagram = f"Grouped Workers (Development)"
    else:
        diagram = f"Grouped Workers (Production)"
    # -------------------------------------------------------

    with Diagram(diagram, show=False, direction="TB"):
        lb = ELB("lb")
        # -------------------------------------------------------
        # dev and prod have different worker count and names
        if environment == "dev":
            workers = [EC2("dev1")] 
        else:
            workers = [EC2("prod1"), EC2("prod2"), EC2("prod3")] 
        # -------------------------------------------------------
        rds = RDS("events")

        lb >> workers >> rds

if __name__ == "__main__":
    scriptname = sys.argv[0]
    if len(sys.argv) == 2:
        environment = sys.argv[1]
        print(f"Creating diagram for '{environment}'.")
        make_diagram(environment)
    else:
        print(f"Invalid usage. Try '{scriptname} [dev|prod]'")
