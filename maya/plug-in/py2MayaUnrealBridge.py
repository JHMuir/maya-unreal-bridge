import sys
import maya.api.OpenMaya as om


def maya_useNewAPI():
    pass


class MayaUnrealBridge(om.MPxCommand):
    kPluginCmdName = "MayaUnrealBridge"

    def __init__(self):
        super().__init__()

    # instantiating the command
    @staticmethod
    def cmdCreator():
        return MayaUnrealBridge()

    # executes the command actions
    def doIt(self, args):
        print("This is a Plugin Test! Part 4")


# every plugin needs this function
def initializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    try:
        # "initializePlugin" will always call registerCommand
        pluginFn.registerCommand(
            MayaUnrealBridge.kPluginCmdName, MayaUnrealBridge.cmdCreator
        )
    except:
        sys.stderr.write(
            f"Failed to register command {MayaUnrealBridge.kPluginCmdName}\n"
        )
        raise


# every plugin needs this function
def uninitializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    try:
        # "uninitializePlugin" will always call deregisterCommand
        pluginFn.deregisterCommand(MayaUnrealBridge.kPluginCmdName)
    except:
        sys.stderr.write(
            "Failed to unregister command: %s\n" % MayaUnrealBridge.kPluginCmdName
        )
        raise
