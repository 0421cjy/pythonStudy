import sys

src = sys.argv[1]
dst = sys.argv[2]

print(src)
print(dst)


f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace('\t', '    ')

f = open(dst, 'w')
f.write(space_content)
f.close()