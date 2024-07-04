import configparser
config = configparser.ConfigParser()
# config['default'] = {'ServerAliveInterval':'45',
#                      'Compression':'yes',
#                      'CompressionLevel':'9'}
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {'port':'50022',
#                                 'Forwardx11':'no'}
# with open('assets/example.ini','w') as configfile:
#     config.write(configfile)


print(config.read('assets/example.ini'))
# print(config.sections())
# print(config.options('default'))
# print(config.items('topsecret.server.com'))


#删除整个标题
config.remove_section('bitbucket.org')

#删除标题下的option
config.remove_option('topsecret.server.com','port')

#添加一个标题
config.add_section('info')
#在标题下添加options
config.set('info','name','derek')

#判断是否存在
print(config.has_section('info'))        #True
print(config.has_option('info','name'))    #True

#将修改的内容存入文件
config.write(open('assets/new_example.ini','w'))


