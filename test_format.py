import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk

darkest_purps = "#362B3D"
dark_purps = "#3F334B"
darker_purps = "#675379"
purps = "#9B7DB6"
light_purps = "#B79ECD"

title = "Mabook"
body = "QuicksandBook-Regular"


# Initialize the customtkinter theme and appearance mode
ctk.set_appearance_mode("dark")  # Options: "System", "Dark", "Light"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("KJ Recommendation Station")

        self.frames = {}
        for F in (MainPage, ComparisonPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Sidebar(ctk.CTkFrame):
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
        self.home_button = ctk.CTkButton(self.sidebar_frame, image=self.go_home, text="Home",
                                         fg_color="transparent", hover_color=dark_purps, font=(body, 15))
        self.home_button.pack(pady=20, padx=10)
        
        self.rec_button = ctk.CTkButton(self.sidebar_frame, image=self.letter_k, text="Find K-Pop",
                                        fg_color="transparent", hover_color=dark_purps, font=(body, 15))
        self.rec_button.pack(pady=20, padx=10)
        
        self.comp_button = ctk.CTkButton(self.sidebar_frame, image=self.letter_j, text="Find J-Pop",
                                         fg_color="transparent", hover_color=dark_purps, font=(body, 15))
        self.comp_button.pack(pady=20, padx=10)
        
        self.about_button = ctk.CTkButton(self.sidebar_frame, image=self.compare_artists, text="Compare Artists",
                                          fg_color="transparent", hover_color=dark_purps, font=(body, 15))
        self.about_button.pack(pady=20, padx=10)
        
        self.about_button = ctk.CTkButton(self.sidebar_frame, image=self.artist_info, text="About the Artists",
                                          fg_color="transparent", hover_color=dark_purps, font=(body, 15))
        self.about_button.pack(pady=20, padx=10)

        self.spacer2 = ctk.CTkLabel(self.sidebar_frame, text="").pack(pady=40)

        # Create a container frame for different pages
        self.container_frame = ctk.CTkScrollableFrame(self, width=990, height=650, scrollbar_button_color=dark_purps)
        self.container_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)



class MainPage(Sidebar):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        back = Image.open("./assets/back.png").resize((15,15))
        self.backtrack = ImageTk.PhotoImage(back)

        self.back = ctk.CTkButton(self.container_frame, image=self.backtrack, text="BACK", fg_color="transparent",
                                  hover_color=dark_purps, font=(title, 15), width=60, corner_radius=30).grid(row=0, column=0, sticky="nw", padx=10, pady=15)
        
        # COMPARISON RESULTS PAGE -------------------------------------------------------------------------------------------------------------------------
        heart = Image.open("./assets/heart.png").resize((26,26))
        self.heart = ImageTk.PhotoImage(heart) 
        ctk.CTkLabel(self.container_frame, text="COMPARE ARTISTS", font=(title, 70), justify="center").grid(row=1, column=0,
                     columnspan=3, padx=185, pady=20)
        ctk.CTkLabel(self.container_frame, text="", image=self.heart, justify="center").grid(row=2, columnspan=3, pady=50)
        
        self.artist1 = "Name: TWICE\n\nPop: k-pop\n\nTop 3 Songs: What is Love?, The Feels, FANCY\n\nGenre Attributes: bubblegum pop, electronic, city pop, EDM"
        self.artist2 = "Name: Ado\n\nPop: j-pop\n\nTop 3 Songs: Show, Usseewa, New Genesis\n\nGenre Attributes: rock, city pop, electronic, hip hop"

        self.artist1_window = ctk.CTkFrame(self.container_frame, fg_color=darkest_purps, border_color=dark_purps, border_width=5,
                                           corner_radius=20, width=400, height=270)
        self.artist1_window.grid(row=3, column=0, padx=25, pady=20, sticky="nsew")
        self.artist1_window.grid_propagate(False)
        ctk.CTkLabel(self.container_frame, text="VS.", font=(title, 40), justify="center").grid(row=3, column=1)
        self.artist2_window = ctk.CTkFrame(self.container_frame, fg_color=darkest_purps, border_color=dark_purps, border_width=5,
                                           corner_radius=20, width=400, height=270)
        self.artist2_window.grid(row=3, column=2, padx=25, pady=20, sticky="nsew")
        self.artist2_window.grid_propagate(False)

        artist1_label = ctk.CTkLabel(self.artist1_window, text=self.artist1, wraplength=350, font=(body, 20), justify="left")
        artist1_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        artist2_label = ctk.CTkLabel(self.artist2_window, text=self.artist2, wraplength=300, font=(body, 20), justify="left")
        artist2_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        '''
        # COMPARISON PAGE ---------------------------------------------------------------------------------------------------------------------------------
        heart = Image.open("./assets/heart.png").resize((26,26))
        self.heart = ImageTk.PhotoImage(heart) 
        sun = Image.open("./assets/sun.png").resize((26,26))
        self.sun = ImageTk.PhotoImage(sun)  
        moon = Image.open("./assets/night.png").resize((26,26))
        self.moon = ImageTk.PhotoImage(moon)  
        shuffle = Image.open("./assets/shuffle.png").resize((20,20))
        self.shuffle = ImageTk.PhotoImage(shuffle)
        ctk.CTkLabel(self.container_frame, text="COMPARE ARTISTS", font=(title, 70), justify="center").grid(row=1, column=0,
                     columnspan=2, padx=185, pady=20)
        ctk.CTkLabel(self.container_frame, text="Want to see a quick comparison of two artists?\nPick two and compare!", justify="center",
                     font=(body, 18), wraplength=700).grid(row=2, column=0, columnspan=2, padx=200)
        ctk.CTkLabel(self.container_frame, text="", image=self.heart, justify="center").grid(row=3, columnspan=2, pady=50)

        # dropdown menus
        self.colored_row = ctk.CTkFrame(self.container_frame, fg_color=darkest_purps)
        self.colored_row.grid(row=4, column=0,columnspan=2, sticky="nsew")
        ctk.CTkLabel(self.colored_row, image=self.sun, text="  Select First Artist  ", compound="left",
                    font=(body, 23), anchor="center").grid(row=0, column=0, pady=10,padx=112, sticky="nsew")
        ctk.CTkLabel(self.colored_row, image=self.moon, text="  Select Second Artist  ", compound="right",
                    font=(body, 23), anchor="center").grid(row=0, column=1, pady=10,padx=112, sticky="nsew")
        
        ctk.CTkComboBox(self.container_frame, values=['Twice', 'Ado', 'VIVINOS', 'ATARASHII GAKKO!'], fg_color=purps, border_color=light_purps, button_color=light_purps,
                        dropdown_fg_color=purps, dropdown_hover_color=dark_purps, corner_radius=30, font=(title, 20),
                        dropdown_font=(body, 15), width=260).grid(row=5, column=0, pady=20)
        ctk.CTkComboBox(self.container_frame, values=['Twice', 'Ado', 'VIVINOS', 'ATARASHII GAKKO!'], fg_color=purps, border_color=light_purps, button_color=light_purps,
                        dropdown_fg_color=purps, dropdown_hover_color=dark_purps, corner_radius=30, font=(title, 20),
                        dropdown_font=(body, 15), width=260).grid(row=5, column=1, pady=20)


        ctk.CTkButton(self.container_frame, text="Face-Off! ", image=self.shuffle, compound="right", fg_color=purps, hover_color=light_purps,
                      corner_radius=60, height=40, width=15, font=(body, 20)).grid(row=6, columnspan=2, pady=30)

        # RECOMMENDAION PAGES ----------------------------------------------------------------------------------------------

        sparkle = Image.open("./assets/sparkle.png").resize((26,26))
        self.sparkle = ImageTk.PhotoImage(sparkle)
        heart = Image.open("./assets/heart.png").resize((26,26))
        self.heart = ImageTk.PhotoImage(heart)   
        next_page = Image.open("./assets/next.png").resize((20, 20))
        self.next = ImageTk.PhotoImage(next_page)   

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
        
        ctk.CTkComboBox(self.container_frame, values=['Twice', 'Ado', 'VIVINOS', 'ATARASHII GAKKO!'], fg_color=purps, border_color=light_purps, button_color=light_purps,
                        dropdown_fg_color=purps, dropdown_hover_color=dark_purps, corner_radius=30, font=(title, 20),
                        dropdown_font=(body, 15), width=260).grid(row=5, column=0, columnspan=2, pady=20)
        
        ctk.CTkButton(self.container_frame, text="Tune In! ", image=self.next, compound="right", fg_color=purps, hover_color=light_purps,
                      corner_radius=60, height=40, width=15, font=(body, 20)).grid(row=6, columnspan=2, pady=20)
        
        ctk.CTkButton(self.container_frame, text="mafumafu", border_width=1, border_spacing=10,fg_color="transparent", font=(body, 20),
                      hover_color=darkest_purps).grid(row=7, column=0, columnspan=2, padx=10, pady=20)

        
           
        # MAIN PAGE -----------------------------------------------------------------------------------------------
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
'''

class ComparisonPage(Sidebar):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        

if __name__ == "__main__":
    app = App()
    app.geometry("1235x700")
    app.mainloop()


'''
class Dashboard(ctk.CTk):
    def __inti__(self):
        super().__init__()

        self.grid_columnconfigure(0,weight=0)
        self.grid_rowconfigure((0,1), weight=1)

        self.sidebar_frame = ctk.CTk(self, width=200, fg_color=yellow)
        self.sidebar_frame.

        self.button = ctk.CTkButton(self.frame, text="=", width=70, font=("winkle", 40), hover_color=pink, fg_color=pink_orange, corner_radius=0, command=self.expand_side_bar)
        self.button.place(relx=1, rely=0, anchor="ne")

        self.text = ctk.CTkLabel(self, text="Hello, World!", font=(body, 40))
        self.text.place(x=100, y=50)

    def expand_side_bar(self):
        if self.frame["width"] != 500:
            self.frame.configure(width=500)
            return
        self.frame.configure(width=70)
#position for top middle 
CTkLabel(master=app, text="KJ Station", font=(title, 70)).place(relx=0.5, rely=0.13, anchor="center")
CTkLabel(master=app, text="Want to get into kpop or jpop? Enter your music preferences and find your music match! Find a list of included artists here! (not yet implemented)\n\nResponse time could take up to 5 seconds!!",wraplength=800, justify="center", font=(body, 20)).place(relx=0.5, rely=0.3, anchor="center")


app.mainloop()
'''