import json
obj=dict(name="小明",age=20)
s=json.dumps(obj,ensure_ascii=True)
t=json.dumps(obj,ensure_ascii=False)
print(s,t)