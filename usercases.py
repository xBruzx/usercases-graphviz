from graphviz import Digraph


# Recreating the use case diagram with proper actor representation
dot = Digraph('WeatherAppUseCase', filename='weather_app_use_case', format='png')

# Define actors (Users, Meteorologists, Admins, Developers)
dot.node('U', '👤 Standard User', shape='plaintext')
dot.node('M', '👨‍🔬 Meteorologist', shape='plaintext')
dot.node('A', '🛠️ Admin', shape='plaintext')
dot.node('D', '💻 Developer', shape='plaintext')

# Define use cases for Standard Users
standard_user_cases = [
    "View Current Weather", "Receive Severe Weather Alerts", "View Hourly Forecast",
    "View 7-Day Forecast", "Save Favorite Locations", "Switch Temperature Units",
    "Receive Weather Notifications", "View Radar Maps", "Check Air Quality Index",
    "Report Local Weather"
]

# Define use cases for Meteorologists
meteorologist_cases = [
    "Manually Update Forecasts", "Annotate Radar Maps", "Analyze Weather Trends",
    "Publish Weather Reports", "Verify User Reports"
]

# Define use cases for Admins
admin_cases = [
    "Manage User Accounts", "Moderate User Reports", "Configure System Settings",
    "Manage API Access", "Schedule Maintenance Notices"
]

# Define use cases for Developers
developer_cases = [
    "Integrate Weather APIs", "Optimize App Performance", "Log and Monitor Errors",
    "Ensure Accessibility Compliance", "Support Multiple Languages"
]

# Add use case nodes
for index, case in enumerate(standard_user_cases + meteorologist_cases + admin_cases + developer_cases, 1):
    dot.node(f'UC{index}', case, shape='ellipse')

# Connect Standard User to their use cases
for i in range(1, len(standard_user_cases) + 1):
    dot.edge('U', f'UC{i}')

# Connect Meteorologist to their use cases
for i in range(len(standard_user_cases) + 1, len(standard_user_cases) + len(meteorologist_cases) + 1):
    dot.edge('M', f'UC{i}')

# Connect Admin to their use cases
for i in range(len(standard_user_cases) + len(meteorologist_cases) + 1,
               len(standard_user_cases) + len(meteorologist_cases) + len(admin_cases) + 1):
    dot.edge('A', f'UC{i}')

# Connect Developer to their use cases
for i in range(len(standard_user_cases) + len(meteorologist_cases) + len(admin_cases) + 1,
               len(standard_user_cases) + len(meteorologist_cases) + len(admin_cases) + len(developer_cases) + 1):
    dot.edge('D', f'UC{i}')

# Render and display the diagram
dot_path = "/mnt/data/weather_app_use_case.png"
dot.render(dot_path)
dot_path
