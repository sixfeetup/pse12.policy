from sixfeetup.utils import helpers as sfutils


def importVariousInitial(context):
    """Run the setup handlers for the initial profile"""
    if context.readDataFile('pse12_policy-initial.txt') is None:
        return
    members = [
        {'id': 'staff',
         'password': 'staff',
         'roles': ['Manager', 'Member'],
         'properties': {
             'email': 'changeme@example.com',
             'fullname': 'pse12 Staff',
             'username': 'staff'
         }
        }
    ]
    sfutils.addUserAccounts(members)


def importVarious(context):
    """Run the setup handlers for the default profile"""
    if context.readDataFile('pse12_policy-default.txt') is None:
        return
    # automagically run a plone migration if needed
    sfutils.runPortalMigration()
    # automagically run the upgrade steps for this package
    sfutils.runUpgradeSteps(u'pse12.policy:default')
