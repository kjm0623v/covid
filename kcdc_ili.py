import requests
import pandas as pd


def flu(column):
    url = 'http://www.cdc.go.kr/npt/biz/npp/iss/influenzaListAjax.do'
    params = {
    'icdNm': 'influenza',
    'startYear': '2019',  # 몇 년 부터
    'endYear': '2020',  # 몇 년 까지
    'age': "",
    'ageText': '전체'  # 연령은 전체로
    }
    epiweek = 202000+column-17
    response = requests.post(url, params)
    datas = response.json()
    data = datas['data'][0]['COLUMN{}'.format(column)]
    data = [{
        'epiweek':epiweek,
        'wili':data,
        'issue':epiweek+1,
        'region':'ROK'
    }]
    data = pd.DataFrame(data)
    df = pd.read_csv('ILI_korea.csv', encoding='utf-8')
    kor_df = pd.merge(df, data, how='outer', left_on=['epiweek', 'wili', 'issue', 'region'], right_on=['epiweek', 'wili', 'issue', 'region'])
    kor_df.to_csv('ILI_korea1.csv', index=False, encoding='utf-8')
    return data