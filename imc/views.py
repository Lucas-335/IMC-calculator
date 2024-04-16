from django.shortcuts import render
from .forms import ImcForm
# Create your views here.

def calculate(request):

    if request.method == 'POST':
        form = ImcForm(request.POST)

        if form.is_valid():
            weight_ = form.cleaned_data.get('weight')
            height_ = form.cleaned_data.get('height')

            imc =  round(weight_/(height_*height_),2)

            context = {
                'form': form,
                'imc': imc,
            }
            
            return render(request,'imc/index.html',context)

    form = ImcForm()
    context = {
        'form':form
    }
    return render(request,'imc/index.html', context)