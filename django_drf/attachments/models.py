from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from items.models import Item


def item_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/item_<id>/<filename>
    return 'item_{0}/{1}'.format(instance.item.id, filename)


class Attachment(models.Model):
    image = models.ImageField(upload_to=item_directory_path)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='attachments')

    def __repr__(self):
        return '<Attachment %s>' % self.image.name

    def __str__(self):
        return self.file
