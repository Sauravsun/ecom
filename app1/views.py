from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os 
from django.conf import settings
from django.core.mail import send_mail
import stripe
# Create your views here.

def index(request):
    qry=adproduct.objects.all()
    # return render(request,'product_table.html',{"data1":qry})    
    return render(request,'index.html',{"data1":qry})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def blog(request):
    return render(request,'blog.html')

def shop(request):
    return render(request,'shop.html')

# def cart(request):
#     return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def wishlist(request):
    return render(request,'wishlist.html')


def product(request):
    return render(request,'product-details.html')

def baudio(request):
    return render(request,"blog-details-audio.html")  

def bgallery(request):
    return render(request,"blog-details-gallery.html")


def bimage(request):
    return render(request,"blog-details-image.html")


def bvideo(request):
    return render(request,"blog-details-video.html")


def bright(request):
    return render(request,"blog-details-right-sidebar.html")


def register(request):
    if request.method=='POST':
        mail=request.POST['regemail']
        password=request.POST['regpass']
        add=registertb(email=mail,passw=password)
        add.save()
        return render(request,"login.html")
    
    else:
         return render(request,"register.html")
    


def prod_modal(request):
    pid=request.GET['uid']
    qry=adproduct.objects.filter(id=pid)
    return render(request,"product-details.html",{"data5":qry})


def logint(request):
    if request.method=='POST':
        user=request.POST['username_email']
        passwo=request.POST['password']
        were=registertb.objects.filter(email=user)
        if were:
            for i in were:
                pas=i.passw
                if pas==passwo:
                    for x in were:
                        request.session['id']=x.id
                        request.session['email']=x.email
                    return redirect('/')
                else:
                     return render(request,"login.html",{'mess':"not registerd pass"})
        else:
            return render(request,"login.html",{'mess':"not registerd email"})
    else:
            return render(request,"login.html",{'mess':"not registerd enter valid details"})     

def updatecart(request):
    ci=request.GET['cid']
    quan=request.POST['qty']
    cart=cart_tb.objects.filter(id=ci)
    totalamount=0
    for i in cart:
        price=i.pids.price
        totalamount=(float(price)*int(quan))
        cart_tb.objects.filter(id=ci).update(quantity=quan,total=totalamount)

    return HttpResponseRedirect("/cart/")


def cart(request):
    use=request.session['id']
    usr=cart_tb.objects.filter(uids=use)
    total=0
    for i in usr:
        total+=float(i.total)
    return render(request,'cart.html',{"data":usr,'total':total})


# addtocart
def addcart(request):
    if request.session.has_key("id"):
        if request.method=='POST':
        
            pid=request.GET['pid']
            prd=adproduct.objects.get(id=pid)

            uid=request.session['id']
            usr=registertb.objects.get(id=uid)
            # addig price of the cart
            products=adproduct.objects.filter(id=pid)
            for x in products:
                cartprice=x.price
                total=0
                total=float(cartprice)

                cart1=cart_tb.objects.filter(uids=usr,pids=prd)
                if cart1:
                    for x in cart1:
                        qty=int(x.quantity)
                        qty+=1
                        total1=float(x.total)
                        total1+=float(total)
                    
                    
                    add=cart_tb.objects.filter(uids=usr,pids=prd,).update(quantity=qty,total=total1)

                    data3=cart_tb.objects.filter(uids=uid)
                    gtotal=0
                    for x in data3:
                        price=x.total
                        gtotal=gtotal+float(price)
                    return render(request,'cart.html',{'data':data3,'total':gtotal})

                else:
                    # adding item in the cart
                    add=cart_tb(uids=usr,pids=prd,quantity='1',total=total)    
                    add.save()
                    data3=cart_tb.objects.filter(uids=uid)
                    total=0
                    for x in data3:
                        price=x.total
                        total=total+float(price)
                    return render(request,'cart.html',{'data':data3,'total':total})
                
        else:
            
            pid=request.GET['uid']
            qry=adproduct.objects.filter(id=pid)
            return render(request,"product-details.html",{"data2":qry})
        
    else:
        return redirect("/login/")
    



def contact(request):

    if request.method=='POST':
        name=request.POST['contact_name']
        cmail=request.POST['contact_email']
        msg=request.POST['contact_message']

        # email message content
        # subject="contact form"
        # message= f'There is message from {name} email {cmail}. The message is {msg}. Thankyou.'
        # email_from = settings.EMAIL_HOST_USER 
        # recipient_list = [settings.EMAIL_HOST_USER, ] 
        # send_mail(subject,message,email_from,recipient_list)


        subject = 'Contact Form'
        message = f'There is message from {name} email {cmail}. The message is {msg}. Thankyou.'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [settings.EMAIL_HOST_USER, ] 
        send_mail( subject, message, email_from, recipient_list ) 


        #replay
        # subject='thank you for submitting'
        # message=f"thank you {name} enquiry wil be in touch with you  soon"
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list=[cmail, ]
        # send_mail(subject,message,email_from,recipient_list)

        subject = ' thank for submitting Contact Form'
        message = f'Hi {name}, Thankyou for submitting form.'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [cmail, ] 
        send_mail( subject, message, email_from, recipient_list )


        return render(request,"index.html")
    else:
        return render(request,'contact.html')
    



stripe.api_key=settings.STRIPE_SECRET_KEY
def checkout(request):

    tot=request.GET['tot']

    print(tot,"///////////////////////////////")
    tot1=float(tot)*100
    
    session=stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            "price_data": {
                "currency": "inr",
                "product_data": {"name": "T-shirt"},
                "unit_amount": int(tot1),
            },
            'quantity':1,


        }],
        mode='payment',
        success_url='http://localhost:8000/about/',
        cancel_url="http://127.0.0.1:8000/cart/"


    )
    return redirect(session.url,code=303)




#admin
def ind(request):
    if request.session.has_key("aid"):
        return render(request,"admin1/index.html")
    else:
       return render(request,"admin1/login.html")            


def base(request):
    return render(request,'admin1/basic_table.html')


def form(request):
    return render(request,"admin1/form_component.html")


def product(request):
    qry=adproduct.objects.all()
    return render(request,'admin1/product_table.html',{"data1":qry})
 
def addprod(request):
    if request.method=='POST':
        mname=request.POST['mcolor']
        mimage=request.FILES['image']
        price=request.POST['price']
        mcolor=request.POST['mcolor']
        descrption=request.POST['proddesciption']
        mcategory=request.POST['category']
        psize=request.POST['msize']
        addp=adproduct(modelname=mname, modelcolor=mcolor,price=price, image=mimage,description=descrption,productsize=psize,category=mcategory)
        addp.save()
        qry=adproduct.objects.all()
        return render(request,'admin1/product_table.html',{"data1":qry})
    else:
        return render(request,'admin1/product.html')
    
    
def admin_login(request):
    if request.method=='POST':
        admail=request.POST['Email']
        adpass=request.POST['Password']
        adcd=admin_logins.objects.filter(email=admail)
        if adcd:
            for i in adcd:
                passwer=i.passw
            if passwer==adpass:
                for x in adcd:
                    request.session['aid']=x.id
                    request.session['Email']=x.email  
                return render(request,'admin1/index.html')
            else:
                return render(request,"admin1/login.html",{"messs":"password is not correct try again"})
        else:
            return render(request,"admin1/login.html",{"messs":"mail is not correct"})    
    else:
        return render(request,"admin1/login.html",{"messs":"enter mail and pass"})  
    


def prod_update(request):
    if request.method=='POST':
        pid=request.GET['uid']
        uname=request.POST['ucolor']
        # uimage=request.FILES['uimage']
        uprice=request.POST['uprice']
        ucolor=request.POST['ucolor']
        udescrption=request.POST['uproddesciption']
        ucategory=request.POST['ucategory']
        usize=request.POST['umsize']
        checkbox=request.POST['imgeup']
        # updating image
        if checkbox == "yes":
            uimage=request.FILES['uimage']
            old_img=adproduct.objects.filter(id=pid)
            new_img=adproduct.objects.get(id=pid)
            for x in old_img: #getting old image path for delete
                imageurl=x.image.url #image url
                imagepath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imageurl #function for finding path
                if os.path.exists(imagepath):
                    os.remove(imagepath)
                    print('succefully delete')
            new_img.image=uimage #image=model varaiable name for image
            new_img.save()    
        adds=adproduct.objects.filter(id=pid).update(modelname=uname,modelcolor=ucolor,price=uprice,description=udescrption,productsize=usize,category=ucategory)
        return HttpResponseRedirect("/product/")
    else:
            
            pid=request.GET['uid']
            adds=adproduct.objects.filter(id=pid)
        
            return render(request,"admin1/proupdate.html",{"data2":adds})


def prod_delete(request):
    dele=request.GET.get('uid')
    # deleteimage
    old_img=adproduct.objects.filter(id=dele)
    for x in old_img:
        imageurl=x.image.url
        imagepath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imageurl
        if os.path.exists(imagepath):
            os.remove(imagepath)
            print('succefully delete')
    add=adproduct.objects.filter(id=dele).delete()
    return HttpResponseRedirect("/product/")   





