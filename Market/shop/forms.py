from django import forms

class RegForm(forms.Form):
	Name = forms.CharField(max_length=255)
	Email = forms.CharField(max_length=255)
	Password = forms.CharField(max_length=255)
	Phone = forms.IntegerField()

class SignInForm(forms.Form):
	Email = forms.CharField(max_length=255)
	Password = forms.CharField(max_length=8)

class AddProductForm(forms.Form):
	Name = forms.CharField(max_length=255)
	Description = forms.CharField(max_length=1000, widget=forms.Textarea)
	image = forms.ImageField()

class SearchProductsForm(forms.Form):
	NameSearch = forms.CharField(max_length=255, label="Поиск по товарам", required=False)