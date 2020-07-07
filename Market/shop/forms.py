from django import forms


class reg_form(forms.Form):
	name = forms.CharField(max_length=255)
	email = forms.CharField(max_length=255)
	password = forms.CharField(max_length=255)
	phone = forms.IntegerField()


class sign_in_form(forms.Form):
	email = forms.CharField(max_length=255)
	password = forms.CharField(max_length=8)


class add_product_form(forms.Form):
	name = forms.CharField(max_length=255)
	description = forms.CharField(max_length=1000, widget=forms.Textarea)
	image = forms.ImageField()


class search_products_form(forms.Form):
	nameSearch = forms.CharField(max_length=255, label="Поиск по товарам", required=False)