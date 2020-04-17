from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Users, Products
from .forms import RegForm, SignInForm, AddProductForm, SearchProductsForm
# Create your views here.
from django.core.files.storage import FileSystemStorage

WalcomeMessage = 'Хотите разместить свой товар? '
AboutMessage = 'Это площядка для размещения объявлений.'


def RootUrl(request):
    return redirect('./about/')


def About(request):

    return render(request, 'About.html', context={'message': AboutMessage, 'Aut': request.session.get('Aut', False)})


def Reg(request):
    if request.method == 'POST':
        user = Users.objects.filter(Email=request.POST['Email'])

        if user.count() > 0:
            return render(request, 'Reg.html', context={'message': 'Такой аккаунт уже есть! '})

        else:
            user = Users()
            user.Email = request.POST['Email']
            user.Phone = request.POST['Phone']
            user.Name = request.POST['Name']
            user.Password = request.POST['Password']
            user.save()

            request.session['Aut'] = True
            request.session['idUser'] = user.id
            return render(request, 'Reg.html', context={'message': 'Вы зарегистрированы'})

    else:
        regform = RegForm()
        return render(request, 'Reg.html', context={'Form': regform})


def SignOut(request):
    if request.session.get('Aut', False):
        request.session['Aut'] = False
        request.session['idUser'] = None
        return render(request, 'SignIn.html', context={'message': 'Вы вышли'})

    else:
        return render(request, 'SignIn.html', context={'message': 'Вы не авторизованы'})


def SignIn(request):
    if request.method == 'POST':
        user = Users.objects.filter(Email=request.POST['Email'])


        if request.session.get('Aut', False) == True:
            return render(request, 'SignIn.html', context={'message': 'Вы уже авторизованы', 'Aut': True})

        elif user.count() == 0:
            NewSignInForm = SignInForm()
            return render(request, 'SignIn.html', context={'Form': NewSignInForm, 'message': 'Неправильный логин или пароль(Такого аккаунта нет)'})

        elif user[0].Password == request.POST['Password']:
            request.session['Aut'] = True
            request.session['idUser'] = user[0].id

            return render(request, 'SignIn.html', context={'message': 'Вход выполнен успешно', 'Aut': True})

        else:
            NewSignInForm = SignInForm()
            return render(request, 'SignIn.html', context={'Form': NewSignInForm, 'message': 'Неправильный логин или пароль'})

    else:
        if not request.session.get('Aut', False):
            NewSignInForm = SignInForm()
            return render(request, 'SignIn.html', context={'Form': NewSignInForm, 'message': WalcomeMessage + 'Пожалуйста, авторизуйтесь'})

        else:
            return render(request, 'SignIn.html', context={'message': 'Вы уже авторизованы', 'Aut': True})


def Me(request):
    if not request.session.get('Aut', False):
        return redirect('../signin/')

    else:
        user = Users.objects.get(id=request.session['idUser'])
        UserProducts = Products.objects.filter(User=user)
        NewForm = RegForm()

        if request.method == 'POST':
            user = Users.objects.get(id=request.session['idUser'])
            user.Email = request.POST['Email']
            user.Phone = request.POST['Phone']
            user.Name = request.POST['Name']
            user.Password = request.POST['Password']
            user.save()

            return render(request, 'Me.html', context={'Aut': True, 'UserData': user, 'Form': NewForm, 'Products': UserProducts, 'message': 'Данные обновлены'})

        else:
            return render(request, 'Me.html', context={'Aut': True, 'UserData': user, 'Form': NewForm, 'Products': UserProducts})


def AddProduct(request):
    if not request.session.get('Aut', False):
        return redirect('../signin/')
    else:
        NewForm = AddProductForm()
        message = ''

        if request.method == 'POST':
            user = Users.objects.get(id=request.session['idUser'])
            newproduct = Products(User=user)
            newproduct.Name = request.POST['Name']
            newproduct.Description = request.POST['Description']

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

def EditProduct(request, idProduct):
    if not request.session.get('Aut', False):
        product = Products.objects.filter(id=idProduct)
    
    if product.count() == 0:
        return render(request, 'ShowProduct.html', context={'Aut'})

def ShowAllProducts(request):
    message = ''
    NameSearch = ''
    Aut = request.session.get('Aut', False)
    SearchForm = SearchProductsForm()
    
    try:
        NameSearch = request.GET['NameSearch']
        if NameSearch != '':
            products = Products.objects.filter(Name=NameSearch)
        else:
            products = Products.objects.all()        
        

    except:
        products = Products.objects.all()        
        
    return render(request, 'ShowAllProducts.html', context={'Aut':Aut, 'products': products, 'Form': SearchProductsForm})

def ShowProduct(request, idProduct):
    product = Products.objects.filter(id=idProduct)
    Aut = request.session.get('Aut', False)
    print(product, product.count())
    if product.count() == 0:
        return render(request, 'ShowProduct.html', context={'Aut':Aut, 'message': 'Такого товара нет'})
    else:
        user = product[0].User.Name
        phoneuser = product[0].User.Name
        return render(request, 'ShowProduct.html', context={'Aut':Aut, 'product': product[0], 'owner': user, 'phoneowner': phoneuser})

