from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from.models import Transacao, Categoria
from django.db.models import Sum
from rest_framework.viewsets import ModelViewSet
from .models import Categoria
from .serializers import CategoriaSerializer, TransacaoSerializer

## Exibe o resumo financeiro do usuário. ##

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TransacaoViewSet(ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)



def dashboard(request):
  receitas = Transacao.objects.filter(tipo='R').aggregate(total=Sum('valor'))['total'] or 0
  despesas = Transacao.objects.filter(tipo='D').aggregate(total=Sum('valor'))['total'] or 0
  saldo = receitas - despesas


  return render(request, 'dashboard.html', {
     'receitas': receitas,
     'despesas': despesas,
     'saldo': saldo
})




def nova_transacao(request):
   if request.method == 'POST':
      Transacao.objects.create(
        descricao=request.POST['descricao'],
        valor=request.POST['valor'],
        tipo=request.POST['tipo'],
        categoria=Categoria.objects.get(id=request.POST['categoria']),
        data=request.POST['data']
      )
      return redirect('dashboard')


   categorias = Categoria.objects.all()
   return render(request, 'nova.html', {'categorias': categorias})




