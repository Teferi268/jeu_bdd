"""
Décomposition :

-Lancement du jeu 
    -Message de bienvenue + règles 
    -Demander les inputs
        -Pseudo
        -Verifier si le pseudo valide
            -Chaine caractère
            -Entre 1 et 12 caractères
    -Choix des heroes
        -Présentation des differents heroes
            -Présentation sous la forme (    1 -> Nom_du_heroe - DGT:40 - PV:100 - DEF:10   )
        -Choix des heroes via l'input de chiffre
            -Verifier que les inputs corresponde bien à des heroes
            -Attribuer les heroes dans l'equipe du joueur
                -Ajout dans la bdd
            -Montrer l'équipe au joueur
            -Demander si il veut en changer
    -Lancement des manches
        BOUCLE
        -Choix du monstre aleatoire parmis la collection
        -Message pour montrer quel monstre on affronte
        -Affrontement de l'equipe et du montre
            -Choix random pour savoir qui commance
            -Attaque des heroes sur le monstre (dgt cumulé de tout les heroes)
            -Monstre subit les degats
                -Calcul avec la defense du monstre
                -Verification pour savoir si il est mort
                    -Si oui
                        -Incrémentation du nombre de vague
                        -prochaine manche
                    -Si non
                        -on continue
            -Monstre attaque les heroes (total des degat du montre divisé par le nombre de heroes en vie)
                -Calcul avec la defense du heroe
                -Verification pour savoir si des heroes sont morts
                    -Si oui
                        -Message de mort pour le heroes en question
                        -Supression du heroes de l'équipe
                    -Si non 
                        -on continue
        BOUCLE
    -Message de fin avec le nombre de vague vaincu + contre quel montre on est mort
-Fin du jeu
            



"""