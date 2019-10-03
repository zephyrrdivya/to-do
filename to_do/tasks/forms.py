from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    # deadline_date = DateTimeField(widget=AdminDateWidget)

    class Meta:
        model = Task
        fields = ('title', 'content', 'deadline_date')
        widgets = {
            'deadline_date': DateInput()
        }

    def save(self, request, commit=True):
        # Save the provided password in hashed format
        task = super(TaskForm, self).save(commit=False)
        task.user = request.user
        if commit:
            task.save(request)
        return task
