import untangle

obj = untangle.parse('data.xml')

# 获取第一个p标签
obj.set.l.p[0]
# 获取第一个p标签的名字
obj.set.l.p[0].['name']
# 获取el标签内容
obj.set.d.el.__dict__['cdata']
