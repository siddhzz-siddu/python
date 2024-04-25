a='''mango city triple single qts'''

b="""mango city triple double qts"""

c="mango city double qts"

d='mango city single qts'

e="mango's city - use single qts inside double qts"

f='mango"s city - use single qts inside double qts'

g='mango\'s city - use slash single qts inside double qts'

h="mango\"s city - use slash double qts inside double qts"

i="mango\s city - use slash inside double qts"

j="mango\n s city - use new line inside double qts"

k="mango\t s city - use tab space inside double qts"

l="mango\b s city - use backspace inside double qts"

m="mango\\ s city - use double slashes inside double qts"



n='''mangos \
city - use \
single qts \
inside double qts'''


o='''mangos 
city - use 
single qts 
inside double qts'''

p="mango\\ s city - use double slashes inside double qts"
print(p)

p="mango\\\\ s city - use double slashes inside double qts"
print(p)

p="mango\\\\\\ s city - use double slashes inside double qts"
print(p)

p="mango\\\\\\\\ s city - use double slashes inside double qts"
print(p)




ui=input('enter the string')
print([w for w in ui.split() if 's' in w])