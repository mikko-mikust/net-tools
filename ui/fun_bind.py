import copy

from PySide6.QtWidgets import *
from PySide6.QtCore import *
import asyncio
res=None


async def scan_port(ip, port):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        writer.close()
        return f"{ip}:{port}, State: Open"
    except (OSError, asyncio.TimeoutError):
        return f"{ip}:{port}, State: Closed"


async def main(ip, min_ports, max_ports):
    tasks = [scan_port(ip, port) for port in range(min_ports, max_ports)]
    results=await asyncio.gather(*tasks)
    global res
    res=''
    for it in results:
        res+=it
        res+='\n'


def port_scan_async(ip="127.0.0.1", min_ports=1, max_ports=1024):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(main(ip=ip, min_ports=min_ports, max_ports=max_ports))
    #print(res)
    loop.close()
def ui_show(aa,wigets):
    #print(aa)
    for bb in range(len(wigets)):
        if bb == aa:
            wigets[bb].show()
        else:
            wigets[bb].hide()

def show_info(self,title='提示'):
    print(str(self))
    word = self.text()
    QMessageBox().information(self, title, word+' you home', QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)
