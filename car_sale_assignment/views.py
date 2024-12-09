from django.shortcuts import get_object_or_404, render
from brand.models import Brand
from car.models import Car


def main(request, brand_slug=None):
    cars = Car.objects.all()
    brands = Brand.objects.all()

    if brand_slug is not None:
        brand = get_object_or_404(Brand, slug=brand_slug)
        cars = cars.filter(brand=brand)  # Filter cars by selected brand

    total_cars = cars.count()

    return render(request, 'index.html', {
        'cars': cars,
        'brands': brands,
        'total_cars': total_cars,
    })