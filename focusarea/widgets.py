from django.contrib.admin.widgets import AdminFileWidget
from django import forms

class FocusAreaWidget(AdminFileWidget):
    @property
    def media(self):
        css={}
        js = [
            "focusarea/js/focusarea-widget.js"
        ]
        print("FocusAreaWidget.media")
        return forms.Media(css=css, js=js)
    
    def render(self, name, value, attrs=None, renderer=None):
        print("FocusAreaWidget.render")
        attrs = {
            "class": "focusarea-target-file"
        }
        render_args = [name, value, attrs, renderer]
        # return "<p>This is a widget</p>"
        return super().render(*render_args)
        # return format_html(
        #     '<div id="focus-area-widget" data-focus-area-value="{}"></div>',
        #     json.dumps(value) if value else "[]"