from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html',)

def count(request):
    dict = {}
    data = request.GET['fulltextarea']
    list_elements = data.split()
    list_length = len(list_elements)
    print (list_elements,list_length)
    for word in list_elements:
        if word in dict:
            dict[word]+=1
        else:
            dict[word] = 1
    sorted_list = sorted(dict.items(), key=operator.itemgetter(1),reverse = True)
    return render(request,'count.html',{'llength' : list_length,'text':data,'dic' : sorted_list})
def about(request):
    return render(request,'about.html',)

