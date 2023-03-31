from django.http import JsonResponse
from http import HTTPStatus
from rest_framework.generics import GenericAPIView
from Libraryapp.models import Literary_genres
from Libraryapp.utils.functions import log_print
from Libraryapp.Serializers.LiteraryGenreSerializer import LiteraryGenresSerializer
from Libraryapp.Code.LiteraryGenreCode import (
    register_new_literary_genre,
    update_literary_genre,
    delete_literary_genre
)


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
            register = register_new_literary_genre(request_data)

            if register:
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
    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            register_deleted = delete_literary_genre(pk)

            if register_deleted:
                return JsonResponse({
                    "message": "Genero Literario Deletado",
                }, status=HTTPStatus.OK)
            
            return JsonResponse({
                    "message": "Erro ao deletar Genero Literario",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)


class UpdateView(GenericAPIView):
    """ Esse endpoint atualiza dados de um Genero Literario no banco pelo seu id"""
    serializer_class = LiteraryGenresSerializer
    def put(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            request_data = request.data

            genre = request_data.get("genre")

            register_update = update_literary_genre(
                pk,
                genre,
            )

            if register_update:
                return JsonResponse({
                    "message": "Genero Literario Atualizado",
                }, status=HTTPStatus.OK)
            
            return JsonResponse({
                    "message": "Erro ao Atualizar o Genero Literario",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
