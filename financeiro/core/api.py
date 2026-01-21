from rest_framework.viewsets import ModelViewSet
from .models import Transacao, Categoria
from .serializers import TransacaoSerializer, CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class TransacaoViewSet(ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer