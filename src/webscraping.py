import os
from requests import get
from zipfile import ZipFile

CVM_URL = 'https://dados.cvm.gov.br/dados/FIDC/DOC/INF_MENSAL/DADOS/'
CVM_INF_MENSAL_FIDC = 'inf_mensal_fidc_{0}.zip'
CVM_INF_MENSAL_FIDC_TAB = 'inf_mensal_fidc_tab_{0}_{1}.csv'
DATA_FOLDER = 'data'

PERIODS = [
    '202112',
    '202201',
    '202202',
    '202203',
    '202204',
    '202205',
    '202206',
    '202207',
    '202208',
    '202209',
    '202210',
    '202211',
    '202212',
]

TABS_TO_EXTRACT = [
    'I', 'IV'
]

for period in PERIODS:
    path = os.path.dirname(__file__)
    filename = CVM_INF_MENSAL_FIDC.format(period)
    response = get(f'{CVM_URL}{filename}', stream = True)
    filename_abs_path = os.path.join(path, DATA_FOLDER, filename)
    
    with open(filename_abs_path, 'wb') as file:
        file.write(response.content)

    zip = ZipFile(filename_abs_path, 'r')
    for tab in TABS_TO_EXTRACT:
        zip.extract(CVM_INF_MENSAL_FIDC_TAB.format(tab, period),
                    path=os.path.dirname(filename_abs_path))

    zip.close()
    os.remove(filename_abs_path)


    


