'''
启动use_flask.py后 即可运行此程序
'''


import requests

requestHeaders = {
    'Content-Type': 'application/json'
}

requestBody = {'username': 'leoanrd', 'age': '18'}

requestParams = {'wd': '666'}

# response = requests.get('http://127.0.0.1:8890/tieba/', params=requestParams,headers=requestHeaders)


response = requests.post('http://127.0.0.1:8890/postApi/',headers=requestHeaders,json=requestBody)


if response.status_code == 200:
    print('请求成功')
    print(response.text)
else:
    print(f'请求失败，状态码: {response.status_code}')


