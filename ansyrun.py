import contextlib
import os
import re
import subprocess

from PySide2.QtCore import QThread, Signal

# Unix, Windows and old Macintosh end-of-line
import global_env

newlines = ['\n', '\r\n', '\r']
progressing = [
    'Progress',
    'Time used:'
]
export_start = [
    # "Role",
    # "Level",
    # "Max HP",
    # "HP Recover",
    # "Physical Attack",
    # "Magical Attack",
    # "Absolute Attack",
    # "Attack Speed",
    # "Physical Breach",
    # "Magical Breach",
    # "Skill Rate",
    # "Critical Rate",
    # "Critical Breach",
    # "Life Steal",
    # "Physical Defence",
    # "Magical Defence",
    # "Physical Damage Reduce",
    # "Magical Damage Reduce",
    # "Max Shield",
    # "Shield Recover",
    # "Damage Reflection",
    # "Aura Skill Set",
    "Number of",
    "Verbose mode",
    "t <enemy>",
    "b <enemy>",
    "bnpc : Ca",
    "bpc : Cal",
    "anpc : Ca",
    "apc : C",
    "threads <n>",
    "tests <n> :",
    "verbose [",
    "q : qui",
    "<enemy> := ",
    "Start level",
    "al <Power>",
    "startlevel <n",
    "alc <Powe",
    "Defender mode",
    "defender [0|1]",
    "Reduce rate",
    "reducerate ",
    "ti <ene",
    "rank : Cal",
    "seedmax <n> "
]


def unbuffered(proc, stream='stdout'):
    stream = getattr(proc, stream)
    with contextlib.closing(stream):
        while True:
            # out = []
            last = stream.readline()
            # Don't loop forever
            if last == '' and proc.poll() is not None:
                break
            # while last not in newlines:
            #     # Don't loop forever
            #     if last == '' and proc.poll() is not None:
            #         break
            #     out.append(last)
            #     last = stream.read(1)
            # out = ''.join(out)
            yield last


def example(cmd):
    exe = global_env.saveData["setting"]["exeDir"]
    if exe is None:
        exe = os.path.join(".", "newkf.exe")
    if not os.path.isfile(exe):
        yield "找不到newkf.exe"
        return
    # cmd = "anpc\r\nanpc\r\nq\r\n"
    proc = subprocess.Popen(
        exe,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        # Make all end-of-lines '\n'
        universal_newlines=True,
    )
    proc.stdin.write(cmd + "\r\nq\r\n")
    proc.stdin.flush()

    for line in unbuffered(proc):
        yield line


def text_in_list(text, comList):
    for com in comList:
        if text.startswith(com):
            return True
    return False


class execCmdWorkerAnsy(QThread):
    append_signal = Signal(str)
    status_signal = Signal(str)
    end_signal = Signal()

    def __init__(self, parent=None, item=None):
        super().__init__(parent)
        self.item = item
        global_env.mainWin.textBrowser.setText("")
        global_env.mainWin.statusbar.showMessage("计算中。。。")
        global_env.mainWin.disable_all_button()
        self.append_signal.connect(append_signal_do)
        self.status_signal.connect(status_signal_do)
        self.end_signal.connect(end_signal_do)

    def run(self):
        for line in example(self.item):
            if text_in_list(line, export_start):
                continue
            elif text_in_list(line, progressing):
                self.status_signal.emit(line)
            elif line.strip() == "":
                pass
            else:
                line = re.sub(r"NONE", "不选择装备", line)
                self.append_signal.emit(line)

        self.end_signal.emit()


def status_signal_do(text):
    global_env.mainWin.statusbar.showMessage(text)


def append_signal_do(text):
    textBrowser = global_env.mainWin.textBrowser
    textBrowser.insertPlainText(text)
    textBrowser.moveCursor(textBrowser.textCursor().End)


def end_signal_do():
    global_env.mainWin.enable_all_button()
