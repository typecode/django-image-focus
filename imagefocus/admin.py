from .widgets import ImageFocusWidget

class ImageFocusAdminMixin:
    def formfield_for_dbfield(self, db_field, **kwargs):
        focus_fields = getattr(self.model, "focus_fields", {})
        if db_field.name in focus_fields:
            kwargs["widget"] = ImageFocusWidget

        return super().formfield_for_dbfield(db_field, **kwargs)