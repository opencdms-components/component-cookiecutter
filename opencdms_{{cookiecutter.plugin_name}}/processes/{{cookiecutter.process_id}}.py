###############################################################################
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
###############################################################################
__version__ = "0.0.1"
import logging
from pygeoapi.process.base import BaseProcessor

LOGGER = logging.getLogger(__name__)

PROCESS_METADATA = {
    "version": "0.0.1",
    "id": "process_id",
    "title": {
        "en": "{{cookiecutter.process_name}}",
    },
    "description": {
        "en": "{{cookiecutter.process_description}}",
    },
    "keywords": [],
    "links": [
        {
            "type": "text/html",
            "rel": "about",
            "title": "information",
            "href": "https://example.org/process",
            "hreflang": "en-US",
        }
    ],
    "inputs": {
        "input_attr_a": {
            "title": "Attribute A",
            "description": "Sample description.",
            "schema": {"type": "string"},
            "minOccurs": 1,
            "maxOccurs": 1,
            "metadata": None,
            "keywords": [],
        },
        "input_attr_b": {
            "title": "Attr B",
            "description": "Sample description. It's optional.",
            "schema": {"type": "string"},
            "minOccurs": 0,
            "maxOccurs": 1,
            "metadata": None,
            "keywords": [],
        },
    },
    "outputs": {
        "output_attr": {
            "title": "Output attribute.",
            "schema": {"type": "string"},
            "description": "You can have multiple output attributes."
        }
    },
    "example": {
        "inputs": {
            "input_attr_a": "foo",
            "input_attr_b": "bar",
        },
        "output": {
            "output_attr": "foobar"
        }
    },
}


class {{cookiecutter.process_name}}(BaseProcessor):
    def __init__(self, processor_def):
        """
        Initialize object
        :param processor_def: provider definition
        :returns: pygeoapi.process.{{cookiecutter.process_id}}.{{cookiecutter.process_name}}
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):
        """
        This method is invoked by pygeoapi when this class is set as a `process` type
        resource in pygeoapi config file.

        :param data: It is the value of `inputs` passed in payload. For a payload
        {
            "inputs": {
                "input_attr_a": foo",
                "input_attr_b": "bar"
            }
        }

        the value of data is

        {
            "input_attr_a": foo",
            "input_attr_b": "bar"
        }

        :return: media_type, json
        """

        mimetype = "application/json"
        try:
            output = {
                "output_attr": data["input_attr_a"] + data["input_attr_a"]
            }
        except Exception as e:
            LOGGER.exception(e)
            output = {"output_attr": None}
        return mimetype, output

    def __repr__(self):
        return "<{{cookiecutter.process_name}}> {}".format(self.name)
