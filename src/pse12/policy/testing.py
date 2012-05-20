from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig


class Pse12Policy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import pse12.policy
        xmlconfig.file('configure.zcml',
                       pse12.policy,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'pse12.policy:default')


PSE12_POLICY_FIXTURE = Pse12Policy()
PSE12_POLICY_INTEGRATION_TESTING = (
    IntegrationTesting(
        bases=(PSE12_POLICY_FIXTURE, ),
        name="Pse12Policy:Integration")
)
