from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['jen'] = 'Python'
favourite_languages['sarah'] = 'C'
favourite_languages['edward'] = 'Cpp'
favourite_languages['alex'] = 'ruby'

for name,language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")
    