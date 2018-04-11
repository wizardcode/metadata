import httplib
import hashlib
import urllib
import random
import json
import re
appKey = '6692283e75add57f'
secretKey = '0amnD80YXqcAkZ1YPMGrOISO3nQQME1a'


def translate(value):
    p = re.compile(r'([a-z]|\d)([A-Z])')
    sub = re.sub(p, r'\1 \2', value)

    httpClient = None
    myurl = '/api'
    q = sub
    fromLang = 'EN'
    toLang = 'zh-CHS'
    salt = random.randint(1, 65536)

    sign = appKey + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = httplib.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        info=response.read()
        return result(info)
    except Exception, e:
        return e
    finally:
        if httpClient:
            httpClient.close()

def result(name):
    data = json.loads(name)
    if data['errorCode'] =='0':
        return data['translation'][0]
    else:
        return ''