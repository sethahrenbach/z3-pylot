import subprocess
import os
from pathlib import Path

path = Path(os.getcwd()).parent
z3 = str(path) + r"/resources/z3.exe"
af447 = str(path) + r"/resources/af447.smt2"
out = str(subprocess.Popen([z3, af447], stdout=subprocess.PIPE).communicate()[0]).strip("b'\\r\\n").split(r'\r\n')
print(out)