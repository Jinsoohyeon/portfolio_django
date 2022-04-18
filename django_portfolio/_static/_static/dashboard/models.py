# from readline import append_history_file
from unicodedata import name
from django.db import models
from pkg_resources import compatible_platforms

class Costs(models.Model):                 
    name = models.CharField(max_length=20) 
    cost = models.IntegerField()           
    cpm = models.IntegerField()            
    cost_0min = models.IntegerField()      
    cost_5min = models.IntegerField()      
    cost_10min = models.IntegerField()     
    cost_15min = models.IntegerField()     
    cost_20min = models.IntegerField()     
    cost_25min = models.IntegerField()     
    cost_30min = models.IntegerField()     
                                           
    class Meta:                            
        managed = False                    
        db_table = 'Costs'                 

class Accident(models.Model):
    yy = models.IntegerField(primary_key=True)
    ac_case = models.IntegerField()
    dead = models.IntegerField()
    injured = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accident'

class AccType(models.Model):
    ac_type = models.CharField(max_length=20)
    ac_detail = models.CharField(primary_key=True, max_length=50)
    ac_case = models.IntegerField()
    ac_per = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acc_type'

class SafetyRule(models.Model):
    rule = models.CharField(primary_key=True, max_length=20)
    follow_rule_case = models.IntegerField(blank=True, null=True)
    follow_rule_per = models.IntegerField(blank=True, null=True)
    not_follow_rule_case = models.IntegerField(blank=True, null=True)
    not_follow_rule_per = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'safety_rule'

class CostsTop5(models.Model):
    name = models.CharField(max_length=20)
    cost = models.IntegerField()
    cpm = models.IntegerField()
    cost_0min = models.IntegerField()
    cost_5min = models.IntegerField()
    cost_10min = models.IntegerField()
    cost_15min = models.IntegerField()
    cost_20min = models.IntegerField()
    cost_25min = models.IntegerField()
    cost_30min = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Costs_top5'