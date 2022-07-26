from django.shortcuts import get_object_or_404, render,redirect
from login.models import Member
from .models import  accesory, body, cosmetic, offers, product ,man, woman ,Cart
from django.db.models import Q

# Create your views here.
def home(request):
    if 'email' in request.session.keys():
        ho=offers.objects.all()
        # user = Member.objects.get()
        s=request.session['email']
        a=Member.objects.get(email=s)
        count = Cart.objects.filter().count()
            # return render(request,"index.html",{'count':count})
        # count = 0
        return render(request,'index.html',{'hh':ho,'count':count})
    else:
        return redirect('Login')

def women(request):
    if 'email' in request.session.keys():
        s=request.session['email']
        a=Member.objects.get(email=s)
        wo=woman.objects.all()
        return render(request,'women.html',{'ad':wo})
    else:
        return redirect('Login')

def men(request):
    if 'email' in request.session.keys():
        s=request.session['email']
        a=Member.objects.get(email=s)
        me=man.objects.all()
        return render(request,'men.html',{'m':me})
    else:
        return redirect('Login')

def products(request):
    if 'email' in request.session.keys():
        s=request.session['email']
        a=Member.objects.get(email=s)
        data1=search(request)
        return render(request,'product.html',data1)
    else:
        return redirect('Login')

def accessory(request):
    if 'email' in request.session.keys():
        s=request.session['email']
        a=Member.objects.get(email=s)
        ac=accesory.objects.all()
        return render(request,'accessory.html',{'ab':ac})
    else:
        return redirect('Login')

def cosmetics(request):
    if 'email' in request.session.keys():
        s=request.session['email']
        a=Member.objects.get(email=s)
        co=cosmetic.objects.all()
        return render(request,'cosmetics.html',{'ac':co})
    else:
        return redirect('Login')

def bodyskin(request):
    if 'email' in request.session.keys():
        s=request.session['email']
        a=Member.objects.get(email=s)
        bo=body.objects.all()
        return render(request,'body&skin.html',{'aa':bo})
    else:
        return redirect('Login')

def cart(request):
    if 'email' in request.session.keys():
        s=request.session['email']
        user = Member.objects.get(email=s)
        cart = Cart.objects.filter(user_id=user.id)
        category = product.objects.all()
        total = []
        for i in cart:
            total.append(i.price)
        total=sum(total)
        return render(request,"cart.html",{'cart':cart,'category':category,'total':total})
        # return render(request,'cart.html')
    else:
        return redirect('Login')

def about(request):
    if 'email' in request.session.keys():
        s=request.session['email']
        a=Member.objects.get(email=s)
        return render(request,'about.html')
    else:
        return redirect('Login')


def search(request):
    q = request.GET.get('search')
    list_pro = product.objects.all()
    if q:
        pro = product.objects.filter(Q(name__icontains=q) | Q(desc__icontains=q))
        data = {
            'pro': pro,
        }
        # print("if executes")
    else:
        data = {
            'pro': list_pro,
        }
        # print("else executes")

    return data



def productall(request):
    if 'email' in request.session.keys():
        data1=search(request)
        s=request.session['email']
        a=Member.objects.get(email=s)

        return render(request,'productall.html',data1)
    else:
        return redirect('Login')
    # a=product.objects.all()

    # return render(request,'productall.html',{'a':a})

def logout(request):
    if 'email' in request.session.keys():
        del request.session['email']
        return redirect('Login')
    else:
        return redirect('Login')


def proview(request,abc):
    g=product.objects.get(id=abc)
    #g=get_object_or_404(product,id=abc)
    return render(request,'proview.html',{'g':g})

def productdelete(req,id):
    b=get_object_or_404(product,id=id)
    b.delete()
    return redirect('product')  

def add_to_cart(request,id):
    if 'email' in request.session.keys():
        s=request.session['email']
        user = Member.objects.get(email=s)
        pr = product.objects.get(id=id)
        count = Cart.objects.filter(user_id=user.id,product_id=pr.id).count()
        cart = Cart.objects.filter(user_id=user.id,product_id=pr.id)
        print("####",count)
        if count>0:
            qty = cart[0].qty+1
            price = qty*pr.offpri
            Cart.objects.filter(user_id=user.id,product_id=pr.id).update(qty=qty,price=price)
            return redirect('cart')
        else:
            Cart(user_id=user.id,product_id=pr.id,qty=1,price=pr.price).save()
            return redirect('cart')
    else:
        return redirect('Login')

def minus(request,id):
    cart = Cart.objects.filter(id=id)
    if cart[0].qty==1:
        qty = 1
    else:
        qty = cart[0].qty-1

    price = qty * cart[0].product.offpri
    Cart.objects.filter(id=id).update(price=price,qty=qty)
    return redirect('cart')

def plus(request,id):
    cart = Cart.objects.filter(id=id)
    qty = cart[0].qty+1
    price = qty * cart[0].product.offpri
    Cart.objects.filter(id=id).update(price=price,qty=qty)
    return redirect('cart')

def price(request,id):
    c= Cart.objects.filter(id=id)
    price= c[0].price
    p= price+c[0].product.offpri
    Cart.objects.filter(id=id).update(price=price)
    return redirect('cart')

def delete(request,id):
    cart = get_object_or_404(Cart,id=id)
    cart.delete()
    return redirect('cart')

# def calculator(request):
#     if request.POST:
#         model=cal()
#         model.val1=int(request.POST['val1'])
#         model.val2=int(request.POST['val2'])
#         opt=request.POST['opt']
#         model.save()
#         if opt =='add':
#             ans=model.val1+model.val2
#             answer=ans
#             ans=answer
#             return render(request,'calculator.html',{'ans':ans,'val1':model.val1,'val2':model.val2,'o':opt})
#         elif opt =='sub':
#             ans=model.val1-model.val2
#             return render(request,'calculator.html',{'ans':ans,'val1':model.val1,'val2':model.val2,'o':opt})
#         elif opt =='mul':
#             ans=model.val1*model.val2
#             return render(request,'calculator.html',{'ans':ans,'val1':model.val1,'val2':model.val2})
#         elif opt =='div':
#             ans=model.val1/model.val2
#             return render(request,'calculator.html',{'ans':ans,'val1':model.val1,'val2':model.val2})

        
#     return render(request,'calculator.html')

