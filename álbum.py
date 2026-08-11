def make_album(artista, album, musicas=''):
    if musicas:
        informações={'Artista': artista, 'Álbum': album, 'Músicas': musicas}
    else:
        informações={'Artista': artista, 'Álbum': album}
    return informações

musica=make_album('Andrea Bocelli', 'Con te partiro')
print(musica)

musica2=make_album('Andrea Bocelli', 'Con te partiro', 12)
print(musica2)

