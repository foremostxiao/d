# 此模块用于生成和修改常见配置文档，
# 当前模块的名称在 python 3.x 版本中变更为 configparser。
import configparser
config = configparser.ConfigParser() #

config.read('db.ini')
print(config.sections())
print(config.default_section)

print(config['bitbucket.org']['User'])
print('------------------------------------')
#循环节点下的值
for k in config['bitbucket.org']:
    print(k)
print('-----------------------------------')
for k,v in config['bitbucket.org'].items():
    print(k,v)
print('----------------------------')
if 'user' in  config['bitbucket.org']:
    print('in')

print('----------------------------')

# 添加，在已有的目录下添加
config['bitbucket.org']['user2'] = 'xiao'
config.write(open('db.ini','w'))

# 添加一个目录
# config.add_section('xiao.org')
# config.write(open('db.ini','w'))

# 删除
# 1
config.remove_section('xiao.org')
config.write(open('db.ini','w'))

#2 删除子目录
config.remove_option('bitbucket.org','user2')
config.write(open('db.ini','w'))
