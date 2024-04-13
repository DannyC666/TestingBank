from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Client
from .forms import ClientSelectForm
from .services import form_data
# Create your views here.
def client_product(request, pk):
    client_chosen = Client.objects.get(id=pk)
    products_list = client_chosen.products.split(',')

    return  render(request, 'productClient.html', {'client': client_chosen, 'products_li': products_list})


def select_client(request):
    
    if request.method == 'POST':
        # Esto asume que estás enviando el ID del cliente directamente desde el formulario HTML.
        client_id = request.POST.get('client_id')
        client = Client.objects.get(id=client_id)
        url = '/client_product/'+str(client.id)
        return HttpResponseRedirect(url)

    else:
        form = ClientSelectForm()
        clients = Client.objects.all()
        return render(request, 'selectClient.html', {'form': form, 'clients': clients})
    
    
    # role = request.GET.get('role')
    # if role == 'user':
    #     return HttpResponseRedirect('/client_product/')
    # elif role == 'employee':
    #     #TODO: Redirigir a pagina de empleado
    #     pass

    return render(request, 'selectClient.html')

def update_client_confirmation(request):
 
    if request.method == 'POST':
        client_id = request.POST.get('cliente_id')
    
        is_confirmed = request.POST.get('isConfirmed') == 'True'
        client = get_object_or_404(Client, id=client_id)
        client.isConfirmed = is_confirmed
        client_get_id = client.id
        confirm_updated = client.isConfirmed 
        form_data.publication_update(client_get_id, confirm_updated)
        client.save()
        
        return HttpResponse("El estado de confirmación ha sido actualizado.")
    clients = Client.objects.all()
    return render(request, 'selectClient.html', {'clients': clients})