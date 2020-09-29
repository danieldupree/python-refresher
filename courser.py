import os
import re
import json

course_file = "course sections - scraped from webui.txt"

with open(course_file,encoding='utf-8') as f:
    course_sections = f.readlines()

section_starts = []

for i,line in enumerate(course_sections):
    if "Section" in line:
        section_starts.append(i)

sections = []
for i,j in enumerate(section_starts):
    section = {}
    try:
        section['name'] = course_sections[j]
        section['data'] = course_sections[j:section_starts[i+1]]
    except:
        section['name'] = course_sections[j]
        section['data'] = course_sections[j::]
    sections.append(section)

print(json.dumps(sections,indent=2))