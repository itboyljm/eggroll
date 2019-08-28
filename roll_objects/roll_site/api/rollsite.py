#
#  Copyright 2019 The Eggroll Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from api import RuntimeInstance
from api.cluster import rollsite as cluster_rollsite


def init(job_id, runtime_conf, server_conf_path="eggroll/conf/server_conf.json"):
    RuntimeInstance.ROLLSITE = cluster_rollsite.init(job_id=job_id, runtime_conf=runtime_conf,
                                                     server_conf_path=server_conf_path)


def push_sync(obj, name: str, tag: str, role=None, idx=-1):
    return RuntimeInstance.ROLLSITE.push_sync(obj=obj)

