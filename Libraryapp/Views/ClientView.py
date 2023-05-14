from django.http import JsonResponse
from http import HTTPStatus
from rest_framework.generics import GenericAPIView
from Libraryapp.Serializers.ClientSerializer import ClientRegisterSerializer, ClientGetSerializer
from Libraryapp.utils.functions import log_print
from Libraryapp.models import Client


class GetAllView(GenericAPIView):
    serializer_class = ClientRegisterSerializer
    def get(self, request, *args, **kwargs):
        try:
            log_print("retornando todos os clientes")
            clients = Client.objects.all()

            list_clients = []

            for result in clients:
                print(result)
                list_clients.append(ClientGetSerializer(result).data) 

            return JsonResponse({
                "data": list_clients
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)    


class GetClientByIdView(GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientRegisterSerializer
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Buscando cliente por id")
            client = Client.objects.get(id=pk)
            
            data = ClientGetSerializer(client).data

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
    """ Esse endpoint faz o registro de um novo cliente no banco"""
    serializer_class = ClientRegisterSerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data

            log_print("Passando request_data para o serializer")
            print(request_data)
            client = ClientRegisterSerializer(data=request_data)

            if client.is_valid():
                log_print(f"Salvando no banco")
                client.save()
                return JsonResponse({
                    "message": "Cliente Cadastrado",
                }, status=HTTPStatus.CREATED)
            
            return JsonResponse({
                    "message": "Erro ao cadastrar cliente",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
        

class DeleteView(GenericAPIView):
    """ Esse endpoint deleta um cliente no banco pelo seu id"""
    queryset = Client.objects.all()
    serializer_class = ClientRegisterSerializer
    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Procurando id no banco")
            client = Client.objects.get(id=pk)
            
            log_print("Deletando cliente")
            client.delete()

            return JsonResponse({
                "message": "Cliente Deletado",
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)

class UpdateView(GenericAPIView):
    """ Esse endpoint atualiza dados de um cliente no banco pelo seu id"""
    queryset = Client.objects.all()
    serializer_class = ClientRegisterSerializer
    def put(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            request_data = request.data

            name = request_data.get("name")
            phone = request_data.get("phone")
            address = request_data.get("address")
            library_fk = request_data.get("library_fk")

            client = Client.objects.get(id=pk)
            log_print(f"fazendo atualizacoes:  nome:{name}, endereco:{address}, telefone:{phone}")

            client.name = name if name != None else client.name
            client.address = address if address != None else client.address
            client.phone = phone if phone != None else client.phone
            client.library_fk = library_fk if library_fk != None else client.library_fk

            
            log_print(f"Salvando no banco")
            client.save()

            return JsonResponse({
                "message": "Cliente Atualizado",
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
