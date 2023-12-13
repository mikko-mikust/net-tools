import base64
import copy
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import asyncio

res,ip_g,min_p,max_p=None,None,1,100,
class T(QThread):
    def run(self):
        port_scan_async()


async def scan_port(ip, port):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        writer.close()
        return f"{ip}:{port}, State: Open"
    except (OSError, asyncio.TimeoutError):
        return f"{ip}:{port}, State: Closed"


async def main():
    tasks = [scan_port(ip_g, port) for port in range(min_p, max_p)]
    results=await asyncio.gather(*tasks)
    global res
    res=''
    for it in results:
        res+=it
        res+='\n'

def port_scan_async():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    #print(res)
    loop.close()

a=T()
def port_scan2(ip="127.0.0.1", min_ports=1, max_ports=1024):
    global ip_g, min_p, max_p
    ip_g = ip
    min_p = min_ports
    max_p = max_ports
    global a
    a.start()
def ui_show(aa,wigets):
    #print(aa)
    for bb in range(len(wigets)):
        if bb == aa:
            wigets[bb].show()
        else:
            wigets[bb].hide()
def swap_text(x,y):
    aa=x.toPlainText()
    bb=y.toPlainText()
    x.setPlainText(bb)
    y.setPlainText(aa)
def b64_enc_text(x,y):
    bb = base64.b64encode(y.toPlainText().encode('UTF-8')).decode('UTF-8')
    print(bb)
    x.setPlainText(str(bb))
def b64_dec_text(x,y):
    bb = base64.b64decode(x.toPlainText().encode('UTF-8')).decode('UTF-8')
    print(bb)
    y.setPlainText(str(bb))
def show_info(self,title='提示'):
    print(str(self))
    word = self.text()
    QMessageBox().information(self, title, word+' you home', QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)


