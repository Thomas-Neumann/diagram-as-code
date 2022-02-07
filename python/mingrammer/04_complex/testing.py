#!/usr/bin/env python3
#
# grouped workers on AWS from external data (faked)
#
# usage:
#   ./testing.py --sanitize production.json
#   ./testing.py production.json

import argparse
import logging
import json
import sys

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


def parse_argv():
    parser = argparse.ArgumentParser(description='Generate diagram.')
    parser.add_argument('--sanitize', dest='sanitize', action='store_true', default=False, help='sanitize the diagram')
    parser.add_argument('configfile', type=str, help='config file')
    args = parser.parse_args()

    config = {
        "MustSanitize": args.sanitize,
        "ConfigFile": args.configfile,
    }
    return config


# {
#    "name": "MyDiagram",
#    "resources": {
#      "external_alb": <str>,
#      "workers": [ <str>, ...],
#      "events_db": <str>
#    }
# }
def load_data_from_json(filename):
    logging.info("Loading configuration file '%s'.", filename)
    try:
        with open(filename, "r") as fh:
            json_data = json.load(fh)
        return json_data
    except FileNotFoundError as e:
        logging.error("Unable to load file: %s", e)
        sys.exit(1)


def make_diagram(data, sanitize=False):
    if sanitize:
        diagram_name = data["name"] + " (sanitized)"
    else:
        diagram_name = data["name"]

    resources = data["resources"]
    with Diagram(diagram_name, filename="testing", show=False, direction="TB"):
        #                       ^-- hard-coding the filename for the demo
        if sanitize:
            lb  = ELB("External ALB", fontcolor = "#a4a4a4")
            rds = RDS("Events Database", fontcolor = "#a4a4a4")
        else:
            lb  = ELB(resources["external_alb"])
            rds = RDS(resources["events_db"])
        workers = []
        idx = 1
        for worker in resources["workers"]:
            if sanitize:
                workers.append(EC2(f"node{idx}", fontcolor = "#a4a4a4"))
                idx += 1
            else:
                workers.append(EC2(worker))
        lb >> workers >> rds


if __name__ == "__main__":
    cfg = parse_argv()
    data = load_data_from_json(cfg["ConfigFile"])
    make_diagram(data, sanitize=cfg["MustSanitize"])
