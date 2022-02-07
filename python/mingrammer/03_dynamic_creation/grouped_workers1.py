#!/usr/bin/env python3
#
# grouped workers on AWS
#
# usage:
#   ./grouped_workers1.py


from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


def make_diagram():
    with Diagram("Grouped Workers", show=False, direction="TB"):
        lb = ELB("lb")
        # -------------------------------------------------------
        # (prepared for edit)
        workers = [EC2("worker1"), EC2("worker2"), EC2("worker3")]
        # -------------------------------------------------------
        rds = RDS("events")
        
        lb >> workers >> rds


if __name__ == "__main__":
    make_diagram()
