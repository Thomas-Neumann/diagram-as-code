#!/usr/bin/env python3
#
# grouped workers on AWS with different environments
#
# usage:
#   ./grouped_workers1.py

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

def make_diagram():
    # -------------------------------------------------------
    # (prepared for edit)
    diagram = f"Grouped Workers"
    # -------------------------------------------------------

    with Diagram(diagram, show=False, direction="TB"):
        lb = ELB("lb")
        # -------------------------------------------------------
        # (prepared for edit)
        workers = [EC2("worker1"), EC2("worker2"), EC2("worker3"), EC2("worker4"), EC2("worker5")] 
        # -------------------------------------------------------
        rds = RDS("events")

        lb >> workers >> rds

if __name__ == "__main__":
    make_diagram()
