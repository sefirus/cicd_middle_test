import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from gallery.models import Category


@pytest.mark.django_db
def test_gallery_view_success(client: Client):
    path = reverse('main')  # Assuming the URL name for gallery_view is 'gallery_view'
    response = client.get(path)
    assert response.status_code == 200


# Test that gallery_view uses the correct template
@pytest.mark.django_db
def test_gallery_view_template(client: Client):
    path = reverse('main')
    response = client.get(path)
    assertTemplateUsed(response, 'gallery.html')


# Test that all categories are passed to the template
@pytest.mark.django_db
def test_gallery_view_categories(client: Client):
    category_1 = Category.objects.create(name="Category 1")
    category_2 = Category.objects.create(name="Category 2")
    category_3 = Category.objects.create(name="Category 3")

    path = reverse('main')
    response = client.get(path)

    # The template context data can be accessed via response.context
    categories_in_template = response.context['categories']
    assert len(categories_in_template) == 3
    assert set(categories_in_template) == {category_1, category_2, category_3}