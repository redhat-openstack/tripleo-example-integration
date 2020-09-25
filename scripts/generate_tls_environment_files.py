#!/usr/bin/env python3
#
# Copyright 2020 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Example execution:
#
# ./generate_tls_environment_files.py \
#        --tripleo-heat-templates ~/tripleo-heat-templates \
#        --plugin-templates ../tripleo/environments/tls-endpoint-data/ \
#        --output-dir ../tripleo/environments/ssl
#
import argparse
import copy
import os
import yaml


SSL_ENV_FILES = ['tls-everywhere-endpoints-dns.yaml',
                 'tls-endpoints-public-dns.yaml',
                 'tls-endpoints-public-ip.yaml']
THT_PATH = '/usr/share/openstack-tripleo-heat-templates'


def get_parser():
    parser = argparse.ArgumentParser(description=('Generate TLS Environment '
                                                  'Files'))
    parser.add_argument('--tripleo-heat-templates', type=str,
                        help=('Path to the tripleo-heat-templates. '
                              'Default: {}'.format(THT_PATH)),
                        default=THT_PATH)
    parser.add_argument('--plugin-templates', type=str,
                        help=('Path to a folder containing files that should '
                              'be merged with the {} from the '
                              'tripleo-heat-templates files.  The directory '
                              'should contain the files with the same name. '
                              'If this directory does not contain a specific '
                              'file, the file is excluded from the '
                              'output.'.format(
                                  ', '.join(SSL_ENV_FILES))),
                        default=THT_PATH)
    parser.add_argument('--output-dir', type=str,
                        help=('Output directory for the generated files. '
                              'Defaults to current working directory.'),
                        default=os.getcwd())
    return parser


def check_files(paths=[]):
    for path in paths:
        if not os.path.exists(path):
            print('SKIPPING: Missing {}'.format(path))
            return False
    return True


def merge_dicts(orig, new):
    data = copy.deepcopy(orig)
    for k, v in new.items():
        if type(v) == dict:
            if k not in orig:
                data[k] = copy.deepcopy(v)
            else:
                data[k] = merge_dicts(data[k], v)
        else:
            data[k] = v
    return data


def merge_files(source, target):
    check_files([source, target])
    if not os.path.exists(source):
        print('SKIPPING: Missing {}'.format(source))
    with open(source) as fin:
        source_data = yaml.safe_load(fin.read())
    with open(target) as fin:
        target_data = yaml.safe_load(fin.read())
    return merge_dicts(source_data, target_data)


def generate_tls_files(args):
    print('Starting merge...')
    for f in SSL_ENV_FILES:
        source_file = os.path.join(args.tripleo_heat_templates, 'environments',
                                   'ssl', f)
        plugin_file = os.path.join(args.plugin_templates, f)
        data = merge_files(source_file, plugin_file)
        if not data:
            continue
        dest_file = os.path.join(args.output_dir, f)
        print('UPDATING: Writing {}'.format(dest_file))
        with open(dest_file, 'w') as fp:
            fp.write("{}\n".format('#' * 80))
            fp.write("# Generated by {}\n".format(os.path.basename(__file__)))
            fp.write("{}\n".format('#' * 80))
            yaml.dump(data, fp, width=120)
    print('Done.')


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    generate_tls_files(args)