from util.api import Api

data_sets = Api('datasets')

print(data_sets.get_trainset('59c3a7afadc71eb86c8956eb', format='pascalvoc'))
