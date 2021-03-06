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

import jsonschema
import yaml

import util


def validate_schema(instance, schema):
    return jsonschema.validate(instance=instance, schema=schema)


if __name__ == '__main__':
    config = util.load_config()
    config_schema = util.load_config_schema()

    validate_schema(config, config_schema)

    print yaml.safe_dump(config, default_flow_style=False)
