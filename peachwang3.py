# encoding: utf-8
print '哈哈'
import urllib

url = "http://wechat.shwilling.com/sjtu/course/detail/MA016/2013-2014-2"
handle = urllib.urlopen(url)
htmlSource = handle.read()
handle.close()

#help handlers
def printlist (list):
    for p in list:
        print p

def splitfinder(s, start, end, count = 0):
    clist = s.split(start)
    clist.pop(0)
    content = []
    if count == 0:
        for row in clist:
            p = row.split(end)[0]
            content.append(p)
    else:
        i = 0
        for i in range(count):
            row = clist[i]
            p = row.split(end)[0]
            content.append(p)
    return content

def courseInfo(s):
    course = []
    course.append(splitfinder(s,'<h1 class="c-name">', '<', 1)[0])
    course.append(splitfinder(s,'<span class="c-term-code">', '<', 1)[0])
    return course

#print htmlSource
splitContent = (htmlSource.split('<div class="course-section container">',1))[1].split('<div id="uni_menu-outer">',1)

#find all courses
splitCourse = splitContent[0].split('<div class="course">') 
splitCourse.pop(0)

courses = []

for course in splitCourse:
    courses.append(courseInfo(course))

print courses[0][1]

for i in range(len(courses)):
    for j in range(len(courses)):
        print courses[i][j]

#find course info


#for rows in splitContent

#print splitContent[0]
#for p in splitContent:
#    print p 
