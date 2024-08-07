from django.db import models
from django.contrib.auth.models import AbstractUser
import math

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    class Meta:
        db_table='auth_user'

    def __str__(self):
        return self.username
    
class UserData(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)    
    # sitename = models.CharField("Site name", max_length=254)
    appname = models.CharField("App name", max_length=254)
    timespent = models.IntegerField("Time spent (seconds)")
    ondate = models.DateField("On date")

    def __str__(self):  
        return (str(self.uid) + str(self.appname))         
        # return (str(self.uid) + " visited " + str(self.sitename) + " for " + str(self.timespent) + " on " + str(self.ondate))
    
    def get_all_names(uid):
        names = UserData.objects.filter(uid=uid).values()
        lst1=[]
        for i in names:
            if i["appname"] not in lst1:
                lst1.append(i["appname"])
        return lst1

    def get_all_dates(uid, actname):
        dates = UserData.objects.filter(uid=uid, appname=actname).order_by("ondate").values()
        lst1=[]
        for i in dates:
            lst1.append(i["ondate"])
        return lst1
    
    def get_graph_data(usid,dt):
        userdata =  UserData.objects.filter(uid_id=usid, ondate=dt).order_by("-timespent").values() 
        times = []
        apps = []
        for i in userdata:
            times.append(i["timespent"])
            apps.append(i["appname"])
        tot = sum(times)
        for j in times:
            j = ((j/tot)*100)
        return apps, times
    
    def get_days_and_timespent_for_app(uid, appnm):
        ud =UserData.objects.filter(uid=uid, appname=appnm).order_by("ondate").values()
        dates=[]
        times = []
        f_times = []
        for i in ud:
            dt = i["ondate"]
            # act_dt = dt.strftime("%d %b, %Y")
            if dt not in dates:
                dates.append(dt)
                tot = UserData.get_total_usage_on_date_for_app(uid,dt,appnm)
                times.append(tot)
        for d in range(len(dates)):
            newdt = dates[d].strftime("%d %b")
            dates[d] = newdt

        tmax = max(times)
        max_time_hours = tmax / 3600
        if max_time_hours < 1:
            labels = [f'{hour}h' for hour in range(0, 10)]  # +2 to include the cushion
        else:
            labels = [f'{min}m' for min in range(0, 61,10)]  # +2 to include the cushion
        return dates,times, labels

    def get_total_usage_on_date_for_app(uid, dt, appnm):
        ud =UserData.objects.filter(uid=uid, ondate=dt, appname=appnm).values()
        # dates=[]
        times = 0
        for i in ud:
            times += i["timespent"]
        return times

    
    def get_days_and_timespent(uid):
        ud =UserData.objects.filter(uid=uid).order_by("ondate").values()
        dates=[]
        times = []
        f_times = []
        for i in ud:
            dt = i["ondate"]
            # act_dt = dt.strftime("%d %b, %Y")
            if dt not in dates:
                dates.append(dt)
                tot = UserData.get_total_usage_on_date(uid,dt)
                times.append(tot)
        for d in range(len(dates)):
            newdt = dates[d].strftime("%d %b")
            dates[d] = newdt

        tmax = max(times)
        max_time_hours = tmax / 3600
        if max_time_hours < 1:
            labels = [f'{hour}h' for hour in range(0, 10)]  # +2 to include the cushion
        else:
            labels = [f'{min}m' for min in range(0, 61,10)]  # +2 to include the cushion
        return dates,times, labels

    def get_total_usage_on_date(uid, dt):
        ud =UserData.objects.filter(uid=uid, ondate=dt).values()
        # dates=[]
        times = 0
        for i in ud:
            times += i["timespent"]
        return times



class UserGoals(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)    
    appname = models.CharField("App name", max_length=254)
    timegoal = models.IntegerField("Time limit (seconds)")

    def __str__(self):  
        return (str(self.uid) + str(self.appname))    

    def get_all_goal_names(uid):
        names = UserGoals.objects.filter(uid=uid).order_by("-timegoal").values()
        lst1=[]
        for i in names:
            lst1.append(i["appname"])

        return lst1
    
    # ondate = models.DateField("On date")
# from tracker.models import UserData as ud; us = u.objects.get(id=2)
#  ud(uid = us, sitename = 'youtube.com', appname = 'google chrome', timespent=250, ondate= dt)