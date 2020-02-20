import os
import subprocess
import re

import global_env


def execCmd():
    # cmd = os.path.join(".", "newkf.exe")
    cmd = global_env.saveData["setting"]["exeDir"]
    if cmd == None:
        cmd = os.path.join(".", "newkf.exe")
    if not os.path.isfile(cmd):
        return ["找不到newkf.exe"]
    p1 = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # p2=subprocess.Popen('bnpc',shell=True,stdin=p1.stdout,stdout=subprocess.PIPE)
    (stdoutdata, stderrdata) = p1.communicate(b"bnpc\nbpc")
    p1.wait()
    mystr = str(stdoutdata, encoding="utf8")
    result_list = re.findall(r'<NPCType> <Level> <Power>(.*?)t <enemy>', mystr, re.S)
    if len(result_list) == 0:
        return [mystr]
    # print(mystr)
    # writeFile("mylog", mystr)
    # return stdoutdata
    return result_list
