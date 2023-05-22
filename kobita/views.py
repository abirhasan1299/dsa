from django.shortcuts import render,HttpResponse,redirect
from .models import User
from django.contrib import messages



# Create your views here.


def signup(request):

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        sex = request.POST['sex']
        date_of_birth = request.POST['dob']

        already_has_name = User.objects.all().filter(name=name).exists()
        already_has_mail = User.objects.all().filter(mail=email).exists()
        already_has_mobile = User.objects.all().filter(mobile=mobile).exists()

        if already_has_name == True:
            messages.warning(request,"Name Already Exits")
            return redirect("signup")
        elif already_has_mail ==True:
            messages.warning(request,"Email Already Exits")
            return redirect("signup")
        elif already_has_mobile == True:
            messages.warning(request,"Mobile Already Exits")
            return redirect("signup")
        else:
            obj = User(name= name,mail=email,mobile=mobile,password=password,date_of_birth= date_of_birth,sex=sex)
            obj.save()
            messages.success(request,"SIGNUP Successfully")
            return redirect("Form")
    else:
        pass
    return render(request,"signup.html")

def kobita_home(request,ud):

    if request.session.has_key('mail') and request.session.has_key('pass'):
        data = User.objects.all().get(unique_id=ud)
    else:
        return redirect("Form")
    context = {
       "data":data
    }
    return render(request,"kobita.html",context)

def logout(request):
    try:
        del request.session['mail']
        del request.session['pass']
    except:
        pass
    return redirect("Form")