mdp = input("Entrer votre mot de passe (min 8 caracteres): ")
mdp_trop_court = "votre mot de passe est trop court."
if len(mdp) == 0:
    print("Vous n'avez pas entré de mot de passe.".upper())
elif len(mdp) < 8:
    print(mdp_trop_court.capitalize())
elif mdp.isdigit():
    print("Votre mot de passe ne contient que des chiffres.")
elif mdp.isalpha():
    print("Votre mot de passe ne contient que des lettres.")
else:
    print("Votre mot de passe est valide.")