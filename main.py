import discord
from discord import app_commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from keep_alive import keep_alive
import os

scope = [
  'https://www.googleapis.com/auth/spreadsheets',
  "https://www.googleapis.com/auth/drive.file",
  "https://www.googleapis.com/auth/drive"
]
creeds = ServiceAccountCredentials.from_json_keyfile_name(
  'service_account.json', scope)
client = gspread.authorize(creeds)


def next_available_row(worksheet):
  str_list = list(filter(None, worksheet.col_values(2)))
  return str(len(str_list) + 1)


sa = gspread.service_account(filename="service_account.json")
sh = sa.open("Mentorship")


class aclient(discord.Client):

  def __init__(self):
    super().__init__(intents=discord.Intents.default())
    self.synced = False  #we use this so the bot doesn't sync commands more than once

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced:  #check if slash commands have been synced
      await mehrab_evan.sync(
        guild=discord.Object(id=Server ID)
      )  #guild specific: leave blank if global (global registration can take 1-24 hours)
      self.synced = True
    print(f"We have logged in as {self.user}.")


client = aclient()
mehrab_evan = app_commands.CommandTree(client)


@mehrab_evan.command(guild=discord.Object(id=Server ID),
                     name='problem_solving',
                     description='Update Regular Problem Solving Sheet'
                     )  #guild specific slash command
async def slash(interaction: discord.Interaction, your_name: str, date: str,
                rating: int, time: int, submit_count: str, hints: bool):
  f = open("users.txt", "r")
  lines = f.read()
  lines = lines.split(",")
  if your_name in lines:
    wks = sh.worksheet(your_name)

    # programming er jonno shuru
    column = 3
    column_cells = wks.col_values(column)

    last_empty_cell = None
    for i in reversed(range(len(column_cells))):
      if column_cells[i] == '':
        last_empty_cell = wks.cell(i + 1, column)
        break

    if last_empty_cell is None:
      last_empty_cell = wks.cell(len(column_cells) + 1, column)

    await interaction.response.send_message(
      f"Thanks Submitted Successfully\n#Problem Solving\nYour Name : {your_name}\nDate : {date}\nRating : {rating}\nTime : {time}\nSubmit Count : {submit_count}\nHints{hints}",
      ephemeral=False)

    wks.update_acell("A{}".format(last_empty_cell.row), date)
    wks.update_acell("B{}".format(last_empty_cell.row), rating)
    wks.update_acell("C{}".format(last_empty_cell.row), time)
    wks.update_acell("D{}".format(last_empty_cell.row), submit_count)
    wks.update_acell("E{}".format(last_empty_cell.row), hints)

  else:
    await interaction.response.send_message(
      f"There's No Sheet named {your_name}. Do you want to open a new sheet?",
      ephemeral=False)

    worksheet = sh.add_worksheet(title=your_name, rows=100,
                                 cols=20)  # worksheet add kortese
    with open('users.txt', 'a') as file:
      file.write(your_name + ',')
    # id += [name]
    wks = sh.worksheet(your_name)
    # define the row data
    row_data = [
      'Date', 'Rating', 'Time', 'Submit Count', 'Hints (No, TC, Sol)', '',
      'Topic Name', 'Time', 'Learing', 'Practice', 'Date (optional)'
    ]
    wks.append_row(row_data)
    # Data entering the new sheet
    wks = sh.worksheet(your_name)

    # programming er jonno shuru
    column = 3
    column_cells = wks.col_values(column)

    last_empty_cell = None
    for i in reversed(range(len(column_cells))):
      if column_cells[i] == '':
        last_empty_cell = wks.cell(i + 1, column)
        break

    if last_empty_cell is None:
      last_empty_cell = wks.cell(len(column_cells) + 1, column)

    await interaction.response.send_message(
      await interaction.response.send_message(
        f"Thanks Submitted Successfully\n#Problem Solving\nYour Name : {your_name}\nDate : {date}\nRating : {rating}\nTime : {time}\nSubmit Count : {submit_count}\nHints{hints}",
        ephemeral=False))

    wks.update_acell("A{}".format(last_empty_cell.row), date)
    wks.update_acell("B{}".format(last_empty_cell.row), rating)
    wks.update_acell("C{}".format(last_empty_cell.row), time)
    wks.update_acell("D{}".format(last_empty_cell.row), submit_count)
    wks.update_acell("E{}".format(last_empty_cell.row), hints)


#MARKS_UPGRADE
#MARKS_UPGRADE
#MARKS_UPGRADE
@mehrab_evan.command(guild=discord.Object(id=Server ID),
                     name='weekly_evaluation',
                     description='mentees progress'
                     )  #guild specific slash command
async def slash(interaction: discord.Interaction, stack_technology_name: str,
                mentee_name: str, date: str, weekly_activity: int,
                communication_skill: int, technical_depth: str, comments: str):

  wks = sh.worksheet("weekly_evaluation")

  # programming er jonno shuru
  column = 3
  column_cells = wks.col_values(column)

  last_empty_cell = None
  for i in reversed(range(len(column_cells))):
    if column_cells[i] == '':
      last_empty_cell = wks.cell(i + 1, column)
      break

  if last_empty_cell is None:
    last_empty_cell = wks.cell(len(column_cells) + 1, column)

  await interaction.response.send_message(
    f"Thanks Marks Added Successfully\n#Weekly Updates\nStack/Technology Name : {stack_technology_name}\n Mentee Name : {mentee_name}\nDate : {date}\nWeekly Activity : {weekly_activity}\nCommunication_skill : {communication_skill}\nTechnical_Depth : {technical_depth}\nComments : {comments}",
    ephemeral=False)

  wks.update_acell("A{}".format(last_empty_cell.row), stack_technology_name)
  wks.update_acell("B{}".format(last_empty_cell.row), mentee_name)
  wks.update_acell("C{}".format(last_empty_cell.row), weekly_activity)
  wks.update_acell("D{}".format(last_empty_cell.row), communication_skill)
  wks.update_acell("E{}".format(last_empty_cell.row), technical_depth)
  wks.update_acell("F{}".format(last_empty_cell.row), comments)
  wks.update_acell("G{}".format(last_empty_cell.row), date)


@mehrab_evan.command(guild=discord.Object(id=Server ID),
                     name='dev_learning',
                     description='Update Development Sheet'
                     )  #guild specific slash command
async def slash2(interaction: discord.Interaction, your_name: str,
                 topic_name: str, time: int, learning: str, practice: str,
                 date: str):
  f = open("users.txt", "r")
  lines = f.read()
  lines = lines.split(",")
  if your_name in lines:
    wks = sh.worksheet(your_name)

    # programming er jonno shuru
    column = 8
    column_cells = wks.col_values(column)

    last_empty_cell = None
    for i in reversed(range(len(column_cells))):
      if column_cells[i] == '':
        last_empty_cell = wks.cell(i + 1, column)
        break

    if last_empty_cell is None:
      last_empty_cell = wks.cell(len(column_cells) + 1, column)

    await interaction.response.send_message(
      f"Submitted Successfully\n#Development\nYour Name : {your_name}\nTopic Name : {topic_name}\nTime : {time}\nLearning : {learning}\nPractice : {practice}\nDate : {date}",
      ephemeral=False)

    wks.update_acell("G{}".format(last_empty_cell.row), topic_name)
    wks.update_acell("H{}".format(last_empty_cell.row), time)
    wks.update_acell("I{}".format(last_empty_cell.row), learning)
    wks.update_acell("J{}".format(last_empty_cell.row), practice)
    wks.update_acell("K{}".format(last_empty_cell.row), date)

  else:
    worksheet = sh.add_worksheet(title=your_name, rows=100,
                                 cols=20)  # worksheet add kortese
    with open('users.txt', 'a') as file:
      file.write(your_name + ',')
    # id += [name]
    wks = sh.worksheet(your_name)
    # define the row data
    row_data = [
      'Date', 'Rating', 'Time', 'Submit Count', 'Hints (No, TC, Sol)', '',
      'Topic Name', 'Time', 'Learing', 'Practice', 'Date (optional)'
    ]
    wks.append_row(row_data)
    # Data entering the new sheet
    wks = sh.worksheet(your_name)

    # programming er jonno shuru
    column = 8
    column_cells = wks.col_values(column)

    last_empty_cell = None
    for i in reversed(range(len(column_cells))):
      if column_cells[i] == '':
        last_empty_cell = wks.cell(i + 1, column)
        break

    if last_empty_cell is None:
      last_empty_cell = wks.cell(len(column_cells) + 1, column)

    await interaction.response.send_message(
      f"Submitted Successfully\n#Development\nYour Name : {your_name}\nTopic Name : {topic_name}\nTime : {time}\nLearning : {learning}\nPractice : {practice}\nDate : {date}",
      ephemeral=False)

    wks.update_acell("G{}".format(last_empty_cell.row), topic_name)
    wks.update_acell("H{}".format(last_empty_cell.row), time)
    wks.update_acell("I{}".format(last_empty_cell.row), learning)
    wks.update_acell("J{}".format(last_empty_cell.row), practice)
    wks.update_acell("K{}".format(last_empty_cell.row), date)

from datetime import date


#Cp_daily
@mehrab_evan.command(guild=discord.Object(id=Server ID),
                     name='cp_daily',
                     description='cp_daily'
                     )  #guild specific slash command
async def slash(interaction: discord.Interaction, your_id: str,
                your_name: str, sheet_link : str, spent_time : str):

  today = date.today()
  date_today = today.strftime("%d/%m/%Y")
  wks = sh.worksheet("cp_daily")

  # programming er jonno shuru
  column = 3
  column_cells = wks.col_values(column)

  last_empty_cell = None
  for i in reversed(range(len(column_cells))):
    if column_cells[i] == '':
      last_empty_cell = wks.cell(i + 1, column)
      break

  if last_empty_cell is None:
    last_empty_cell = wks.cell(len(column_cells) + 1, column)
  
  await interaction.response.send_message(
    f"Thanks cp_daily Updated Successfully\nName : {your_name}\nID : {your_id}\nDate : {date_today}\nSpent Time : {spent_time}",
    ephemeral=False)

  wks.update_acell("A{}".format(last_empty_cell.row), your_id)
  wks.update_acell("B{}".format(last_empty_cell.row), your_name)
  wks.update_acell("C{}".format(last_empty_cell.row), spent_time)
  wks.update_acell("D{}".format(last_empty_cell.row), sheet_link)
  wks.update_acell("E{}".format(last_empty_cell.row), date_today)

keep_alive()

client.run(os.getenv('Mehrab_Farabi'))
