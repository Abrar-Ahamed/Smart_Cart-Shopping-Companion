import os
from collections import Counter
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Diary
import pandas as pd
import csv

from django.core.files.storage import FileSystemStorage


# Create your views here.

def home(request):
    return render(request, 'index.html', context={"name": "CalCart"})


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


def results(request):
    # message = "I found "+str(rows)+" rows and "+str(columns)+" columns"
    # messages.warning(request, message)

    labels = []
    dataset = []

    queryset = Diary.objects.all()
    for product in queryset:
        labels.append(product.name)
        dataset.append(product.calcium)

    return render(request, 'results.html', {
        'labels': labels,
        'dataset': dataset,
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

def cart_viz(request):

    labels = ["Protein","Carbohydrates","Sugar"]
    dataset = [protein_sum,carbs_sum,sug_sum]

    return render(request, 'cartotal.html', {
        'labels': labels,
        'dataset': dataset,
         })

def fats_viz(request):

    labels = ["Saturated", "Monounsaturated", "PolyUnsaturated"]
    dataset = [sat_sum, mono_sum, poly_sum]

    return render(request, 'satunsat.html', {
        'labels': labels,
        'dataset': dataset,
    })

def cholest_viz(request):
    labels = ["Less than 200","range 200-239","range 240-279","above 280"]
    dataset = [below200_range, range200_239, range240_279,above_range280]

    return render(request, 'cholesterolviz.html', {
        'labels': labels,
        'dataset': dataset,
    })

def upload_csv(request):
    # To store ID's of products in cart
    id_list = []
    global protein_sum, carbs_sum, sug_sum, sat_sum, mono_sum, poly_sum, below200_range, range200_239, range240_279, above_range280
    protein_sum, carbs_sum, sug_sum,sat_sum, mono_sum, poly_sum, below200_range, range200_239, range240_279, above_range280 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    # Get the uploaded file from the request
    csv_file = open("C:/pythonProject/pythonProject/pythonProject/TARP_final/smartstore/food_data_sample.csv", "r")

    # Read the data from the CSV file
    data = csv.reader(csv_file.read().splitlines())

    # To avoid overlapping or repetition
    # of existing products when the csv file is read more than once.

    if Diary.objects.count() > 0:
        Diary.objects.all().delete()
        # for i in id_list:
        #     if Diary.objects.filter(id=i).exists():
        #         Diary.objects.get(id=i).delete()

    c = 0
    # Loop through the rows in the CSV file
    for row in data:

        # Create an instance of the model for each row
        if c >= 1:  # This condition is checked because 1st row is header row and doesn't contain data
            # filling data to obj from 2nd row onwards
            id_list.append(row[0])
            #Calculating total cart product nutrient
            protein_sum += float(row[3])
            carbs_sum += float(row[4])
            sug_sum += float(row[5])
            sat_sum += float(row[9])
            mono_sum += float(row[10])
            poly_sum += float(row[11])
            if float(row[12]) <= 200.0:
                below200_range += 1
            elif float(row[12]) > 200.0 and float(row[12]) < 240.0:
                range200_239 += 1
            elif float(row[12]) >= 240.0 and float(row[12]) < 280.0:
                range240_279 += 1
            elif float(row[12]) >= 280.0:
                above_range280 += 1

            obj = Diary()
            # Set the attributes of the model instance to the values in the CSV file
            obj.name = row[1]
            obj.energy = row[2]
            obj.protein = row[3]
            obj.carbs = row[4]
            obj.sugar = row[5]
            obj.calcium = row[6]
            obj.potassium = row[7]
            obj.sodium = row[8]
            obj.fa_sat = row[9]
            obj.fa_mono = row[10]
            obj.fa_poly = row[11]
            obj.cholest = row[12]
            # Save the model instance to the database
            obj.save()
        c += 1

        # Return a success message to the user
    return render(request, 'home.html')


def display_cart(request):
    cart_items = Diary.objects.all()
    context = {"cart_items": cart_items}
    return render(request, 'display_1/index.html', context)

def cart_summary(request):
    fat_sum = sat_sum + mono_sum + poly_sum
    total_cpf = carbs_sum + protein_sum + fat_sum
    cart_cpf_prof = []
    cart_cholest_prof = []
    cart_fats_prof = []
    text_cpf, text_fats, text_cholest = "", "", ""

    #Calculating Percentage fat,carbs,proteins
    carbs_percent = (carbs_sum/total_cpf) * 100
    protein_percent = (protein_sum/total_cpf) *100
    fats_percent = (fat_sum/total_cpf) * 100

    #Cart summary for carbs, protein, fats balance
    if (carbs_percent > 45.0 and carbs_percent < 65.0) and (protein_percent > 10.0 and protein_percent < 35.0) and (fats_percent > 20.0 and fats_percent < 20.0):
        text_cpf = "Great job pal!\nYour cart has a good balance of carbohydrates, protein and fats.\nStay healthy and live at the top of the world\nHope you enjoyed shopping with me!"
        # cart_cpf_prof = text.split("\n")
    if (carbs_percent < 45.0 or carbs_percent > 65.0) or (protein_percent < 10.0 or protein_percent < 35.0) or (fats_percent < 20.0 or fats_percent > 20.0):
        text_cpf = "Uh Oh!!\nSeems like my pal has lost control\nYour cart has a poor balance of carbohydrates, fats and proteins."
        # cart_cpf_prof = text.split("\n")


    fats = [sat_sum,mono_sum,poly_sum]
    unsaturated = mono_sum + poly_sum
    cholest_range = [below200_range, range200_239, range240_279, above_range280]

    if below200_range == max(cholest_range):
        text_cholest = "Good job buddy!\nYour cart's Cholesterol level is well below the consumption limit.\nEnjoy your experience with CalCart!"
        # cart_cholest_prof = text.split("\n")
    if range200_239 == max(cholest_range):
        text_cholest = "Hmmm? Not bad\nYour cholesterol range is in the mid range.\nYou have done pretty well but you can do better."
        # cart_cholest_prof = text.split("\n")
    if range240_279 == max(cholest_range):
        text_cholest = "Uh Oh! Pretty bad pal\nMany of your products in your cart seem to have high cholesterol levels!!. Try to "
        # cart_cholest_prof = text.split("\n")

    if sat_sum == max(fats):
        text_fats = "Ooops! Your cart is high on saturated fats.\nYou seem to prefer junk foods huh?\nC'mon pal lets stock up some products high on unsaturated fats as well! "
        # cart_fats_prof = text.split("\n")

    context = {"cart_cholest_prof": text_cholest,
               "cart_cpf_prof": text_cpf,
               "cart_fats_prof": text_fats}
    return render(request,"cartsum.html",context)

# fat_sum = sat_sum + mono_sum + poly_sum
#     total_cpf = carbs_sum + protein_sum + fat_sum
#     cart_cpf_prof = []
#     cart_cholest_prof = []
#     cart_fats_prof = []
#     text_cpf,text_fats,text_cholest = "", "", ""
#
#     # Calculating Percentage fat,carbs,proteins
#     carbs_percent = (carbs_sum / total_cpf) * 100
#     protein_percent = (protein_sum / total_cpf) * 100
#     fats_percent = (fat_sum / total_cpf) * 100
#
#     # Cart summary for carbs, protein, fats balance
#     if (carbs_percent > 45.0 and carbs_percent < 65.0) and (protein_percent > 10.0 and protein_percent < 35.0) and (
#             fats_percent > 20.0 and fats_percent < 20.0):
#         text_cpf += "Great job pal!\nYour cart has a good balance of carbohydrates, protein and fats.\nStay healthy and live at the top of the world\nHope you enjoyed shopping with me!"
#         # cart_cpf_prof.append(text.split("\n"))
#     if (carbs_percent < 45.0 or carbs_percent > 65.0) or (protein_percent < 10.0 or protein_percent < 35.0) or (
#             fats_percent < 20.0 or fats_percent > 20.0):
#         text_cpf += "Uh Oh!!\nSeems like my pal has lost control\nYour cart has a poor balance of carbohydrates, fats and proteins."
#         # cart_cpf_prof.append(text.split("\n"))
#
#     fats = [sat_sum, mono_sum, poly_sum]
#     unsaturated = mono_sum + poly_sum
#     cholest_range = [below200_range, range200_239, range240_279, above_range280]
#
#     if below200_range == max(cholest_range):
#         text_cholest = "Good job buddy!\nYour cart's Cholesterol level is well below the consumption limit.\nEnjoy your experience with CalCart!"
#         # cart_cholest_prof.append(text.split("\n"))
#     if range200_239 == max(cholest_range):
#         text_cholest = "Hmmm? Not bad\nYour cholesterol range is in the mid range.\nYou have done pretty well but you can do better."
#         # cart_cholest_prof.append(text.split("\n"))
#     if range240_279 == max(cholest_range):
#         text_cholest = "Uh Oh! Pretty bad pal\nMany of your products in your cart seem to have high cholesterol levels!!. Try to "
#         # cart_cholest_prof.append(text.split("\n"))
#
#     if sat_sum == max(fats):
#         text_fats += "Ooops! Your cart is high on saturated fats.\nYou seem to prefer junk foods huh?\nC'mon pal lets stock up some products high on unsaturated fats as well! "
#         # cart_fats_prof.append(text.split("\n"))
#
#     context = {"cart_cholest_prof": text_cholest}
#                # "cart_cpf_prof": cart_cpf_prof,
#                # "cart_fats_prof": cart_fats_prof}
#
#
#
#










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
