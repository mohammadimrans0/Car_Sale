from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from brand.forms import BrandForm
from brand.models import Brand

# Create Brand
@login_required
def create_brand(request):
    if request.method == 'POST':
        brand_form = BrandForm(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            brand_form = BrandForm()
    else:
        brand_form = BrandForm()

    brands = Brand.objects.all()

    return render(request, 'create_brand.html', {'form': brand_form, 'brands': brands})