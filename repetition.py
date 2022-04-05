a_string="AAbcdeadsfsdfffioufffaab"
words=a_string.lower()
countinfo={}
for i in ['aab','fff']:
    countinfo[i]=words.count(i)
print(countinfo)
