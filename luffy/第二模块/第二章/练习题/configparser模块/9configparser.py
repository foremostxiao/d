import configparser
config =configparser.ConfigParser()
config.read('my.cnf.ini')
print(config.sections())

print(config.default_section)

# 修改时区 default-time-zone = '+8:00' 为 校准的全球时间 +00:00
config['mysqld']['default-time-zone'] = '+00:00'
config.write(open('my.cnf.ini','w'))

# 删除 explicit_defaults_for_timestamp = true
config.remove_option('mysqld','explicit_defaults_for_timestamp = true')
config.write(open('my.cnf.ini','w'))

# 为DEFAULT增加一条 character-set-server = utf8
config['DEFAULT']['character-set-server'] = 'utf8'
config.write(open('my.cnf.ini','w'))


print('se_keys:',config.options('mysqld'))