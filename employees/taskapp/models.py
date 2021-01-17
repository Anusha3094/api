from django.db import models


class Employee(models.Model):
    role=models.CharField(max_length=200,null=False)
    name=models.CharField(max_length=200,null=False)
    task=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    # def get_views(self):
    # views=0
    # for comment in comment_set:
    #     views+=.views
    # return views
    # comment=models.ForeignKey(Comment,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "{} of {}".format(self.name, self.role)
class Comment(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} of {}".format(self.author, self.text)
class Role(models.Model):
    role_name=models.CharField(max_length=200,null=False)
    department=models.CharField(max_length=200,null=False)
    def __str__(self):
        return self.role_name



