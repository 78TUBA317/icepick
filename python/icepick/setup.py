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

from setuptools import setup

setup(
    name='icepick',
    maintainer='Peter Sanders',
    author_email='p.e.sanders@kpn-mail.nl',
    description='Icepick is a new ..',
    keywords='icepick',
    url='https://github.com/../../master/README.md',
    python_requires='>=3.7',
    install_requires=['botocore',
                      'boto3',
                      'pandas',
                      'pyarrow>=3.0.0<4.0.0'
                      ],
    extras_require={
        "dev": [
            "tox-travis==0.12",
            "virtualenv<20.0.0",
        ],
    },
    setup_requires=['setupmeta'],
    license="Apache License 2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)