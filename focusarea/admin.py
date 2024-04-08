from .fields import FocusAreaField, FocusAreaJSONField
from .widgets import FocusAreaWidget

class FocusAreaAdminMixin:
    def __init__(self, *args, **kwargs):
        print("--> FocusAreaAdminMixin.__init__")
        print(args)
        print(kwargs)
        super().__init__(*args, **kwargs)
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        # if isinstance(db_field, FocusAreaField) or isinstance(db_field, FocusAreaJSONField):
        #     kwargs["widget"] = FocusAreaWidget
        focus_fields = getattr(self.model, "focus_fields", {})
        print("")
        print("--> FocusAreaAdminMixin.formfield_for_dbfield")
        if db_field.name in focus_fields:
            print("db_field", db_field)
            print("update widget for", db_field.name)
            print("FocusAreaWidget", FocusAreaWidget)
            kwargs["widget"] = FocusAreaWidget
        print("")

        return super().formfield_for_dbfield(db_field, **kwargs)