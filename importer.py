#!/usr/bin/python3

import xml.etree.ElementTree as ET
import datetime
import argparse

def get_parser():
    parser = argparse.ArgumentParser(
        description = "Script to append hosts to an exported configuration of PfSense aliases"
    )
    parser.add_argument(
        "--hosts",
        help = "Path to a hosts file",
        type = str,
        required = True
    )
    parser.add_argument(
        "-o", "--out",
        help = "Output path name",
        type = str,
        default = "hosts.csv"
    )
    return parser

def read_hosts(hosts_file):
    # https://github.com/jonhadfield/python-hosts would be better but we don't want to have any pypi dependencies
    # we make our own shitty parser instead
    hosts = set()
    with open(hosts_file, "r") as f:
        for line in f.read().strip().split("\n"):
            if not line.startswith("#"):
                s = line.split()
                if len(s) >= 2:
                    hosts.add(s[1])
    return hosts

def main(**kwargs):
    with open(kwargs["out"], "w") as f:
        f.write("\n".join(read_hosts(kwargs["hosts"])))

if __name__ == "__main__":
    main(**vars(get_parser().parse_args()))

