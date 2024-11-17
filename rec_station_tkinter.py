# MILESTONE 1 USER STORIES:
# 1. find a kpop artist based on my jpop tastes
# 2. compare two artists and see a summary of both artists
# 3. finding a jpop arist based on my kpop tastes

import json
import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from communication.http_service import get_jpop_from_kpop, get_kpop_from_jpop, get_comparison

def load_artist_info():
    with open('data/artist_info.json') as f:
        return json.load(f)
    
def load_kpop_artists(artist_data):
    return [artist for artist in artist_data['artists'] if 'kpop' in artist.get('pop')]

def load_jpop_artists(artist_data):
    return [artist for artist in artist_data['artists'] if 'jpop' in artist.get('pop')]

def load_artist_names():
    with open('data/artist_info.json') as f:
        data = json.load(f)
    return [artist['name'] for artist in data['artists']]

class RecommendationStation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("KJ Recommendation Station")
        self.artist_names = load_artist_names()
        artist_data = load_artist_info()
        self.kpop_artists = load_kpop_artists(artist_data)
        self.jpop_artists = load_jpop_artists(artist_data)


        self.frames = {}
        for F in (MainPage, ComparisonPage, ComparisonResultPage, KpopRecPage, JpopRecPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
    
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        ttk.Label(self, text="KJ STATION", font=100).grid(row=1, column=0, padx=100, pady=10)
        ttk.Label(self, text="Want to get into kpop or jpop? Enter yout music preferences and find your music match!\nFind a list of included artists here! (not yet implemented)\n\nResponse time could take up to 5 seconds!!",
                  justify="center").grid(row=2, column=0, padx=40, pady=10)

        ttk.Button(self, text="Compare Artists", command=lambda: controller.show_frame("ComparisonPage")).grid(row=3 ,column=0, padx=50, pady=10)
        ttk.Button(self, text="Get K-pop Recommendation", command=lambda: controller.show_frame("KpopRecPage")).grid(row=4 ,column=0, padx=50, pady=10)
        ttk.Button(self, text="Get J-pop Recommendation", command=lambda: controller.show_frame("JpopRecPage")).grid(row=5 ,column=0, padx=50, pady=10)


class ComparisonPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.artist_var1 = tk.StringVar()
        self.artist_var2 = tk.StringVar()

        ttk.Label(self, text="COMPARE ARTISTS", font=100).grid(row=2,  column=0, columnspan=2, pady=10)
        ttk.Label(self, text="Want to see a brief synopsis about two artists side-by-side?\nPick two artists and compare!", justify="center").grid(row=3, column=0, columnspan=2, padx=100, pady=10)

        #dropdowns for selecting artists to compare
        ttk.Label(self, text="Select First Artist", justify="left").grid(row=4, column=0, pady=5)
        ttk.Label(self, text="Select Second Artist",justify="left").grid(row=5, column=0, pady=5)

        self.dropdown1 = ttk.Combobox(self, textvariable=self.artist_var1, values=controller.artist_names, state="readonly")
        self.dropdown2 = ttk.Combobox(self, textvariable=self.artist_var2, values=controller.artist_names, state="readonly")
        self.dropdown1.grid(row=4, column=1)
        self.dropdown2.grid(row=5, column=1)

        ttk.Button(self, text="Compare", command=self.show_comparison).grid(row=6, column=0, columnspan=2)

        #back button
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage")).grid(row=7, column=0, columnspan=2, pady=10)


    def show_comparison(self):
        artist1=self.artist_var1.get()
        artist2=self.artist_var2.get()

        comparison = get_comparison(artist1, artist2)

        self.controller.frames["ComparisonResultPage"].set_comparison_data(comparison)
        self.controller.show_frame("ComparisonResultPage")


class ComparisonResultPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.comparison_text = tk.StringVar()

        ttk.Label(self, text="COMPARE ARTISTS", font=100, justify="center").grid(row=0,  column=0, columnspan=2, pady=10)

        # label to show the comparison result
        self.label = ttk.Label(self, textvariable=self.comparison_text, wraplength=400)
        self.label.grid(row=1, column=0, padx=10, pady=10)

        #back button
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("ComparisonPage")).grid(row=2, column=0, pady=10)

    def set_comparison_data(self, comparison):
        if 'message' in comparison:
            self.comparison_text.set(comparison['message'])
        else:
            comparison_text = "\n\n".join([
                f"Name: {artist['name']}\nPop: {artist['pop']}\nTop 3 Songs: {', '.join(artist['top3'])}\nAttributes: {', '.join(artist['attributes'])}"
                for artist in comparison
            ])
            self.comparison_text.set(comparison_text)


class JpopRecPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.artist_var = tk.StringVar()
        self.recommendation_text = tk.StringVar()


        ttk.Label(self, text="FIND YOUR JPOP MATCH", font=100).grid(row=0,  column=0, columnspan=2, pady=10)
        ttk.Label(self, text="New to jpop? Find a kpop group you like and we will find you a match!", justify="center").grid(row=1, column=0, columnspan=2, padx=100, pady=10)

        # dropdown for selecting kpop artist
        ttk.Label(self, text="Select a K-pop Artist").grid(row=2, column=0, pady=5)
        self.dropdown = ttk.Combobox(self, textvariable=self.artist_var, values=[artist['name'] for artist in self.controller.kpop_artists], state="readonly")
        self.dropdown.grid(row=2, column=1)

        #button to show recommendation result
        ttk.Button(self, text="Get Recommendation", command=self.show_recommendation).grid(row=3, column=0, columnspan=2)

        #back button
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage")).grid(row=4, column=0, columnspan=2, pady=10)

        #label to show recommendation result
        ttk.Label(self, textvariable=self.recommendation_text, wraplength=400).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def show_recommendation(self):
        selcted_artist = self.artist_var.get()
        recommendation = get_jpop_from_kpop(selcted_artist)

        if recommendation:
            recommended_jpop = random.choice(recommendation)
            self.recommendation_text.set(f"Recommended J-pop Artist(s): {recommended_jpop['name']}")
        else:
            self.recommendation_text.set("No Jpop artist with a matching attribute.")

class KpopRecPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.artist_var = tk.StringVar()
        self.recommendation_text = tk.StringVar()

        ttk.Label(self, text="FIND YOUR KPOP MATCH", font=100).grid(row=0,  column=0, columnspan=2, pady=10)
        ttk.Label(self, text="New to kpop? Find a jpop group you like and we will find you a match!", justify="center").grid(row=1, column=0, columnspan=2, padx=100, pady=10)

        # dropdown for selecting kpop artist
        ttk.Label(self, text="Select a J-pop Artist").grid(row=2, column=0, pady=5)
        self.dropdown = ttk.Combobox(self, textvariable=self.artist_var, values=[artist['name'] for artist in self.controller.jpop_artists], state="readonly")
        self.dropdown.grid(row=2, column=1)

        #button to show recommendation result
        ttk.Button(self, text="Get Recommendation", command=self.show_recommendation).grid(row=3, column=0, columnspan=2)
        
        #back button
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage")).grid(row=4, column=0, columnspan=2, pady=10)

        #label to show recommendation result
        ttk.Label(self, textvariable=self.recommendation_text, wraplength=400).grid(row=5, column=0, columnspan=2, padx=10, pady=10)


    def show_recommendation(self):
        selcted_artist = self.artist_var.get()
        recommendation = get_kpop_from_jpop(selcted_artist)

        if recommendation:
            recommended_kpop = random.choice(recommendation)
            self.recommendation_text.set(f"Recommended K-pop Artist(s): {recommended_kpop['name']}")
        else:
            self.recommendation_text.set("No K-pop artist with a matching attribute.")


if __name__ == '__main__':
    app = RecommendationStation()
    app.geometry("600x400")
    app.mainloop()