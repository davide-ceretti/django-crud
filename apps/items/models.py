from django.db import models


class Item(models.Model):
    """A generic item with a very simple structure that has
    no business logic at all. """

    # When this item was created
    created = models.DateTimeField(auto_now_add=True, null=False)

    # The text this item is storing
    content = models.TextField()

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return self.ref

    @property
    def ref(self):
        return 'ITEM-%06d' % self.id
