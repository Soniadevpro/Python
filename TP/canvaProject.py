import tkinter as tk
from PIL import Image, ImageTk  # Utiliser Pillow pour gérer les images .jpg

# Créer une fenêtre principale
root = tk.Tk()
root.title("Cadre Principal")
root.geometry("600x400")  # Dimensions de la fenêtre

# Cadre principal
main_frame = tk.Frame(root, bg="lightgray", bd=2, relief="solid")
main_frame.pack(expand=True, fill="both", padx=10, pady=10)

# Cadre des boutons
button_frame = tk.Frame(main_frame, bg="blue", bd=2, relief="solid")
button_frame.pack(side="top", fill="x", padx=10, pady=10)
button_frame.config(width=600, height=50)

# Cadre des images
image_frame = tk.Frame(main_frame, bg="yellow", bd=2, relief="solid")
image_frame.pack(side="top", expand=True, fill="both", padx=10, pady=10)
image_frame.config(width=600, height=300)

# Fonction pour afficher l'image
def afficher_image():
    try:
        img1 = Image.open("C:/Users/sonia/Desktop/Python/TP/image1.jpg")  # Chemin de l'image
        img1 = img1.resize((150, 150))  # Redimensionner si nécessaire
        img_tk = ImageTk.PhotoImage(img1)

        # Ajouter l'image dans un Label
        label1 = tk.Label(image_frame, image=img_tk)
        label1.image = img_tk  # Conserver une référence pour éviter la suppression
        label1.place(relx=0.5, rely=0.5, anchor="center")  # Centrer l'image
    except Exception as e:
        print("Erreur lors du chargement de l'image :", e)
        placeholder = tk.Label(image_frame, text="Impossible de charger l'image", bg="white", fg="red")
        placeholder.pack()

# Ajout du bouton avec la fonction de callback
button1 = tk.Button(button_frame, text="Afficher le poney", bg="red", fg="white", command=afficher_image)
button1.pack(side="left", padx=50, pady=10)

# Lancer la boucle principale
root.mainloop()
