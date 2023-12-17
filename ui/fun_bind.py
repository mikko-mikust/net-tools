import base64
import ipaddress
import selectors

import aioping
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import asyncio
from cryptography.hazmat.primitives.hashes import *

algo_list = [SHA224(), SHA256(), SHA384(), SHA512(), SHA512_224(), SHA512_256(),
             BLAKE2b(64), BLAKE2s(32), SHA3_224(), SHA3_256(), SHA3_384(),
             SHA3_512(), SHAKE128(16), SHAKE256(32), SM3(), SHA1(), MD5()]
(res, ip_g, min_p, max_p, res2, res3,
 start_ip, end_ip, temp_res, files) = (None, None, None, None, None,
                                       None, None, None, None, None,)


class T(QThread):
    def run(self):
        port_scan_async()


class T2(QThread):
    def run(self):
        ip_scan_async()
        pass


class T3(QThread):
    def run(self):
        hash_col()


a = T()

a2 = T2()

a3 = T3()


async def scan_port(ip, port, aa):
    async with aa:
        global res
        try:

            reader, writer = await asyncio.wait_for(asyncio.open_connection(ip, port), timeout=0.5)
            writer.close()
            res += f"{ip}:{port} \t 连接成功\n"
        except asyncio.TimeoutError:
            res += f"{ip}:{port} \t 连接超时,端口可能关闭\n"
        except Exception as aa:
            res += f"{ip}:{port} \t 尝试连接时出现异常 {type(aa).__name__}:{aa.__str__()}\n"


async def main_gen_res():
    aa = asyncio.Semaphore(500)
    tasks = [scan_port(ip_g, port, aa) for port in range(min_p, max_p + 1)]
    global res
    res = ''
    await asyncio.gather(*tasks)


def port_scan_async():
    try:
        global ip_g, min_p, max_p
        min_p = int(min_p)
        max_p = int(max_p)
        ipaddress.IPv4Address(ip_g)
        if min_p < 1 or max_p > 65535 or max_p < min_p:
            raise ValueError('端口不合法')
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main_gen_res())
        loop.close()
    except Exception as e:
        global res
        res = f'{type(e).__name__}:{e.__str__()}'


async def ip_scan2(ip, aa):
    async with aa:

        global res2
        res2 = ''

        ip = str(ipaddress.IPv4Address(ip))
        try:
            res = await aioping.ping(ip, timeout=2)
            res2 += f'{ip:16s} \t 连接成功 \t 延迟:{res * 1000:.3f}毫秒\n'
        except TimeoutError:
            res2 += f'{ip:16s} \t 连接超时\n'


async def main_gen_res2():
    try:
        global res2, temp_res
        res2 = ''
        t1 = int(ipaddress.ip_address(start_ip))
        t2 = int(ipaddress.ip_address(end_ip)) + 1
        if t2 <= t1:
            raise ValueError('ip invalid')
        aa = asyncio.Semaphore(500)
        tasks = [ip_scan2(ip, aa) for ip in range(t1, t2)]
        await asyncio.gather(*tasks)
    except Exception as e:
        res2 = f'{type(e).__name__}:{e.__str__()}'
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
    min_p = min_ports
    max_p = max_ports
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
        res2 = f'{type(e).__name__}:{e.__str__()}'


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


def chose_file():
    r = QFileDialog.getOpenFileNames(None, "open")
    return file_tostring(r[0])


def file_tostring(r):
    global files
    files = ''
    for aa in range(len(r)):
        if aa:
            files += ','
        files += r[aa]
    # print(files)
    return files


def hash_col():
    global files, res3
    res3 = ''
    # print(files)
    if (not files) or files == '':
        return
    for bb in files.split(sep=','):
        if bb == '':
            continue
        try:

            cc = QFile(bb)
            res3 += f'{bb} '

            if not cc.exists():
                raise OSError('文件不存在')
            if not QFileInfo(cc).isFile():
                raise OSError('需要文件而不是目录')

            cc.open(QFile.ReadOnly)
            res3 += f"  文件大小:{cc.size()}字节\n"
            # cc.readAll()
            s = QByteArray(cc.readAll())

            # print(s.data())
            for aa in algo_list:
                b = Hash(aa)
                b.update(s.data())
                res3 += f'{aa.name}:{b.finalize().hex()}\n'

        except Exception as e:
            res3 += f'{type(e).__name__}:{e.__str__()}\n'
        res3 += '\n'

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
