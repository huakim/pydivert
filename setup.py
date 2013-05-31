#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2013  Fabio Falcinelli
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
__author__ = 'fabio'

from setuptools import setup

setup(name='pydivert',
      version='0.0.1a',
      description='Python library to divert tcp/udp/icmp packets',
      author='Fabio Falcinelli',
      author_email='fabio.falcinelli@gmail.com',
      url='https://github.com/ffalcinelli/pydivert',
      packages=['pydivert', ],
      package_dir={'pydivert': 'pydivert'},
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Win32 (MS Windows)',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Intended Audience :: Telecommunications Industry',
          'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
          #'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows :: Windows Vista',
          'Operating System :: Microsoft :: Windows :: Windows Server 2008',
          'Operating System :: Microsoft :: Windows :: Windows 7',
          #'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Networking :: Firewalls',
          'Topic :: System :: Networking :: Monitoring',
          'Topic :: Utilities',
      ],
      setup_requires=['nose'],
      test_suite='nose.collector',
)