from Libraryapp.models import Literary_genres
from Libraryapp.Serializers.LiteraryGenreSerializer import LiteraryGenresSerializer
from Libraryapp.utils.functions import log_print

def register_new_literary_genre(request_data):
    try:
        log_print("Passando request_data para o serializer")
        print(request_data)
        literary_genre = LiteraryGenresSerializer(data=request_data)

        if literary_genre.is_valid():
            log_print(f"Salvando no banco")
            literary_genre.save()
            return True
        
        return False

    except Exception as e:
        log_print(f"exception args:  {e.args}")
        log_print(f"Erro ao cadastrar, erro -> {type(e).__name__}")
        return False 
    

def delete_literary_genre(pk):
    try:
        log_print("Procurando id no banco")
        literary_genre = Literary_genres.objects.get(id=pk)
        
        log_print("Deletando literary_genre")
        literary_genre.delete()

        return True
    except Exception as e:
        log_print(f"exception args:  {e.args}")
        log_print(f"Erro ao deletar, erro -> {type(e).__name__}")
        return False 


def update_literary_genre(
    pk,
    genre=None,
):
    try:
        literary_genre = Literary_genres.objects.get(id=pk)
        log_print(f"fazendo atualizacoes:  genero:{genre}")

        literary_genre.genre = genre if genre != None else literary_genre.genre


        log_print(f"Salvando no banco")
        literary_genre.save()
        return True

    
    except Exception as e:
        log_print(f"exception args:  {e.args}")
        log_print(f"Erro ao atualizar, erro -> {type(e).__name__}")
        return False 