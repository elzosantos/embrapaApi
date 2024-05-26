
from fastapi import FastAPI

import requests
from bs4 import BeautifulSoup

app = FastAPI()

from api.endpoints.endpoints import *

link = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}


req = requests.get(link, headers=head)
print(req)
site = BeautifulSoup(req.text, "html.parser")
pesquisa = site.find("table", class_="tb_base tb_dados")
print(pesquisa, get_text())


