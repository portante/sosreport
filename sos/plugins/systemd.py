## Copyright (C) 2012 Red Hat, Inc., Bryn M. Reeves <bmr@redhat.com>

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

from sos.plugins import Plugin, RedHatPlugin

class Systemd(Plugin, RedHatPlugin):
    """ Information on systemd and related subsystems
    """

    plugin_name = "systemd"

    packages = ('systemd',)
    files = ('/usr/lib/systemd/systemd',)

    def setup(self):
        self.add_cmd_outputs([
            "systemctl show --all",
            "systemctl list-units",
            "systemctl list-units --failed",
            "systemctl list-units --all",
            "systemctl list-unit-files",
            "systemctl show-environment",
            "systemd-delta",
            "journalctl --verify",
            "journalctl --all --this-boot --no-pager",
            "journalctl --all --this-boot --no-pager -o verbose",
            "ls -l /lib/systemd",
            "ls -l /lib/systemd/system-shutdown",
            "ls -l /lib/systemd/system-generators",
            "ls -l /lib/systemd/user-generators"
        ])

        self.add_copy_specs([
            "/etc/systemd",
            "/lib/systemd/system",
            "/lib/systemd/user",
            "/etc/vconsole.conf",
            "/etc/yum/protected.d/systemd.conf"
        ])

# vim: et ts=4 sw=4
