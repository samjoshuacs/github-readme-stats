import os

file = open('./vercel.json', 'r')
str = file.read()
file = open('./vercel.json', 'w')

str = str.replace('"maxDuration": 10', '"maxDuration": 5')

file.write(str)
file.close()
