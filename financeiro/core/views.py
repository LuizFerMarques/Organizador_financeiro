from django.shortcuts import render, redirect
from.models import Transacao, Categoria
from django.db.models import Sum


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




