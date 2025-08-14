from django import forms
<<<<<<< HEAD
from django.utils import timezone
=======
>>>>>>> f8dcbca673eb9f35137c00ab5f9569ac4f53d56c
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'room', 'checkin', 'checkout']
<<<<<<< HEAD
        labels = {
            'name': 'نام رزرو کننده',
            'room': 'اتاق',
            'checkin': 'تاریخ ورود',
            'checkout': 'تاریخ خروج',
        }
=======
>>>>>>> f8dcbca673eb9f35137c00ab5f9569ac4f53d56c
        widgets = {
            'checkin': forms.DateInput(attrs={'type': 'date'}),
            'checkout': forms.DateInput(attrs={'type': 'date'}),
        }
<<<<<<< HEAD

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = timezone.localdate().isoformat()
        self.fields['checkin'].widget.attrs['min'] = today
        self.fields['checkout'].widget.attrs['min'] = today

    def clean(self):
        cleaned_data = super().clean()
        checkin = cleaned_data.get('checkin')
        checkout = cleaned_data.get('checkout')
        today = timezone.localdate()

        if checkin and checkin < today:
            self.add_error('checkin', 'تاریخ ورود نمی‌تواند به گذشته باشد.')

        if checkin and checkout and checkout <= checkin:
            self.add_error('checkout', 'تاریخ خروج باید بعد از تاریخ ورود باشد.')
=======
>>>>>>> f8dcbca673eb9f35137c00ab5f9569ac4f53d56c
