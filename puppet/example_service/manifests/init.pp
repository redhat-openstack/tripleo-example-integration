# Copyright 2020 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# == Class: example_service
#
# Example service puppet module
#
# === Parameters
#
# [*foo*]
#   (Optional) foo value in /etc/example_service.conf
#   Defaults to 'foo'
#
class example_service (
  $foo = 'foo'
) {
  file { '/etc/example_service.conf':
    ensure  => file,
    mode    => '0644',
    owner   => 'root',
    group   => 'root',
    content =>  "foo: ${foo}"
  }
}
