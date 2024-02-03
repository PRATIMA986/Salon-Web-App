from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import userForm
from service.models import service

from detailsform.models import details

def HomePage(request):
    servicesData=service.objects.all()
    # for a in servicesData:
    #      print(a.service_title)
    # print(service)
    data ={
        'servicesData': servicesData
    }
    return render(request,"index.html",data)

def Login(request):
    return render(request,"Login.html")

def Signup(request):
    return render(request,"Signup.html")

def saveDetails(request):
     if request.method=="POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          password=request.POST.get('password')
          conpassword=request.POST.get('conpassword')
          mob=request.POST.get('mobno')
        #   address=request.POST.get('address')
          city=request.POST.get('city')
          state=request.POST.get('state')
          pincode=request.POST.get('pincode')
        #   country=request.POST.get('country')
          cname=request.POST.get('cname')
          occupation=request.POST.get('Occupation')
          yearofexperience=request.POST.get('yoe')

          data=details(name=name,email=email,password=password,confirmpassword=conpassword,mobileno=mob,city=city,state=state,pincode=pincode,cname=cname,occupation=occupation,yearofexperience=yearofexperience)
          data.save()









     return render(request,"Signup.html")

     
     

def aboutUs(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"aboutus.html",{'output':output})

def contactUs(request):
    return HttpResponse("contact Us by Likedin")

def course(request):
    return HttpResponse("welcome to our courses")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def Form(request):
        finalans= 0
        fn= userForm()

        data={'form':fn}
        try:
            if request.method=="POST":
            # n1=int(request.GET['num1'])
            # n2=int(request.GET['num2'])
                n1 = int(request.POST.get('num1'))
                n2 = int(request.POST.get('num2'))
        
            finalans=n1+n2
            data ={
                'form':fn,
                'output':finalans
            }
            url="/about-us/?output={}".format(finalans)

            return redirect(url)
        except:
            pass
        return render(request,"form.html",data)

def submitform(request):
     try:
            if request.method=="POST":
            # n1=int(request.GET['num1'])
            # n2=int(request.GET['num2'])
                n1 = int(request.POST.get('num1'))
                n2 = int(request.POST.get('num2'))
        
            finalans=n1+n2
            data ={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            
            return HttpResponse(finalans)
     
     except:
            pass
     




def calculator(request):
    
    c=''
    data={}
    try:
         if request.method=="POST":
              n1=eval(request.POST.get('num1'))
              n2=eval(request.POST.get('num2'))
              opr=request.POST.get('opr')
              if opr=="+":
                   c=n1+n2
              elif opr=="-":
                   c=n1-n2
              elif opr=="/":
                    c=n1/n2
              elif opr=="*":
                   c=n1*n2
                   data ={
                        'n1':n1,
                        'opr':opr,
                        'n2':n2,
                        'output':c
                    }
                    
                
                   
    except:
         c="Invalid operatiov...."
         
    return render(request,"Calculator.html",data)         


def EvenOdd(request):
    c=''
    
    if request.method =="POST":
        if request.POST.get('num')=="":
             return render(request,"evenodd.html",{'error':True})
        n= eval(request.POST.get('num')) 

        if n%2==0:
            c="Even Number"
        else:
            c="Odd Number"
      
    
    return render(request,"evenodd.html",{'c':c})

def Marksheet(request):
    if request.method=="POST":
         s1=eval(request.POST.get('sub1'))
         s2=eval(request.POST.get('sub2'))
         s3=eval(request.POST.get('sub3'))
         s4=eval(request.POST.get('sub4'))
         s5=eval(request.POST.get('sub5'))

         t=s1+s2+s3+s4+s5
         p=t*100/500;
         if p>60:
              d="First Div"
         elif p>40:
              d="Second Div"
         elif p>30:
              d="Third Div"
         else:
              d="Fail"
         data={
              'total':t,
              'per':p,
              'div':d
         }
         return render(request,"Marksheet.html",data)
    return render(request,"Marksheet.html")
         




    

     



