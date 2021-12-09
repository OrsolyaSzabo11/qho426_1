song = '''
Come on ladies, come on ladies
Come on ladies, come on ladies, 1 pound fish
Have, have a look, 1 pound fish
Have, have a look, 1 pound fish
Very very good, 1 pound fish
Very very cheap, 1 pound fish
6 for £5, or £1 each
6 for £5, or £1 each
Very very good and very very cheap,
One pound, one pound

Come on ladies, come on ladies
Come on ladies, come on ladies, 1 pound fish
Have, have a look, 1 pound fish
Have, have a look, 1 pound fish
Very very good, 1 pound fish
Very very cheap, 1 pound fish

Come on ladies, come on ladies
Come on ladies, come on ladies
Come on ladies, come on ladies, 1 pound fish
Come on ladies, come on ladies, 1 pound fish

Come on ladies, come on ladies, 1 pound fish

6 for £5, or £1 each
6 for £5, or £1 each
Very very good and very very cheap
One pound fish

Come on ladies, come on ladies, 1 pound fish
Come on ladies, come on ladies, 1 pound fish
'''

#l = song.split(",")
l = song.replace(",", ""). split()
print(l)
print("-"*20)
song_set = set(l)
print(song_set)
print(len(song_set))
dicto = {}
for i in l:
    dicto[i] = dicto.get(i, 0) + 1

print(dicto)
print(len(dicto))
#dicto["come"]
#come:1, on:1, ladies:1, 