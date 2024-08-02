class User:

    def __init__(self, user_id,username):  # puoi aggiungere quanti parametri tu vuoi (parametri sono le parole dentro le parentesi)
        self.id = user_id
        self.username = username  # ha bisogno di un input per impostare il parametro
        self.followers = 0  # setta di default un valore senza il bisogno di aggiungerlo all'attribute come ID o Username
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "Carmelo")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# si chiama il metodo quando crei una funzione dentro un Oggetto (class)
