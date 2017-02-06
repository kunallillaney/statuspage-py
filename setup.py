# Copyright 2016 Kunal Lillaney (http://kunallillaney.github.io)
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

from core.component import Component

#Spatial Database
component = Component()
component.name = 'Spatial Database API'
component.description = 'The following tests: test_blosc, test_image, test_jpeg, test_raw, test_propagate, test_time'
component.create()

component = Component()
component.name = 'IO API'
component.description = 'The following tests: test_autoingest, test_io, test_query'
component.create()

component = Component()
component.name = 'Ramon API'
component.description = 'The following tests: test_annoid, test_ramon, test_jsonann, test_neuron'
component.create()

component = Component()
component.name = 'Stats/Graph'
component.description = 'The following tests: test_graphgen, test_probability, test_stats'
component.create()

component = Component()
component.name = 'Metadata'
component.description = 'The following tests: test_info, test_resource, test_settings'
component.create()

