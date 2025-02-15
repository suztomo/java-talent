# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import synthtool.languages.java as java
import os

AUTOSYNTH_MULTIPLE_COMMITS = True

versions = ['v4beta1', 'v4']
service = 'talent'

for version in versions:
  library = java.bazel_library(
      service=service,
      version=version,
      bazel_target=f'//google/cloud/{service}/{version}:google-cloud-{service}-{version}-java',
  )
os.remove('proto-google-cloud-talent-v4beta1/src/main/java/com/google/cloud/talent/v4beta1/BatchProto.java')
java.common_templates(excludes=[
  '.kokoro/build.sh',
  '.kokoro/nightly/samples.cfg',
  '.kokoro/presubmit/samples.cfg',
])
