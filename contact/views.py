from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'Title':'Contact',
        'Heading':'Kontak Kami'
    }

    if request.method == 'POST':
        context['nama'] = request.POST['nama']
        context['email'] = request.POST['email']
        context['password'] = request.POST['password']
    return render(request, 'contact/index.html', context)