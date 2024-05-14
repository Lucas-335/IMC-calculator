from django.shortcuts import render
from .forms import ImcForm
from.utils import Imc
# Create your views here.

def calculate(request):

    if request.method == 'POST':
        form = ImcForm(request.POST)
        
        if form.is_valid():
    
            weight_ = form.cleaned_data.get('weight')
            height_ = form.cleaned_data.get('height')

            imc_instance = Imc(weight_, height_)  
            imc = f'Resultado: {imc_instance.imc_calculated()}'
            context = {
                'form': form,
                'imc': imc,
            }
            return render(request,'imc/index.html',context)
        else:
            context = {
                'form':form
            }
            return render(request,'imc/index.html', context)
    form = ImcForm()
    context = {
        'form':form
    }
    return render(request,'imc/index.html', context)
