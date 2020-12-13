# PenduPY

lien github : https://github.com/Malkrich/PenduPY

Le mode console est fonctionnel

Après le travail de ce week-end (12-13 décembre), voicie les fonctionnalités implémentées dans le programme pendu_interface :
	- Possibilité de jouer avec détection d'une défaite ou d'une victoire
	- Enregistrement et affichage du score du joueur sur un fichier texte (score = nombre de mot.s trouvés)
	- Possibilité de recommencer le jeux
	- Ajout d'une bar de menu dans laquelle se trouve :
		- Un bouton quitter le jeux
		- Un bouton de mise à jour de la liste de mots

Problèmes rencontrés :
J'ai essayé de faire changer l'image sur le canvas (voir le commentaire entres " dans la fonction macro_jouer()), mais le canvas m'affichait sans cesse un fond blanc.
Je n'ai pas réussi à corriger ce problème même en essayant de voir l'exemple du cours sur le changement d'image .gif. J'ai aussi ajouté le tableau permettant de référencer le chemin d'accés de chaque images (voir table_images[...]).
