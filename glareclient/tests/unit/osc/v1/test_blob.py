# Copyright (c) 2016 Mirantis, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import mock

from glareclient.osc.v1 import blobs as osc_blob
from glareclient.tests.unit.osc.v1 import fakes
from glareclient.v1 import artifacts as api_art
import testtools


class TestBlobs(fakes.TestArtifacts):
    def setUp(self):
        super(TestBlobs, self).setUp()
        self.blob_mock = \
            self.app.client_manager.artifact.blobs
        self.http = mock.MagicMock()


class TestUploadBlob(TestBlobs):
    def setUp(self):
        super(TestUploadBlob, self).setUp()
        self.blob_mock.call.return_value = \
            api_art.Controller(self.http, type_name='sample_artifact')

        # Command to test
        self.cmd = osc_blob.UploadBlob(self.app, None)

        self.COLUMNS = ('blob_property', 'id', 'name',
                        'size', 'status', 'version')

    def test_upload_images(self):
        exp_data = ('image', 'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                    'art1', '1B', 'active', '0.0.0')
        arglist = ['images',
                   'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                   '--blob', '/path/to/file']
        verify = [('type_name', 'images')]

        parsed_args = self.check_parser(self.cmd, arglist, verify)
        columns, data = self.cmd.take_action(parsed_args)
        self.assertEqual(self.COLUMNS, columns)
        self.assertEqual(exp_data, data)

    def test_upload_tosca_template(self):
        exp_data = ('template', 'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                    'art1', '1B', 'active', '0.0.0')
        arglist = ['tosca_templates',
                   'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                   '--blob', '/path/to/file']
        verify = [('type_name', 'tosca_templates')]

        parsed_args = self.check_parser(self.cmd, arglist, verify)
        columns, data = self.cmd.take_action(parsed_args)
        self.assertEqual(self.COLUMNS, columns)
        self.assertEqual(exp_data, data)

    def test_upload_heat_template(self):
        exp_data = ('template', 'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                    'art1', '1B', 'active', '0.0.0')
        arglist = ['heat_templates',
                   'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                   '--blob', '/path/to/file']
        verify = [('type_name', 'heat_templates')]

        parsed_args = self.check_parser(self.cmd, arglist, verify)
        columns, data = self.cmd.take_action(parsed_args)
        self.assertEqual(self.COLUMNS, columns)
        self.assertEqual(exp_data, data)

    def test_upload_environment(self):
        exp_data = ('environment', 'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                    'art1', '1B', 'active', '0.0.0')
        arglist = ['heat_environments',
                   'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                   '--blob', '/path/to/file']
        verify = [('type_name', 'heat_environments')]

        parsed_args = self.check_parser(self.cmd, arglist, verify)
        columns, data = self.cmd.take_action(parsed_args)
        self.assertEqual(self.COLUMNS, columns)
        self.assertEqual(exp_data, data)

    def test_upload_package(self):
        exp_data = ('package', 'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                    'art1', '1B', 'active', '0.0.0')
        arglist = ['murano_packages',
                   'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                   '--blob', '/path/to/file']
        verify = [('type_name', 'murano_packages')]

        parsed_args = self.check_parser(self.cmd, arglist, verify)
        columns, data = self.cmd.take_action(parsed_args)
        self.assertEqual(self.COLUMNS, columns)
        self.assertEqual(exp_data, data)

    def test_upload_bad(self):
        arglist = ['sample_artifact',
                   'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                   '--blob', '/path/to/file']
        verify = [('type_name', 'sample_artifact')]

        parsed_args = self.check_parser(self.cmd, arglist, verify)
        with testtools.ExpectedException(SystemExit):
            self.cmd.take_action(parsed_args)

    def test_upload_blob_with_blob_prop(self):
        exp_data = ('blob', 'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                    'art1', '1B', 'active', '0.0.0')
        arglist = ['sample_artifact',
                   'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                   '--blob', '/path/to/file',
                   '--blob-property', 'blob']
        verify = [('type_name', 'sample_artifact')]

        parsed_args = self.check_parser(self.cmd, arglist, verify)
        columns, data = self.cmd.take_action(parsed_args)
        self.assertEqual(self.COLUMNS, columns)
        self.assertEqual(exp_data, data)


class TestDownloadBlob(TestBlobs):
    def setUp(self):
        super(TestDownloadBlob, self).setUp()
        self.blob_mock.call.return_value = \
            api_art.Controller(self.http, type_name='sample_artifact')

        # Command to test
        self.cmd = osc_blob.DownloadBlob(self.app, None)

        self.COLUMNS = ('blob_property', 'id', 'name',
                        'size', 'status', 'version')

    def test_download_exception(self):
        arglist = ['images',
                   'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                   '--blob-property', 'blob',
                   '--file', None]
        verify = [('type_name', 'images')]

        parsed_args = self.check_parser(self.cmd, arglist, verify)
        with testtools.ExpectedException(SystemExit):
            self.cmd.take_action(parsed_args)

    def test_download_blob(self):
        arglist = ['images',
                   'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                   '--blob-property', 'blob',
                   '--file', '/path/to/file']
        verify = [('type_name', 'images')]

        parsed_args = self.check_parser(self.cmd, arglist, verify)
        self.cmd.take_action(parsed_args)

    def test_download_without_blob_property(self):
        arglist = ['images',
                   'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                   '--file', '/path/to/file']
        verify = [('type_name', 'images')]

        parsed_args = self.check_parser(self.cmd, arglist, verify)
        self.cmd.take_action(parsed_args)

    def test_download_progress(self):
        arglist = ['images',
                   'fc15c365-d4f9-4b8b-a090-d9e230f1f6ba',
                   '--file', '/path/to/file',
                   '--progress', 'True']
        verify = [('type_name', 'images')]

        parsed_args = self.check_parser(self.cmd, arglist, verify)
        self.cmd.take_action(parsed_args)