# Copyright 2016 OpenStack Foundation
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

FIXTURE_SCHEMA = {
    u'name': u'sample_artifact',
    u'properties': {
        u'activated_at': {
            u'description': u'Datetime when artifact has became active.',
            u'filter_ops': [u'eq',
                            u'neq',
                            u'in',
                            u'gt',
                            u'gte',
                            u'lt',
                            u'lte'],
            u'format': u'date-time',
            u'glareType': u'DateTime',
            u'readOnly': True,
            u'required_on_activate': False,
            u'sortable': True,
            u'type': [u'string',
                      u'null']},
        u'created_at': {
            u'description': u'Datetime when artifact has been created.',
            u'filter_ops': [u'eq',
                            u'neq',
                            u'in',
                            u'gt',
                            u'gte',
                            u'lt',
                            u'lte'],
            u'format': u'date-time',
            u'glareType': u'DateTime',
            u'readOnly': True,
            u'sortable': True,
            u'type': u'string'},
        u'description': {u'default': u'',
                         u'description': u'Artifact description.',
                         u'filter_ops': [u'eq',
                                         u'neq',
                                         u'in'],
                         u'glareType': u'String',
                         u'maxLength': 4096,
                         u'mutable': True,
                         u'required_on_activate': False,
                         u'type': [u'string',
                                   u'null']},
        u'icon': {u'additionalProperties': False,
                  u'description': u'Artifact icon.',
                  u'filter_ops': [],
                  u'glareType': u'Blob',
                  u'properties': {u'md5': {u'type': [u'string', u'null']},
                                  u'sha1': {u'type': [u'string', u'null']},
                                  u'sha256': {u'type': [u'string', u'null']},
                                  u'content_type': {u'type': u'string'},
                                  u'external': {u'type': u'boolean'},
                                  u'size': {u'type': [u'number',
                                                      u'null']},
                                  u'status': {u'enum': [u'saving',
                                                        u'active',
                                                        u'pending_delete'],
                                              u'type': u'string'}},
                  u'required': [u'size',
                                u'md5', u'sha1', u'sha256',
                                u'external',
                                u'status',
                                u'content_type'],
                  u'required_on_activate': False,
                  u'type': [u'object',
                            u'null']},
        u'id': {u'description': u'Artifact UUID.',
                u'filter_ops': [u'eq',
                                u'neq',
                                u'in'],
                u'glareType': u'String',
                u'maxLength': 255,
                u'pattern': u'^([0-9a-fA-F]){8}-([0-9a-fA-F]){4}-([0-9a-'
                            u'fA-F]){4}-([0-9a-fA-F]){4}-([0-9a-fA-F]){12}$',
                u'readOnly': True,
                u'sortable': True,
                u'type': u'string'},
        u'license': {u'description': u'Artifact license type.',
                     u'filter_ops': [u'eq',
                                     u'neq',
                                     u'in'],
                     u'glareType': u'String',
                     u'maxLength': 255,
                     u'required_on_activate': False,
                     u'type': [u'string',
                               u'null']},
        u'license_url': {u'description': u'URL to artifact license.',
                         u'filter_ops': [u'eq',
                                         u'neq',
                                         u'in'],
                         u'glareType': u'String',
                         u'maxLength': 255,
                         u'required_on_activate': False,
                         u'type': [u'string',
                                   u'null']},
        u'metadata': {u'additionalProperties': {u'type': u'string'},
                      u'default': {},
                      u'description': u'Key-value dict with useful information'
                                      u'about an artifact.',
                      u'filter_ops': [u'eq',
                                      u'neq'],
                      u'glareType': u'StringDict',
                      u'maxProperties': 255,
                      u'required_on_activate': False,
                      u'type': [u'object',
                                u'null']},
        u'name': {u'description': u'Artifact Name.',
                  u'filter_ops': [u'eq',
                                  u'neq',
                                  u'in'],
                  u'glareType': u'String',
                  u'maxLength': 255,
                  u'required_on_activate': False,
                  u'sortable': True,
                  u'type': u'string'},
        u'owner': {u'description': u'ID of user/tenant who uploaded artifact.',
                   u'filter_ops': [u'eq',
                                   u'neq',
                                   u'in'],
                   u'glareType': u'String',
                   u'maxLength': 255,
                   u'readOnly': True,
                   u'required_on_activate': False,
                   u'sortable': True,
                   u'type': u'string'},
        u'provided_by': {u'additionalProperties': False,
                         u'description': u'Info about artifact authors.',
                         u'filter_ops': [u'eq',
                                         u'neq',
                                         u'in'],
                         u'glareType': u'StringDict',
                         u'maxProperties': 255,
                         u'properties': {u'company': {u'type': u'string'},
                                         u'href': {u'type': u'string'},
                                         u'name': {u'type': u'string'}},
                         u'required_on_activate': False,
                         u'type': [u'object',
                                   u'null']},
        u'release': {u'default': [],
                     u'description': u'Target OpenStack release for artifact. '
                                     u'It is usually the same when artifact '
                                     u'was uploaded.',
                     u'filter_ops': [u'eq',
                                     u'neq',
                                     u'in'],
                     u'glareType': u'StringList',
                     u'items': {u'type': u'string'},
                     u'maxItems': 255,
                     u'required_on_activate': False,
                     u'type': [u'array',
                               u'null'],
                     u'unique': True},
        u'status': {u'default': u'drafted',
                    u'description': u'Artifact status.',
                    u'enum': [u'drafted',
                              u'active',
                              u'deactivated',
                              u'deleted'],
                    u'filter_ops': [u'eq',
                                    u'neq',
                                    u'in'],
                    u'glareType': u'String',
                    u'sortable': True,
                    u'type': u'string'},
        u'supported_by': {u'additionalProperties': {u'type': u'string'},
                          u'description': u'Info about persons who '
                                          u'responsible for artifact support',
                          u'filter_ops': [u'eq',
                                          u'neq',
                                          u'in'],
                          u'glareType': u'StringDict',
                          u'maxProperties': 255,
                          u'required': [u'name'],
                          u'required_on_activate': False,
                          u'type': [u'object',
                                    u'null']},
        u'tags': {u'default': [],
                  u'description': u'List of tags added to Artifact.',
                  u'filter_ops': [u'eq',
                                  u'neq',
                                  u'in'],
                  u'glareType': u'StringList',
                  u'items': {u'type': u'string'},
                  u'maxItems': 255,
                  u'mutable': True,
                  u'required_on_activate': False,
                  u'type': [u'array',
                            u'null']},
        u'updated_at': {
            u'description': u'Datetime when artifact has been updated '
                            u'last time.',
            u'filter_ops': [u'eq',
                            u'neq',
                            u'in',
                            u'gt',
                            u'gte',
                            u'lt',
                            u'lte'],
            u'format': u'date-time',
            u'glareType': u'DateTime',
            u'readOnly': True,
            u'sortable': True,
            u'type': u'string'},
        u'version': {u'default': u'0.0.0',
                     u'description': u'Artifact version(semver).',
                     u'filter_ops': [u'eq',
                                     u'neq',
                                     u'in',
                                     u'gt',
                                     u'gte',
                                     u'lt',
                                     u'lte'],
                     u'glareType': u'String',
                     u'pattern': u'/^([0-9]+)\\.([0-9]+)\\.([0-9]+)(?:-'
                                 u'([0-9A-Za-z-]+(?:\\.[0-9A-Za-z-]+)*))?'
                                 u'(?:\\+[0-9A-Za-z-]+)?$/',
                     u'required_on_activate': False,
                     u'sortable': True,
                     u'type': u'string'},
        u'visibility': {u'default': u'private',
                        u'description': u'Artifact visibility that defines if '
                                        u'artifact can be available to other '
                                        u'users.',
                        u'filter_ops': [u'eq'],
                        u'glareType': u'String',
                        u'maxLength': 255,
                        u'sortable': True,
                        u'type': u'string'},
        u'image': {u'additionalProperties': False,
                   u'description': u'Image binary.',
                   u'filter_ops': [],
                   u'glareType': u'Blob',
                   u'properties': {
                       u'md5': {u'type': [u'string', u'null']},
                       u'sha1': {u'type': [u'string', u'null']},
                       u'sha256': {u'type': [u'string', u'null']},
                       u'content_type': {u'type': u'string'},
                       u'external': {u'type': u'boolean'},
                       u'size': {u'type': [u'number',
                                           u'null']},
                       u'status': {u'enum': [u'saving',
                                             u'active',
                                             u'pending_delete'],
                                   u'type': u'string'}},
                   u'required': [u'size',
                                 u'md5', u'sha1', u'sha256',
                                 u'external',
                                 u'status',
                                 u'content_type'],
                   u'required_on_activate': False,
                   u'type': [u'object', u'null']},
        u'package': {
            u'additionalProperties': False,
            u'description': u'Murano Package binary.',
            u'filter_ops': [],
            u'glareType': u'Blob',
            u'properties': {u'md5': {u'type': [u'string', u'null']},
                            u'sha1': {u'type': [u'string', u'null']},
                            u'sha256': {u'type': [u'string', u'null']},
                            u'content_type': {u'type': u'string'},
                            u'external': {u'type': u'boolean'},
                            u'size': {u'type': [u'number',
                                                u'null']},
                            u'status': {u'enum': [u'saving',
                                                  u'active',
                                                  u'pending_delete'],
                                        u'type': u'string'}},
            u'required': [u'size',
                          u'md5', u'sha1', u'sha256',
                          u'external',
                          u'status',
                          u'content_type'],
            u'required_on_activate': False,
            u'type': [u'object',
                      u'null']},
        u'environment': {
            u'additionalProperties': False,
            u'description': u'Heat Environment text body.',
            u'filter_ops': [],
            u'glareType': u'Blob',
            u'properties': {u'md5': {u'type': [u'string', u'null']},
                            u'sha1': {u'type': [u'string', u'null']},
                            u'sha256': {u'type': [u'string', u'null']},
                            u'content_type': {u'type': u'string'},
                            u'external': {u'type': u'boolean'},
                            u'size': {u'type': [u'number',
                                                u'null']},
                            u'status': {u'enum': [u'saving',
                                                  u'active',
                                                  u'pending_delete'],
                                        u'type': u'string'}},
            u'required': [u'size',
                          u'md5', u'sha1', u'sha256',
                          u'external',
                          u'status',
                          u'content_type'],
            u'type': [u'object',
                      u'null']},
        u'blob': {
            u'additionalProperties': False,
            u'description': u'I am Blob',
            u'filter_ops': [],
            u'glareType': u'Blob',
            u'mutable': True,
            u'properties': {
                u'md5': {u'type': [u'string', u'null']},
                u'sha1': {u'type': [u'string', u'null']},
                u'sha256': {u'type': [u'string', u'null']},
                u'content_type': {
                    u'type': u'string'},
                u'external': {
                    u'type': u'boolean'},
                u'size': {u'type': [
                    u'number',
                    u'null']},
                u'status': {
                    u'enum': [
                        u'saving',
                        u'active',
                        u'pending_delete'],
                    u'type': u'string'}},
            u'required': [u'size',
                          u'md5', u'sha1', u'sha256',
                          u'external',
                          u'status',
                          u'content_type'],
            u'required_on_activate': False,
            u'type': [u'object',
                      u'null']},
        u'template': {
            u'additionalProperties': False,
            u'description': u'TOSCA template body.',
            u'filter_ops': [],
            u'glareType': u'Blob',
            u'properties': {
                u'md5': {u'type': [u'string', u'null']},
                u'sha1': {u'type': [u'string', u'null']},
                u'sha256': {u'type': [u'string', u'null']},
                u'content_type': {
                    u'type': u'string'},
                u'external': {u'type': u'boolean'},
                u'size': {u'type': [u'number',
                                    u'null']},
                u'status': {u'enum': [u'saving',
                                      u'active',
                                      u'pending_delete'],
                            u'type': u'string'}},
            u'required': [u'size',
                          u'md5', u'sha1', u'sha256',
                          u'external',
                          u'status',
                          u'content_type'],
            u'type': [u'object',
                      u'null']},
    }
}
