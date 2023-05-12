from django.http import JsonResponse
from http import HTTPStatus
from rest_framework.generics import  GenericAPIView
from Libraryapp.Serializers.BookSerializer import BookSerializer
from Libraryapp.utils.functions import log_print
from Libraryapp.models import Book


class GetAllView(GenericAPIView):
    """ Esse endpoint busca todos os livros no banco"""
    serializer_class = BookSerializer
    def get(self, request, *args, **kwargs):
        try:
            log_print("retornando todos os livros")
            books = Book.objects.all()

            list_books = []

            for result in books:
                print(result)
                list_books.append(BookSerializer(result).data) 

            return JsonResponse({
                "data": list_books
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
        

class GetBookByIdView(GenericAPIView):
    """ Esse endpoint busca um livro por id no banco"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Buscando Livro por id")
            book = Book.objects.get(id=pk)
            data = BookSerializer(book).data

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
    """ Esse endpoint faz o registro de um novo livro no banco"""
    serializer_class = BookSerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data
            log_print("Passando request_data para o serializer")
            print(request_data)
            book = BookSerializer(data=request_data)

            if book.is_valid():
                log_print(f"Salvando no banco")
                book.save()

                return JsonResponse({
                    "message": "Livro Cadastrado",
                    "data": book.data
                }, status=HTTPStatus.CREATED)
            
            return JsonResponse({
                "message": "Erro ao cadastrar livro",
            }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)

class DeleteView(GenericAPIView):
    """ Esse endpoint deleta um livro no banco pelo seu id"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')

            log_print("Procurando id no banco")
            book = Book.objects.get(id=pk)
        
            log_print("Deletando livro")
            book.delete()

            return JsonResponse({
                "message": "Livro Deletado",
            }, status=HTTPStatus.OK)

        except Exception as e:
            log_print(f"exception args:  {e.args}")
            log_print(f"Erro ao deletar, erro -> {type(e).__name__}")

            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)


class UpdateView(GenericAPIView):
    """ Esse endpoint atualiza dados de um livro na biblioteca no banco pelo seu id"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def put(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            request_data = request.data

            title = request_data.get("title")
            author = request_data.get("author")
            publisher = request_data.get("publisher")
            especie = request_data.get("especie")
            data = request_data.get("data")
            tombo = request_data.get("tombo")
            procedencia = request_data.get("procedencia")


            book = Book.objects.get(id=pk)
            log_print(f"fazendo atualizacoes: titulo:{title}, autor:{author}, publicacao: {publisher}")

            book.title = title if title != None else book.title
            book.author = author if author != None else book.author
            book.publisher = publisher if publisher != None else book.publisher

            book.especie = especie if especie != None else book.especie
            book.data = data if data != None else book.data
            book.tombo = tombo if tombo != None else book.tombo
            book.procedencia = procedencia if procedencia != None else book.procedencia

            log_print(f"Salvando no banco")
            book.save()

            return JsonResponse({
                "message": "Livro Atualizado",
                "data": book.data
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
