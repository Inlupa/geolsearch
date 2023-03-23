from django.shortcuts import render
from .forms import *
import pandas as pd
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse




def Search(request):
    form = UserSearch(request.POST or None)

    submitbutton = request.POST.get("submit")

    text =''
    tag=''
    table=''
    df=''
    if form.is_valid():
            text = form.cleaned_data.get("text")
            tag = form.cleaned_data.get("tag")
            table = form.cleaned_data.get("table")

            # тут функция для создания дата фрейма из solr
            df = pd.read_excel('C:\\Users\\Anton\\Desktop\\python\\geochemistry.xlsx')  # use pandas to read the csv
            # тут надо сохранить в нужном формате этот дата фрейм в файл в директорию /static/docs/

            form = UserSearch()
    return render(request, "insert_article/search.html",
                  context={'form': form, 'df':df, 'submitbutton':submitbutton})


def download_file(requests):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'text.txt'
    # Define the full file path
    filepath = BASE_DIR + '/static/doc/' + filename
    # Open the file for reading content
    path = open(filepath, 'br')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value

    #документы
    return response