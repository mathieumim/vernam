import streamlit as st
import numpy as np
import pandas as pd
import SessionState
session_state = SessionState.get(name="", button_sent=False, startkey = False)


### METTRE UN TEST DE NORMALITE DE LA CLE EN PLACE + SUPPRIMER LE COMMENCER LA CLE A 2 QUAND Y A PAS DE CLE + Remplacer tapez votre message par tapez votre message ou votre message codé
#GERER BUG CALCUL DE CLE DECODAGE

# Titre du programme

st.header("Vernam")

# Alphabet utilisé par le programme ou liste des caractères
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z","0","1","2","3","4","5","6","7","8","9","@","é","è","ê","à","ç"," ",".",",","-","?","!","'",":","(",")"]

# Constantes
## Longueur maximum de la clé
LENCLE = 10000
KEY = 0

# Outil de génération de clé
generationcle = st.sidebar.radio("Gestion de votre clé",["Charger","Générer"],key = KEY)

if generationcle == "Générer":

	st.title("Génération d'une clé")
	cle = list(np.random.randint(0,len(alphabet), size = LENCLE))
	st.text_area("",str(cle))

	filename = st.text_input("Nom du fichier","cle")
	## Ici %s veut dire qu'on a pas encore le contenu de la string mais remplace par le % qui suit
	if st.button("Sauvegarder la clé"):
		session_state.button_sent = True
		f = open("%s.txt" %filename,"w")
		f.write(str(cle)[1:-1])
		f.close()

	if session_state.button_sent:

		# Choix de la partie de clé à travailler
		st.title("Choix de la partie de clé à travailler")

		message = st.text_input("Tapez votre message : ","")
		a = int(st.text_input("A partir de quel endroit commencer l'utilisation de la clé (la première valeur est 0) ? ",0))

		listmessage = list(message)
		    
		cletrav = []
		for i in range(a,len(listmessage)+a+1):
		    cletrav.append(cle[i])


		c = a + len(listmessage) + 2

		# Bouton choix du programme
		choixprogram = st.sidebar.selectbox("Selectionnez ce que vous souhaitez faire",["","Encodage","Décodage"])
		
		if choixprogram == "":
			st.write("")

		elif choixprogram == "Encodage":

		# Encodage
			st.title("Texte encodé")

			messagenum = []
			for i in range (0,len(message)):
			    messagenum.append(alphabet.index(listmessage[i]))
			    i += 1
			    
			messagecode = []
			for i in range (0,len(messagenum)):
			    messagecode.append(messagenum[i]+cletrav[i])
			    i += 1

			messagecodemod = []
			for i in range(0,len(messagecode)):
			    messagecodemod.append(messagecode[i]%len(alphabet))
			    i += 1

			messagecodelettre = []
			for i in range(0,len(messagecodemod)):
			    messagecodelettre.append(alphabet[messagecodemod[i]])
			    i += 1

			final = "".join(messagecodelettre)
			st.write(final)
			st.write("Vous recommencerez à partir de la valeur n° "+ str(c) + " incluse.")

		elif choixprogram == "Décodage":

		# Décodage
			st.title("Texte décodé")
			messageadecoder = st.text_input('Copiez votre message codé : ')

			listmessageadecoder = []
			for letters in messageadecoder:
			    listmessageadecoder.append (str(letters))

			messagenum2 = []
			for i in range (0,len(messageadecoder)):
			    messagenum2.append(alphabet.index(listmessageadecoder[i]))
			    i += 1

			cletrav2 = []
			for i in range(a,len(listmessageadecoder)+a+1):
				cletrav2.append(cle[i])

			messagedecode = []
			for i in range (0,len(messagenum2)):
			    messagedecode.append(messagenum2[i]-cletrav2[i])
			    i += 1

			for i in range (0,len(messagedecode)):
			    if messagedecode[i] < 0:
			        while messagedecode[i] <0:
			            messagedecode[i] = messagedecode[i] + len(alphabet)

			messageclair = []
			for i in range (0,len(messagedecode)):
			    messageclair.append(alphabet[messagedecode[i]])
			    i += 1

			final = "".join(messageclair)
			st.write(final)
			st.write("Si vous devez répondre à ce message commencez à utiliser la clé à partir de la valeur n° "+ str(len(listmessageadecoder)) + " incluse.")


else:

	# Insertion de la clé
	st.title("Charger une clé")
	cle = st.text_input("Copiez-collez la clé à utiliser et validez par ENTER",0)
	cle = cle.split(",")
	for i in range(0,len(cle)):
		cle[i] = int(cle[i])


	# Choix de la partie de clé à travailler
	
	if cle != [0]:
		st.title("Choix de la partie de clé à travailler")

		message = st.text_input("Tapez votre message : ","")
		a = int(st.slider("A partir de quel endroit commencer l'utilisation de la clé (la première valeur est 0) ? ",0,LENCLE-len(message),0))

		listmessage = list(message)
		    
		cletrav = []
		for i in range(a,len(listmessage)+a+1):
		    cletrav.append(cle[i])


		c = a + len(listmessage) + 2

		# Bouton choix du programme
		choixprogram = st.sidebar.selectbox("Selectionnez ce que vous souhaitez faire",["","Encodage","Décodage"])
		
		if choixprogram == "":
			st.write("")

		elif choixprogram == "Encodage":

		# Encodage
			st.title("Texte encodé")

			messagenum = []
			for i in range (0,len(message)):
			    messagenum.append(alphabet.index(listmessage[i]))
			    i += 1
			    
			messagecode = []
			for i in range (0,len(messagenum)):
			    messagecode.append(messagenum[i]+cletrav[i])
			    i += 1

			messagecodemod = []
			for i in range(0,len(messagecode)):
			    messagecodemod.append(messagecode[i]%len(alphabet))
			    i += 1

			messagecodelettre = []
			for i in range(0,len(messagecodemod)):
			    messagecodelettre.append(alphabet[messagecodemod[i]])
			    i += 1

			final = "".join(messagecodelettre)
			st.write(final)
			st.write("Vous recommencerez à partir de la valeur n° "+ str(c) + " incluse.")

		elif choixprogram == "Décodage":

		# Décodage
			st.title("Texte décodé")
			messageadecoder = st.text_input('Copiez votre message codé : ')

			listmessageadecoder = []
			for letters in messageadecoder:
			    listmessageadecoder.append (str(letters))

			messagenum2 = []
			for i in range (0,len(messageadecoder)):
			    messagenum2.append(alphabet.index(listmessageadecoder[i]))
			    i += 1

			cletrav2 = []
			for i in range(a,len(listmessageadecoder)+a+1):
				cletrav2.append(cle[i])

			messagedecode = []
			for i in range (0,len(messagenum2)):
			    messagedecode.append(messagenum2[i]-cletrav2[i])
			    i += 1

			for i in range (0,len(messagedecode)):
			    if messagedecode[i] < 0:
			        while messagedecode[i] <0:
			            messagedecode[i] = messagedecode[i] + len(alphabet)

			messageclair = []
			for i in range (0,len(messagedecode)):
			    messageclair.append(alphabet[messagedecode[i]])
			    i += 1

			final = "".join(messageclair)
			st.write(final)
			st.write("Si vous devez répondre à ce message commencez à utiliser la clé à partir de la valeur n° "+ str(len(listmessageadecoder)) + " incluse.")



# Bouton affichage d'informations complémentaires

infocompl = st.sidebar.selectbox("Afficher les informations de travail",["Non","Oui"])
if infocompl == "Oui":

# Informations sur les données travaillées

	st.title("Informations sur les données travaillées")
	st.write('Votre alphabet est composé de ' + str(len(alphabet)) + ' valeurs.')
	st.text_area("",alphabet)
	if choixprogram ==  "Encodage":
		st.write('La partie de clé travaillée est composé des valeurs :')
		st.text_area("",str(cletrav)[1:-1])
		st.write("Cela représente " + str(len(cletrav)) + " valeurs")
	elif choixprogram == "Décodage":
		st.write('La partie de clé travaillée est composé des valeurs :')
		st.text_area("",str(cletrav2)[1:-1])
		st.write("Cela représente " + str(a + len(cletrav2) + 2) + " valeurs")
	else:
		st.write("")

	from PIL import Image
	image = Image.open("Joseph_Mauborgne.jpg")
	st.sidebar.image(image, caption="Gilbert Vernam 1890-1960",width = 150)
