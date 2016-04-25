#!/usr/bin/env python

from __future__ import print_function

import argparse
import logging
import os
import rdflib
import requests
import sys
import yaml


def main():
    '''Parse args, loop over repository and restore.'''

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Restore serialized Fedora repository.')
    parser.add_argument('-c', '--config', required=True,
        help='relative or absolute path to the YAML config file')
    args = parser.parse_args()
    
    # load and parse specified configuration settings
    with open(args.config, 'r') as configfile:
        globals().update(yaml.safe_load(configfile))
    
    # check connection to fcrepo
    print('\nReady to load to endpoint at: {0}'.format(REST_ENDPOINT))
    print('\nTesting connection to server with provided credentials ...')
    resp = requests.get(REST_ENDPOINT, auth=(FEDORA_USER, FEDORA_PASSWORD))
    print(resp)
    
    # check the backup tree
    print('\nScanning repository backup at {0}'.format(BACKUP_LOCATION))
    backup = [r for r in os.walk(BACKUP_LOCATION)]
    for path, dirs, files in backup:
        print("\n{0}".format(path))
        for n, f in enumerate(files):
            print("  {0}. {1}".format(n+1, f))


if __name__ == "__main__":
    main()
