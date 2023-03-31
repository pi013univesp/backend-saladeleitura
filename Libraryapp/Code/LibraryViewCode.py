from Libraryapp.models import Library
from Libraryapp.Serializers.LibrarySerializer import (
    LibraryLoginSerializer,
    LibraryRegisterSerializer
)
from Libraryapp.utils.functions import log_print

def verify_password(data, user_password):
    if data["password"] == user_password:
        return True
    else:
        return False

def verify_if_email_and_password_is_correct(email, user_password):
    try:
        log_print(f"Buscando email: {email}")
        library = (Library.objects.get(email=email))

        data = LibraryLoginSerializer(library).data

        log_print("Verificando se as senhas sao iguais")
        password_is_true = verify_password(data, user_password)

        if(password_is_true):
            log_print("email e senha validos")
            return True
        else:
            log_print("senha incorreta")
            return False
    except Exception as e:
        log_print(f"exception args:  {e.args}")
        log_print(f"email nao cadastrado, erro -> {type(e).__name__}")
        return False

def register_new_library(request_data):
    try:
        log_print("Passando request_data para o serializer")
        print(request_data)
        library = LibraryRegisterSerializer(data=request_data)

        if library.is_valid():
            log_print(f"Salvando no banco")
            library.save()
            return True
        
        return False

    except Exception as e:
        log_print(f"exception args:  {e.args}")
        log_print(f"Erro ao cadastrar, erro -> {type(e).__name__}")
        return False 
    
def delete_library(pk):
    try:
        log_print("Procurando id no banco")
        library = Library.objects.get(id=pk)
        
        log_print("Deletando biblioteca")
        library.delete()

        return True
    except Exception as e:
        log_print(f"exception args:  {e.args}")
        log_print(f"Erro ao deletar, erro -> {type(e).__name__}")
        return False 
    

def update_library(
    pk,
    name=None,
    address=None,
    email=None,
    password=None
):
    try:
        library = Library.objects.get(id=pk)
        log_print(f"fazendo atualizacoes:  nome:{name}, endereco:{address}, email:{email}, senha: {password}")

        library.name = name if name != None else library.name
        library.address = address if address != None else library.address
        library.email = email if email != None else library.email
        library.password = password if password != None else library.password

        log_print(f"Salvando no banco")
        library.save()
        return True
    
    except Exception as e:
        log_print(f"exception args:  {e.args}")
        log_print(f"Erro ao atualizar, erro -> {type(e).__name__}")
        return False 