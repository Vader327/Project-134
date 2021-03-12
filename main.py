import csv

rows = []

with open("data.csv", "r", encoding="UTF-8") as f:
  reader = csv.reader(f)

  for row in reader:
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

final = []

for star_data in star_data_rows:
  distance = star_data[2]

  if len(star_data) == 13:
    gravity = star_data[12]
    distance = distance.replace(",", "")

    if distance and gravity:
      gravity = float(gravity) / 1000
      if float(distance) <= 100 and gravity >= 150 and gravity <= 300:
        final.append(star_data)
        star_data[12] = gravity


with open("final.csv", "w", newline="", encoding="utf-8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(final)

