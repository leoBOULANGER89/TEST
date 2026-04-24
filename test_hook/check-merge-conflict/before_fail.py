# Test check-merge-conflict - File with conflict markers
# Intentional errors: <<<<<<<, =======, >>>>>>> markers

def ma_fonction():
    resultat = "base"

<<<<<<< HEAD
    resultat = "feature"
=======
    resultat = "fix"
>>>>>>> fix-branch

    return resultat
