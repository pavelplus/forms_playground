from django import forms


class TestForm(forms.Form):
    SEX_CHOICES = [
        (None, 'не указывать'),
        ('M', 'мужской'),
        ('F', 'женский'),
    ]
    CONTACT_TYPE_CHIOCES = [
        (None, 'не беспокоить'),
        ('email', 'E-Mail'),
        ('phone', 'Телефон'),
        ('whatsapp', 'Whatsapp'),
        ('telegram', 'Telegram'),
    ]
    COLORS_CHOICES = [
        ('R', 'Red'),
        ('G', 'Green'),
        ('B', 'Blue'),
        ('W', 'White'),
        ('B', 'Black'),
    ]

    USERNAME_MAX_LENGTH = 10

    prefix="testform"

    username = forms.CharField(
        max_length=USERNAME_MAX_LENGTH,
        label='Имя пользователя',
        help_text=f'Не более {USERNAME_MAX_LENGTH} символов',
        error_messages={'required': 'Поле обязательно для ввода!', 'max_length': f'Максимум {USERNAME_MAX_LENGTH} символов!'},
        widget=forms.widgets.TextInput(attrs={'autocomplete': 'off'})
        )
    password = forms.CharField(min_length=8, label='Пароль', help_text='Минимум 8 символов', widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=8, label='Пароль (повторно)', help_text='Повторите введенный пароль', widget=forms.PasswordInput())
    age = forms.IntegerField(label='Возраст', help_text='Для проверки на совершеннолетие')
    sex = forms.ChoiceField(choices=SEX_CHOICES, label='Пол', help_text='Для уточнения предлагаемых сервисов', required=False, widget=forms.RadioSelect())
    colors = forms.MultipleChoiceField(choices=COLORS_CHOICES, label='Любимые цвета', help_text='Можно выбрать несколько')
    contact_type = forms.ChoiceField(choices=CONTACT_TYPE_CHIOCES, label='Способ связи', help_text='Как направлять вам важную информацию?', required=False)
    about = forms.CharField(label="О себе", help_text="Поделитесь информацией с другими пользователями", required=False, widget=forms.Textarea(attrs={'rows':'3'}))
    autologin = forms.BooleanField(label='Запомнить', help_text='Входить автоматически')
    token = forms.CharField(widget=forms.HiddenInput())