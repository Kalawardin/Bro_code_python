# dictionary = A changeable, unordered collection of unique key: value pairs
#              fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'} 

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')

#print(capitals['Germany']) #--> addressing dictionary
#print(capitals.get('Germany')) #-->check dictionry
#print(capitals.keys()) #-->shows keys
#print(capitals.items()) #--> shows items

for key,value in capitals.items():
    print(key,value)

