SECRET_KEY = "123456@789"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20
DATABASE_PATH = "/database/embrapa_base.db"
DATABASE_URL = "sqlite:///dados/embrapa_base.db"
URL_BASE = 'http://vitibrasil.cnpuv.embrapa.br'
TIMEOUT_REQUEST = 5

DICT_OPTIONS = {
    "producao":"opt_02",
    "comercializacao":"opt_04",
    "processamento":"opt_03",
    "importacao":"opt_05",
    "exportacao":"opt_06",
}

DICT_SUBOPTIONS = {
    "processamento":{
        'Viniferas':'subopt_01',
        'Americanas':'subopt_02',
        'Mesas':'subopt_03',
        'SClass':'subopt_04',
    },
    "importacao":{
        "Vinhos":"subopt_01",
        "Espumantes":"subopt_02",
        "Frescas":"subopt_03",
        "Passas":"subopt_04",
        "Suco":"subopt_05",
    },
    "exportacao":{
        "Vinho":"subopt_01",
        "Espumantes":"subopt_02",
        "Suco":"subopt_03",
        "Uva":"subopt_04",
    },
}

DADOS_BASE = [
    'Producao.csv',
    'Comercio.csv',
    'ExpVinho.csv',
    'ExpEspumantes.csv',
    'ExpUva.csv',
    'ExpSuco.csv',
    'ImpVinhos.csv',
    'ImpEspumantes.csv',
    'ImpFrescas.csv',
    'ImpPassas.csv',
    'ImpSuco.csv',
    'ProcessaViniferas.csv',
    'ProcessaAmericanas.csv',
    'ProcessaMesa.csv',
    'ProcessaSemclass.csv',
]

COLUNAS_COMERCIO = [
    'id', 'controle', 'produto',
    '1970','1971','1972','1973','1974',
    '1975','1976','1977','1978','1979',
    '1980','1981','1982','1983','1984',
    '1985','1986','1987','1988','1989',
    '1990','1991','1992','1993','1994',
    '1995','1996','1997','1998','1999',
    '2000','2001','2002','2003','2004',
    '2005','2006','2007','2008','2009',
    '2010','2011','2012','2013','2014',
    '2015','2016','2017','2018','2019',
    '2020','2021','2022'
]