#!/usr/bin/env python
# coding: utf-8

# # Python@Library 2024 - Teil 2
# 
# Jitao David Zhang, Januar 2024
# 
# Diese kurze Python Tutorial is stark vom Software Carpentry Kurs [*Plotting and Programming in Python*](https://swcarpentry.github.io/python-novice-gapminder/), und von [Python Tutorial](https://github.com/kdungs/teaching-SMD2-2016/blob/master/tutorials/Python%20Tutorial.ipynb) von *kdungs* inspiriert.

# ## Variablen und Datentypen

# In[1]:


# Hier ist ein Kommentar

x = 3 # integer
print(x) ## drucken
print(x * 20)

y = 'Grüzi'
print(y)

z = [1, 2, 3] ## z ist eine Liste
print(z)
print(z[0])
print(z[1])
print(z[0:-1])

name = 'Zoe'
print(name[0])
print(name[2])
## print(name[5])


# * Der `NoneType`, None
# * Der `bool` type: `True` und `False`
# * Numerische Typen
#     * `int`, z.B. 42
#     * `float`, z.B. 3.1415926
#     * `comlex`
# * Sequenzen:
#     * `string`, z.B. 'Hallo, Welt!'
#     * `list`, z.B. `[1, 2, 3]`
#     * `tuple`, z.B. `('Manuel', 15, 177, 62)`
# * Der `dict` (*Dictionary* in Englisch, Wörterbuch), z.B. `{'name': 'Manuel','alter': 15, 'Grösse': 177, 'Gewicht': 62}`.
# * Det `Set` (Menge), z.B. '{1, 2, 3}'

# ### Übungen
# 
# 1. Wie viele Sekunden gibt es in einem Tag? In einer Woche?
# 2. Was erwartet man?
# ```
# name = 'Maximillian'
# print(name[3])
# print(name[7])
# print(name[15])
# print(name[:3]) ## fortschrittende
# print(name[7:]) ## fortschrittende
# ```

# ## Konversion zwischen Typen

# In[2]:


x = '3.52'
xf = float(x)
print(xf)

print(type(x))
print(type(xf))


# In[3]:


x = 0
xb = bool(x)
print(xb)

y=1
yb = bool(y)
print(yb)

bool(-1) ## aufpassen: alle nicht-0 werte sind als True konvertiert


# In[4]:


nt = not True
print(nt)

ne = not []
print(ne)


# ### Übungen
# 
# 1. Konvertiere das String '7.34' in eine Zahl mit `float`.
# 2. Konvertiere die Zahl 3.58 in einer String mit `str`.

# ## Operatoren
# 
# Mit Hilfe von Operatoren kann man mit Variablen von gleichen Typen rechnen. Für numerische Typen gibt es beispielsweise die arithmetischen Operatoren
# 
# * `+` Addition
# * `-` Subtraktion
# * `*` Multiplikation
# * `/` Division
# * `//` ganzzahlige Division
# * `%` Restwertbildung
# * `**` Potenzieren

# In[5]:


wert = 1.68
wert_2 = wert * 5
wert_3 = wert ** 10

print(wert_2)
print(wert_3)


# In[6]:


vorname = 'Elena'
nachname = 'Seitz'
print(vorname + nachname)
vollname = vorname + ' ' + nachname
print(vollname)


# In[7]:


torwart = ['Hitz']
verteidigung = ['Schmid', 'Frei', 'Van Breemen', 'Dräger']
mittelfeld = ['Veiga', 'Xhaka', 'Gauto', 'Essiam']
sturm = ['Kade', 'Jovanovic']
team = torwart + verteidigung + mittelfeld + sturm
print(team)


# In[8]:


# Achtung

## print("Die Temperatur heute ist " + 3 + " Grad.")
print("Die Temperatur heute ist " + str(3) + " Grad.")


# ### Übungen
# 
# 1. Probiere folgende Zeilen aus und erkläre Deine Beobachtungen
# 
# ```
# 24 / 5
# 24 // 5
# 24 % 5
# 24 ** 5
# ```
# 
# 2. Wieso gibt es ein Fehler wenn man `"Temperatur is " + 3` eingibt? Wie kann man den Fehler beseitigen?

# ## Kotrollstrukturen: if-else, *while* Schleife, und *for* Schleife

# In[9]:


temperatur = 13
if temperatur > 10: # if = falls
    print("Es ist eher warm für Basel in Januar")
else: # else = ansonsten
    print('Saukalt wie immer')


# In[10]:


i = 0
while i < 5: ## while = während
    print(i)
    i = i + 1


# In[11]:


s = 0
for i in range(12):
    s = s + i

print(s)


# In[12]:


for index, name in enumerate(team):
    print('Der ' + str(index+1) + '. spieler heute heisst' + str(name))


# In[13]:


torwart = ['Hitz']
verteidigung = ['Schmid', 'Frei', 'Van Breemen', 'Dräger']
mittelfeld = ['Veiga', 'Xhaka', 'Gauto', 'Essiam']
sturm = ['Kade', 'Jovanovic']
team = torwart + verteidigung + mittelfeld + sturm
print(team)

for spieler in team:
    print("Heute spielt " + spieler + " für den FCB")


# In[14]:


for index, name in enumerate(team):
    human_index = index + 1
    human_index_str = str(human_index)
    print('Der ' + human_index_str + '. spieler heute heisst ' + name)


# In[15]:


torwart_nummer = [1]
verteidigung_nummer = [31, 20, 25, 6]
mittelfeld_nummer = [40, 34, 33, 18]
sturm_nummer = [30, 99]
team_nummer = torwart_nummer + verteidigung_nummer + mittelfeld_nummer + sturm_nummer


# In[16]:


for index, name in enumerate(team):
    spieler_nummer = team_nummer[index]
    print('Der spieler ' + name + 'hat Trikot mit der Nummer '  + str(spieler_nummer))


# In[17]:


team_dict = dict(zip(team, team_nummer))
print(team_dict['Frei'])
## team_dict['Kayombo']
print(team_dict.get('Kayombo'))


# In[18]:


for key in team_dict.keys():
    print('Der spieler ' + key + 'hat Trikot mit der Nummer '  + str(team_dict[key]))


# In[19]:


for key, value in team_dict.items():
    print('Der spieler ' + key + 'hat Trikot mit der Nummer '  + str(value))


# ### Übungen
# 
# 1. Druck alle gerade Zahlen zwischen 1 und 100.
# 2. Finde die Trikotnummer von folgenden Spieler: Kade, Van breemen, Boey. Wenn die Nummer nicht gefunden ist, druck 'Nicht gefunden'.

# ## Funktion

# In[20]:


def verdoppeln(x):
    """Die funktion verdoppelt deren Eigabe
        x - Eine Zahl
    """
    return x * 2

x = 1
print(verdoppeln(x))
print(x)


# In[21]:


help(verdoppeln)


# In[22]:


for i in range(10):
    print(i, verdoppeln(i)) 


# ### Übungen
# 
# 1. Schreib eine Funktion, welche die Zahl verdreifacht.
# 2. Schreib eine andere Funktion, welche das erste Alphabet von dem String in der Eingabe zurückgibt. Zum Beispiel, wenn die Eingabe 'Hallo' wäre, gibt es 'H' zurück.

# ## Funktion mit mehreren Parametern und Kontrollkonstruten

# In[23]:


greetings = {
    'English': 'Hello',
    'Deutsch': 'Hallo',
    'Mundart': 'Grüezi',
    'Francais': 'Salut'}

def greet(name, language=None): ## name=Name, language=Sprache
    if language is None:
        language = 'English'
    greeting = greetings.get(language)
    if greeting is None:
        print("Es tut mir Leid, ich kann " + language + " leider nicht.")
    else:
        print(greeting + ", " + name + "!")
        
greet("Henry")
greet("Henry", language="Deutsch")
greet("Henry", language="Mundart")
greet("Guillaume", "Francais")

greet("David", "Chinesisch")


# ## Ein Spiel mit dem Collatz Problem

# In[24]:


def m3p1(x):
    return x * 3 + 1

print(m3p1(4))


# In[25]:


def halb(x):
    return x//2

print(halb(4))


# In[26]:


def ist_gerade(x):
    return x % 2 == 0

print(ist_gerade(5))
print(ist_gerade(6))


# In[27]:


x = 15
while x != 1:
    nachricht = str(x)
    if ist_gerade(x):
        nachricht += "/2 =>"
        x = halb(x)
    else:
        nachricht += "*3+1 =>"
        x = m3p1(x)
    print(nachricht)
print(x)


# In[28]:


def collatz(x): 
    """Eine Funktion für das Collatz-Problem oder die (3n+1) Vermutung, https://de.wikipedia.org/wiki/Collatz-Problem"""
    nachricht = ""
    while x != 1:
        nachricht += str(x) + ","
        if ist_gerade(x):
            x = halb(x)
        else:
            x = m3p1(x)
    nachricht += str(x)
    print(nachricht)
    
collatz(123456789)

