'''
Flask 轻量级webapp框架

像springboot一样快速启动一个webApp

'''


from flask import Flask,request,Response,jsonify

app = Flask(__name__)

class JsonResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response,dict):
            response = jsonify(response)
        return super(JsonResponse, cls).force_type(response,environ)

app.response_class = JsonResponse

# Get 请求
@app.route('/')
def hello_world():
    return '<b>Hello World</b>'

# http://127.0.0.1:8890/tieba/?wd=666
@app.route('/tieba/')
def tieba():
    # 获取 header
    headers = request.headers
    for key, value in headers.items():
        print(f"{key}: {value}")

    wd = request.args.get('wd')
    return '获取的参数的是%s'%wd

@app.route('/p/<id>/')
def article_detail(id):
    return '你访问的文章第%s篇'%id

@app.route('/<any(blog,user):url_path>/<id>')
def detail(url_path,id):
    if url_path == 'blog':
        return '博客详情%s'%id
    else:
        return '用户详情%s'%id
    
# 127.0.0.1:8890/article/baidu.com/
@app.route('/article/<path:test>/')
def test_article(test):
    return 'test_article:{}'.format(test)

# Post 请求
@app.route('/postApi/', methods=['POST'])
def post_api():
    print(request.get_json()) # {'username': 'leoanrd', 'age': '18'}
    return request.get_json() # 返回的是非字符、非元祖、非Response对象，所以执行force_type方法


if __name__ == '__main__':
    app.run(port=8890,debug=True)

