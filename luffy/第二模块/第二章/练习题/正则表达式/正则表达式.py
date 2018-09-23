# 利用正则表达式提取到 luffycity.com ，内容如下
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="UTF-8">
# <title>luffycity.com</title>
# </head>
# <body>
# </body>
# </html>

import re
f = open('index.html','r',encoding='utf-8')
data = f.read()
print(re.findall('luffycity.com',data))