from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Users, Products
from .forms import reg_form, sign_In_form, add_product_form, search_products_form
from django.core.files.storage import FileSystemStorage


WelcomeMessage = 'Хотите разместить свой товар? '
AboutMessage = 'Это площядка для размещения объявлений.'


def root_url(request):
    return redirect('./about/')


def about(request):
    return render(request, 'About.html', context={'message': AboutMessage, 'Aut': request.session.get('Aut', False)})


def reg(request):
    if request.method == 'POST':
        user = users.objects.filter(email=request.POST['email'])

        if user.count() > 0:
            return render(request, 'Reg.html', context={'message': 'Такой аккаунт уже есть! '})

        else:
            user = users()
            user.email = request.POST['email']
            user.phone = request.POST['phone']
            user.name = request.POST['name']
            user.password = request.POST['password']
            user.save()

            request.session['Aut'] = True
            request.session['iduser'] = user.id
            return render(request, 'Reg.html', context={'message': 'Вы зарегистрированы'})

    else:
        reg_form = reg_form()
        return render(request, 'Reg.html', context={'Form': reg_form})


def sign_out(request):
    if request.session.get('Aut', False):
        request.session['Aut'] = False
        request.session['iduser'] = None
        return render(request, 'SignIn.html', context={'message': 'Вы вышли'})

    else:
        return render(request, 'SignIn.html', context={'message': 'Вы не авторизованы'})


def sign_in(request):
    if request.method == 'POST':
        user = users.objects.filter(email=request.POST['email'])


        if request.session.get('Aut', False) == True:
            return render(request, 'SignIn.html', context={'message': 'Вы уже авторизованы', 'Aut': True})

        elif user.count() == 0:
            Newsign_In_form = sign_In_form()
            return render(request, 'SignIn.html', context={'Form': Newsign_In_form, 'message': 'Неправильный логин или пароль(Такого аккаунта нет)'})

        elif user[0].password == request.POST['password']:
            request.session['Aut'] = True
            request.session['iduser'] = user[0].id

            return render(request, 'SignIn.html', context={'message': 'Вход выполнен успешно', 'Aut': True})

        else:
            Newsign_In_form = sign_In_form()
            return render(request, 'SignIn.html', context={'Form': Newsign_In_form, 'message': 'Неправильный логин или пароль'})

    else:
        if not request.session.get('Aut', False):
            Newsign_In_form = sign_In_form()
            return render(request, 'SignIn.html', context={'Form': Newsign_In_form, 'message': WelcomeMessage + 'Пожалуйста, авторизуйтесь'})

        else:
            return render(request, 'SignIn.html', context={'message': 'Вы уже авторизованы', 'Aut': True})


def me(request):
    if not request.session.get('Aut', False):
        return redirect('../signin/')

    else:
        user = users.objects.get(id=request.session['iduser'])
        userProducts = Products.objects.filter(user=user)
        NewForm = reg_form()

        if request.method == 'POST':
            user = users.objects.get(id=request.session['iduser'])
            user.email = request.POST['email']
            user.phone = request.POST['phone']
            user.name = request.POST['name']
            user.password = request.POST['password']
            user.save()

            return render(request, 'Me.html', context={'Aut': True, 'userData': user, 'Form': NewForm, 'Products': userProducts, 'message': 'Данные обновлены'})

        else:
            return render(request, 'Me.html', context={'Aut': True, 'userData': user, 'Form': NewForm, 'Products': userProducts})


def add_product(request):
    if not request.session.get('Aut', False):
        return redirect('../signin/')
    else:
        NewForm = add_product_form()
        message = ''

        if request.method == 'POST':
            user = users.objects.get(id=request.session['iduser'])
            newproduct = Products(user=user)
            newproduct.name = request.POST['name']
            newproduct.description = request.POST['description']

            newproduct.save()

            uplfile = request.FILES['image']
            fs = FileSystemStorage()
            save_url = str(user.id) + '_' + str(newproduct.id) + '_img.jpg' 
            filename =  fs.save(save_url,uplfile)
            print(filename, fs.url(filename))
            newproduct.img = filename

            newproduct.save()
            message = 'Товар добален'
            

        return render(request, 'AddProduct.html', context={'Aut':True, 'Form': NewForm, 'message':message})

def edit_product(request, idProduct):
    if not request.session.get('Aut', False):
        product = Products.objects.filter(id=idProduct)
    
    if product.count() == 0:
        return render(request, 'ShowProduct.html', context={'Aut'})

def show_all_products(request):
    message = ''
    nameSearch = ''
    Aut = request.session.get('Aut', False)
    SearchForm = search_products_form()
    
    try:
        nameSearch = request.GET['nameSearch']
        if nameSearch != '':
            products = Products.objects.filter(name=nameSearch)
        else:
            products = Products.objects.all()        
        

    except:
        products = Products.objects.all()        
        
    return render(request, 'ShowAllProducts.html', context={'Aut':Aut, 'products': products, 'Form': search_products_form})

def show_product(request, idProduct):
    product = Products.objects.filter(id=idProduct)
    Aut = request.session.get('Aut', False)
    print(product, product.count())
    if product.count() == 0:
        return render(request, 'ShowProduct.html', context={'Aut':Aut, 'message': 'Такого товара нет'})
    else:
        user = product[0].user.name
        phoneuser = product[0].user.name
        return render(request, 'ShowProduct.html', context={'Aut':Aut, 'product': product[0], 'owner': user, 'phoneowner': phoneuser})

