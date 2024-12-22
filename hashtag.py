import re

pattern = r'#\w+'

file = 'fichier.txt'
output_file = 'fichier1'

with open(file, 'r', encoding='utf-8') as fichier:
    contenu = fichier.read()

hashtags = re.findall(pattern, contenu)

with open(output_file, 'w', encoding='utf-8') as output:
    if hashtags:
        output.write("Les hashtags trouvés dans le fichier :\n")
        for hashtag in hashtags:
            output.write(hashtag + '\n')
    else:
        output.write("Aucun hashtag trouvé dans le fichier.\n")
