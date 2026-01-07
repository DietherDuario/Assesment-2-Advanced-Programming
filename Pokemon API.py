import tkinter as tk
from tkinter import messagebox
import requests




class PokeAPI:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

    def get_pokemon(self, identifier):
        """
        Fetch Pokémon data from the API.
        identifier can be a name or ID.
        """
        url = self.BASE_URL + str(identifier).lower()
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return None





class Pokemon:
    def __init__(self, data):
        self.name = data["name"].capitalize()
        self.height = data["height"]
        self.weight = data["weight"]
        self.abilities = self.extract_abilities(data)
        self.stats = self.extract_stats(data)

    def extract_abilities(self, data):
        return [ability["ability"]["name"] for ability in data["abilities"]]

    def extract_stats(self, data):
        stats = {}
        for stat in data["stats"]:
            stats[stat["stat"]["name"]] = stat["base_stat"]
        return stats




class PokemonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon Explorer")
        self.root.geometry("400x500")

        self.api = PokeAPI()

        self.create_widgets()

    def create_widgets(self):
     
        tk.Label(self.root, text="Pokémon Explorer", font=("Arial", 18, "bold")).pack(pady=10)

       
        tk.Label(self.root, text="Enter Pokémon Name or ID:").pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

      
        tk.Button(self.root, text="Search", command=self.search_pokemon).pack(pady=10)

     
        self.output = tk.Text(self.root, height=20, width=45)
        self.output.pack(pady=10)

    def search_pokemon(self):
        identifier = self.entry.get().strip()

        if not identifier:
            messagebox.showwarning("Input Error", "Please enter a Pokémon name or ID.")
            return

        data = self.api.get_pokemon(identifier)

        if data is None:
            messagebox.showerror("Not Found", "Pokémon not found.")
            return

        pokemon = Pokemon(data)
        self.display_pokemon(pokemon)

    def display_pokemon(self, pokemon):
        self.output.delete("1.0", tk.END)

        self.output.insert(tk.END, f"Name: {pokemon.name}\n")
        self.output.insert(tk.END, f"Height: {pokemon.height}\n")
        self.output.insert(tk.END, f"Weight: {pokemon.weight}\n\n")

        self.output.insert(tk.END, "Abilities:\n")
        for ability in pokemon.abilities:
            self.output.insert(tk.END, f" - {ability}\n")

        self.output.insert(tk.END, "\nStats:\n")
        for stat, value in pokemon.stats.items():
            self.output.insert(tk.END, f" - {stat}: {value}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonApp(root)
    root.mainloop()