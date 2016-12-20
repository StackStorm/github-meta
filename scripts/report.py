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

import os

from github import Github
import yaml

import util


g = Github(os.environ.get('GITHUB_TOKEN'))


if __name__ == '__main__':
    config = util.load_config()

    for section in config:
        defined_labels = [label['name'] for label in section.get('labels')]

        labels_unknown = {}

        for repo_name in section.get('repositories'):
            for label in g.get_repo(repo_name).get_labels():
                if label.name not in defined_labels:
                    if repo_name not in labels_unknown:
                        labels_unknown[repo_name] = []

                    labels_unknown[repo_name].append(label.name)

        if labels_unknown:
            print('# Labels that are not in spec:')
            print(yaml.safe_dump(labels_unknown, default_flow_style=False))
