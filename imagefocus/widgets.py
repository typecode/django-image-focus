from django.contrib.admin.widgets import AdminFileWidget
from django import forms

class ImageFocusWidget(AdminFileWidget):
    template_name = "imagefocus/imagefocus_file_widget.html"

    @property
    def media(self):
        css={
            "all": ["imagefocus/css/imagefocus-file-widget.css"]
        }
        js = [
            "imagefocus/js/imagefocus-file-widget.js"
        ]
        return forms.Media(css=css, js=js)

class ImageFocusPointWidget(forms.TextInput):
    template_name = "imagefocus/imagefocus_point_widget.html"

    @property
    def media(self):
        css={
            "all": ["imagefocus/css/imagefocus-point-widget.css"]
        }
        js = [
            "imagefocus/js/imagefocus-point-widget.js"
        ]
        return forms.Media(css=css, js=js)
    
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        print("ImageFocusPointWidget.get_context", value)
        return context
    
    def format_value(self, value):
        print("ImageFocusPointWidget.format_value", value)
        return super().format_value(value)