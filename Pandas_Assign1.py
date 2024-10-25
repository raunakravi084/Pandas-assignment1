"""
30-July

1 .Find out there avarage rating on weekly basis keep this in a mind that they take two days of leave
2 .Total working days for each agents
3. Total query that you hvae taken
4. total Feedback that you have received
5. a agent name who have average rating between 3.5 to 4
6 . Agent name who have rating lesss then 3.5
7 . agent name who have rating more then 4.5
8 . how many feedaback agents have received more then 4.5 average
9 . average weekly response time for each agent
10 . average weekely resolution time for each agents
11 . list of all agents name
12 . percentage of chat on which they have received a feedback
13 . Total contributation hour for each and every agents weekly basis
14. total percentage of active hour for a month

"""
import pandas as pd
login = pd.read_excel('C:\\Users\\Raunak.Ravi\\OneDrive - GlobalData PLC\\Documents\\ipython\\ipython_july2024\\31.30-july\\Agent_Login_Report (4).xls',header=2)
agent = pd.read_excel('C:\\Users\\Raunak.Ravi\\OneDrive - GlobalData PLC\\Documents\\ipython\\ipython_july2024\\31.30-july\\AgentPerformance (1).xlsx',header=1)
# print(login.info())
# print(agent.info())
agent['Date'] = pd.to_datetime(agent['Date'])

agent['Average Response Time'] = pd.to_timedelta(agent['Average Response Time'])
agent['Average Resolution Time'] = pd.to_timedelta(agent['Average Resolution Time'])

agent['date_week'] = agent['Date'].dt.isocalendar().week

# 1 .Find out there avarage rating on weekly basis keep this in a mind that they take two days of leave

# method-1
weekly_avg_rating = agent.groupby(['Agent Name','date_week'])[['Average Rating']].mean().reset_index()

# method-2
weekly_avg_rating1 = agent.groupby(['Agent Name','date_week']).agg({'Average Rating':'mean'}).reset_index()

#print(weekly_avg_rating1)

# 2 .Total working days for each agents

working_days = agent.groupby(['Agent Name'])['Date'].nunique().reset_index()
working_days.columns = ['Agent Name','Total working days']
#print(working_days)

# 3. Total query that you hvae taken

Total_query = agent.groupby(['Agent Name'])['Total Chats'].sum().reset_index()
Total_query.columns = ['Agent Name','Total query']
# print(Total_query)

# 4. total Feedback that you have received

Total_feedback = agent.groupby(['Agent Name'])['Total Chats'].sum().reset_index()
Total_feedback.columns = ['Agent Name','Total feedback']
# print(Total_feedback)

# 5. a agent name who have average rating between 3.5 to 4

#print(agent[(3.5 < agent['Average Rating']) & (agent['Average Rating'] < 4)]['Agent Name'].unique())

# 6 . Agent name who have rating lesss then 3.5

#print(agent[(3.5 < agent['Average Rating'])]['Agent Name'].unique())

# 7 . agent name who have rating more then 4.5

# print(agent[(4.5 < agent['Average Rating'])]['Agent Name'].unique())

# 8 . how many feedaback agents have received more then 4.5 average

agent_feedback = agent[(4.5 < agent['Average Rating'])][['Agent Name','Total Feedback']]
#print(agent_feedback.groupby('Agent Name')['Total Feedback'].sum().reset_index())

# 9 . average weekly response time for each agent

#print(agent.groupby(['Agent Name','date_week'])['Average Response Time'].mean().reset_index())

# 10 . average weekely resolution time for each agents

#print(agent.groupby(['Agent Name','date_week'])['Average Resolution Time'].mean().reset_index())

# 11 . list of all agents name

#print([agent['Agent Name'].unique()])

# 12 . percentage of chat on which they have received a feedback

agent['Feedback Percentage'] = (agent['Total Feedback'] / agent['Total Chats']) * 100
#print(agent.groupby(['Agent Name'])['Feedback Percentage'].mean().reset_index())

### Login data

login['Date'] = pd.to_datetime(login['Date'])
login['Login Time'] = pd.to_timedelta(login['Login Time'])
login['Logout Time'] = pd.to_timedelta(login['Logout Time'])
login['Duration'] = pd.to_timedelta(login['Duration'])

# 13 . Total contributation hour for each and every agents weekly basis

login['date_week'] = login['Date'].dt.isocalendar().week
#print(login.groupby(['Agent','date_week'])['Duration'].sum().reset_index())

# 14. total percentage of active hour for a month

total_duration = login.groupby(['Agent'])['Duration'].sum().reset_index()
total_possible_hours_per_month = pd.to_timedelta(8 * 5 * 4, unit='hours')
total_duration['Active Hours Percentage'] = (total_duration['Duration'] / total_possible_hours_per_month ) * 100
print(total_duration)