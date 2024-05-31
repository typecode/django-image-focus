# Django Image Focus

A django field and widgets for setting the focal point of an image

## Usage

1. Add the `ImageFocusField` to your model

```python
# models.py
from django.db import models
from imagefocus import ImageFocusField

class ImageModel(models.Model):
    source = models.ImageField(upload_to="/images")
    focal_point = ImageFocusField(image_field="source")
```

2. Add the `ImageFocusAdminMixin` to your model admin

```python
# admin.py
from django.contrib import admin
from imagefocus import ImageFocusAdminMixin
from .models import ImageModel

@admin.register(ImageModel)
class ImageAdmin(ImageFocusAdminMixin, admin.ModelAdmin):
    pass
```


## Setup

### Installation

```shell
python3 -m pip install django-image-focus
```

### Settings

```python
#settings.py
INSTALLED_APPS = [
    # ...
    'imagefocus',
]
```