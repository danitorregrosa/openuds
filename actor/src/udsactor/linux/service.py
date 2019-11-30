# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2019 Virtual Cable S.L.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#    * Neither the name of Virtual Cable S.L. nor the names of its contributors
#      may be used to endorse or promote products derived from this software
#      without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
@author: Adolfo Gómez, dkmaster at dkmon dot com
'''
import signal
import typing

from . import operations
from . import daemon

from ..log import logger
from ..service import CommonService


try:
    from prctl import set_proctitle  # @UnresolvedImport
except ImportError:  # Platform may not include prctl, so in case it's not available, we let the "name" as is
    def set_proctitle(_):
        pass


class UDSActorSvc(daemon.Daemon, CommonService):
    def __init__(self, args=None) -> None:
        daemon.Daemon.__init__(self, '/var/run/udsactor.pid')
        CommonService.__init__(self)

        # Captures signals so we can stop gracefully
        signal.signal(signal.SIGINT, self.markForExit)
        signal.signal(signal.SIGTERM, self.markForExit)

    def markForExit(self, signum, frame) -> None:
        self._isAlive = False

    def joinDomain(  # pylint: disable=unused-argument, too-many-arguments
            self,
            name: str,
            domain: str,
            ou: str,
            account: str,
            password: str
        ) -> None:
        logger.fatal('Join domain is not supported on linux platforms right now')

    def run(self) -> None:
        logger.debug('Running Daemon: {}'.format(self._isAlive))
        set_proctitle('UDSActorDaemon')

        # Linux daemon will continue running unless something is requested to
        if not self.initialize():
            self.notifyStop()
            return # Stop daemon if initializes told to do so

        logger.debug('Initialized, setting ready')
        # Initialization is done, set machine to ready for UDS, communicate urls, etc...
        self.setReady()

        # *********************
        # * Main Service loop *
        # *********************
        # Counter used to check ip changes only once every 10 seconds, for
        # example
        counter = 0
        while self._isAlive:
            counter += 1
            if counter % 10 == 0:
                self.checkIpsChanged()
            # In milliseconds, will break
            self.doWait(1000)

        self.notifyStop()