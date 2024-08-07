# import tkinter as tk
# import mysql.connector
# import json, time
# import datetime 

# def show_popup_90(appname):
#     # Create the root window
#     root = tk.Tk()
#     root.withdraw()  # Hide the root window

#     # Create a new Toplevel window for the popup
#     popup = tk.Toplevel()
#     popup.title("Nearing usage limit")

#     # Set the size of the popup window
#     window_width = 500
#     window_height = 150
#     popup.geometry(f"{window_width}x{window_height}")

#     # Calculate the position to center the popup
#     screen_width = popup.winfo_screenwidth()
#     screen_height = popup.winfo_screenheight()
#     position_top = int(screen_height / 2 - window_height / 2)
#     position_right = int(screen_width / 2 - window_width / 2)

#     # Set the position of the popup
#     popup.geometry(f"+{position_right}+{position_top}")

#     # Create a Label in the popup window
#     label = tk.Label(popup, text="You have reached 90"+"%"+f" of the set time limit on {appname}\nConsider taking a break :)", padx=20, pady=20)
#     label.pack()

#     # Create a Close button in the popup window
#     close_button = tk.Button(popup, text="Close", command=popup.quit, padx=10, pady=5)
#     close_button.pack()

#     # Run the main loop for the popup window
#     popup.mainloop()

#     # Close the application after the popup is closed
#     root.quit()

# def show_popup_over(appname):
#     # Create the root window
#     root = tk.Tk()
#     root.withdraw()  # Hide the root window

#     # Create a new Toplevel window for the popup
#     popup = tk.Toplevel()
#     popup.title("Nearing usage limit")

#     # Set the size of the popup window
#     window_width = 500
#     window_height = 150
#     popup.geometry(f"{window_width}x{window_height}")

#     # Calculate the position to center the popup
#     screen_width = popup.winfo_screenwidth()
#     screen_height = popup.winfo_screenheight()
#     position_top = int(screen_height / 2 - window_height / 2)
#     position_right = int(screen_width / 2 - window_width / 2)

#     # Set the position of the popup
#     popup.geometry(f"+{position_right}+{position_top}")

#     # Create a Label in the popup window
#     label = tk.Label(popup, text=f"You have reached the set time limit on {appname}\nConsider taking a break :)", padx=20, pady=20)
#     label.pack()

#     # Create a Close button in the popup window
#     close_button = tk.Button(popup, text="Close", command=popup.quit, padx=10, pady=5)
#     close_button.pack()

#     # Run the main loop for the popup window
#     popup.mainloop()

#     # Close the application after the popup is closed
#     root.quit()

# # Database connection details for MySQL


# # Connect to the database and fetch data for MySQL
# def fetch_goals_from_db():
#     db_config = {
#     'database': 'detox_db_1',
#     'user': 'ak_user',
#     'password': 'ytterbium',
#     'host': 'localhost',
#     'port': 3306,
#     }
#     connection = None
#     goals = []
#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()
#         cursor.execute("SELECT id, appname, timegoal, uid_id FROM tracker_usergoals ORDER BY timegoal DESC")
#         goals = cursor.fetchall()
#     except Exception as error:
#         print(f"Error fetching data: {error}")
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#     return goals


# def fetch_data_from_db():
#     db_config = {
#         'database': 'detox_db_1',
#         'user': 'ak_user',
#         'password': 'ytterbium',
#         'host': 'localhost',
#         'port': 3306,
#     }
#     connection = None
#     userdata = []
#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()
#         current_date = datetime.date.today().isoformat()  # Get the current date in YYYY-MM-DD format
#         query = """
#         SELECT uid_id, appname, timespent, ondate 
#         FROM tracker_userdata 
#         WHERE uid_id=%s AND ondate=%s
#         ORDER BY timespent desc
#         """
#         cursor.execute(query, (2, current_date))
#         userdata = cursor.fetchall()
#     except Exception as error:
#         print(f"Error fetching data: {error}")
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#     return userdata

# def clean_goals():
#     goals = fetch_goals_from_db()
#     # gdict = {}
#     glst = []
#     for g in goals:
#         an = g[1]; tm = g[2]
#         # gdict[an] = tm
#         tup = (an,tm)
#         glst.append(tup)
#     return glst

# def clean_data():
#     data = fetch_data_from_db()
#     dlst = []
#     for d in data:
#         dlst.append((d[1],d[2]))
#     return dlst

# def check_usage(warned_apps):
#     usage = clean_data()
#     goals = clean_goals()
#     # warned_apps = []
#     for use in usage:
#         for limit in goals:
#             if use[0]==limit[0]:
#                 #check if goal is less or not
#                     lim_90 = 0.9*(limit[1])
#                     if limit[1]<use[1]:
#                         if use[0] not in warned_apps:
#                             return (use[0], 1)    #1 specifies full time
#                         else:
#                             continue
#                     elif (use[1]>lim_90) and (use[1]<limit[1]):
#                             return (use[0], 0)    #0 specifies 90% time
#                     else:
#                         continue
#     return (0,0)
# checked_apps = []

# if __name__ == '__main__':
#     while True:
#         try:
#             app, flag = check_usage(checked_apps)
#             if app==0:
#                 time.sleep(11)
#                 continue
#             if flag==0:
#                 show_popup_90(app)
#                 checked_apps.append(app)
#             elif flag==1:
#                 show_popup_over(app)
#                 checked_apps.append(app)
#             # show_popup()
#             time.sleep(11)

#         except KeyboardInterrupt:
#             print("Stopping script...")
#             break

#         except Exception as e:
#             print(e)
#             break

#     print("Application closed")

""""end of originial code"""

# import tkinter as tk
# import mysql.connector
# import json, time
# import datetime

# def show_popup_90(appname):
#     root = tk.Tk()
#     root.withdraw()
#     popup = tk.Toplevel()
#     popup.title("Nearing usage limit")

#     window_width = 500
#     window_height = 150
#     popup.geometry(f"{window_width}x{window_height}")

#     screen_width = popup.winfo_screenwidth()
#     screen_height = popup.winfo_screenheight()
#     position_top = int(screen_height / 2 - window_height / 2)
#     position_right = int(screen_width / 2 - window_width / 2)
#     popup.geometry(f"+{position_right}+{position_top}")

#     label = tk.Label(popup, text="You have reached 90%" + f" of the set time limit on {appname}\nConsider taking a break :)", padx=20, pady=20)
#     label.pack()

#     close_button = tk.Button(popup, text="Close", command=popup.destroy, padx=10, pady=5)
#     close_button.pack()

#     popup.mainloop()
#     root.destroy()

# def show_popup_over(appname):
#     root = tk.Tk()
#     root.withdraw()
#     popup = tk.Toplevel()
#     popup.title("Usage limit reached")

#     window_width = 500
#     window_height = 150
#     popup.geometry(f"{window_width}x{window_height}")

#     screen_width = popup.winfo_screenwidth()
#     screen_height = popup.winfo_screenheight()
#     position_top = int(screen_height / 2 - window_height / 2)
#     position_right = int(screen_width / 2 - window_width / 2)
#     popup.geometry(f"+{position_right}+{position_top}")

#     label = tk.Label(popup, text=f"You have reached the set time limit on {appname}\nConsider taking a break :)", padx=20, pady=20)
#     label.pack()

#     close_button = tk.Button(popup, text="Close", command=popup.destroy, padx=10, pady=5)
#     close_button.pack()

#     popup.mainloop()
#     root.destroy()

# db_config = {
#     'database': 'detox_db_1',
#     'user': 'ak_user',
#     'password': 'ytterbium',
#     'host': 'localhost',
#     'port': 3306,
# }

# def fetch_goals_from_db():
#     connection = None
#     goals = []
#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()
#         cursor.execute("SELECT id, appname, timegoal, uid_id FROM tracker_usergoals ORDER BY timegoal DESC")
#         goals = cursor.fetchall()
#     except Exception as error:
#         print(f"Error fetching data: {error}")
#     finally:
#         if connection and cursor:
#             cursor.close()
#             connection.close()
#     return goals

# def fetch_data_from_db():
#     connection = None
#     userdata = []
#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()
#         current_date = datetime.date.today().isoformat()
#         query = """
#         SELECT uid_id, appname, timespent, ondate 
#         FROM tracker_userdata 
#         WHERE uid_id=%s AND ondate=%s
#         ORDER BY timespent desc
#         """
#         cursor.execute(query, (2, current_date))
#         userdata = cursor.fetchall()
#     except Exception as error:
#         print(f"Error fetching data: {error}")
#     finally:
#         if connection and cursor:
#             cursor.close()
#             connection.close()
#     return userdata

# def clean_goals():
#     goals = fetch_goals_from_db()
#     glst = [(g[1], g[2]) for g in goals]
#     return glst

# def clean_data():
#     data = fetch_data_from_db()
#     dlst = [(d[1], d[2]) for d in data]
#     return dlst

# def check_usage(warned_apps):
#     usage = clean_data()
#     goals = clean_goals()
#     for use in usage:
#         for limit in goals:
#             if use[0] == limit[0]:
#                 lim_90 = 0.9 * limit[1]
#                 if use[1] >= limit[1]:
#                     if use[0] not in warned_apps:
#                         return use[0], 1
#                 elif lim_90 <= use[1] < limit[1]:
#                     return use[0], 0
#     return None, None

# checked_apps = []

# if __name__ == '__main__':
#     while True:
#         try:
#             app, flag = check_usage(checked_apps)
#             if app and flag is not None:
#                 if flag == 0:
#                     show_popup_90(app)
#                     checked_apps.append(app)
#                 elif flag == 1:
#                     show_popup_over(app)
#                     checked_apps.append(app)
#             time.sleep(10)
#         except KeyboardInterrupt:
#             print("Stopping script...")
#             break
#         except Exception as e:
#             print(e)
#             break

#     print("Application closed")
"""____"""
# import tkinter as tk
# import mysql.connector
# import time
# import datetime

# # Global variable for the main Tk instance
# root = tk.Tk()
# root.withdraw()  # Hide the root window

# def show_popup_90(appname):
#     popup = tk.Toplevel(root)
#     popup.title("Nearing usage limit")

#     window_width = 500
#     window_height = 150
#     popup.geometry(f"{window_width}x{window_height}")

#     screen_width = popup.winfo_screenwidth()
#     screen_height = popup.winfo_screenheight()
#     position_top = int(screen_height / 2 - window_height / 2)
#     position_right = int(screen_width / 2 - window_width / 2)
#     popup.geometry(f"+{position_right}+{position_top}")

#     label = tk.Label(popup, text="You have reached 90%" + f" of the set time limit on {appname}\nConsider taking a break :)", padx=20, pady=20)
#     label.pack()

#     close_button = tk.Button(popup, text="Close", command=popup.destroy, padx=10, pady=5)
#     close_button.pack()

#     popup.grab_set()  # Ensure popup is modal
#     root.wait_window(popup)  # Wait until popup is destroyed

# def show_popup_over(appname):
#     popup = tk.Toplevel(root)
#     popup.title("Usage limit reached")

#     window_width = 500
#     window_height = 150
#     popup.geometry(f"{window_width}x{window_height}")

#     screen_width = popup.winfo_screenwidth()
#     screen_height = popup.winfo_screenheight()
#     position_top = int(screen_height / 2 - window_height / 2)
#     position_right = int(screen_width / 2 - window_width / 2)
#     popup.geometry(f"+{position_right}+{position_top}")

#     label = tk.Label(popup, text=f"You have reached the set time limit on {appname}\nConsider taking a break :)", padx=20, pady=20)
#     label.pack()

#     close_button = tk.Button(popup, text="Close", command=popup.destroy, padx=10, pady=5)
#     close_button.pack()

#     popup.grab_set()  # Ensure popup is modal
#     root.wait_window(popup)  # Wait until popup is destroyed

# db_config = {
#     'database': 'detox_db_1',
#     'user': 'ak_user',
#     'password': 'ytterbium',
#     'host': 'localhost',
#     'port': 3306,
# }

# def fetch_goals_from_db():
#     connection = None
#     goals = []
#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()
#         cursor.execute("SELECT id, appname, timegoal, uid_id FROM tracker_usergoals ORDER BY timegoal DESC")
#         goals = cursor.fetchall()
#     except Exception as error:
#         print(f"Error fetching data: {error}")
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#     return goals

# def fetch_data_from_db():
#     connection = None
#     userdata = []
#     try:
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor()
#         current_date = datetime.date.today().isoformat()
#         query = """
#         SELECT uid_id, appname, timespent, ondate 
#         FROM tracker_userdata 
#         WHERE uid_id=%s AND ondate=%s
#         ORDER BY timespent desc
#         """
#         cursor.execute(query, (2, current_date))
#         userdata = cursor.fetchall()
#     except Exception as error:
#         print(f"Error fetching data: {error}")
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#     return userdata

# def clean_goals():
#     goals = fetch_goals_from_db()
#     glst = [(g[1], g[2]) for g in goals]
#     return glst

# def clean_data():
#     data = fetch_data_from_db()
#     dlst = [(d[1], d[2]) for d in data]
#     return dlst

# def check_usage(warned_apps_90, warned_apps):
#     usage = clean_data()
#     goals = clean_goals()
#     for use in usage:
#         for limit in goals:
#             if use[0] == limit[0]:
#                 lim_90 = 0.9 * limit[1]
#                 if use[1] >= limit[1]:
#                     if use[0] not in warned_apps:
#                         return use[0], 1
#                 elif lim_90 <= use[1] < limit[1]:
#                     if use[0] not in warned_apps_90:
#                         return use[0], 0
#                     # return use[0], 0
#     return None, None

# checked_apps_90 = []
# checked_apps = []

# if __name__ == '__main__':
#     try:
#         while True:
#             app, flag = check_usage(checked_apps_90,checked_apps)
#             if app and flag is not None:
#                 if flag == 0:
#                     show_popup_90(app)
#                     checked_apps_90.append(app)
#                 elif flag == 1:
#                     show_popup_over(app)
#                     checked_apps.append(app)
#             time.sleep(10)
#     except KeyboardInterrupt:
#         print("Stopping script...")
#     except Exception as e:
#         print(e)
#     finally:
#         root.update()

#     root.destroy()
#     print("Application closed")

import sys
import tkinter as tk
import mysql.connector
import time
import datetime
import threading

# Global variable for the main Tk instance
root = tk.Tk()
root.withdraw()  # Hide the root window

def show_popup_90(appname):
    popup = tk.Toplevel(root)
    popup.title("Nearing usage limit")

    window_width = 500
    window_height = 150
    popup.geometry(f"{window_width}x{window_height}")

    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    popup.geometry(f"+{position_right}+{position_top}")

    label = tk.Label(popup, text="You have reached 90%" + f" of the set time limit on {appname}\nConsider taking a break :)", padx=20, pady=20)
    label.pack()

    close_button = tk.Button(popup, text="Close", command=popup.destroy, padx=10, pady=5)
    close_button.pack()

    popup.grab_set()  # Ensure popup is modal
    root.wait_window(popup)  # Wait until popup is destroyed

def show_popup_over(appname):
    popup = tk.Toplevel(root)
    popup.title("Usage limit reached")

    window_width = 500
    window_height = 150
    popup.geometry(f"{window_width}x{window_height}")

    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    popup.geometry(f"+{position_right}+{position_top}")

    label = tk.Label(popup, text=f"You have reached the set time limit on {appname}\nConsider taking a break :)", padx=20, pady=20)
    label.pack()

    close_button = tk.Button(popup, text="Close", command=popup.destroy, padx=10, pady=5)
    close_button.pack()

    popup.grab_set()  # Ensure popup is modal
    root.wait_window(popup)  # Wait until popup is destroyed

db_config = {
    'database': 'detox_db_1',
    'user': 'ak_user',
    'password': 'ytterbium',
    'host': 'localhost',
    'port': 3306,
}

def fetch_goals_from_db():
    connection = None
    goals = []
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT id, appname, timegoal, uid_id FROM tracker_usergoals ORDER BY timegoal DESC")
        goals = cursor.fetchall()
    except Exception as error:
        print(f"Error fetching data: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()
    return goals

def fetch_data_from_db():
    connection = None
    userdata = []
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        current_date = datetime.date.today().isoformat()
        query = """
        SELECT uid_id, appname, timespent, ondate 
        FROM tracker_userdata 
        WHERE uid_id=%s AND ondate=%s
        ORDER BY timespent desc
        """
        cursor.execute(query, (2, current_date))
        userdata = cursor.fetchall()
    except Exception as error:
        print(f"Error fetching data: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()
    return userdata

def clean_goals():
    goals = fetch_goals_from_db()
    glst = [(g[1], g[2]) for g in goals]
    return glst

def clean_data():
    data = fetch_data_from_db()
    dlst = [(d[1], d[2]) for d in data]
    return dlst

def check_usage(warned_apps_90, warned_apps):
    usage = clean_data()
    goals = clean_goals()
    for use in usage:
        for limit in goals:
            if use[0] == limit[0]:
                lim_90 = 0.9 * limit[1]
                if use[1] >= limit[1]:
                    if use[0] not in warned_apps:
                        return use[0], 1
                elif lim_90 <= use[1] < limit[1]:
                    if use[0] not in warned_apps_90:
                        return use[0], 0
    return None, None

checked_apps_90 = []
checked_apps = []

def periodic_check():
    app, flag = check_usage(checked_apps_90, checked_apps)
    if app and flag is not None:
        if flag == 0:
            show_popup_90(app)
            checked_apps_90.append(app)
        elif flag == 1:
            show_popup_over(app)
            checked_apps.append(app)
    root.after(10000, periodic_check)  # Schedule next check after 10 seconds

if __name__ == '__main__':
    try:
        root.after(1000, periodic_check)  # Start periodic checking after 1 second
        root.mainloop()  # Start Tkinter event loop
    except KeyboardInterrupt:
        print("Stopping script...")
        # quit(1)
        sys.exit()
    except Exception as e:
        print(e)
    finally:
        print("Application closed")
