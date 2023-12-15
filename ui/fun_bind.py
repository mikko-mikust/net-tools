import base64
import ipaddress
import aioping
# from PySide6.QtWidgets import *
# from PySide6.QtGui import *
from PySide6.QtCore import QThread
import asyncio

(res, ip_g, min_p, max_p, res2,
 start_ip, end_ip, temp_res) = (None, None, None,
                                None, None, None, None, None,)

semp = asyncio.Semaphore(500)


class T(QThread):
    def run(self):
        port_scan_async()


class T2(QThread):
    def run(self):
        ip_scan_async()
        pass


async def scan_port(ip, port, aa):
    async with aa:
        try:
            reader, writer = await asyncio.open_connection(ip, port)
            writer.close()
            return f"{ip}:{port}, State: Open"
        except (OSError, asyncio.TimeoutError):
            return f"{ip}:{port}, State: Closed"


async def main_gen_res():
    tasks = [scan_port(ip_g, port, semp) for port in range(min_p, max_p + 1)]
    results = await asyncio.gather(*tasks)
    global res
    res = ''
    for it in results:
        res += it
        res += '\n'


def port_scan_async():
    try:

        ipaddress.IPv4Address(ip_g)
        if min_p < 1 or max_p > 65535:
            raise ValueError('port invalid')
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main_gen_res())
        # print(res)
        loop.close()
    except Exception as e:
        global res
        res = '%s:%s' % (type(e).__name__, e.__str__())


a = T()

a2 = T2()


async def ip_scan2(ip, aa):
    async with aa:
        global temp_res

        ip = str(ipaddress.IPv4Address(ip))
        try:
            await aioping.ping(ip)
            temp_res.append(f'{ip} alive\n')
        except TimeoutError:
            temp_res.append(f'{ip} dead\n')


async def main_gen_res2():
    try:
        global res2, temp_res
        res2 = ''
        t1 = int(ipaddress.ip_address(start_ip))
        t2 = int(ipaddress.ip_address(end_ip)) + 1
        if t2 <= t1:
            raise ValueError('ip invalid')

        temp_res = []
        tasks = [ip_scan2(ip, semp) for ip in range(t1, t2)]
        await asyncio.gather(*tasks)
        for it in temp_res:
            res2 += it
    except Exception as e:
        res2 = '%s:%s' % (type(e).__name__, e.__str__())
        # print(res2)
    pass


def ip_scan_async():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main_gen_res2())
    # print(res)
    loop.close()


def port_scan2(ip="127.0.0.1", min_ports=1, max_ports=1024):
    global ip_g, min_p, max_p
    ip_g = ip
    min_p = int(min_ports)
    max_p = int(max_ports)
    global a
    a.start()


def ip_scan(start, end):
    try:
        global start_ip, end_ip

        start_ip = ipaddress.IPv4Address(start)
        end_ip = ipaddress.IPv4Address(end)
        a2.start()
    except Exception as e:
        global res2
        res2 = '%s:%s' % (type(e).__name__, e.__str__())


def ui_show(aa, widgets):
    # print(aa)
    for bb in range(len(widgets)):
        if bb == aa:
            widgets[bb].show()
        else:
            widgets[bb].hide()


def swap_text(x, y):
    aa = x.toPlainText()
    bb = y.toPlainText()
    x.setPlainText(bb)
    y.setPlainText(aa)


def b64_enc_text(x, y):
    bb = base64.b64encode(y.toPlainText().encode('UTF-8')).decode('UTF-8')
    # print(bb)
    x.setPlainText(str(bb))


def b64_dec_text(x, y):
    bb = base64.b64decode(x.toPlainText().encode('UTF-8')).decode('UTF-8')
    # print(bb)
    y.setPlainText(str(bb))

# def show_info(title='提示', word=''):
#     QMessageBox().information(QWidget(), title, word, QMessageBox.StandardButton.Ok)
#
#
# def show_warn(title='警告', word=''):
#     QMessageBox().warning(QWidget(), title, word, QMessageBox.StandardButton.Ok)
#
#
# def show_err(title='错误', word=''):
#     QMessageBox().critical(QWidget(), title, word, QMessageBox.StandardButton.Ok)
