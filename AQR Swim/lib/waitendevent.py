#Wait end event execution
from subprocess import Popen
import filehandling,os,sys


myp = os.path.dirname(sys.argv[0]) + os.sep
main = myp.split("lib")[0] +os.sep
temp = main + "temp" +os.sep
lib = main + "lib" +os.sep
result_p = main + "results" +os.sep


ExpName, ft,wt,mt,temperature,salinity, UNIXtime, Dateime = filehandling.GetExperimentInfo()
print mt
# Popen(["python", lib + os.sep +"aquabeep.py", mt])