from django.http import JsonResponse
from http import HTTPStatus
from rest_framework.generics import GenericAPIView
from Libraryapp.Serializers.LibrarySerializer import (
    LibraryLoginSerializer,
    LibraryRegisterSerializer,
)
from Libraryapp.utils.functions import log_print
from Libraryapp.models import Library


def verify_password(data, user_password):
    if data["password"] == user_password:
        return True
    else:
        return False

class LoginView(GenericAPIView): 
    """Esse endpoint busca uma biblioteca no banco para fazer login"""
    serializer_class = LibraryLoginSerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data

            email = request_data.get("email")
            user_password = request_data.get("password")

            log_print(f"Buscando email: {email}")
            library = Library.objects.get(email=email)

            data = LibraryLoginSerializer(library).data

            log_print("Verificando se as senhas sao iguais")
            password_is_true = verify_password(data, user_password)

            if(password_is_true):
                log_print("email e senha validos")
                return JsonResponse({
                    "message": "Ok",
                }, status=HTTPStatus.OK)   
            else:
                log_print("senha incorreta")
                return JsonResponse({
                    "message": "email ou senha incorreto",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)

class RegisterView(GenericAPIView):
    """ Esse endpoint faz o registro de uma nova biblioteca no banco"""
    serializer_class = LibraryRegisterSerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data


            try:
                log_print("verificando se ja existe esse email no banco")
                email = request_data.get("email")

                library = Library.objects.get(email=email)
            
            except Library.DoesNotExist:
                log_print("Passando request_data para o serializer")
                log_print(request_data)
                library = LibraryRegisterSerializer(data=request_data)

                if library.is_valid():
                    log_print(f"Salvando no banco")
                    library.save()
                    
                    return JsonResponse({
                        "message": "Biblioteca Cadastrada",
                    }, status=HTTPStatus.CREATED)
                
            
            return JsonResponse({
                    "message": "Erro ao cadastrar biblioteca",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
        

class DeleteView(GenericAPIView):
    """ Esse endpoint deleta uma biblioteca no banco pelo seu id"""
    queryset = Library.objects.all()
    serializer_class = LibraryRegisterSerializer
    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Procurando id no banco")
            library = Library.objects.get(id=pk)
            
            log_print("Deletando biblioteca")
            library.delete()

            return JsonResponse({
                "message": "Biblioteca Deletada",
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)

class UpdateView(GenericAPIView):
    """ Esse endpoint atualiza dados de uma biblioteca no banco"""
    queryset = Library.objects.all()
    serializer_class = LibraryRegisterSerializer
    def put(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            request_data = request.data

            name = request_data.get("name")
            address = request_data.get("address")
            email = request_data.get("email")
            password = request_data.get("password")

            library = Library.objects.get(id=pk)
            log_print(f"fazendo atualizacoes:  nome:{name}, endereco:{address}, email:{email}, senha: {password}")

            library.name = name if name != None else library.name
            library.address = address if address != None else library.address
            library.email = email if email != None else library.email
            library.password = password if password != None else library.password

            log_print(f"Salvando no banco")
            library.save()

            return JsonResponse({
                "message": "Biblioteca Atualizada",
            }, status=HTTPStatus.OK)


        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)

class GetAllView(GenericAPIView):
    """ Esse endpoint busca todas as bibliotecas no banco"""
    serializer_class = LibraryRegisterSerializer
    def get(self, request, *args, **kwargs):
        try:
            log_print("retornando todos os livros")
            library = Library.objects.all()

            list_library = []

            for result in library:
                print(result)
                list_library.append(LibraryRegisterSerializer(result).data) 

            return JsonResponse({
                "data": list_library
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
        

class GetLibraryByIdView(GenericAPIView):
    """ Esse endpoint busca uma biblioteca por id no banco"""
    queryset = Library.objects.all()
    serializer_class = LibraryRegisterSerializer
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Buscando Livro por id")
            library = Library.objects.get(id=pk)
            data = LibraryRegisterSerializer(library).data

            return JsonResponse({
                "data": data
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
