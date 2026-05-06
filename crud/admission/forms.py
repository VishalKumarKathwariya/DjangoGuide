from django import forms 
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in  self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Enter Valid Phone Number")
        return phone
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo and photo.size > 2*1024*1024:
            raise forms.ValidationError("Image < 2MB only")
        return photo
    
        