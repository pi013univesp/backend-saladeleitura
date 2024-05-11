from django.http import JsonResponse
from http import HTTPStatus
from rest_framework.generics import GenericAPIView
from Libraryapp.Serializers.TrilhaSerializer import TrilhaSerializer, TrilhaLivroSerializer, GETTrilhaLivroSerializer
from Libraryapp.utils.functions import log_print
from Libraryapp.models import Trilha, TrilhaLivros


class GetAllTrilhaView(GenericAPIView):
    serializer_class = TrilhaSerializer
    def get(self, request, *args, **kwargs):
        try:
            log_print("retornando todos as Trilhas")
            trilhas = Trilha.objects.all()

            list_trilhas = []

            for result in trilhas:
                print(result)
                list_trilhas.append(TrilhaSerializer(result).data) 

            return JsonResponse({
                "data": list_trilhas
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)    


class GetTrilhaByIdView(GenericAPIView):
    queryset = Trilha.objects.all()
    serializer_class = TrilhaSerializer
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Buscando trilha por id")
            trilha = Trilha.objects.get(id=pk)
            
            data = TrilhaSerializer(trilha).data

            return JsonResponse({
                "data": data
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)    

class GetTrilhaLivroByIdView(GenericAPIView):
    queryset = TrilhaLivros.objects.all()
    serializer_class = GETTrilhaLivroSerializer
    def get(self, request, *args, **kwargs):
        try:
            fk = kwargs.get('pk')
            log_print("Buscando trilha por id")
            trilha = TrilhaLivros.objects.filter(trilha_fk=fk).order_by('posicao_na_trilha')
            
            list_trilhas = []

            for result in trilha:
                print(result)
                list_trilhas.append(GETTrilhaLivroSerializer(result).data) 

            return JsonResponse({
                "data": list_trilhas
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)    


class RegisterView(GenericAPIView):
    """ Esse endpoint faz o registro de uma nova trilha no banco"""
    serializer_class = TrilhaSerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data

            log_print("Passando request_data para o serializer")
            print(request_data)
            trilha = TrilhaSerializer(data=request_data)

            if trilha.is_valid():
                log_print(f"Salvando no banco")
                trilha.save()
                return JsonResponse({
                    "message": "trilha Cadastrada",
                }, status=HTTPStatus.CREATED)
            
            return JsonResponse({
                    "message": "Erro ao cadastrar trilha",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
        

class DeleteView(GenericAPIView):
    """ Esse endpoint deleta uma trilha no banco pelo seu id"""
    queryset = Trilha.objects.all()
    serializer_class = TrilhaLivroSerializer
    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Procurando id no banco")
            trilha = Trilha.objects.get(id=pk)
            
            log_print("Deletando trilha")
            trilha.delete()

            return JsonResponse({
                "message": "Trilha Deletado",
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)


class RegisterTrilhaLivroView(GenericAPIView):
    """ Esse endpoint faz o registro de um novo livro na trilha do banco"""
    serializer_class = TrilhaLivroSerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data

            log_print("Passando request_data para o serializer")
            print(request_data)
            trilhaLivro = TrilhaLivroSerializer(data=request_data)

            if trilhaLivro.is_valid():
                log_print(f"Salvando no banco")
                trilhaLivro.save()
                return JsonResponse({
                    "message": "trilhaLivro Cadastrada",
                }, status=HTTPStatus.CREATED)
            
            return JsonResponse({
                    "message": "Erro ao cadastrar trilhaLivro",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
