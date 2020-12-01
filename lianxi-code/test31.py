# 单例模式
# 单例
# 如果想将贪婪模式变为非贪婪模式，就在正则后面加上？
import re
import request
path = 'src="https://timgsa.baidu.com/timg?image&amp;quality=80&amp;size=b9999_10000&amp;sec=1598782958735&amp;di' \
       '=223ff942e0892ab7c99d5daae77ea1b6&amp;imgtype=0&amp;src=http%3A%2F%2Fs4.sinaimg.cn%2Fmiddle' \
       '%2F50316f49taa97224f1023%26690" width="750" height="468" style="top: 152px; left: 65px; width: 360px; height: ' \
       '360px; cursor: pointer; display: block;" log-rightclick="p=5.102" title="点击查看源网页"> '
result = re.match(r'src="(.+)"', path)
print(result.group(1))

response = request.get(resultre)

'''with open('aa.jpg', wb) as wstream:
    wstream.write(response.content)'''

