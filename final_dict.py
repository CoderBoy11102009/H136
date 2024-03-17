import matplotlib as mb
import pandas as pd

import csv

rows = []

with open("/content/H129/unit_converted_stars.csv") as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    rows.append(row)

headers = rows[0]
sun_data_rows = rows[1:]
print(headers)
print(sun_data_rows[0])

temp_sun_data_rows = list(sun_data_rows)

for sun_data in temp_sun_data_rows:
  if sun_data[1].lower() == "hd 100546 b":
    sun_data_rows.remove(sun_data)

sun_masses = []
sun_radiuses = []
sun_names = []

for sun_data in sun_data_rows:
  sun_masses.append(sun_data[3])
  sun_radiuses.append(sun_data[4])
  sun_names.append(sun_data[0])

sun_gravity = []

low_gravity_sun = []
for index, gravity in enumerate(sun_gravity):
  if gravity < 150 - 350:
    low_gravity_sun.append(sun_data_rows[index])

print(len(low_gravity_sun))

print(headers)

suitable_suns = []

for sun_data in low_gravity_sun:
  if sun_data[6].lower() == "terrestrial" or sun_data[6].lower() == "super earth":
    suitable_suns.append(sun_data)

print(len(suitable_suns))

temp_suitable_suns = list(suitable_suns)
for sun_data in temp_suitable_suns:
  if sun_data[5].lower() == "unknown":
    suitable_suns.remove(sun_data)

for sun_data in suitable_suns:
  if sun_data[9].split(" ")[1].lower() == "days":
    sun_data[9] = float(sun_data[9].split(" ")[0]) #Days
  else:
    sun_data[9] = float(sun_data[9].split(" ")[0])*365 #Years
  sun_data[8] = float(sun_data[8].split(" ")[0])

orbital_radiuses = []
orbital_periods = []
for sun_data in suitable_suns:
  orbital_radiuses.append(sun_data[8])
  orbital_periods.append(sun_data[9])

sun_speeds = []
for sun_data in suitable_suns:
  distance = 2 * 3.14 * (sun_data[8] * 1.496e+8)
  time = sun_data[9] * 86400
  speed = distance / time
  sun_speeds.append(speed)

speed_supporting_sun = list(suitable_suns) #We will leave suitable sun list as it is

temp_speed_supporting_suns = list(suitable_suns)
for index, sun_data in enumerate(temp_speed_supporting_suns):
  if sun_speeds[index] > 200:
    speed_supporting_sun.remove(sun_data)

print(len(speed_supporting_sun))

goldilock_suns = list(suitable_suns) #We will leave suitable sun list as it is

temp_goldilock_suns = list(suitable_suns)
for sun_data in temp_goldilock_suns:
  if sun_data[8] < 0.38 or sun_data[8] > 2:
    goldilock_suns.remove(sun_data)

print(len(suitable_suns))
print(len(goldilock_suns))

final_dict = {}

for index, sun_data in enumerate(sun_data_rows):
  features_list = []
  gravity = (float(sun_data[3])*5.972e+24) / (float(sun_data[7])*float(sun_data[7])*6371000*6371000) * 6.674e-11
  try:
    if gravity < 100:
      features_list.append("gravity")
  except: pass
  try:
    if sun_data[6].lower() == "terrestrial" or sun_data[6].lower() == "super earth":
      features_list.append("sun_type")
  except: pass
  try:
    if float(sun_data[8].split(" ")[0]) > 0.38 and float(sun_data[8].split(" ")[0]) < 2:
      features_list.append("goldilock")
  except:
    try:
      if sun_data[8] > 0.38 and sun_data[8] < 2:
        features_list.append("goldilock")
    except: pass
  try:
    distance = 2 * 3.14 * (sun_data[8] * 1.496e+8)
    time = sun_data[9] * 86400
    speed = distance / time
    if speed < 200:
      features_list.append("speed")
  except: pass
  final_dict[sun_data[1]] = features_list

print(final_dict)

