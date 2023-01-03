from django.db import models



class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name



class Person(models.Model):
    name = models.CharField(max_length=124)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    age = models.PositiveIntegerField()
    gender_choice = (('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=gender_choice)
    phn = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    purpose_choice=(('enquiry','ENQUIRY'),
                    ('place','PLACE'),
                    ('order','ORDER'),
                    ('return','RETURN'))
    purpose=models.CharField(max_length=8,choices=purpose_choice)
    debitnotebook=models.BooleanField("Debit Notebook",default=False)
    pen=models.BooleanField("Pens",default=False)
    exampappers=models.BooleanField("Exam Pappers",default=False)

    def __str__(self):
        return self.name
