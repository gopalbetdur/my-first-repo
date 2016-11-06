from django.db import models

# Create your models here.
class TaskList(models.Model):
 timeStamp = models.CharField(max_length=200, primary_key = True)
 taskName = models.CharField(max_length=200)
	
 def __unicode__(self):
  return (self.timeStamp, self.taskName)
	

class RegisteredObject(models.Model):
 registeredObjID = models.IntegerField(primary_key = True)
 registeredObjName = models.CharField(max_length=50)
	
 def __unicode__(self):
  return(self.registeredObjID, self.registeredObjName)

class TaskObject(models.Model):
 predefinedTaskName = models.ForeignKey('TaskList')
 predefinedObjID = models.ForeignKey('RegisteredObject')
 
 def __unicode__(self):
  return(self.predefinedTaskName, self.predefinedObjID)
#class Meta:
 #unique_together = (('predefinedTaskName', 'predefinedObjID'),)  

 
	
#class ActiveObjects(models.Model):
 #inputTimeStamp = models.DateTimeField(auto_now_add=True, blank=True, primary_key=True)
 #activeObjID = models.ForeignKey('RegisteredObjects')

 #class Meta1:
  #unique_together = (('inputTimestamp','activeObjID'),)  

  #def __unicode__(self):
   #return(self.inputTimeStamp, self.activeObjID)

