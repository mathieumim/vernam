import streamlit as st
st.header('Chiffre de César')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','0','1','2','3','4','5','6','7','8','9','@','é','è','ê','à','ç',' ','.',',','-','?','!',"'"]
messagecode1 = []
messagecode2 = []

code = st.text_input('Saisissez un chiffre entre 0 et 26 : ',0)
if int(code) > 26:
    code = st.text_input('Saisissez un chiffre entre 0 et 26 : ',0)
code = int(code)

message = st.text_input('Tapez votre message sans apostrophe : ')

listmessage = []
for letters in message:
    listmessage.append(str(letters))

alphacode = alphabet[code:len(alphabet)] + alphabet[0:code]

for i in range(0,len(message)):
    messagecode1.append(alphacode.index(listmessage[i]))
    i += 1

for i in range(0,len(message)):
    messagecode2.append(alphabet[messagecode1[i]])
    i += 1

final = ''.join(messagecode2)
st.write('Votre code est ',final)


# Là c'est le décodage

messagecode1 = []
messagecode2 = []
messagecode3 = []

code = st.text_input('Saisissez la clé comprise entre 0 et 26 : ',0)
if int(code) > 26:
    code = st.text_input('Saisissez la clé comprise entre 0 et 26 : ',0)
code = int(code)

message = st.text_input('Copiez votre message codé : ')

listmessage = []
for letters in message:
    listmessage.append (str(letters))

alphacode = alphabet[code:len(alphabet)] + alphabet[0:code]

for i in range (0,len(message)):
    messagecode1.append(alphabet.index(listmessage[i]))
    i += 1

for i in range (0,len(message)):
    messagecode3.append(int(messagecode1[i]))
    i += 1

for i in range (0,len(message)):
    messagecode2.append(alphacode[messagecode3[i]])
    i += 1

final = ''.join(messagecode2)
st.write("Votre message est ",final)

st.sidebar.text_input('Salut les amis')