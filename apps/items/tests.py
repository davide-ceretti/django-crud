from django.test import TestCase
from django.core.urlresolvers import reverse

from apps.items.models import Item


def create_items(n):
    return [
        Item.objects.create(content='Hello, World - %s' % i)
        for i in xrange(n)
    ]


# TODO: Use django urls.py instead of static urls in these tests

class ItemsViewsEmptyDbTestCase(TestCase):
    def test_get_list(self):
        resp = self.client.get(reverse('item_list'))
        self.assertEqual(resp.status_code, 200)

    def test_get_add(self):
        resp = self.client.get(reverse('item_create'))
        self.assertEqual(resp.status_code, 200)

    def test_post_add(self):
        resp = self.client.post(
            reverse('item_create'),
            data={
                'content': 'Hello, World.',
            })
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Item.objects.all().count(), 1)

    def test_post_add_empty_data(self):
        # We basically test the form here
        resp = self.client.post(
            reverse('item_create'),
            data={
                'content': '',
            })
        self.assertContains(
            resp, 'This field is required.',
            status_code=200)
        self.assertEqual(Item.objects.all().count(), 0)

    def test_get_detail_doesnt_exist(self):
        resp = self.client.get(reverse('item_detail', args=[1]))
        self.assertEqual(resp.status_code, 404)


class ItemsViewsWithItemTestCase(TestCase):
    def setUp(self):
        create_items(1)

    def test_get_detail(self):
        resp = self.client.get(reverse('item_detail', args=[1]))
        self.assertEqual(resp.status_code, 200)

    def test_get_update(self):
        resp = self.client.get(reverse('item_update', args=[1]))
        self.assertEqual(resp.status_code, 200)

    def test_post_update(self):
        resp = self.client.post(
            reverse('item_update', args=[1]),
            data={
                'content': 'Edited item',
            })
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Item.objects.get().content, 'Edited item')

    def test_get_delete(self):
        resp = self.client.get(reverse('item_delete', args=[1]))
        self.assertEqual(resp.status_code, 200)

    def test_post_delete(self):
        resp = self.client.post(
            reverse('item_delete', args=[1]),
            data={})
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Item.objects.all().count(), 0)


class ItemModelTestCase(TestCase):
    def setUp(self):
        self.item = create_items(1)[0]

    def test_creation(self):
        self.assertEqual(Item.objects.all().count(), 1)

    def test_ref(self):
        self.assertEqual(self.item.ref, "ITEM-000001")
