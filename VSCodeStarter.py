import subprocess
import os
import pdb
bp = pdb.set_trace


# home_path= r'"C:\Users\qiliang.huang\AppData\Local\Programs\Microsoft VS Code\Code.exe"'

home_path = r'"C:\Users\ps\AppData\Local\Programs\Microsoft VS Code\Code.exe"'

cur_path = os.path.abspath(os.path.dirname(__file__))

command = f"""
 {home_path} {cur_path}
"""
def run_command(command):
    command = command.strip()
    sb = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    subprocess_return = sb.stdout.read()
    result = subprocess_return.decode(encoding='utf-8')
    return result


print(command)

result = run_command(command)

# bp()