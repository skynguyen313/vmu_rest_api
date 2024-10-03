from django.db import models

class Question(models.Model):
    content = models.CharField(max_length=250, null=False)
    answer01 = models.CharField(max_length=30, null=True)
    answer02 = models.CharField(max_length=30, null=True)
    answer03 = models.CharField(max_length=30, null=True)
    answer04 = models.CharField(max_length=30, null=True)
    class Meta:
        db_table = 'pysc_Question'

class Test(models.Model):
    name = models.CharField(max_length=50, null=False)
    note = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=False)
    class Meta:
        db_table = 'pysc_Test'

class TestDetails(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='test_details',
        on_delete=models.CASCADE,
        )
    test = models.ForeignKey(
        Test,
        related_name='test_details',
        on_delete=models.CASCADE,
        )
    class Meta:
        unique_together = (("question", "test"),)
        db_table = 'pysc_TestDetails'