from django.shortcuts import render, redirect; from django.http import HttpResponse, HttpResponseRedirect   #django stuff
#from .models import 
import calendar; from datetime import datetime                              #datetime stuff
import base64; import imghdr                                                #image stuff
from django.urls import reverse
import json
import matplotlib                                                           #plotting graphs
matplotlib.use('Agg')       
import datetime as dt
#for main loop outside main thread error being thrown when accessing graph multiple times 
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import User, UserData, UserGoals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from tracker.forms import SignUpForm
from django.core.exceptions import ValidationError

# import json
from datetime import datetime
from django.db.models import Q


@login_required(login_url="/accounts/login/")
def home(request):
    # return HttpResponse('hello, this is home page')
    # user_name_obj  = User.objects.get(username=request.user.username)
    # user_id = user_name_obj.id
    # vehicle_names_set =  Userdata.objects.filter(uid_id=user_id).order_by("date_added").values() 
    context = {"username": request.user.username}
    return render(request, 'tracker/home.html', context)

@login_required(login_url="/accounts/login/")
def disp(request):
    # f = open('../activities.json','a+')
    # ab = f.read()
    # ab = json.load(f)
    populate_table(request)
    flag = scr_graph(request)
    user_name_obj  = User.objects.get(username=request.user.username)
    user_id = user_name_obj.id
    curr_dt = datetime.now().date() - dt.timedelta(days=2)
    userdata =  UserData.objects.filter(uid_id=user_id, ondate=curr_dt).order_by("-timespent").values() 
    for i in userdata:
        i['timespent'] = from_seconds(i['timespent'])
    username = request.user.username
    context = {
        # 'jsondata': data,
        "username":username,
        "userdata":userdata,
        # "res":res,
        "flag":flag,
        }
    return render(request,'tracker/disp.html', context)

@login_required(login_url="/accounts/login/")
def disp_goal(request):
    user_name_obj  = User.objects.get(username=request.user.username)
    user_id = user_name_obj.id
    user_goals = UserGoals.objects.filter(uid=user_id).order_by("appname").values()
    for i in user_goals:
        i["timegoal"]= from_seconds(i["timegoal"])
    context = {"usergoals":user_goals}
    return render(request, "tracker/goals/dispgoals.html", context)


@login_required(login_url="/accounts/login/")
def add_goal(request):
    # pass
    return render(request, "tracker/goals/add.html")


@login_required(login_url="/accounts/login/")
def add_goal_suc(request):
    # pass
    user_name_obj  = User.objects.get(username=request.user.username)
    user_id = user_name_obj.id
    names = UserGoals.get_all_goal_names(uid=user_id)
    new_name = request.POST["new_goal_name"]
    h = request.POST["hours"]
    m = request.POST["minutes"]
    s = request.POST["seconds"]
    if new_name in names:
        context= {"flag":1}
        return render(request, "tracker/goals/add.html",context)
    seconds = to_seconds(int(h),int(m),int(s))
    try:
        new_rec = UserGoals(uid=user_name_obj, appname=new_name, timegoal=seconds)
        new_rec.save()
    except:
        return render(request, "tracker/goals/success.html",{"h":h,"m":m,"s":s,"e":seconds})
    context = {"added":1, "appname":new_name}
    return render(request, "tracker/goals/success.html",context)


@login_required(login_url="/accounts/login/")
def edit_goal(request):
    pass

@login_required(login_url="/accounts/login/")
def del_goal(request):    
    # pass
    user_name_obj  = User.objects.get(username=request.user.username)
    user_id = user_name_obj.id
    names = UserGoals.get_all_goal_names(uid=user_id)
    if not names:
        return render(request, "tracker/goals/del.html", {"flag_no_recs":1})
    else:
        return render(request, "tracker/goals/del.html", {"names":names})
    
@login_required(login_url="/accounts/login/")
def del_goal_suc(request):    
    # pass
    user_name_obj  = User.objects.get(username=request.user.username)
    user_id = user_name_obj.id
    appname = request.POST["appname_to_del"]

    # names = UserGoals.get_all_goal_names(uid=user_id)

    rectodel = UserGoals.objects.get(uid=user_id,appname=appname)
    rectodel.delete()
    # if names:
    context =  {"deleted":1, "appname":appname}
    return render(request, "tracker/goals/success.html", context)
    # else:
        # return render(request, "tracker/goals/del.html", {"names":names})


@login_required(login_url="/accounts/login/")
def appwise(request):
    user_name_obj  = User.objects.get(username=request.user.username)
    user_id = user_name_obj.id
    names = UserData.get_all_names(uid=user_id)
    if names:
        return render(request, "tracker/aw.html", {"recs":1,"names":names})
    else:
        return render(request, "tracker/aw.html")

# @login_required(login_url="/accounts/login/")
# def appwise_suc(request):
#     user_name_obj  = User.objects.get(username=request.user.username)
#     user_id = user_name_obj.id
#     savename = "static/tracker/images/graphs/app_output.jpg"
#     appname = request.POST["appname_to_view"]

#     dates, times, labels = UserData.get_days_and_timespent_for_app(user_id, appname)
#     # Create the figure and axis objects
#     fig, ax = plt.subplots(figsize=(12, 5))  # Width=10 inches, Height=6 inches


#     # Set the face color of the figure (the whole area including padding)
#     fig.patch.set_facecolor('black')

#     # Set the face color of the axes (the plot area)
#     ax.set_facecolor('gray')

#     # Create the bar chart
#     ax.bar(dates, times, color='skyblue')

#     # Add title and labels with white text
#     ax.set_title('Usage trend', color='white')
#     ax.set_xlabel('Dates', color='white')
#     ax.set_ylabel('Time Spent', color='white')

#     # Rotate x-axis labels and change their color to white
#     plt.xticks(rotation=45, color='white')
#     plt.yticks(color='white')
#     ax.set_yticklabels(labels, color='white')

#     # Change the color of the spines (borders of the plot area)
#     ax.spines['bottom'].set_color('white')
#     ax.spines['top'].set_color('white')
#     ax.spines['right'].set_color('white')
#     ax.spines['left'].set_color('white')

#     # Change the color of the tick marks
#     ax.tick_params(axis='x', colors='white')
#     ax.tick_params(axis='y', colors='white')

#     # Save the chart to a file
#     plt.savefig(savename, bbox_inches='tight', facecolor=fig.get_facecolor())

#     # return render(request, 'tracker/bargraph.html', {"flag":1})
#     context =  {"flag":1, "appname":appname}
#     return render(request, "tracker/appwise.html", context)

def appwise_suc(request):
    user_name_obj = User.objects.get(username=request.user.username)
    user_id = user_name_obj.id
    savename = "static/tracker/images/graphs/app_output.jpg"
    appname = request.POST["appname_to_view"]

    dates, times, labels = UserData.get_days_and_timespent_for_app(user_id, appname)
    # Create the figure and axis objects
    fig, ax = plt.subplots(figsize=(12, 5))  # Width=10 inches, Height=6 inches

    # Set the face color of the figure (the whole area including padding)
    fig.patch.set_facecolor('black')

    # Set the face color of the axes (the plot area)
    ax.set_facecolor('gray')

    # Create the bar chart
    ax.bar(dates, times, color='skyblue')

    # Add title and labels with white text
    ax.set_title('Usage trend', color='white')
    ax.set_xlabel('Dates', color='white')
    ax.set_ylabel('Time Spent', color='white')

    # Rotate x-axis labels and change their color to white
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')

    # Function to format y-axis labels
    def format_time(seconds, pos=None):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        if hours > 0:
            return f'{hours}h {minutes}m'
        else:
            return f'{minutes}m'

    # Calculate maximum time and set yticks at 5-minute intervals
    max_time = max(times)
    max_minutes = (max_time // 60) + 1  # Convert to minutes and add 1 to cover the range
    tick_interval = 5  # Interval of 5 minutes
    yticks = np.arange(0, max_minutes * 60, tick_interval * 60)  # Convert minutes back to seconds

    # Set yticks manually
    ax.set_yticks(yticks)
    ax.yaxis.set_major_formatter(FuncFormatter(format_time))

    # Change the color of the spines (borders of the plot area)
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')

    # Change the color of the tick marks
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Save the chart to a file
    plt.savefig(savename, bbox_inches='tight', facecolor=fig.get_facecolor())

    # return render(request, 'tracker/bargraph.html', {"flag":1})
    context = {"flag": 1, "appname": appname}
    return render(request, "tracker/appwise.html", context)


@login_required(login_url="/accounts/login/")
def scr_graph(request):
    savename = "static/tracker/images/graphs/pi_output.jpg"
    user_name_obj  = User.objects.get(username=request.user.username)
    user_id = user_name_obj.id
    curr_date = datetime.now().date() - dt.timedelta(days=2) 
    userdata =  UserData.objects.filter(uid_id=user_id).order_by("ondate").values() 
    labels, sizes = UserData.get_graph_data(user_id,curr_date)
    if labels:
        grph = plt.figure(figsize=(10,10))
        grph.patch.set_facecolor('black')
        fig, ax = plt.subplots(figsize=(13,5))
        fig.patch.set_facecolor('black')
        ax.pie(sizes, labels=labels, textprops=dict(color="white"))
        plt.savefig(savename)
        return 1
    else:
        return 0

@login_required(login_url="/accounts/login/")
# def disp_month(request):
#     savename = "static/tracker/images/graphs/bar_output.jpg"
#     user_name_obj  = User.objects.get(username=request.user.username)
#     user_id = user_name_obj.id

#     dates, times, labels = UserData.get_days_and_timespent(user_id)
#     # Create the figure and axis objects
#     fig, ax = plt.subplots(figsize=(12, 5))  # Width=10 inches, Height=6 inches


#     # Set the face color of the figure (the whole area including padding)
#     fig.patch.set_facecolor('black')

#     # Set the face color of the axes (the plot area)
#     ax.set_facecolor('gray')

#     # Create the bar chart
#     ax.bar(dates, times, color='skyblue')

#     # Add title and labels with white text
#     ax.set_title('Usage trend', color='white')
#     ax.set_xlabel('Dates', color='white')
#     ax.set_ylabel('Time Spent', color='white')

#     # Rotate x-axis labels and change their color to white
#     plt.xticks(rotation=45, color='white')
#     plt.yticks(color='white')
#     ax.set_yticklabels(labels, color='white')

#     # Change the color of the spines (borders of the plot area)
#     ax.spines['bottom'].set_color('white')
#     ax.spines['top'].set_color('white')
#     ax.spines['right'].set_color('white')
#     ax.spines['left'].set_color('white')

#     # Change the color of the tick marks
#     ax.tick_params(axis='x', colors='white')
#     ax.tick_params(axis='y', colors='white')

#     # Save the chart to a file
#     plt.savefig(savename, bbox_inches='tight', facecolor=fig.get_facecolor())

#     return render(request, 'tracker/bargraph.html', {"flag":1})
def disp_month(request):
    savename = "static/tracker/images/graphs/bar_output.jpg"
    user_name_obj = User.objects.get(username=request.user.username)
    user_id = user_name_obj.id

    dates, times, labels = UserData.get_days_and_timespent(user_id)
    # Create the figure and axis objects
    fig, ax = plt.subplots(figsize=(12, 5))  # Width=10 inches, Height=6 inches

    # Set the face color of the figure (the whole area including padding)
    fig.patch.set_facecolor('black')

    # Set the face color of the axes (the plot area)
    ax.set_facecolor('gray')

    # Create the bar chart
    ax.bar(dates, times, color='skyblue')

    # Add title and labels with white text
    ax.set_title('Usage trend', color='white')
    ax.set_xlabel('Dates', color='white')
    ax.set_ylabel('Time Spent', color='white')

    # Rotate x-axis labels and change their color to white
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')

    # Function to format y-axis labels
    def format_time(seconds, pos=None):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        if hours > 0:
            return f'{hours}h {minutes}m'
        else:
            return f'{minutes}m'

    # Calculate maximum time and set yticks interval
    max_time = max(times)
    max_minutes = (max_time // 60) + 1  # Convert to minutes and add 1 to cover the range
    
    # Determine appropriate tick interval
    tick_interval = 5  # Start with 5 minutes
    num_ticks = max_minutes / tick_interval

    if num_ticks > 10:
        tick_interval = 10
        num_ticks = max_minutes / tick_interval
        if num_ticks > 10:
            tick_interval = 15

    yticks = np.arange(0, max_minutes * 60, tick_interval * 60)  # Convert minutes back to seconds

    # Set yticks manually
    ax.set_yticks(yticks)
    ax.yaxis.set_major_formatter(FuncFormatter(format_time))

    # Change the color of the spines (borders of the plot area)
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')

    # Change the color of the tick marks
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Save the chart to a file
    plt.savefig(savename, bbox_inches='tight', facecolor=fig.get_facecolor())

    return render(request, 'tracker/bargraph.html', {"flag": 1})

# Show the chart
# plt.show()
def signup(request):
    if request.method=="POST":
        # form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                # raise ValidationError("Please choose unique email, this is already registered")            
                form = SignUpForm()
                return render(request, 'garage/Accs/signup.html', {'form': form, 'flag':1})

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("garage:vehicles")
    else:
        # form = UserCreationForm()    
        form = SignUpForm()

    return render(request, 'tracker/Accs/signup.html', {'form': form})


def from_seconds(seconds):
    # hours = seconds // 3600
    # minutes = (seconds % 3600) // 60
    # seconds = seconds % 60
    # return f"{hours}h {minutes}m {seconds}s"
    # def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    time_parts = []
    if hours > 0:
        time_parts.append(f"{hours}h")
    if minutes > 0 or (hours > 0 and seconds > 0):
        time_parts.append(f"{minutes}m")
    if seconds > 0:
        time_parts.append(f"{seconds}s")
    
    return ' '.join(time_parts)

def to_seconds(hours, minutes, seconds):
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds



def populate_table(request):
    uid = User.objects.get(username=request.user.username)
    curr_date = datetime.now().date()

    with open('activities.json', 'r') as file:
        try:
            data = json.load(file)

            for key in data["activities"]:
                act_name = key["name"]
                avoid = ["https:", "","\n", "Task Switching"]
                if act_name in avoid:
                    break
                dt = key["time_entries"][0]["date"]
                act_dt = datetime.strptime(dt, "%Y-%m-%d").date()
                act_time = key["time_entries"][0]["total_seconds"]

                # Check if the record already exists
                record_exists = UserData.objects.filter(
                    uid=uid, 
                    appname=act_name, 
                    ondate=act_dt
                ).exists()

                if not record_exists:
                    # Insert new record
                    ude = UserData(uid=uid, appname=act_name, timespent=act_time, ondate=act_dt)
                    ude.save()
                else:
                    # Update existing record
                    rec = UserData.objects.get(uid=uid, appname=act_name, ondate=act_dt)
                    rec.timespent = act_time
                    rec.save()

        except Exception as e:
            # Handle the exception as needed
            print(f"Error: {e}")



# def populate_table(request):
#     uid  = User.objects.get(username=request.user.username)
#     # user_id = user_name_obj.id
#     curr_date = datetime.now().date()

#     with open('activities.json', 'r') as file:
#         try:
#             data = json.load(file)

#             #TODO add day support
#             for key in data["activities"]:
#                 act_name = key["name"]
#                 names = UserData.get_all_names(uid)
#                 dt = key["time_entries"][0]["date"]
#                 act_dt = datetime.strptime(dt, "%Y-%m-%d")
#                 act_time = key["time_entries"][0]["total_seconds"]

#                 if act_name not in names:
#                     # act_time = 0
#                     # for j in key["time_entries"]:
#                     #     h = j["hours"]
#                     #     m = j["minutes"]
#                     #     s = j["seconds"]
#                     #     tm = to_seconds(h,m,s)
#                     #     act_time += tm

#                     # act_time = from_seconds(act_time)
#                     ude = UserData(uid=uid, appname = act_name, timespent = act_time, ondate = act_dt)
#                     ude.save()

#                 elif act_name in names:
#                     dates = UserData.get_all_dates(uid,act_name)
#                     #updating time
#                     if act_dt in dates:
#                         rec = UserData.objects.get(appname=act_name, ondate=act_dt)
#                         rec.timespent = act_time
#                         rec.save()
#                     #making entry of that date
#                     else:
#                         ude = UserData(uid=uid, appname = act_name, timespent = act_time, ondate = act_dt)
#                         ude.save()
#         except Exception as e:
#                 # return e
#                 pass
        
        # else:
        #     return 0
    
    
    # with open('activities.json', 'w') as file:
    #     pass


# def rem_appname(nm):
#     appnames = {" - Visual Studio Code":"Visual Studio Code",
#                 "\u2014 Mozilla Firefox" :"Mozilla Firefox"}