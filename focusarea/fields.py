from django import forms
from django.db import models
from django.core import signals

class FocusAreaFieldBaseMixin:
    def setup(
            self,
            image_field=None,
            verbose_name=None,
            help_text=None,
            **kwargs
    ):
        if not image_field:
            return
        
        self.image_field_name = image_field
        self.image_fk_name = None

        if "__" in image_field:
            self.image_field_name, self.image_fk_name = image_field.split("__")

        field_kwargs = {
            "verbose_name": verbose_name,
            "help_text": help_text,
        }
        field_kwargs.update(kwargs)
    
    def contribute_to_class(self, cls: models.Model, name: str, **kwargs) -> None:
        if cls._meta.abstract:
            return
        if not hasattr(cls, "focus_fields"):
            cls.add_to_class("focus_fields", {})
        print("")
        print("contribute_to_class")
        print("")
        cls.focus_fields[self.image_field_name] = {
            "fk_field": self.image_fk_name,
        }
    
    def form_field(self, **kwargs):
        kwargs["widget"] = forms.TextInput(
            attrs={
                "class": "focusarea-input"
            }
        )

def FocusAreaFieldDecorator(cls):
    cls.setup = FocusAreaFieldBaseMixin.setup
    cls.form_field = FocusAreaFieldBaseMixin.form_field
    cls.contribute_to_class = FocusAreaFieldBaseMixin.contribute_to_class
    return cls

class FocusAreaField(models.CharField):
    def __init__(self, *args, **kwargs):
        image_field = kwargs.pop("image_field", "")
        self.image_field = image_field
        self.image_fk_name = None

        if "__" in image_field:
            self.image_field, self.image_fk_name = image_field.split("__")
        # self.setup(*args, image_field=image_field, **kwargs)
        
        self.max_length = 125
        super().__init__(**kwargs)
    
    def contribute_to_class(self, cls: models.Model, name: str, **kwargs) -> None:
        if cls._meta.abstract:
            return
        if not hasattr(cls, "focus_fields"):
            cls.add_to_class("focus_fields", {})
        print("")
        print("contribute_to_class")
        print("")
        cls.focus_fields[self.image_field] = {
            "fk_field": self.image_fk_name,
        }
        super().contribute_to_class(cls, name, **kwargs)
    
    def form_field(self, **kwargs):
        kwargs["widget"] = forms.TextInput(
            attrs={
                "class": "focusarea-input"
            }
        )

class FocusAreaJSONField(models.JSONField, FocusAreaFieldBaseMixin):
    pass