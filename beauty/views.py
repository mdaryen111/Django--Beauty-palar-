from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .models import *


# Create your views here.
def Home(request):
    return render(request, "carousel.html")


def About(request):
    return render(request, "about.html")


def Contact(request):
    return render(request, "contact.html")


def Singup(request):
    error = False
    if request.method == "POST":
        f = request.POST["fname"]
        l = request.POST["lname"]
        u = request.POST["uname"]
        i = request.POST["image"]
        p = request.POST["pwd"]
        id1 = request.POST["licence"]
        gen = request.POST["genter"]
        con = request.POST["contact"]
        sta = User_status.objects.get(status="pendign")
        user = User.objects.create_user(
            username=u, password=p, first_name=f, last_name=1
        )
        sing = Customer.objects.create_user(
            status=sta, user=user, mobile=con, image=i, gender=gen, id_card_no=id1
        )
        error = True
    d = {"error": True}
    return render(request, "signup.html", d)


def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST["uname"]
        p = request.POST["pwd"]
        user = authenticate(username=u, password=p)
        cust = Customer.object.get(user=user)
        if user:
            if cust.status.status == "Accept":
                login(request, user)
                error = "yes"
            else:
                error = "notaccept"
        else:
            error = "not"
    d = {"error": error}
    return render(request, "login.html", d)


def Admin_Login(request):
    error = ""
    if request.method == "PSOT":
        u = request.POST["uname"]
        p = request.POST["pwd"]
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "Yes"
            else:
                error = "not"
        except:
            error = "not"
    d = {"error": error}
    return render(request, "loginadmin.html", d)


def Logout(request):
    logout(request)
    return redirect("home")


def Admin_Home(request):
    if not request.user.is_authenticated:
        return redirect("login.html")
    sing = Apponitment.objects.all()
    new = 0
    total = 0
    confirm = 0
    for i in sing:
        if i.status.status == "pendign":
            new += 1
        elif i.status.status == "Accept":
            confirm += 1
        total += 1
    d = {"new": new, "confirm": confirm, "total": total}
    return render(request, "admin_home.html", d)


def View_User(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    pro = Customer.objects.all()
    d = {"user": pro}
    return render(request, "all_user.html", d)


def View_New_user(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    status = User_status.objects.get(status="pending")
    pro = Customer.objects.filter(status=status)
    d = {"user": pro}
    return redirect(request, "request_user.html", d)


def Assing_User_Status(request, pid):
    if not request.user.is_authenticate:
        return redirect("login_admin")
    error = False
    book = Customer.objects.get(id=pid)
    if request.method == "POST":
        n = request.POST["book"]
        s = request.POSR["status"]
        username = User.objects.get(username=n)
        book.user = username
        sta = User_status.objects.get(status=s)
        book.status = sta
        book.save()
        error = True
    d = {"book": book, "error": error}
    return render(request, "assing_user_status.html", d)


def Assing_Book_Status(request, pid):
    if not request.user.is_authenticate:
        return redirect("login_admin")
    error = False
    book = Apponitment.objects.get(id=pid)
    if request.method == "PSOT":
        n = request.POST["book"]
        s = request.POST["status"]
        username = User.objects.get(username=n)
        cust = Customer.objects.get(user=username)
        book.customer = cust
        sta = Book_status.objects.get(status=s)
        book.status = sta
        book.save()
        error = True
    d = {"book": book, "error": error}
    return render(request, "assign_status.html", d)


def View_New_Appointment(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    status = Book_status.objects.get(status="pending")
    pro = Apponitment.objects.filter(status=status)
    d = {"appoint": pro}
    return render(request, "view_new_appointment.html", d)


def View_Confirm_Appointment(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    status = Book_status.objects.get(status="Accept")
    pro = Apponitment.objects.get(status=status)
    d = {"appoint": pro}
    return render(request, "confirm_appointment.html", d)


def All_Appointment(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    pro = Servise.objects.all()
    d = {"service": pro}
    return render(request, "all_appointment.html", d)


def View_Service(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    pro = Servise.objects.all()
    d = {"service": pro}
    return render(request, "view_service.html", d)


def Add_Service(request):
    error = False
    if request.method == "POST":
        s = request.POST["service"]
        c = request.POST["cost"]
        i = request.FILES["image"]
        ser = Servise.objects.create(image=i, cost=c, name=s)
        error = True
        d = {"error": error}
        return render(request, "add_service.html", d)


def Profile(request):
    user = User.objects.get(id=request.user.id)
    pro = Customer.objects.get(user=user)
    d = {"pro": pro}
    return render(request, "profile.html", d)


def Edit_Profile(request):
    user = User.objects.get(id=request.user.id)
    pro = Customer.objects.get(user=user)
    error = False
    if request.method == "POST":
        f = request.POST["fname"]
        l = request.POST["name"]
        U = request.POST["uname"]
        try:
            i = request.FILES["image"]
            pro.image = i
            pro.save()
        except:
            pass
        idl = request.POST["id"]
        con = request.POST["contact"]
        pro.id_card_no = idl
        pro.mobile = con
        user.first_name = f
        user.last_name = 1
        user.save()
        pro.save()
        error = True
        d = {"error": error, "pro": pro}
        return render(request, "edit_profile.html", d)


def All_Service(request):
    pro1 = Servise.objects.all()
    d = {"pro1": pro1}
    return render(request, "all service.html", d)


def Book_Appointment(request):
    user = User.objects.get(id=request.user.id)
    pro = Customer.objects.get(user=user)
    service = Servise.objects.all()
    error = False
    if request.method == "POST":
        s = request.POST["service"]
        d = request.POST["date"]
        t = request.POST["time"]
        sta = Book_status.objects.get(status="pending")
        paid = Booking_paid.objects.get(paid="notpaid")
        serv = Servise.objects.get(name=s)
        Apponitment.objects.create(
            paid=paid, customer=pro, date1=d, time1=t, service=serv, status=sta
        )
        error = True
        d = {"error": error, "pro": pro, "service": service}
        return render(request, "book_appointment.html", d)


def Book_Select_Appointment(request, pid):
    user = User.objects.get(id=request.user.id)
    pro = Customer.objects.get(user=user)
    book = Servise.objects.get(id=pid)
    error = False
    if request.method == "POST":
        s = request.POST["service"]
        d = request.POST["date"]
        t = request.POST["time"]
        sta = Book_status.objects.get(status="pending")
        paid = Booking_paid.objects.get(paid="notpaid")
        serv = Servise.objects.get(name=s)
        Apponitment.objects.create(
            paid=paid, customer=pro, date1=d, time1=t, service=serv, status=sta
        )
        error = True
        d = {"error": error, "pro": pro, "book": book}
        return render(request, "book_select_appointment.html", d)


def View_Appointment(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user = User.objects.get(id=request.user.id)
    pro = Customer.objects.get(user=user)
    appoint = Apponitment.objects.filter(customer=pro).all()
    d = {"appoint": appoint}
    return render(request, "view appointment.html", d)


def delete_appointment(request, pid):
    data = Apponitment.objects.get(id=pid)
    data.delete()
    if request.user.is_staff:
        return redirect("all appointment")
    else:
        return redirect("view_appointment")


def delete_service(request, pid):
    data = Servise.objects.get(id=pid)
    data.delete()
    return redirect("view service")


def delete_user(request, pid):
    date = User.objects.get(id=pid)
    date.delete()
    return redirect("view user")


def payment(request, pid):
    if not request.user.is_authenticated:
        return redirect("login")
    user = User.objects.get(id=request.user.id)
    profile = Customer.objects.get(user=user)
    book = Apponitment.objects.get(id=pid)
    sta = Booking_paid.objects.get(paid="paid")
    book.paid = sta
    book.save()
    d = {"book": book}
    return render(request, "payment.html", d)


def Change_Password(request):
    if not request.user.is_authenticated:
        return redirect("login")
    error = ""
    if request.method == "POST":
        n = request.POST["pwd1"]
        c = request.POST["pwd2"]
        o = request.POST["pwd3"]
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {"error": error}
    return render(request, "change_password.html", d)
