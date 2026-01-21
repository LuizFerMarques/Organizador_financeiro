from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Transacao, Categoria
from .serializers import TransacaoSerializer, CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Categoria.objects.all()


class TransacaoViewSet(ModelViewSet):
   serializer_class = TransacaoSerializer
   permission_classes = [IsAuthenticated]


   def get_queryset(self):
       return Transacao.objects.filter(usuario=self.request.user)


   def perform_create(self, serializer):
       serializer.save(usuario=self.request.user)