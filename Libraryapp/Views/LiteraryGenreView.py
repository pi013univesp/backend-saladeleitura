from django.http import JsonResponse
from http import HTTPStatus
from rest_framework.generics import GenericAPIView
from Libraryapp.models import Literary_genres
from Libraryapp.utils.functions import log_print
from Libraryapp.Serializers.LiteraryGenreSerializer import LiteraryGenresSerializer


class GetAllView(GenericAPIView):
    serializer_class = LiteraryGenresSerializer
    def get(self, request, *args, **kwargs):
        try:
            log_print("retornando todos os generos literarios")
            literary_genres = Literary_genres.objects.all()

            list_literary_genres = []

            for result in literary_genres:
                print(result)
                list_literary_genres.append(LiteraryGenresSerializer(result).data) 

            return JsonResponse({
                "data": list_literary_genres
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)    


class GetLiteraryGenreByIdView(GenericAPIView):
    queryset = Literary_genres.objects.all()
    serializer_class = LiteraryGenresSerializer
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Buscando genero literario por id")
            literary_genres = Literary_genres.objects.get(id=pk)
            
            data = LiteraryGenresSerializer(literary_genres).data

            return JsonResponse({
                "data": data
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)    


class RegisterView(GenericAPIView):
    """ Esse endpoint faz o registro de um novo Genero Literario no banco"""
    serializer_class = LiteraryGenresSerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data
            log_print("Passando request_data para o serializer")
            print(request_data)
            literary_genre = LiteraryGenresSerializer(data=request_data)

            if literary_genre.is_valid():
                log_print(f"Salvando no banco")
                literary_genre.save()


                return JsonResponse({
                    "message": "Genero Literario Cadastrado",
                }, status=HTTPStatus.CREATED)
            
            return JsonResponse({
                    "message": "Erro ao cadastrar Genero Literario",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
        

class DeleteView(GenericAPIView):
    """ Esse endpoint deleta um Genero Literario no banco pelo seu id"""
    queryset = Literary_genres.objects.all()
    serializer_class = LiteraryGenresSerializer
    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Procurando id no banco")
            literary_genre = Literary_genres.objects.get(id=pk)
            
            log_print("Deletando literary_genre")
            literary_genre.delete()

            return JsonResponse({
                "message": "Genero Literario Deletado",
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)


class UpdateView(GenericAPIView):
    """ Esse endpoint atualiza dados de um Genero Literario no banco pelo seu id"""
    queryset = Literary_genres.objects.all()
    serializer_class = LiteraryGenresSerializer
    def put(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            request_data = request.data

            genre = request_data.get("genre")

            literary_genre = Literary_genres.objects.get(id=pk)
            log_print(f"fazendo atualizacoes:  genero:{genre}")

            literary_genre.genre = genre if genre != None else literary_genre.genre


            log_print(f"Salvando no banco")
            literary_genre.save()

            return JsonResponse({
                "message": "Genero Literario Atualizado",
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
