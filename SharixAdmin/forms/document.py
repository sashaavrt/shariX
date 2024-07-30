import datetime

from django import forms
from django.core.exceptions import ValidationError


class DocumentUploadForm(forms.Form):
    doc_expire_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        }),
        label='Дата окончания действия документа (при наличии)'
    )
    doc_file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=True,
    )

    # Дата истечения срока документа не может быть в прошлом
    def clean_doc_expire_date(self):
        doc_expire_date = self.cleaned_data.get('doc_expire_date')
        if doc_expire_date and doc_expire_date < datetime.date.today():
            raise ValidationError("Дата окончания действия документа не может быть в прошлом.")
        return doc_expire_date

    # Загружаемые файлы должны иметь только допустимый тип и расширение
    def clean_doc_file(self):
        files = self.files.getlist('doc_file')
        allowed_mime_types = ['image/jpeg', 'image/png', 'application/pdf']
        allowed_extensions = ['jpg', 'jpeg', 'png', 'pdf']
        
        for file in files:
            # Проверяем расширение файла
            extension = file.name.split('.')[-1].lower()
            if extension not in allowed_extensions:
                raise ValidationError(f"Файл {file.name} имеет недопустимое расширение. Допустимые расширения: {', '.join(allowed_extensions)}.")

            # Проверяем MIME тип файла
            if file.content_type not in allowed_mime_types:
                raise ValidationError(f"Файл {file.name} имеет недопустимый формат. Допустимые форматы: {', '.join(allowed_mime_types)}.")
        
        return files