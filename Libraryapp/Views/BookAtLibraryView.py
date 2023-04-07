from django.http import JsonResponse
from http import HTTPStatus
from rest_framework.generics import  GenericAPIView
from Libraryapp.Serializers.BookAtLibrarySerializer import BookAtLibrarySerializer, GETBookAtLibrarySerializer
from Libraryapp.utils.functions import log_print
from Libraryapp.models import Books_at_library, Book, Library


class GetAllView(GenericAPIView):
    """ Esse endpoint busca todos os livros da biblioteca no banco"""
    serializer_class = GETBookAtLibrarySerializer
    def get(self, request, *args, **kwargs):
        try:
            log_print("retornando todos os livros")
            books = Books_at_library.objects.all()

            list_books = []

            for result in books:
                print(result)
                list_books.append(GETBookAtLibrarySerializer(result).data) 

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
    """ Esse endpoint busca um livro da biblioteca por id no banco"""
    queryset = Books_at_library.objects.all()
    serializer_class = GETBookAtLibrarySerializer
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Buscando Livro por id")
            book = Books_at_library.objects.get(id=pk)
            
            data = GETBookAtLibrarySerializer(book).data

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
    """ Esse endpoint faz o registro de um novo livro na biblioteca no banco"""
    serializer_class = BookAtLibrarySerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data
            log_print("Passando request_data para o serializer")
            print(request_data)
            book = BookAtLibrarySerializer(data=request_data)

            if book.is_valid():
                log_print(f"Salvando no banco")
                book.save()

                return JsonResponse({
                    "message": "Livro Cadastrado",
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
    """ Esse endpoint deleta um livro da biblioteca do banco pelo seu id"""
    queryset = Books_at_library.objects.all()
    serializer_class = BookAtLibrarySerializer
    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')

            log_print("Procurando id no banco")
            book = Books_at_library.objects.get(id=pk)
        
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
    """ Esse endpoint atualiza dados de um livro da biblioteca no banco pelo seu id"""
    queryset = Books_at_library.objects.all()
    serializer_class = BookAtLibrarySerializer
    def put(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            request_data = request.data

            library_fk = request_data.get("library_fk")
            book_fk = request_data.get("book_fk")
            book_stock = request_data.get("book_stock")
            number_of_borrowed_books = request_data.get("number_of_borrowed_books")

            book = Books_at_library.objects.get(id=pk)
            log_print(f"fazendo atualizacoes: biblioteca:{library_fk}, livro:{book_fk}, estoque de livros:{book_stock}, numero de livros emprestados: {number_of_borrowed_books}")

            book.library_fk = Library.objects.get(pk=library_fk) if library_fk != None else book.library_fk
            book.book_fk = Book.objects.get(pk=book_fk) if book_fk != None else book.book_fk
            book.book_stock = book_stock if book_stock != None else book.book_stock
            book.number_of_borrowed_books = number_of_borrowed_books if number_of_borrowed_books != None else book.number_of_borrowed_books

            log_print(f"Salvando no banco")
            book.save()

            return JsonResponse({
                "message": "Livro Atualizado",
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
