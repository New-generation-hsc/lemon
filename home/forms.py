from django import forms

class ValidateFrom(forms.Form):
    name = forms.CharField(max_length=30, required=True, min_length=1)
    color = forms.CharField(max_length=10, required=True, min_length=1)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', '')
        self.model = kwargs.pop('model', None)
        super(ValidateFrom, self).__init__(*args, **kwargs)

    def clean(self):
        clean_data = super().clean()
        if self.model.objects.filter(name=clean_data['name'], owner=self.user).exists():
            raise forms.ValidationError("name already exists")
        return clean_data
