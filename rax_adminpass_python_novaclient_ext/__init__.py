# Copyright 2012 Matt Martz <matt@sivel.net>
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Admin Pass extension
"""

from novaclient import utils
from novaclient.v1_1 import servers
from novaclient.v1_1 import shell

def add_args():
    utils.add_arg(shell.do_boot,
        '--admin-pass',
        default=None,
        metavar='<admin-pass>',
        help="Specifies the admin password of the server to be used during creation")


def bind_args_to_resource_manager(args):
    def add_admin_pass(args):
        return dict(admin_pass=args.admin_pass)

    utils.add_resource_manager_extra_kwargs_hook(
        shell.do_boot, add_admin_pass)


def __pre_parse_args__():
    add_args()


def __post_parse_args__(args):
    bind_args_to_resource_manager(args)
