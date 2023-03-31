from Libraryapp.models import Client
from Libraryapp.Serializers.ClientSerializer import ClientRegisterSerializer
from Libraryapp.utils.functions import log_print

def register_new_client(request_data):
    try:
        log_print("Passando request_data para o serializer")
        print(request_data)
        client = ClientRegisterSerializer(data=request_data)

        if client.is_valid():
            log_print(f"Salvando no banco")
            client.save()
            return True
        
        return False

    except Exception as e:
        log_print(f"exception args:  {e.args}")
        log_print(f"Erro ao cadastrar, erro -> {type(e).__name__}")
        return False 
    

def delete_client(pk):
    try:
        log_print("Procurando id no banco")
        client = Client.objects.get(id=pk)
        
        log_print("Deletando cliente")
        client.delete()

        return True
    except Exception as e:
        log_print(f"exception args:  {e.args}")
        log_print(f"Erro ao deletar, erro -> {type(e).__name__}")
        return False 


def update_client(
    pk,
    name=None,
    phone=None,
    address=None,
):
    try:
        client = Client.objects.get(id=pk)
        log_print(f"fazendo atualizacoes:  nome:{name}, endereco:{address}, telefone:{phone}")

        client.name = name if name != None else client.name
        client.address = address if address != None else client.address
        client.phone = phone if phone != None else client.phone
        
        log_print(f"Salvando no banco")
        client.save()
        return True

    except Exception as e:
        log_print(f"exception args:  {e.args}")
        log_print(f"Erro ao atualizar, erro -> {type(e).__name__}")
        return False 