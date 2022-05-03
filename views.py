# import Http Response from django
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from crud.models import Person

  
# create a function
def students_view(request):
    print(request)
    #request["method"]
    #request.method
    if request.method == 'GET':
        person = Person.objects.all().order_by('-id')
        #person = person.objects.all()
        person2 = [
            {"fname": person[0].first_name,"lname":person[0].last_name},
            {"fname": person[1].first_name,"lname":person[1].last_name},
        ]
        # #return HttpResponse(json.dumps(person2,indent=2,default=str), content_type='application/json')

        #context =  {"person2":person2}
        context =  {"persons":person}
        return render(request, "crud/students.html",context)
        #return render(request, "crud/students.html")
    elif request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        person = Person.objects.create(first_name=fname,last_name=lname)
        return redirect('/students')
        #return render(request, "crud/students_old.html")
        #return HttpResponse(json.dumps({"fname":f"{fname}_000","lname":f"{lname}_000"}), content_type='application/json')
        #return HttpResponse(json.dumps({"fname":f"{person.first_name}_000","lname":f"{person.last_name}_000"}), content_type='application/json')


    





def students_delete_view(request,id):
    if request.method == 'GET':
        person = Person.objects.get(id=id)
        context={"person": person}
        return render(request, "crud/students_delete.html",context)
    if request.method == 'POST':
        person = Person.objects.get(id=id)
        person.delete()
        return redirect('/students')


def students_edit_view(request,id):
    print(id)
    print(request.method)
    if request.method == 'GET':
        person = Person.objects.get(id=id)
        context={"person": person}
        return render(request, "crud/students_edit.html",context)    
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        person = Person.objects.create(first_name=fname,last_name=lname)
        return redirect('/students')        



  

