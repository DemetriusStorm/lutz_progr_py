"""
Реализация веб-сервера на языке Python, способная запускать серверные
CGI-сценарии на языке Python; обслуживает файлы и сценарии в текущем
рабочем каталоге; сценарии на языке Python должны находиться в каталоге
webdir\cgi-bin или webdir\htbin;
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

web_dir = '.'               # место, где находятся файлы html и подкаталог cgi-bin
port = 80                   # по умолчанию http://localhost/, иначе используйте http://localhost:XXXX/
os.chdir(web_dir)           # перейти в корневой каталог HTML
srv_adr = ("", port)        # имя хоста и номер порта
srv_obj = HTTPServer(srv_adr, CGIHTTPRequestHandler)
srv_obj.serve_forever()     # запустить как бесконечный фоновый процесс
