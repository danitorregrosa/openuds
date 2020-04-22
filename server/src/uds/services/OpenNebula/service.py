# -*- coding: utf-8 -*-

#
# Copyright (c) 2012-2019 Virtual Cable S.L.
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

"""
.. moduleauthor:: Adolfo Gómez, dkmaster at dkmon dot com
"""
import logging
import typing

from django.utils.translation import ugettext_noop as _
from uds.core.transports import protocols
from uds.core.services import Service, types as serviceTypes
from uds.core.util import validators
from uds.core.ui import gui

from .publication import LivePublication
from .deployment import LiveDeployment

# Not imported at runtime, just for type checking
if typing.TYPE_CHECKING:
    from . import on
    from .provider import OpenNebulaProvider
    from uds.core import Module

logger = logging.getLogger(__name__)


class LiveService(Service):
    """
    Opennebula Live Service
    """
    # : Name to show the administrator. This string will be translated BEFORE
    # : sending it to administration interface, so don't forget to
    # : mark it as _ (using ugettext_noop)
    typeName = _('OpenNebula Live Images')
    # : Type used internally to identify this provider
    typeType = 'openNebulaLiveService'
    # : Description shown at administration interface for this provider
    typeDescription = _('OpenNebula live images based service')
    # : Icon file used as icon for this provider. This string will be translated
    # : BEFORE sending it to administration interface, so don't forget to
    # : mark it as _ (using ugettext_noop)
    iconFile = 'provider.png'

    # Functional related data

    # : If the service provides more than 1 "deployed user" (-1 = no limit,
    # : 0 = ???? (do not use it!!!), N = max number to deploy
    maxDeployed = -1
    # : If we need to generate "cache" for this service, so users can access the
    # : provided services faster. Is usesCache is True, you will need also
    # : set publicationType, do take care about that!
    usesCache = True
    # : Tooltip shown to user when this item is pointed at admin interface, none
    # : because we don't use it
    cacheTooltip = _('Number of desired machines to keep running waiting for an user')

    # : If the service needs a s.o. manager (managers are related to agents
    # : provided by services itselfs, i.e. virtual machines with actors)
    needsManager = True
    # : If true, the system can't do an automatic assignation of a deployed user
    # : service from this service
    mustAssignManually = False
    canReset = True

    # : Types of publications (preparated data for deploys)
    # : In our case, we do no need a publication, so this is None
    publicationType = LivePublication
    # : Types of deploys (services in cache and/or assigned to users)
    deployedType = LiveDeployment

    allowedProtocols = protocols.GENERIC + (protocols.SPICE,)
    servicesTypeProvided = (serviceTypes.VDI,)

    # Now the form part
    datastore = gui.ChoiceField(
        label=_("Datastore"),
        order=100,
        tooltip=_('Service clones datastore'),
        required=True
    )

    template = gui.ChoiceField(
        label=_("Base Template"),
        order=110,
        tooltip=_('Service base template'),
        tab=_('Machine'),
        required=True
    )

    baseName = gui.TextField(
        label=_('Machine Names'),
        rdonly=False,
        order=111,
        tooltip=_('Base name for clones from this machine'),
        tab=_('Machine'),
        required=True
    )

    lenName = gui.NumericField(
        length=1,
        label=_('Name Length'),
        defvalue=5,
        order=112,
        tooltip=_('Size of numeric part for the names of these machines'),
        tab=_('Machine'),
        required=True
    )

    def initialize(self, values: 'Module.ValuesType') -> None:
        """
        We check here form values to see if they are valid.

        Note that we check them throught FROM variables, that already has been
        initialized by __init__ method of base class, before invoking this.
        """
        if not values:
            return

        self.baseName.value = validators.validateHostname(self.baseName.value, maxLength=15-self.lenName.num(), asPattern=True)

    def parent(self) -> 'OpenNebulaProvider':
        return typing.cast('OpenNebulaProvider', super().parent())

    def initGui(self) -> None:
        """
        Loads required values inside
        """

        t: 'on.types.TemplateType'
        self.template.setValues(
            [gui.choiceItem(t.id, t.name) for t in self.parent().getTemplates()]
        )

        d: 'on.types.StorageType'
        self.datastore.setValues(
            [gui.choiceItem(d.id, d.name) for d in self.parent().getDatastores()]
        )

    def sanitizeVmName(self, name: str) -> str:
        return self.parent().sanitizeVmName(name)

    def makeTemplate(self, templateName: str) -> str:
        return self.parent().makeTemplate(self.template.value, templateName, self.datastore.value)

    def checkTemplatePublished(self, templateId: str) -> bool:
        return self.parent().checkTemplatePublished(templateId)

    def deployFromTemplate(self, name: str, templateId: str) -> str:
        """
        Deploys a virtual machine on selected cluster from selected template

        Args:
            name: Name (sanitized) of the machine
            comments: Comments for machine
            templateId: Id of the template to deploy from
            displayType: 'vnc' or 'spice'. Display to use ad OpenNebula admin interface
            memoryMB: Memory requested for machine, in MB
            guaranteedMB: Minimum memory guaranteed for this machine

        Returns:
            Id of the machine being created form template
        """
        logger.debug('Deploying from template %s machine %s', templateId, name)
        # self.datastoreHasSpace()
        return self.parent().deployFromTemplate(name, templateId)

    def removeTemplate(self, templateId: str) -> None:
        """
        invokes removeTemplate from parent provider
        """
        self.parent().removeTemplate(templateId)

    def getMachineState(self, machineId: str) -> 'on.types.VmState':
        """
        Invokes getMachineState from parent provider
        (returns if machine is "active" or "inactive"

        Args:
            machineId: If of the machine to get state

        Returns:
            one of this values:
             unassigned, down, up, powering_up, powered_down,
             paused, migrating_from, migrating_to, unknown, not_responding,
             wait_for_launch, reboot_in_progress, saving_state, restoring_state,
             suspended, image_illegal, image_locked or powering_down
             Also can return'unknown' if Machine is not known
        """
        return self.parent().getMachineState(machineId)

    def getMachineSubstate(self, machineId: str) -> int:
        """
        On OpenNebula, the machine can be "active" but not "running".
        Any active machine will have a LCM_STATE, that is what we get here
        """
        return self.parent().getMachineSubstate(machineId)

    def startMachine(self, machineId: str) -> None:
        """
        Tries to start a machine. No check is done, it is simply requested to OpenNebula.

        This start also "resume" suspended/paused machines

        Args:
            machineId: Id of the machine

        Returns:
        """
        self.parent().startMachine(machineId)

    def stopMachine(self, machineId: str) -> None:
        """
        Tries to stop a machine. No check is done, it is simply requested to OpenNebula

        Args:
            machineId: Id of the machine

        Returns:
        """
        self.parent().stopMachine(machineId)

    def suspendMachine(self, machineId: str) -> None:
        """
        Tries to suspend machine. No check is done, it is simply requested to OpenNebula

        Args:
            machineId: Id of the machine

        Returns:
        """
        self.parent().suspendMachine(machineId)

    def resetMachine(self, machineId: str) -> None:
        self.parent().resetMachine(machineId)

    def removeMachine(self, machineId: str) -> None:
        """
        Tries to delete a machine. No check is done, it is simply requested to OpenNebula

        Args:
            machineId: Id of the machine

        Returns:
        """
        self.parent().removeMachine(machineId)

    def getNetInfo(self, machineId: str, networkId: typing.Optional[str] = None) -> typing.Tuple[str, str]:
        """
        Changes the mac address of first nic of the machine to the one specified
        """
        return self.parent().getNetInfo(machineId, networkId=None)

    def getBaseName(self) -> str:
        """
        Returns the base name
        """
        return self.baseName.value

    def getLenName(self) -> int:
        """
        Returns the length of numbers part
        """
        return self.lenName.num()

    def getConsoleConnection(self, machineId: str) -> typing.Dict[str, typing.Any]:
        return self.parent().getConsoleConnection(machineId)

    def desktopLogin(self, machineId: str, username: str, password: str, domain: str) -> typing.Dict[str, typing.Any]:
        return self.parent().desktopLogin(machineId, username, password, domain)