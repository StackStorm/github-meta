# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import yaml

CONFIG_FILENAME = 'config.yaml'
CONFIG_SCHEMA_FILENAME = 'config.schema.yaml'

def load_yaml_file(path):
    with file(path, 'r') as stream:
        text = yaml.load(stream)

    return text


def load_config():
    return load_yaml_file(CONFIG_FILENAME)


def load_config_schema():
    return load_yaml_file(CONFIG_SCHEMA_FILENAME)
