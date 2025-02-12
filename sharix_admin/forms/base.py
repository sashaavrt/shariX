from django import forms


class BaseForm(forms.Form):
    """
    Базовая форма, которая автоматически добавляет класс 'form-control' 
    к каждому полю формы.
    """

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
