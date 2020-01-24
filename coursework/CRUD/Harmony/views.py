from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,Context
from . models import *


# Create your views here.
def view_Music_page(request):
    return render(request,'Music.html')

def view_Music_lists(request):
    list_of_Music= Music.objects.all()
    print(list_of_Music)
    context_variable = {
        'Music':list_of_Music
    }
    return render(request,'Music.html',context_variable)

def view_Music_form(request):
    return render(request,'Music.html')

def view_Musicdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_Username = request.POST['Username']
        print(type(get_Username))
        get_Song_Name = request.POST['Song_Name']
        get_Feedback = request.POST['Feedback']
        print(type(get_Username))
        Music_obj = Music(Username=get_Username,Song_Name=get_Song_Name,Feedback=get_Feedback)
        Music_obj.save()
        return HttpResponse("Saved")
        #return redirect('Harmonyapp/Musicdata')
    else:
        return HttpResponse("Error record saving")

def view_Musicdata_updateform(request,ID):
    print(ID)
    Music_obj = Music.Objects.get(id=ID)
    print(Music_obj)
    context_varible = {
        'Music':Music_obj
    }
    return render(request,'MusicUpdateForm.html',context_varible)

def view_update_form_data_in_db(request,ID):
    Music_obj = Music.Objects.get(id=ID)
    print(Music_obj)
    Music_form_data = request.POST
    print(Music_form_data)
    Music_obj.UserName = request.POST['Music_UserName']
    Music_obj.SongName =request.POST['Music_SongName']
    Music_obj.Lyric = request.POST['Music_Lyric']
    
    return HttpResponse("Record Updated!")     