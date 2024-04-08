from django import forms
from django.db import models
from .widgets import ImageFocusPointWidget

class ImageFocusFieldBase(models.Field):
    def __init__(
            self,
            *args,
            **kwargs
    ):
        image_field = kwargs.pop("image_field", "")
        super().__init__(*args, **kwargs)
        if not image_field:
            return
        
        self.image_field = image_field
        self.image_fk_name = None

        if "__" in image_field:
            self.image_field, self.image_fk_name = image_field.split("__")

    def contribute_to_class(self, cls: models.Model, name: str, **kwargs) -> None:
        if cls._meta.abstract:
            return
        
        if not hasattr(cls, "focus_fields"):
            cls.add_to_class("focus_fields", {})

        cls.focus_fields[self.image_field] = {
            "fk_field": self.image_fk_name,
        }
        
        super().contribute_to_class(cls, name, **kwargs)
    
    def formfield(self, **kwargs):
        kwargs["widget"] = ImageFocusPointWidget(
            attrs={
                "class": "imagefocus-input",
                "data-image-field": self.image_field,
            }
        )
        return super().formfield(**kwargs)
    
    def to_python(self, value):
        return value

class ImageFocusField(ImageFocusFieldBase, models.CharField):
    pass

class ImageFocusJSONField(ImageFocusFieldBase, models.JSONField):
    pass