from django.http import JsonResponse
from http import HTTPStatus
from rest_framework.generics import  GenericAPIView
from Libraryapp.Serializers.BorrowSerializer import BorrowSerializer, GETBorrowSerializer
from Libraryapp.utils.functions import log_print
from Libraryapp.models import Borrow, Client, Book, Library, Books_at_library
from datetime import datetime
from django.db.models import Count


class GetAllView(GenericAPIView):
    """ Esse endpoint busca todos os emprestimos da biblioteca no banco"""
    serializer_class = GETBorrowSerializer
    def get(self, request, *args, **kwargs):
        try:
            log_print("retornando todos os emprestimos")
            borrow = Borrow.objects.all()

            list_borrows = []

            for result in borrow:
                print(result)
                list_borrows.append(GETBorrowSerializer(result).data) 

            return JsonResponse({
                "data": list_borrows
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
        

class GetAllBorrowInDebt(GenericAPIView):
    """ Esse endpoint busca todos os emprestimos em debito da biblioteca no banco"""
    serializer_class = GETBorrowSerializer
    def get(self, request, *args, **kwargs):
        try:
            log_print("retornando todos os emprestimos")
            borrow = Borrow.objects.all().filter(return_date=None)

            list_borrows = []

            for result in borrow:
                print(result)
                list_borrows.append(GETBorrowSerializer(result).data) 

            return JsonResponse({
                "data": list_borrows
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)

class GetBorrowByIdView(GenericAPIView):
    """ Esse endpoint busca um emprestimo da biblioteca por id no banco"""
    queryset = Borrow.objects.all()
    serializer_class = GETBorrowSerializer
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Buscando emprestimo por id")
            borrow = Borrow.objects.get(id=pk)
            
            data = GETBorrowSerializer(borrow).data

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
    """ Esse endpoint faz o registro de um novo emprestimo na biblioteca no banco"""
    serializer_class = BorrowSerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data

            book_fk = request_data.get("book_fk")
            client_fk = request_data.get("client_fk")

            log_print("procurando cliente pelo id")
            client = Client.objects.get(id=client_fk)
            log_print(f"procurando emprestimos desse cliente: {client.name}")
            borrow = (Borrow.objects
                .filter(client_fk=client.id, return_date=None)
                .count()
            )

            #  aqui poderia ser feito a quantidade de livros que a biblioteca permite deixar emprestado pra uma só pessoa
            if borrow < 1:
                log_print(f"Elegivel  para emprestimo")
                log_print("Buscando livro na biblioteca")
                book_at_library = Books_at_library.objects.get(book_fk=book_fk)
                
                log_print("verificando se ainda ha livros disponiveis")
                if(book_at_library.number_of_borrowed_books == book_at_library.book_stock):
                    log_print("Todos os livros estao emprestados")
                    return JsonResponse({
                        "message": "Todos os livros estao emprestados",
                    }, status=HTTPStatus.BAD_REQUEST)
                
                inDate = datetime.now()
                date_formated = inDate.strftime("%Y-%m-%d %H:%M:%S")

                log_print("salvando data do emprestimo")
                request_data["borrow_date"] = date_formated

                log_print("Passando request_data para o serializer")
                borrow_save = BorrowSerializer(data=request_data)
                
                if borrow_save.is_valid():
                    log_print("Salvando no banco")
                    borrow_save.save()
                    book_at_library.number_of_borrowed_books += 1
                    book_at_library.save()

                    return JsonResponse({
                        "message": "Emprestimo Cadastrado",
                    }, status=HTTPStatus.CREATED)
            else:
                return JsonResponse({
                    "message": "Esse cliente tem pendencia de livro"
                }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)


class DeleteView(GenericAPIView):
    """ Esse endpoint deleta um emprestimo da biblioteca do banco pelo seu id"""
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')

            log_print("Procurando id no banco")
            borrow = Borrow.objects.get(id=pk)
        

            log_print("procurando o livro na biblioteca")
            bookAtLibrary = Books_at_library.objects.get(book_fk=borrow.book_fk)
            log_print("removendo o numero de livros emprestados")
            if bookAtLibrary.number_of_borrowed_books > 0:
                bookAtLibrary.number_of_borrowed_books -= 1 
                bookAtLibrary.save()

            log_print("Deletando emprestimo")
            borrow.delete()

            return JsonResponse({
                "message": "Emprestimo Deletado",
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
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    def put(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            request_data = request.data

            book_fk = request_data.get("book_fk")
            client_fk = request_data.get("client_fk")
            library_fk = request_data.get("library_fk")
            borrow_date = request_data.get("borrow_date")
            end_date = request_data.get("end_date")
            return_date = request_data.get("return_date")


            book = Borrow.objects.get(id=pk)

            book.library_fk = Library.objects.get(pk=library_fk) if library_fk != None else book.library_fk
            book.book_fk = Book.objects.get(pk=book_fk) if book_fk != None else book.book_fk
            book.client_fk = Client.objects.get(pk=client_fk) if client_fk != None else book.client_fk
            book.borrow_date = borrow_date if borrow_date != None else book.borrow_date
            book.end_date = end_date if end_date != None else book.end_date
            book.return_date = return_date if return_date != None else book.return_date


            log_print(f"Salvando no banco")
            book.save()

            return JsonResponse({
                "message": "Emprestimo Atualizado",
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)


class BorrowCloseView(GenericAPIView):
    """Esse endpoint faz o fechamento de um emprestimo de livro"""
    queryset = Borrow.objects.all()
    serializer_class = GETBorrowSerializer
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Buscando emprestimo por id")
            borrow = Borrow.objects.get(id=pk)

            if(borrow.return_date is None):
                log_print("Adicionando a data de devolucao")
                inDate = datetime.now()
                date_formated = inDate.strftime("%Y-%m-%d %H:%M:%S")

                log_print("salvando emprestimo e livro na biblioteca")
                borrow.return_date = date_formated
                borrow.save()

                log_print("procurando o livro na biblioteca")
                bookAtLibrary = Books_at_library.objects.get(book_fk=borrow.book_fk)
                log_print("removendo o numerode livros emprestados")
                if bookAtLibrary.number_of_borrowed_books > 0:
                    bookAtLibrary.number_of_borrowed_books -= 1 
                    bookAtLibrary.save()


                return JsonResponse({
                    "response": "Emprestimo finalizado",
                }, status=HTTPStatus.OK)
            
            return JsonResponse({
                "response":"Livro ja devolvido"
            }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)   

class TopBorrowedBooks(GenericAPIView):
    def get(self, request):
        top_borrowed_books = Borrow.objects.values('book_fk').annotate(total_borrows=Count('book_fk')).order_by('-total_borrows')[:10]

        top_borrowed_books_details = []
        
        for book_info in top_borrowed_books:
            book_id = book_info['book_fk']
            total_borrows = book_info['total_borrows']
            book = Book.objects.get(id=book_id) 
            book_name = book.title 
            top_borrowed_books_details.append({
                'nome': book_name,
                'numerode_alugueis': total_borrows
            })

        return JsonResponse({
            "data": top_borrowed_books_details
        }, status=HTTPStatus.OK)