from django import forms


class reg_form(forms.Form):
	Name = forms.CharField(max_length=255)
	Email = forms.CharField(max_length=255)
	Password = forms.CharField(max_length=255)
	Phone = forms.IntegerField()


class sign_in_form(forms.Form):
	Email = forms.CharField(max_length=255)
	Password = forms.CharField(max_length=8)


class add_product_form(forms.Form):
	Name = forms.CharField(max_length=255)
	Description = forms.CharField(max_length=1000, widget=forms.Textarea)
	image = forms.ImageField()


class search_products_form(forms.Form):
	NameSearch = forms.CharField(max_length=255, label="Поиск по товарам", required=False)