# MILESTONE 1 USER STORIES:
# 1. find a kpop artist based on my jpop tastes
# 2. compare two artists and see a summary of both artists
# 3. finding a jpop arist based on my kpop tastes

import json
import random
import tkinter as tk
import customtkinter as ctk
from customtkinter import *
from PIL import Image, ImageTk
from communication.http_service import get_jpop_from_kpop, get_kpop_from_jpop, get_comparison

ctk.set_appearance_mode("dark")
darkest_purps = "#362B3D"
dark_purps = "#3F334B"
darker_purps = "#675379"
purps = "#9B7DB6"
light_purps = "#B79ECD"

title = "Mabook"
body = "QuicksandBook-Regular"

def load_artist_info():
    with open('data/artist_info.json') as f:
        return json.load(f)
    
def load_kpop_artists(artist_data):
    return [artist for artist in artist_data['artists'] if 'k-pop' in artist.get('pop')]

def load_jpop_artists(artist_data):
    return [artist for artist in artist_data['artists'] if 'j-pop' in artist.get('pop')]

def load_artist_names():
    with open('data/artist_info.json') as f:
        data = json.load(f)
    return [artist['name'] for artist in data['artists']]

class RecommendationStation(ctk.CTk):
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
    

class BasePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller=controller
        # import icons ------------------------------------------------------------
        music_notes = Image.open("./assets/music-note.png").resize((100,100))
        self.photo_music = ImageTk.PhotoImage(music_notes)
        home = Image.open("./assets/home.png").resize((15,15))
        self.go_home = ImageTk.PhotoImage(home)
        information = Image.open("./assets/information.png").resize((15,15))
        self.artist_info = ImageTk.PhotoImage(information)
        j_rec = Image.open("./assets/letter-j.png").resize((15,15))
        self.letter_j = ImageTk.PhotoImage(j_rec)
        k_rec = Image.open("./assets/letter-k.png").resize((15,15))
        self.letter_k = ImageTk.PhotoImage(k_rec)
        comaprison = Image.open("./assets/compare.png").resize((15,15))
        self.compare_artists = ImageTk.PhotoImage(comaprison)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar Frame --------------------------------------------------------------------------------
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=10, fg_color=darkest_purps)
        self.sidebar_frame.grid(row=0, column=0, sticky="nswe")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.spacer = ctk.CTkLabel(self.sidebar_frame, text="",image=self.photo_music)
        self.spacer.pack(pady=80, padx=20)

        # Create navigation buttons on the sidebar --------------------------------------------------------
        self.home_button = ctk.CTkButton(self.sidebar_frame, image=self.go_home, text="Home",command=lambda: controller.show_frame("MainPage"),
                                         fg_color="transparent", hover_color=dark_purps, font=(body, 15))
        self.home_button.pack(pady=20, padx=10)
        
        self.rec_button = ctk.CTkButton(self.sidebar_frame, image=self.letter_k, text="Find K-Pop",command=lambda: controller.show_frame("KpopRecPage"),
                                        fg_color="transparent", hover_color=dark_purps, font=(body, 15))
        self.rec_button.pack(pady=20, padx=10)
        
        self.comp_button = ctk.CTkButton(self.sidebar_frame, image=self.letter_j, text="Find J-Pop",command=lambda: controller.show_frame("JpopRecPage"),
                                         fg_color="transparent", hover_color=dark_purps, font=(body, 15))
        self.comp_button.pack(pady=20, padx=10)
        
        self.about_button = ctk.CTkButton(self.sidebar_frame, image=self.compare_artists, text="Compare Artists",command=lambda: controller.show_frame("ComparisonPage"),
                                          fg_color="transparent", hover_color=dark_purps, font=(body, 15))
        self.about_button.pack(pady=20, padx=10)
        
        self.about_button = ctk.CTkButton(self.sidebar_frame, image=self.artist_info, text="About the Artists",
                                          fg_color="transparent", hover_color=dark_purps, font=(body, 15))
        self.about_button.pack(pady=20, padx=10)

        self.spacer2 = ctk.CTkLabel(self.sidebar_frame, text="").pack(pady=40)

        # Create a container frame for different pages
        self.container_frame = ctk.CTkScrollableFrame(self, width=990, height=650, scrollbar_button_color=dark_purps)
        self.container_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)


class MainPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        self.spacer = ctk.CTkLabel(self.container_frame, text="").grid(row=0, column=0, pady=10)
        
        self.main_1 = ctk.CTkLabel(self.container_frame, text="KJ STATION", font=(title, 70), justify="center")
        self.main_1.place(x=240, y=80)
        
        self.main_2 = ctk.CTkLabel(self.container_frame, text="Want to get into kpop or jpop? Enter yout music preferences and find your music match! Find a list of included artists here! (not yet implemented)\n\nResponse time could take up to 5 seconds!!",
                  justify="center", wraplength=700, font=(body, 18))
        self.main_2.place(x=100, y=190)

        self.spacer = ctk.CTkLabel(self.container_frame, text="").grid(row=1, column=0, pady=200)


        lsfm = Image.open("./assets/lesserafim-icon.png").resize((140,140))
        self.lsfm_icon = ImageTk.PhotoImage(lsfm)
        tuyu = Image.open("./assets/tuyu-icon.png").resize((100,100))
        self.tuyu_icon = ImageTk.PhotoImage(tuyu)
        ado = Image.open("./assets/ado-icon.png").resize((100,100))
        self.ado_icon = ImageTk.PhotoImage(ado)
        twice = Image.open("./assets/twice-icon.png").resize((100,100))
        self.twice_icon = ImageTk.PhotoImage(twice)
        kiof = Image.open("./assets/kissoflife-icon.png").resize((160,160))
        self.kiof_icon = ImageTk.PhotoImage(kiof)
        
        self.spacer_lsfm = ctk.CTkLabel(self.container_frame, text="", image=self.lsfm_icon).place(x=80, y=310)
        self.spacer_tuyu = ctk.CTkLabel(self.container_frame, text="", image=self.tuyu_icon).place(x=260, y=325)
        self.spacer_ado = ctk.CTkLabel(self.container_frame, text="", image=self.ado_icon).place(x=390, y=325)
        self.spacer_twice = ctk.CTkLabel(self.container_frame, text="", image=self.twice_icon).place(x=530, y=330)
        self.spacer_kiof = ctk.CTkLabel(self.container_frame, text="", image=self.kiof_icon).place(x=680, y=300)

        ctk.CTkButton(self.container_frame, text="Compare Artists", command=lambda: controller.show_frame("ComparisonPage"),
                      fg_color=purps, hover_color=light_purps, font=(body, 17), corner_radius=60, height=60).grid(row=3, column=2,padx=50, pady=10)
        ctk.CTkButton(self.container_frame, text="Get K-pop\nRecommendation", command=lambda: controller.show_frame("KpopRecPage"),
                      fg_color=purps, hover_color=light_purps, font=(body, 17), corner_radius=60, height=60).grid(row=3, column=3, padx=50, pady=10)
        ctk.CTkButton(self.container_frame, text="Get J-pop\nRecommendation", command=lambda: controller.show_frame("JpopRecPage"),
                      fg_color=purps, hover_color=light_purps, font=(body, 17), corner_radius=60, height=60).grid(row=3, column=4, padx=50, pady=10)


class ComparisonPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        back = Image.open("./assets/back.png").resize((15,15))
        self.backtrack = ImageTk.PhotoImage(back)
        heart = Image.open("./assets/heart.png").resize((26,26))
        self.heart = ImageTk.PhotoImage(heart) 
        sun = Image.open("./assets/sun.png").resize((26,26))
        self.sun = ImageTk.PhotoImage(sun)  
        moon = Image.open("./assets/night.png").resize((26,26))
        self.moon = ImageTk.PhotoImage(moon)  
        shuffle = Image.open("./assets/shuffle.png").resize((20,20))
        self.shuffle = ImageTk.PhotoImage(shuffle)

        self.back = ctk.CTkButton(self.container_frame, image=self.backtrack, text="BACK", fg_color="transparent", command=lambda: controller.show_frame("MainPage"),
                                  hover_color=dark_purps, font=(title, 15), width=60, corner_radius=30).grid(row=0, column=0, sticky="nw", padx=10, pady=15)

        ctk.CTkLabel(self.container_frame, text="COMPARE ARTISTS", font=(title, 70), justify="center").grid(row=1, column=0,
                     columnspan=2, padx=185, pady=20)
        ctk.CTkLabel(self.container_frame, text="Want to see a quick comparison of two artists?\nPick two and compare!", justify="center",
                     font=(body, 18), wraplength=700).grid(row=2, column=0, columnspan=2, padx=200)
        ctk.CTkLabel(self.container_frame, text="", image=self.heart, justify="center").grid(row=3, columnspan=2, pady=50)

        #dropdowns for selecting artists to compare
        self.colored_row = ctk.CTkFrame(self.container_frame, fg_color=darkest_purps)
        self.colored_row.grid(row=4, column=0,columnspan=2, sticky="nsew")
        ctk.CTkLabel(self.colored_row, image=self.sun, text="  Select First Artist  ", compound="left",
                    font=(body, 23), anchor="center").grid(row=0, column=0, pady=10,padx=112, sticky="nsew")
        ctk.CTkLabel(self.colored_row, image=self.moon, text="  Select Second Artist  ", compound="right",
                    font=(body, 23), anchor="center").grid(row=0, column=1, pady=10,padx=112, sticky="nsew")
        
        self.artist1=ctk.CTkComboBox(self.container_frame, values=controller.artist_names, state="readonly",
                        fg_color=purps, border_color=light_purps, button_color=light_purps,
                        dropdown_fg_color=purps, dropdown_hover_color=dark_purps, corner_radius=30, font=(title, 20),
                        dropdown_font=(body, 15), width=260)
        self.artist1.grid(row=5, column=0, pady=20)
        self.artist2=ctk.CTkComboBox(self.container_frame, values=controller.artist_names, state="readonly",
                        fg_color=purps, border_color=light_purps, button_color=light_purps,
                        dropdown_fg_color=purps, dropdown_hover_color=dark_purps, corner_radius=30, font=(title, 20),
                        dropdown_font=(body, 15), width=260)
        self.artist2.grid(row=5, column=1, pady=20)

        ctk.CTkButton(self.container_frame, text="Face-Off! ", command=self.show_comparison, image=self.shuffle, compound="right", fg_color=purps, hover_color=light_purps,
                      corner_radius=60, height=40, width=15, font=(body, 20)).grid(row=6, columnspan=2, pady=30)


    def show_comparison(self):
        artist1=self.artist1.get()
        artist2=self.artist2.get()

        comparison = get_comparison(artist1, artist2)

        self.controller.frames["ComparisonResultPage"].set_comparison_data(comparison)
        self.controller.show_frame("ComparisonResultPage")


class ComparisonResultPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        back = Image.open("./assets/back.png").resize((15,15))
        self.backtrack = ImageTk.PhotoImage(back)
        heart = Image.open("./assets/heart.png").resize((26,26))
        self.heart = ImageTk.PhotoImage(heart) 

        self.back = ctk.CTkButton(self.container_frame, image=self.backtrack, text="BACK", fg_color="transparent", command=lambda: controller.show_frame("ComparisonPage"),
                                  hover_color=dark_purps, font=(title, 15), width=60, corner_radius=30).grid(row=0, column=0, sticky="nw", padx=10, pady=15)


        ctk.CTkLabel(self.container_frame, text="COMPARE ARTISTS", font=(title, 70), justify="center").grid(row=1, column=0,
                     columnspan=3, padx=200, pady=20)
        ctk.CTkLabel(self.container_frame, text="", image=self.heart, justify="center").grid(row=2, columnspan=3, pady=50)

        self.artist1_window = ctk.CTkFrame(self.container_frame, fg_color=darkest_purps, border_color=dark_purps, border_width=5,
                                           corner_radius=20, width=400, height=300)
        self.artist1_window.grid(row=3, column=0, padx=25, pady=20, sticky="nsew")
        self.artist1_window.grid_propagate(False)
        ctk.CTkLabel(self.container_frame, text="VS.", font=(title, 40), justify="center").grid(row=3, column=1)
        self.artist2_window = ctk.CTkFrame(self.container_frame, fg_color=darkest_purps, border_color=dark_purps, border_width=5,
                                           corner_radius=20, width=400, height=300)
        self.artist2_window.grid(row=3, column=2, padx=25, pady=20, sticky="nsew")
        self.artist2_window.grid_propagate(False)

        # label to show the comparison result
        self.artist1 = ctk.CTkLabel(self.artist1_window, text="", wraplength=350, font=(body, 20), justify="left")
        self.artist1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        self.artist2 = ctk.CTkLabel(self.artist2_window, text="" ,wraplength=350, font=(body, 20), justify="left")
        self.artist2.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    def set_comparison_data(self, comparison):
        if 'message' in comparison:
            self.artist1.configure(text=comparison['message'])
            self.artist2.configure(text="")
        else:
            artist1_info = f"Name: {comparison[0]['name']}\n\nPop: {comparison[0]['pop']}\n\nTop 3 Songs: {', '.join(comparison[0]['top3'])}\n\nGenre Attributes: {', '.join(comparison[0]['attributes'])}"
            artist2_info = f"Name: {comparison[1]['name']}\n\nPop: {comparison[1]['pop']}\n\nTop 3 Songs: {', '.join(comparison[1]['top3'])}\n\nGenre Attributes: {', '.join(comparison[1]['attributes'])}"

            self.artist1.configure(text=artist1_info)
            self.artist2.configure(text=artist2_info)

class JpopRecPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        sparkle = Image.open("./assets/sparkle.png").resize((26,26))
        self.sparkle = ImageTk.PhotoImage(sparkle)
        heart = Image.open("./assets/heart.png").resize((26,26))
        self.heart = ImageTk.PhotoImage(heart)   
        next_page = Image.open("./assets/next.png").resize((20, 20))
        self.next = ImageTk.PhotoImage(next_page)   
        back = Image.open("./assets/back.png").resize((15,15))
        self.backtrack = ImageTk.PhotoImage(back)

        self.back = ctk.CTkButton(self.container_frame, image=self.backtrack, text="BACK", fg_color="transparent", command=lambda: controller.show_frame("MainPage"),
                                  hover_color=dark_purps, font=(title, 15), width=60, corner_radius=30).grid(row=0, column=0, sticky="nw", padx=10, pady=15)

        ctk.CTkLabel(self.container_frame, text="FIND YOUR J-POP MATCH", font=(title, 70), justify="center").grid(row=1,  column=0,
                    columnspan=2, padx=60,pady=20)
        ctk.CTkLabel(self.container_frame, text="New to j-pop? Find a k-pop group you like and we will find you a match!", justify="center",
                    font=(body, 18), wraplength=700).grid(row=2, column=0, padx=100, columnspan=2)
        ctk.CTkLabel(self.container_frame, text="", image=self.heart, justify="center").grid(row=3, columnspan=2, pady=50)

        # dropdown for selecting kpop artist
        self.colored_row = ctk.CTkFrame(self.container_frame, fg_color=darkest_purps)
        self.colored_row.grid(row=4, column=0,columnspan=1, sticky="nsew")
        ctk.CTkLabel(self.colored_row, image=self.sparkle, text="  Select a K-pop Artist  ", compound="right",
                    font=(body, 23), anchor="center").grid(row=0, column=0, pady=10,padx=350, sticky="nsew")
        # Filter the list of artist names to include only those with "kpop" in their "pop" attribute


        self.artist = ctk.CTkComboBox(self.container_frame, values=[artist['name'] for artist in self.controller.kpop_artists], state="readonly",
                                        fg_color=purps, border_color=light_purps, button_color=light_purps, dropdown_fg_color=purps, dropdown_hover_color=dark_purps, corner_radius=30,
                                        font=(title, 20), dropdown_font=(body, 15), width=260)
        self.artist.grid(row=5, column=0, columnspan=2, pady=20)

        #button to show recommendation result
        ctk.CTkButton(self.container_frame, text="Tune In! ", image=self.next, compound="right", fg_color=purps, hover_color=light_purps,
                      corner_radius=60, height=40, width=15, font=(body, 20), command=self.show_recommendation).grid(row=6, columnspan=2, pady=20)


        #label to show recommendation result
        self.recommendation_text = ctk.CTkLabel(self.container_frame, text="", font=(body, 20))
        self.recommendation_text.grid(row=7, column=0, columnspan=2, padx=10, pady=20)


    def show_recommendation(self):
        selcted_artist = self.artist.get()
        recommendation = get_jpop_from_kpop(selcted_artist)

        if recommendation:
            recommended_jpop = random.choice(recommendation)
            self.recommendation_text.configure(text=f"Recommended J-pop Artist: {recommended_jpop['name']}")
        else:
            self.recommendation_text.configure(text="No Jpop artist with a matching attribute.")

class KpopRecPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

        back = Image.open("./assets/back.png").resize((15,15))
        self.backtrack = ImageTk.PhotoImage(back)
        sparkle = Image.open("./assets/sparkle.png").resize((26,26))
        self.sparkle = ImageTk.PhotoImage(sparkle)
        heart = Image.open("./assets/heart.png").resize((26,26))
        self.heart = ImageTk.PhotoImage(heart)   
        next_page = Image.open("./assets/next.png").resize((20, 20))
        self.next = ImageTk.PhotoImage(next_page)   

        self.back = ctk.CTkButton(self.container_frame, image=self.backtrack, text="BACK", fg_color="transparent",command=lambda: controller.show_frame("MainPage"),
                                  hover_color=dark_purps, font=(title, 15), width=60, corner_radius=30).grid(row=0, column=0, sticky="nw", padx=10, pady=15)

        ctk.CTkLabel(self.container_frame, text="FIND YOUR K-POP MATCH", font=(title, 70), justify="center").grid(row=1,  column=0,
                    columnspan=2, padx=60,pady=20)
        ctk.CTkLabel(self.container_frame, text="New to k-pop? Find a j-pop group you like and we will find you a match!", justify="center",
                    font=(body, 18), wraplength=700).grid(row=2, column=0, padx=100, columnspan=2)
        ctk.CTkLabel(self.container_frame, text="", image=self.heart, justify="center").grid(row=3, columnspan=2, pady=50)

        # dropdown for selecting kpop artist
        self.colored_row = ctk.CTkFrame(self.container_frame, fg_color=darkest_purps)
        self.colored_row.grid(row=4, column=0,columnspan=1, sticky="nsew")
        ctk.CTkLabel(self.colored_row, image=self.sparkle, text="  Select a J-pop Artist  ", compound="right",
                    font=(body, 23), anchor="center").grid(row=0, column=0, pady=10,padx=350, sticky="nsew")


        self.artist = ctk.CTkComboBox(self.container_frame, values=[artist['name'] for artist in self.controller.jpop_artists], state="readonly",
                        fg_color=purps, border_color=light_purps, button_color=light_purps, dropdown_fg_color=purps, dropdown_hover_color=dark_purps, corner_radius=30,
                        font=(title, 20), dropdown_font=(body, 15), width=260)
        self.artist.grid(row=5, column=0, columnspan=2, pady=20)


        #button to show recommendation result
        ctk.CTkButton(self.container_frame, text="Tune In! ", image=self.next, compound="right", fg_color=purps, hover_color=light_purps,
                      corner_radius=60, height=40, width=15, font=(body, 20), command=self.show_recommendation).grid(row=6, columnspan=2, pady=20)

        #label to show recommendation result
        self.recommendation_text = ctk.CTkLabel(self.container_frame, text="", font=(body, 20))
        self.recommendation_text.grid(row=7, column=0, columnspan=2, padx=10, pady=20)


    def show_recommendation(self):
        selcted_artist = self.artist.get()
        recommendation = get_kpop_from_jpop(selcted_artist)

        if recommendation:
            recommended_kpop = random.choice(recommendation)
            self.recommendation_text.configure(text=f"Recommended K-pop Artist: {recommended_kpop['name']}")
        else:
            self.recommendation_text.configure(test="No K-pop artist with a matching attribute.") 


if __name__ == '__main__':
    app = RecommendationStation()
    app.geometry("1235x700")
    app.mainloop()
