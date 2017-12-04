from django import forms
from django.contrib.auth.models import User
from .models import Employee, Mentor, Student , ClassName

class EmployeeForm(forms.ModelForm):
    class Meta:
         model = Employee
         fields = ('Employee_Id','Employee_name','Employee_phone','Employee_Address',  )



class MentorForm(forms.ModelForm):
    class Meta:
         model = Mentor
         fields = ('Mentor_Id','Mentor_name','Mentor_phone','Mentor_Address' ,'Mentor_Gender' ,'begining_date','ending_date','Mentor_email',)

class StudentForm(forms.ModelForm):
    class Meta:
         model = Student
         fields =('Student_id','Student_name','Student_curr_grade','Student_prev_grade','Student_Class',
                   'Parents_email','Parents_phone','School','Men_name','Emp_name','Comments','start_date','last_date',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password',]


class ClassNameForm(forms.ModelForm):
      class Meta:
          model = ClassName
          fields=('class_name', 'class_date','Mentor',)