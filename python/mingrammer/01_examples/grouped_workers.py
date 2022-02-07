#!/usr/bin/env python3
#
# https://diagrams.mingrammer.com/docs/getting-started/examples
#
# this is the first example on above page
# (slightly rewritten to improve clarity)
#
# usage:
#  ./grouped_workers.py
#
# executing this script generates the file "grouped_workers.png"
# in the current directory

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Grouped Workers", show=False, direction="TB"):
    #           ^-- title of diagram as well as normalized filename

    # define resources
    lb      = ELB("lb")
    workers = [EC2("worker1"), EC2("worker2"), EC2("worker3"), EC2("worker4"), EC2("worker5")]
    db      = RDS("events")

    # define relationship between resources
    lb >> workers >> db
