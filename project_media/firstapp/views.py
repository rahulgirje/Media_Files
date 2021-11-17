from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Document
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm




def Baseview(request):
    template_name='firstapp/base.html'
    return render(request,template_name)

def uploadview(request):
    template_name = 'firstapp/upload.html'
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        a = FileSystemStorage()
        filename = a.save(myfile.name, myfile)
        uploaded_file_url =  a.url(filename)
        context = {'uploaded_file_url': uploaded_file_url}
        return render(request, template_name, context)
    return render(request, template_name)


def model_form_upload(request):
    template_name = 'firstapp/newupload.html'
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,'File is uploaded Successfullyy!!!...')
            return redirect('newfile')
    else:
        form = DocumentForm()
    context = {'form': form}
    return render(request, template_name, context)


def showdataview(request):
    file=Document.objects.all()
    template_name='firstapp/show.html'
    context={'file':file}
    return render(request,template_name,context)