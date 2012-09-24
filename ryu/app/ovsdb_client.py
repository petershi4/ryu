# Copyright (C) 2012 Nippon Telegraph and Telephone Corporation.
# Copyright (C) 2012 Isaku Yamahata <yamahata at private email ne jp>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gevent
import gflags
import logging
import sys

from ryu.base import app_manager
from ryu.lib.ovs import db_client as db_client_lib

FLAGS = gflags.FLAGS
LOG = logging.getLogger(__name__)


class OVSDBClient(app_manager.RyuApp):
    _CONTEXTS = {}

    def __init__(self, *_args, **_kwargs):
        super(OVSDBClient, self).__init__()
        LOG.debug('argv %s', sys.argv)

        args = FLAGS(sys.argv)
        LOG.debug('args %s', args)
        args = args[args.index('--', 1) + 1:]
        LOG.debug('args %s', args)

        remote = args[0]
        args = args[1:]
        db_client = db_client_lib.DBClient(remote)
        gevent.spawn_later(0, db_client.run_command, args=args)