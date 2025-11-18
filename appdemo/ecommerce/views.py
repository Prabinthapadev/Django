from django.shortcuts import render,redirect
from .models import User , Product , CartItem
from django.contrib.auth import authenticate,login as auth_login
# Create your views here.
def home(request):
    username = request.session.get('username')
    password = request.session.get('password')

    user_info = {
        "username":username,
        "password":password,
    }
    return render(request,'home.html',user_info)

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pw = request.POST.get('pass')

        # Authenticate user using Django's built-in method
        user = authenticate(request, username=uname, password=pw)

        if user is not None:
            # Log the user in and create a session
            auth_login(request, user)
            return redirect('product_list')  # or 'cart_page' if you prefer
        else:
            # Invalid credentials
            return render(request, 'login.html', {
                'error_msg': "Username or password is incorrect."
            })

    # GET request — show login form
    return render(request, 'login.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        confirm_pass = request.POST.get('cpass')

        # Storing the data into the database
        if password == confirm_pass:
            User.objects.create(username = username,password = password)
            return redirect('login')
        else:
            return render(request,'signup.html',{
                "error_msg":"Details didnot matched",
            })

    return render(request,'signup.html')

def logout(request):
    request.session.flush()
    return redirect('login')

# Now from here code for add_to_cart button

def product_list(request):
    products = Product.objects.all()
    cart_count = CartItem.objects.filter(user = request.user).count() if request.user.is_authenticated else 0
    return render(request,'product_list.html',{
        "products":products,
        "cart_count":cart_count
    })

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('product_list')
    # if cart is None:
    #     cart = {}
    #     product_id = str(product_id)
    # if product_id in cart:
    #     cart[product_id]+=1
    # else:
    #     cart[product_id]= 1
    # request.session['cart'] = cart

# def get_cart_count(request):
#     cart = request.session.get('cart',{})
#     return sum(cart.values())

def cart_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = CartItem.objects.filter(user=request.user)
    total_amount = sum(item.total_price() for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_amount': total_amount,
    })

