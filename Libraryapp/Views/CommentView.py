from django.http import JsonResponse
from http import HTTPStatus
from rest_framework.generics import GenericAPIView
from Libraryapp.Serializers.CommentSerializer import CommentSerializer
from Libraryapp.utils.functions import log_print
from Libraryapp.models import Comment


class GetAllView(GenericAPIView):
    serializer_class = CommentSerializer
    def get(self, request, *args, **kwargs):
        try:
            log_print("retornando todos os comentarios")
            comment = Comment.objects.all()

            list_Comment = []

            for result in comment:
                print(result)
                list_Comment.append(CommentSerializer(result).data) 

            return JsonResponse({
                "data": list_Comment
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
        


class RegisterView(GenericAPIView):
    
    """ Esse endpoint faz o registro de um novo cliente no banco"""
    serializer_class = CommentSerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data

            log_print("Passando request_data para o serializer")
            print(request_data)
            comment = CommentSerializer(data=request_data)

            if comment.is_valid():
                log_print(f"Salvando no banco")
                comment.save()
                return JsonResponse({
                    "message": "Comentario Cadastrado",
                }, status=HTTPStatus.CREATED)
            
            return JsonResponse({
                    "message": "Erro ao cadastrar comentario",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
        

class GetCommentByIdView(GenericAPIView):
    """ Esse endpoint busca um livro por id no banco"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def get(self, request, *args, **kwargs):
        try:
            idp = kwargs.get('id')
            log_print("Buscando comentarios por id do forum")
            comments = Comment.objects.all().filter(forum=idp)

            list_Comment = []

            for result in comments:
                print(result)
                list_Comment.append(CommentSerializer(result).data) 

            return JsonResponse({
                "data": list_Comment
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)    