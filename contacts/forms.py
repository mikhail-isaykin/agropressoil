from django import forms


class ContactForm(forms.Form):
    INPUT_CLASS = (
        "w-full px-4 py-3 bg-[#f5f6f8] border border-transparent rounded "
        "text-[15px] text-[#1a1f2b] placeholder-[#9aa2b1] focus:outline-none "
        "focus:border-[var(--accent)] focus:bg-white transition-colors"
    )
    REQUEST_TYPES = [
        ('Покупка оборудования', 'Покупка оборудования'),
        ('Запасные части', 'Запасные части'),
        ('Ремонт оборудования', 'Ремонт оборудования'),
        ('Другое', 'Другое'),
    ]
    name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Иван Иванов',
            'class': INPUT_CLASS,
        })
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': '+7 (___) ___-__-__',
            'class': INPUT_CLASS,
        })
    )
    request_type = forms.ChoiceField(
        choices=REQUEST_TYPES,
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Модель пресса, требуемые позиции, количество…',
            'rows': 4,
            'class': INPUT_CLASS + " resize-y",
        })
    )
