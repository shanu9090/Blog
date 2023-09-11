from django.shortcuts import render, redirect
from app.models import *

# Create your views here.
def homepage(req):
    return render(req, "app/homepage.html")
# ***************************************************************************
def adminreg(req):
    return render(req, "app/adminreg.html")

def adminreginsert(req):
    if req.method == "POST":
        n = req.POST.get('aname')
        if not n.isalpha():
            msg1 = "please passed character input"
            return render(req, "app/adminreg.html", {'msg1': msg1})
        e = req.POST.get('aemail')
        p = req.POST.get('apswd')
        cp = req.POST.get('apswdd')
       # print("fatch paswadd:.......")
        user = AdminDB.objects.filter(Email=e)
      #  print("match emailId.....")
        if user:
            msg = "User Are Already Exist"
            return render(req, "app/adminreg.html", {'msg': msg})
        else:
            if p == cp:
                msg = "Login Successfully"
                AdminDB.objects.create(Fname=n, Email=e, Password=p)
                return render(req, "app/adminlogin.html", {'msg': msg})
            else:
                msg = "Password and currentpassword don't match"
                return render(req, "app/adminreg.html", {'msg': msg})

    return render(req, "app/adminreg.html")


def adminlogin(req):
    return render(req, "app/adminlogin.html")


def adminlogininsert(req):
    if req.method == "POST":
        email = req.POST.get('email')
        passw = req.POST.get('password')
       # print("fatch adminlogin inforation....")
        ad = AdminDB.objects.get(Email=email)
       # print("match email adminlogin")
        if ad:
            if ad.Password == passw:
                AdminDB.objects.get(Email=email, Password=passw)
                #print("password are matched")
                return render(req, "app/admindashbod.html")
            else:
                msg = "Password and Email are not match"
                return render(req, "app/adminlogin.html", {'msg': msg})
    return render(req, "app/adminlogin.html")


# *******************************************************************************

def userreg(req):
    return render(req, "app/userreg.html")


def userreginsert(req):
    if req.method == "POST":
        n = req.POST.get('aname')
        if not n.isalpha():
            msg1 = "please passed character input"
            return render(req, "app/userreg.html", {'msg1': msg1})
        e = req.POST.get('aemail')
        p = req.POST.get('apswd')
        cp = req.POST.get('apswdd')
       # print("fatch paswadd:.......")
    try:   
        user = UserDB.objects.filter(Email=e)
       # print("match emailId.....")
        if user:
            msg = "User Are Already Exist"
            return render(req, "app/userreg.html", {'msg': msg})
        else:
            if p == cp:
                msg = "Login Successfully"
                UserDB.objects.create(Fname=n, Email=e, Password=p)
                return render(req, "app/userlogin.html", {'msg': msg})
            else:
                msg = "Password and currentpassword don't match"
                return render(req, "app/userreg.html", {'msg': msg})
    except:
         msg = "email don't match"
         return render(req, "app/userreg.html", {'msg': msg})

def userlogin(req):
    return render(req, "app/userlogin.html")


def userlogininsert(req):
    if req.method == "POST":
        email = req.POST['email']
        passw = req.POST['password']
        #print("fatch adminlogin inforation....")
        try:
            user = UserDB.objects.filter(Email=email).first()
            #print("match email userlogin")
            if user:
                if user.Password == passw:
                    UserDB.objects.get(Email=email, Password=passw)
                    #print("password are matched")
                    return render(req, "app/insertrecord.html")
                else:
                   msg1 = "Password and Email are not match"
                   return render(req, "app/userlogin.html", {'msg1': msg1})
        except:
            msg1 = "Email are not match"
            return render(req, "app/userlogin.html", {'msg1': msg1})
    return render(req, "app/userlogin.html")

# ********************************************************************************


def insertrecord(req):
    return render(req, "app/insertrecord.html")


def quiryinsert(req):
    if req.method == "POST":
        fname = req.POST['fname']
        lname = req.POST['lname']
        email = req.POST['email']
        phone = req.POST['phone']
        quiry = req.POST['enquiry']
        #print("insert data")
        EnquiryDB.objects.create(
            Fname=fname, Lname=lname, Email=email, Contact=phone, Quiry=quiry)
        msg = "Data are Successfully Insert"
        return render(req, "app/insertrecord.html", {'msg': msg})
    return render(req, "app/insertrecord.html")

# ******************************************************************************


def displayrecord(req):
    all_data = EnquiryDB.objects.all()
    return render(req, "app/displayrecord.html", {'key1': all_data})


def updatepage(req, pk):
    data_update = EnquiryDB.objects.get(id=pk)
    return render(req, "app/updatepage.html", {'key2': data_update})


def update(req, pk):
   ddata = EnquiryDB.objects.get(id=pk)
   ddata.Fname = req.POST['fname']
   ddata.Lname = req.POST['lname']
   ddata.Quiry = req.POST['enquiry']
   ddata.Email = req.POST['email']
   ddata.Contact = req.POST['phone']

   ddata.save()
   return redirect('displayrecord')


def delete(req, pk):
    deletedata = EnquiryDB.objects.get(id=pk)
    # Query for delete
    deletedata.delete()
    return redirect('displayrecord')
