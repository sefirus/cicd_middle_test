import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from gallery.models import Category, Image


@pytest.mark.django_db
def test_image_detail_view_success(client: Client):
    category = Category.objects.create(name="Category 1")
    image = Image.objects.create(title="Image 1", image="test_image.jpg", created_date="2023-01-01", age_limit=18)
    image.categories.add(category)
    path = reverse('image_detail', args=[image.id])  # Assuming the URL name for image_detail is 'image_detail'
    response = client.get(path)
    assert response.status_code == 200


# Test that image_detail uses the correct template
@pytest.mark.django_db
def test_image_detail_view_template(client: Client):
    category = Category.objects.create(name="Category 1")
    image = Image.objects.create(title="Image 1", image="test_image.jpg", created_date="2023-01-01", age_limit=18)
    image.categories.add(category)
    path = reverse('image_detail', args=[image.id])
    response = client.get(path)
    assertTemplateUsed(response, 'image_detail.html')


# Test that the correct Image instance is passed to the template
@pytest.mark.django_db
def test_image_detail_view_image(client: Client):
    category = Category.objects.create(name="Category 1")
    image = Image.objects.create(title="Image 1", image="test_image.jpg", created_date="2023-01-01", age_limit=18)
    image.categories.add(category)
    path = reverse('image_detail', args=[image.id])
    response = client.get(path)

    # The template context data can be accessed via response.context
    image_in_template = response.context['image']
    assert image_in_template == image