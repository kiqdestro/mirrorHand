# In Maya, via Python:
# Modulo de comunicacao com o Maya
# Esse modulo deve ser rodado no script editor do Maya
# Joao Carlos Cardoso - 2019
import maya.cmds as mc
import maya.mel as mm

# Boilerplate retirado da internet - Creditos # Eric Pavey - 2011-01-26
# Our mel global proc.
melproc = """
global proc portData(string $arg){
    python(("portData(\\"" + $arg + "\\")"));
}
"""
mm.eval(melproc)

# Our Python function that can be changed to do whatever we want:
def portData(arg):
    """
    Read the 'serial' data passed in from the commandPort
    """
    print "Received!: ", arg

    # Some silly example code to scale a sphere:
    mappedVal = (float(arg)/1023.0) * 10
    if mc.objExists('joint1'):
        mc.setAttr('joint1.RotateY', mappedVal)

# Open the commandPort.  The 'prefix' argument string is calling to the defined
# mel script above (which then calls to our Python function of the same name):
mc.commandPort(name="127.0.0.1:7777", echoOutput=False, noreturn=False,
               prefix="portData", returnNumCommands=True)