from django.shortcuts import render, get_object_or_404

from gallery.models import Category, Image


def gallery_view(request):
    categories = Category.objects.all()
    return render(request, 'gallery.html', {'categories': categories})


def image_detail(request, pk: int):
    image = Image.objects.filter(pk=pk).first()
    return render(request, 'image_detail.html', {'image': image})
