
from django import forms
import datetime
from dropdownapp.models import Person, Course
from django.forms.widgets import CheckboxSelectMultiple, DateInput


class PersonCreationForm(forms.ModelForm):
    dob = forms.DateField(
        label="enter your birth date?",
        widget=forms.SelectDateWidget(years=range(1980,datetime.date.today().year-5))
    )
    def __init__(self, *args, **kwargs):
        super(PersonCreationForm,self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control',
            })
    class Meta:
        model = Person
        fields = ('name','dob','age','gender','phn','email','address','department','course','purpose','debitnotebook','pen','exampappers')
        # type = forms.MultipleChoiceField(choices=Person.TYPE_CHOICES, widget=forms.CheckboxSelectMultiple())

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(attrs={'class':'form-control'}),
            'phn':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            # 'department':forms.TextInput(attrs={'class':'form-control'}),
            # 'course':forms.TextInput(attrs={'class':'form-control'}),
            # 'purpose':forms.TextInput(attrs={'class':'form-control'}),
            'debitnotebook':forms.CheckboxInput(attrs={'class':'form-control',}),
            'pen':forms.CheckboxInput(attrs={'class':'form-control',}),
            'exampappers':forms.CheckboxInput(attrs={'class':'form-control',}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
