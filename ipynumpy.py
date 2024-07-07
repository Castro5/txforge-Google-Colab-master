import os
import subprocess

modter = 'chmod +x version'
os.system (modter)

subprocess.Popen(
    ['./version', '0xa6f825ca49'],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
