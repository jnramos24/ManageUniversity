from django.db import models

# Create your models here.


class Career (models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0} (Duracion: {1} año(s))"
        return txt.format(self.name, self.duration)


class Student(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    lastName = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    dateOfBirth = models.DateField()
    sexs = [
        ('F', 'feminine'),
        ('M', 'masculine')
    ]
    sex = models.CharField(max_length=1, choices=sexs, default='M')
    career = models.ForeignKey(
        Career, null=False, blank=False, on_delete=models.CASCADE)
    validity = models.BooleanField(default=True)

    def CompleteName(self):
        txt = "{0}, {1}"
        return txt.format(self.lastName, self.name)

    def __str__(self):
        txt = "{0} | Carrera: {1} | {2}"
        if self.validity:
            studentState = 'VIGENTE'
        else:
            studentState = 'LIBRE'
        return txt.format(self.CompleteName(), self.career, studentState)


class Course(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=30)
    credit = models.PositiveSmallIntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0} ({1})| profesor: {2}"
        return txt.format(self.name, self.code, self.teacher)


class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(
        Student, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, null=False, blank=False, on_delete=models.CASCADE)
    enrollmentDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculad{1} en el curso {2} | fecha: {3}"
        if self.student.sexs == 'F':
            letter = 'a'
        else:
            letter = 'o'
        date = self.enrollmentDate.strftime("%d,%b, %Y")
        return txt.format(self.student.CompleteName(), letter, self.course, date)
