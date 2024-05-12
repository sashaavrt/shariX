from django import forms

from dbsynce.models import Company


class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        # Добавляем класс .form-control для всех полей формы
        for field in iter(self.fields):
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Company
        fields = ['legal_name', 'inn', 'kpp', 'ogrn', 'bank_name', 'bik', 'rs', 'ks', 'address']