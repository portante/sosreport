## nis.py
## A plugin to gather all the NIS information

### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from sos.plugins import Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin
import os

class Nis(Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin):
    """NIS related information
    """

    plugin_name = 'nis'

    files = ('/var/yp',)

    def setup(self):
        self.add_copy_specs([
            "/etc/yp*.conf",
            "/var/yp/*"
        ])
        self.add_cmd_output("domainname")

# vim: et ts=4 sw=4
