# This is a template
# Saved as .py for easier editing
#from __future__ import unicode_literals

# pylint: disable=import-error, no-name-in-module, too-many-format-args, undefined-variable

import os
import subprocess
from uds.forward import forward  # @UnresolvedImport
from os.path import expanduser

from uds import tools  # @UnresolvedImport


forwardThread, port = forward(sp['tunHost'], sp['tunPort'], sp['tunUser'], sp['tunPass'], sp['ip'], sp['port'])

if forwardThread.status == 2:
    raise Exception('Unable to open tunnel')

tools.addTaskToWait(forwardThread)
# Care, expanduser is encoding using "mcbs", so treat it as bytes always
home = expanduser('~').replace('\\', '\\\\') + '#1;'
keyFile = tools.saveTempFile(sp['key'])
theFile = sp['xf'].format(export=home, keyFile=keyFile.replace('\\', '/'), ip='127.0.0.1', port=port)
filename = tools.saveTempFile(theFile)

x2goPath = os.environ['PROGRAMFILES(X86)'] + '\\x2goclient'
executable = tools.findApp('x2goclient.exe', [x2goPath])
if executable is None:
    raise Exception('''<p>You must have installed latest X2GO Client in default program file folder in order to connect to this UDS service.</p>
<p>You can download it for windows from <a href="http://wiki.x2go.org/doku.php">X2Go Site</a>.</p>''')

subprocess.Popen([executable, '--session-conf={}'.format(filename), '--session=UDS/connect', '--close-disconnect', '--hide', '--no-menu', '--add-to-known-hosts'])
