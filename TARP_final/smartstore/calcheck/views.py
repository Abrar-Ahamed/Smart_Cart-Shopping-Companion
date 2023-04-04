import os
from collections import Counter
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Diary
import pandas as pd
import csv
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
    return render(request, 'index.html', context={"name":"CalCart"})

# def title_page(request):
#     if request.method == "POST":
#         uploaded_file = request.FILES['document']
#         print(uploaded_file)
#
#         if uploaded_file.name.endswith('.csv'):
#             savefile  = FileSystemStorage()
#             name = savefile.save(uploaded_file.name,uploaded_file)
#
#             d = os.getcwd()
#             file_dir = d+'\media\\'+name
#
#             readfile(file_dir)
#             return redirect(results)
#         else:
#             messages.warning(request,'File not uploaded, Upload csv file')
#     # food_list = Diary.objects.all()
#     # context = {'food_list': food_list}
#     return render(request, 'home.html')
#
#
# def readfile(filename):
#     global rows, columns, myfile, data
#     myfile = pd.read_csv(filename, engine='python')
#     data = pd.DataFrame(myfile)
#     print(data)
#
#     rows = len(data.axes[0])
#     columns = len(data.axes[1])
#
def results(request):
    # message = "I found "+str(rows)+" rows and "+str(columns)+" columns"
    # messages.warning(request, message)


    labels=[]
    dataset=[]


    queryset = Diary.objects.all()
    for product in queryset:
        labels.append(product.name)
        dataset.append(product.calcium)

    return render(request, 'results.html', {
        'labels':labels,
        'dataset':dataset,
    })

def doughnut_chart(request):
    labels = []
    dataset = []
    queryset = Diary.objects.all()
    for cal in queryset:
        labels.append(cal.name)
        dataset.append(cal.energy)

    return render(request, 'doughnut.html', {
        'labels': labels,
        'dataset': dataset,
    })

def upload_csv(request):

            # Get the uploaded file from the request
    csv_file = open("smartstore/food_data.csv","r")

            # Read the data from the CSV file
    data = csv.reader(csv_file.read().splitlines())

    c = 0
    # Loop through the rows in the CSV file
    for row in data:
                # Create an instance of the model for each row
                if c >= 1:
                    obj = Diary()
                    obj.name = row[0]
                    obj.energy = row[1]
                    obj.protein = row[2]
                obj.save()
                # Set the attributes of the model instance to the values in the CSV file
                c += 1
                # Save the model instance to the database


            # Return a success message to the user
    return render(request, 'results.html')

        # If the request method is not POST, return the file upload form




    # dashboard = []  # ['A11','A11',A'122',]
    # for x in data['Protein_(g)']:
    #     dashboard.append(x)
    #
    # my_dashboard = dict(Counter(dashboard))  # {'A121': 282, 'A122': 232, 'A124': 154, 'A123': 332}
    #
    # print(my_dashboard)
    #
    # keys = my_dashboard.keys()  # {'A121', 'A122', 'A124', 'A123'}
    # values = my_dashboard.values()
    #
    # listkeys = []
    # listvalues = []
    #
    # for x in keys:
    #     listkeys.append(x)
    #
    # for y in values:
    #     listvalues.append(y)
    #
    # print(listkeys)
    # print(listvalues)
    #
    # context = {
    #     'listkeys': listkeys,
    #     'listvalues': listvalues,
    # }

