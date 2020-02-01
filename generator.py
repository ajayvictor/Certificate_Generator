
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
from pandas import read_excel
import os


excel_data_df = read_excel('students.xlsx', sheet_name='Sheet2', usecols=['Student Name', 'Group / Section', 'Absentees'])

data = excel_data_df.to_dict(orient='record')

for item in data:
	if item['Absentees'] not in ["absent", "Absent"]:
		name = item['Student Name'].title()
		cls = item['Group / Section']
		text = name + ' of Class ' + cls
		img = Image.open('part.jpeg')
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype('adine-kirnberg.regular.ttf', 60)
		draw.text((230, 400), text, (11, 41, 137), font=font)
		directory = cls
		if not os.path.exists(directory):
    			os.makedirs(directory)
		img.save(directory+'/'+str(name)+'.jpeg')
