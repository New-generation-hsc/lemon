from django import forms
import re

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


class TaskForm(forms.Form):
    content = forms.CharField(max_length=30, required=True, min_length=1)
    remind_time = forms.CharField(max_length=30, required=True, min_length=1)

    def clean(self):
        clean_data = super().clean()
        time = clean_data['remind_time']
        matched = re.match(r'(\d{1,2})/(\d{1,2})/(\d{1,4})', time)
        if matched:
            clean_data['remind_time'] = matched.group(3) + '-' + matched.group(1) + '-' + matched.group(2)
        else:
            raise forms.ValidationError("time format error")
        return clean_data
