# MILESTONE 1 USER STORIES:
# 1. find a kpop artist based on my jpop tastes
# 2. compare two artists and see a summary of both artists
# 3. finding a jpop arist based on my kpop tastes

import json
import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from communication.http_service import get_jpop_from_kpop, get_kpop_from_jpop, get_comparison, get_info
import requests  # aya
from PIL import Image, ImageTk # aya


def load_artist_info():
    with open('data/artist_info.json') as f:
        return json.load(f)


# aya - MILESTONE (not calling program directly)
def get_artist_details(artist_name):
    print(f"Requesting details for artist: {artist_name}")  # logging
    response = requests.get(f'http://localhost:5004/artist_details', params={'name': artist_name})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error response: {response.text}")  # log error
        return None


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
        for F in (MainPage, ComparisonPage, ComparisonResultPage, KpopRecPage, JpopRecPage, ArtistDetailsPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainPage")

    # aya
    def show_artist_details(self, artist_name):
        print(f"Loading details for artist: {artist_name}")
        artist_data = get_artist_details(artist_name)
        if artist_data:
            self.frames["ArtistDetailsPage"].set_artist_data(artist_data)
            self.show_frame("ArtistDetailsPage")
        else:
            messagebox.showerror("Error", "Artist not found.")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="KJ STATION", font=100).grid(row=1, column=0, padx=100, pady=10)
        ttk.Label(self,
                  text="Want to get into kpop or jpop? Enter yout music preferences and find your music match!\n"
                       "Find a list of included artists here! (not yet implemented)",
                  justify="center").grid(row=2, column=0, padx=40, pady=10)

        (ttk.Button(self, text="Compare Artists", command=lambda: controller.show_frame("ComparisonPage"))
         .grid(row=3,column=0,padx=50, pady=20))
        (ttk.Button(self, text="Get K-pop Recommendation", command=lambda: controller.show_frame("KpopRecPage"))
         .grid(row=4, column=0, padx=50, pady=20))
        (ttk.Button(self, text="Get J-pop Recommendation", command=lambda: controller.show_frame("JpopRecPage"))
         .grid(row=5, column=0, padx=50, pady=20))


class ComparisonPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.artist_var1 = tk.StringVar()
        self.artist_var2 = tk.StringVar()

        ttk.Label(self, text="COMPARE ARTISTS", font=100).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Label(self, text="Want to see a brief synopsis about two artists side-by-side?\nPick two artists "
                             "and compare!", justify="center").grid(row=3, column=0, columnspan=2, padx=100, pady=10)

        # dropdowns for selecting artists to compare
        ttk.Label(self, text="Select First Artist", justify="left").grid(row=4, column=0, pady=5)
        ttk.Label(self, text="Select Second Artist", justify="left").grid(row=5, column=0, pady=5)

        self.dropdown1 = ttk.Combobox(self, textvariable=self.artist_var1, values=controller.artist_names,
                                      state="readonly")
        self.dropdown2 = ttk.Combobox(self, textvariable=self.artist_var2, values=controller.artist_names,
                                      state="readonly")
        self.dropdown1.grid(row=4, column=1)
        self.dropdown2.grid(row=5, column=1)

        ttk.Button(self, text="Compare", command=self.show_comparison).grid(row=6, column=0, columnspan=2)

        # back button
        (ttk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage"))
         .grid(row=7, column=0,columnspan=2, pady=10))

    def show_comparison(self):
        artist1 = self.artist_var1.get()
        artist2 = self.artist_var2.get()

        comparison = get_comparison(artist1, artist2)

        self.controller.frames["ComparisonResultPage"].set_comparison_data(comparison)
        self.controller.show_frame("ComparisonResultPage")


class ComparisonResultPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.comparison_text = tk.StringVar()

        ttk.Label(self, text="COMPARE ARTISTS", font=100, justify="center").grid(row=0, column=0, columnspan=2, pady=10)

        # label to show the comparison result
        self.label = ttk.Label(self, textvariable=self.comparison_text, wraplength=400)
        self.label.grid(row=1, column=0, padx=10, pady=10)

        # back button
        (ttk.Button(self, text="Back", command=lambda: controller.show_frame("ComparisonPage")).
         grid(row=2, column=0,pady=10))

    def set_comparison_data(self, comparison):
        if 'message' in comparison:
            self.comparison_text.set(comparison['message'])
        else:
            comparison_text = "\n\n".join([
                f"Name: {artist['name']}\nPop: {artist['pop']}\nTop 3 Songs: "
                f"{', '.join(artist['top3'])}\nAttributes: {', '.join(artist['attributes'])}"
                for artist in comparison
            ])
            self.comparison_text.set(comparison_text)


class JpopRecPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.artist_var = tk.StringVar()
        self.recommendation_text = tk.StringVar()

        ttk.Label(self, text="FIND YOUR JPOP MATCH", font=100).grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(self, text="New to jpop? Find a kpop group you like and we will find you a match!",
                  justify="center").grid(row=1, column=0, columnspan=2, padx=100, pady=10)

        # dropdown for selecting kpop artist
        ttk.Label(self, text="Select a K-pop Artist").grid(row=2, column=0, pady=5)
        self.dropdown = ttk.Combobox(self, textvariable=self.artist_var,
                                     values=[artist['name'] for artist in self.controller.kpop_artists],
                                     state="readonly")
        self.dropdown.grid(row=2, column=1)

        # button to show recommendation result
        (ttk.Button(self, text="Get Recommendation", command=self.show_recommendation)
         .grid(row=3, column=0, columnspan=2))

        # back button
        (ttk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage"))
         .grid(row=4, column=0, columnspan=2, pady=10))

        # label to show recommendation result
        (ttk.Label(self, textvariable=self.recommendation_text, wraplength=400)
         .grid(row=5, column=0, columnspan=2, padx=10, pady=10))

        # aya - show details button; initially hidden
        self.view_details_button = ttk.Button(self, text="View Details",
                                              command=lambda: controller.show_artist_details(self.artist_var.get()))
        self.view_details_button.grid(row=6, column=0, columnspan=2)
        self.view_details_button.grid_remove()

    def show_recommendation(self):
        selcted_artist = self.artist_var.get()
        recommendation = get_jpop_from_kpop(selcted_artist)

        if recommendation:
            recommended_jpop = random.choice(recommendation)
            self.recommendation_text.set(f"Recommended J-pop Artist(s): {recommended_jpop['name']}")
            # aya - show info button
            self.view_details_button.config(
                command=lambda: self.controller.show_artist_details(recommended_jpop['name']))
            self.view_details_button.grid()
        else:
            self.recommendation_text.set("No Jpop artist with a matching attribute.")


class KpopRecPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.artist_var = tk.StringVar()
        self.recommendation_text = tk.StringVar()

        ttk.Label(self, text="FIND YOUR KPOP MATCH", font=100).grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(self, text="New to kpop? Find a jpop group you like and we will find you a match!",
                  justify="center").grid(row=1, column=0, columnspan=2, padx=100, pady=10)

        # dropdown for selecting kpop artist
        ttk.Label(self, text="Select a J-pop Artist").grid(row=2, column=0, pady=5)
        self.dropdown = ttk.Combobox(self, textvariable=self.artist_var,
                                     values=[artist['name'] for artist in self.controller.jpop_artists],
                                     state="readonly")
        self.dropdown.grid(row=2, column=1)

        # button to show recommendation result
        ttk.Button(self, text="Get Recommendation", command=self.show_recommendation).grid(row=3, column=0,
                                                                                           columnspan=2)

        # back button
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage")).grid(row=4, column=0,
                                                                                              columnspan=2, pady=10)

        # label to show recommendation result
        ttk.Label(self, textvariable=self.recommendation_text, wraplength=400).grid(row=5, column=0, columnspan=2,
                                                                                    padx=10, pady=10)
        # aya - show details button; initially hidden
        self.view_details_button = ttk.Button(self, text="View Details",
                                              command=lambda: controller.show_artist_details(self.artist_var.get()))
        self.view_details_button.grid(row=6, column=0, columnspan=2)
        self.view_details_button.grid_remove()

    def show_recommendation(self):
        selcted_artist = self.artist_var.get()
        recommendation = get_kpop_from_jpop(selcted_artist)

        if recommendation:
            recommended_kpop = random.choice(recommendation)
            self.recommendation_text.set(f"Recommended K-pop Artist(s): {recommended_kpop['name']}")
            # aya - display info button
            self.view_details_button.config(
                command=lambda: self.controller.show_artist_details(recommended_kpop['name']))
            self.view_details_button.grid()
        else:
            self.recommendation_text.set("No K-pop artist with a matching attribute.")


# aya yaaaaaa
class ArtistDetailsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # ui
        self.artist_image_label = ttk.Label(self)
        self.artist_image_label.grid(row=0, column=0, rowspan=5, padx=10, pady=10, sticky='n')

        self.artist_name_label = ttk.Label(self, text="", font=("Helvetica", 16, "bold"))
        self.artist_name_label.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.top_songs_label = ttk.Label(self, text="", wraplength=400, justify="left")
        self.top_songs_label.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        self.years_active_label = ttk.Label(self, text="", wraplength=400, justify="left")
        self.years_active_label.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        self.attributes_label = ttk.Label(self, text="", wraplength=400, justify="left")
        self.attributes_label.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        self.members_label = ttk.Label(self, text="", wraplength=400, justify="left")
        self.members_label.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        ttk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage")).grid(row=5, column=0, columnspan=2, pady=20)

    def set_artist_data(self, artist_data):
        # set artist name
        self.artist_name_label.config(text=artist_data.get("name", "Unknown Artist"))

        # set artist top 3 songs
        self.top_songs_label.config(text="Top 3 Songs:\n " + ", ".join(artist_data.get("top3", [])))

        # attributes
        self.attributes_label.config(text="Attributes:\n " + ", ".join(artist_data.get("attributes", [])))

        years_active = artist_data.get("years_active", "Unknown Years Active")
        self.years_active_label.config(text=f"Years Active:\n {years_active}")

        self.members_label.config(text="Members:\n " + ", ".join(artist_data["members"]))

        self.load_artist_img(artist_data.get("name", ""))

    def load_artist_img(self, artist_name):
        try:
            image_path = f"data/pics/{artist_name}.jpg"
            img = Image.open(image_path)
            img = img.resize((250, 250), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.artist_image_label.config(image=photo)
            self.artist_image_label.image = photo
        except FileNotFoundError:
            self.artist_image_label.config(image="", text="No Image Available")


if __name__ == '__main__':
    app = RecommendationStation()
    app.geometry("600x400")
    app.mainloop()
