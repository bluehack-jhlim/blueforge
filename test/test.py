from blueforge.api import Api

whatsit_api = Api('whatsit')

print(whatsit_api.get_trainset('59c3a7afadc71eb86c8956eb', format='pascalvoc'))
print(whatsit_api.get_dataset('59c37325abc7c600134297c5'))
