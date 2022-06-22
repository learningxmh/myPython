import yaml

file = open('../data/data.yaml', 'r', encoding='utf-8')
values = yaml.load(stream=file, Loader=yaml.FullLoader)
for i in values:
    print(i)
print(type(values))
