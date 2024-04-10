from .widgets import ImageFocusWidget

class ImageFocusAdminMixin:
    def __init__(self, *args, **kwargs):
        print("--> FocusAreaAdminMixin.__init__")
        print(args)
        print(kwargs)
        super().__init__(*args, **kwargs)
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        # if isinstance(db_field, ImageFocusField) or isinstance(db_field, ImageFocusJSONField):
        #     kwargs["widget"] = ImageFocusWidget
        focus_fields = getattr(self.model, "focus_fields", {})
        print("")
        print("--> FocusAreaAdminMixin.formfield_for_dbfield", focus_fields, db_field.name)
        if db_field.name in focus_fields:
            print("db_field", db_field)
            print("update widget for", db_field.name)
            print("ImageFocusWidget", ImageFocusWidget)
            kwargs["widget"] = ImageFocusWidget
        print("")

        return super().formfield_for_dbfield(db_field, **kwargs)