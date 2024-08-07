# 
#from __future__ import print_function
# import time
# import json
# import datetime
# import sys
# import win32gui
# import uiautomation as auto
# from dateutil import parser

# class ActivityList:
#     def __init__(self, activities):
#         self.activities = activities
    
#     def initialize_me(self):
#         activity_list = ActivityList([])
#         try:
#             with open('activities.json', 'r') as f:
#                 data = json.load(f)
#                 activity_list = ActivityList(
#                     activities=self.get_activities_from_json(data)
#                 )
#         except FileNotFoundError:
#             print('No json')

#         except:
#             pass
#         return activity_list
    
#     def get_activities_from_json(self, data):
#         return_list = []
#         for activity in data['activities']:
#             return_list.append(
#                 Activity(
#                     name=activity['name'],
#                     time_entries=self.get_time_entries_from_json(activity['time_entries']),
#                 )
#             )
#         self.activities = return_list
#         return return_list
    
#     def get_time_entries_from_json(self, data):
#         return_list = []
#         for entry in data:
#             return_list.append(
#                 TimeEntry(
#                     date=parser.parse(entry['date']),
#                     total_seconds=entry['total_seconds']
#                 )
#             )
#         return return_list
    
#     def serialize(self):
#         return {
#             'activities': self.activities_to_json()
#         }
    
#     def activities_to_json(self):
#         activities_ = []
#         for activity in self.activities:
#             activities_.append(activity.serialize())
#         return activities_

# class Activity:
#     def __init__(self, name, time_entries):
#         self.name = name
#         self.time_entries = time_entries

#     def serialize(self):
#         return {
#             'name': self.name,
#             'time_entries': self.make_time_entries_to_json()
#         }
    
#     def make_time_entries_to_json(self):
#         time_list = []
#         for time in self.time_entries:
#             time_list.append(time.serialize())
#         return time_list

# class TimeEntry:
#     def __init__(self, date, total_seconds=0):
#         self.date = date
#         self.total_seconds = total_seconds

#     def add_seconds(self, seconds):
#         self.total_seconds += seconds

#     def serialize(self):
#         return {
#             'date': self.date.strftime("%Y-%m-%d"),
#             'total_seconds': self.total_seconds
#         }

# def url_to_name(url):
#     string_list = url.split('/')
#     return string_list[2]

# def get_active_window():
#     window = win32gui.GetForegroundWindow()
#     window_title = win32gui.GetWindowText(window)
#     return window_title

# def get_chrome_url():
#     window = win32gui.GetForegroundWindow()
#     chromeControl = auto.ControlFromHandle(window)
#     edit = chromeControl.EditControl()
#     return 'https://' + edit.GetValuePattern().Value

# active_window_name = ""
# activity_name = ""
# start_time = datetime.datetime.now()
# activeList = ActivityList([]).initialize_me()
# first_time = True

# try:
#     while True:
#         new_window_name = get_active_window()
#         if ('Google Chrome' in new_window_name):
#             #or ('Microsoft​ Edge' in new_window_name) 
#             # or ('Mozilla Firefox' in new_window_name) or ('Brave' in new_window_name))
#             new_window_name = url_to_name(get_chrome_url())

#         if active_window_name != new_window_name:
#             print(active_window_name)
#             activity_name = active_window_name

#             if not first_time:
#                 end_time = datetime.datetime.now()
#                 time_spent = (end_time - start_time).total_seconds()

#                 exists = False
#                 for activity in activeList.activities:
#                     if activity.name == activity_name:
#                         exists = True
#                         current_date_str = start_time.strftime("%Y-%m-%d")
#                         entry_exists = False
#                         for entry in activity.time_entries:
#                             if entry.date.strftime("%Y-%m-%d") == current_date_str:
#                                 entry.add_seconds(time_spent)
#                                 entry_exists = True
#                                 break
#                         if not entry_exists:
#                             activity.time_entries.append(TimeEntry(start_time, time_spent))

#                 if not exists:
#                     new_entry = TimeEntry(start_time, time_spent)
#                     new_activity = Activity(activity_name, [new_entry])
#                     activeList.activities.append(new_activity)

#                 with open('activities.json', 'w') as json_file:
#                     json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)
                
#                 start_time = datetime.datetime.now()
#             first_time = False
#             active_window_name = new_window_name

#         time.sleep(1)
    
# except KeyboardInterrupt:
#     with open('activities.json', 'w') as json_file:
#         json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)


from __future__ import print_function
import time
import json
import datetime
import sys
import win32gui
import uiautomation as auto
from dateutil import parser

class ActivityList:
    def __init__(self, activities):
        self.activities = activities
    
    def initialize_me(self):
        activity_list = ActivityList([])
        try:
            with open('activities.json', 'r') as f:
                data = json.load(f)
                activity_list = ActivityList(
                    activities=self.get_activities_from_json(data)
                )
        except FileNotFoundError:
            print('No json')

        except Exception as e:
            print(f"An error occurred: {e}")
            pass
        return activity_list
    
    def get_activities_from_json(self, data):
        return_list = []
        for activity in data['activities']:
            return_list.append(
                Activity(
                    name=activity['name'],
                    time_entries=self.get_time_entries_from_json(activity['time_entries']),
                )
            )
        self.activities = return_list
        return return_list
    
    def get_time_entries_from_json(self, data):
        return_list = []
        for entry in data:
            return_list.append(
                TimeEntry(
                    date=parser.parse(entry['date']),
                    total_seconds=entry['total_seconds']
                )
            )
        return return_list
    
    def serialize(self):
        return {
            'activities': self.activities_to_json()
        }
    
    def activities_to_json(self):
        activities_ = []
        for activity in self.activities:
            activities_.append(activity.serialize())
        return activities_

class Activity:
    def __init__(self, name, time_entries):
        self.name = name
        self.time_entries = time_entries

    def serialize(self):
        return {
            'name': self.name,
            'time_entries': self.make_time_entries_to_json()
        }
    
    def make_time_entries_to_json(self):
        time_list = []
        for time in self.time_entries:
            time_list.append(time.serialize())
        return time_list

class TimeEntry:
    def __init__(self, date, total_seconds=0):
        self.date = date
        self.total_seconds = total_seconds

    def add_seconds(self, seconds):
        self.total_seconds += seconds

    def serialize(self):
        return {
            'date': self.date.strftime("%Y-%m-%d"),
            'total_seconds': self.total_seconds
        }

def url_to_name(url):
    string_list = url.split('/')
    return string_list[2]

def get_active_window():
    window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(window)
    return window_title

def get_chrome_url():
    window = win32gui.GetForegroundWindow()
    chromeControl = auto.ControlFromHandle(window)
    edit = chromeControl.EditControl()
    return 'https://' + edit.GetValuePattern().Value

active_window_name = ""
activity_name = ""
start_time = datetime.datetime.now()
activeList = ActivityList([]).initialize_me()
first_time = True

try:
    while True:
        new_window_name = get_active_window()
        if 'Google Chrome' in new_window_name:
            # or 'Microsoft Edge' in new_window_name
            # or 'Mozilla Firefox' in new_window_name or 'Brave' in new_window_name:
            new_window_name = url_to_name(get_chrome_url())

        if active_window_name != new_window_name:
            if active_window_name:  # Only print if it's not an empty string
                print(active_window_name)
            activity_name = active_window_name

            if not first_time:
                end_time = datetime.datetime.now()
                time_spent = (end_time - start_time).total_seconds()

                exists = False
                for activity in activeList.activities:
                    if activity.name == activity_name:
                        exists = True
                        current_date_str = start_time.strftime("%Y-%m-%d")
                        entry_exists = False
                        for entry in activity.time_entries:
                            if entry.date.strftime("%Y-%m-%d") == current_date_str:
                                entry.add_seconds(time_spent)
                                entry_exists = True
                                break
                        if not entry_exists:
                            activity.time_entries.append(TimeEntry(start_time, time_spent))

                if not exists:
                    new_entry = TimeEntry(start_time, time_spent)
                    new_activity = Activity(activity_name, [new_entry])
                    activeList.activities.append(new_activity)

                with open('activities.json', 'w') as json_file:
                    json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)
                
                start_time = datetime.datetime.now()
            first_time = False
            active_window_name = new_window_name

        time.sleep(1)
    
except KeyboardInterrupt:
    with open('activities.json', 'w') as json_file:
        json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)
