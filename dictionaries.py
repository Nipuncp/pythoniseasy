#This program prints the name and meta data of a song

songMeta = {'SongName' : "Devakanyaka", 'Genre' : "Classical", 
                'Durationinseconds' : 214, 'NoOfWords' : 42, 'Tempo' : 4.2,
                'Artist' : "Yesudas", 'AlbumName' : "Ee puzhayum kadannu",
                'CoSinger' : "Sujatha", 'Language' : "Malayalam"}

for key in songMeta:
    print(key,':',songMeta[key])