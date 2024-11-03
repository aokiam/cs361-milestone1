# MILESTONE 1 USER STORIES:
# 1. find an artist's top songs
# 2. browse and get into the genre
# 3. finding a jpop arist based on my kpop tastes


class Artist:
    def __init__(self, name, pop, attributes, genres, top3, active, company, members, recommendations, more):
        self.name = name # artist name
        self.pop = pop # kpop or jpop
        self.attributes = attributes # genre attributes for matching
        self.genres = genres # genres of music the artist makes
        self.top3 = top3 # artist's top 3 songs
        self.active = active # years the artist is/was active
        self.company = company # record label company the artist is under
        self.members = members # members of the artist (if group or solo ortist)
        self.recommendations = recommendations # my personal song recommendations
        self.more = more # link to an outside source to learn more

class RecommendationSystem:
    def __init__(self):
        self.artists = []

    def add_artist(self, artist):
        # adds an artist to the list
        self.artists.append(artist)


    def recommend_by_genre(self, attributes):
        # recommend artist by a specific list of choosable attributes
        return [artist for artist in self.artists if artist.attributes == attributes]
    
recommendation_system = RecommendationSystem()

# list of kpop artists
kpop1 = Artist(name="aespa", pop="kpop", attributes=["hip hop", "electronic", "EDM"],
               genres=["electropop", "hyperpop", "dance pop", 'EDM'],top3=["Supernova", "Armageddon", "Drama"],
               active="2020 - Present",company="SM Entertainment", members=["Karina", "Giselle", "Winter", "Ningning"],
               recommendations=["Black Mamba", "Lucid Dream", "Whiplash"], more="https://kpop.fandom.com/wiki/Aespa")
kpop2 = Artist(name="G-(I)DLE", pop="kpop", attributes=["electronic", "hip hop", "r&b", "rap"],
               genres=["contemporary r&b", "hip hop", "pop rap", "pop rock"],top3=["Queencard", "Klaxon", "TOMBOY"],
               active="2018 - Present",company="Cube Entertainment", members=["Minnie", "Miyeon", "Soyeon", "Yuqi", "Shuhua", "Soojin (former)"],
               recommendations=["HWAA", "DAHLIA", "I burn"], more="https://kpop.fandom.com/wiki/(G)I-DLE")
kpop3 = Artist(name="ILLIT", pop="kpop", attributes=["bubblegum pop"],
               genres=["dance pop", "contemporary r&b"],top3=["Magnetic", "Cherish (My Love)", "Lucky Girl Syndrome"],
               active="2024 - Present", company="HYBE Corporation",members=["Moka", "Wonhee", "Minju", "Yunah", "Iroha"],
               recommendations=["I'll Like You", "Midnight Fiction", "SUPER REAL ME"], more="https://kpop.fandom.com/wiki/ILLIT")
kpop4 = Artist(name="ITZY", pop="kpop", attributes=["rock", "electronic", "EDM"],
               genres=["dance pop", "rap", "electropop", "EDM"],top3=["WANNABE", "UNTOUCHABLE", "LOCO"],
               active="2019 - Present",company="JYP Entertainment", members=["Yeji", "Ryujin", "Chaeryeong", "Lia", "Yuna"],
               recommendations=["DALLA DALLA", "Voltage", "KILL MY DOUBT"], more="https://kpop.fandom.com/wiki/ITZY")
kpop5 = Artist(name="IVE", pop="kpop", attributes=["bubblegum pop", "electronic", "r&b"],
               genres=["dance pop", "contemporary r&b", "electropop"],top3=["I AM", "After LIKE", "LOVE DIVE"],
               active="2021 - Present",company="Starship Entertainment", members=["Yujin", "Gaeul", "Rei", "Wonyoung", "Liz", "Lesseo"],
               recommendations=["ELEVEN", "I WANT", "I've IVE"], more="https://kpop.fandom.com/wiki/IVE")
kpop6 = Artist(name="KISS OF LIFE", pop="kpop", attributes=["hip hop", "ro&b"],
               genres=["hip hop", "contemporary r&b"],top3=["Sticky", "Midas Touch", "Sugarcoat (NATTY Solo)"],
               active="2023 - Present",company="S2 Entertainment",members=["Julie", "Belle", "Natty", "Haneul"],
               recommendations=["Get Loud", "Te Quiero", "Lose Yourself"], more="https://kpop.fandom.com/wiki/KISS_OF_LIFE")
kpop7 = Artist(name="LE SSERAFIM", pop="kpop", attributes=["electronic", "hip hop", "rock", "r&b"],
               genres=["dance pop", "contemporary r&b", "hip hop", "phonk"],top3=["CRAZY", "Perfect Night", "Smart"],
               active="2022 - Present", company="HYBE Corporation",members=["Chaewon", "Yunjin", "Sakura", "Kazuha", "Eunchae", "Garam (former)"],
               recommendations=["UNFORGIVEN", "Jewelry", "FEARLESS"], more="https://kpop.fandom.com/wiki/LE_SSERAFIM")
kpop8 = Artist(name="LOONA", pop="kpop", attributes=["bubblegum pop", "electronic", "r&b"],
               genres=["dance pop", "electropop", "contemporary r&b"],top3=["Heart Attack", "PTT", "Hi High"],
               active="2016 - 2022", company="Blockberry Creative",members=["HeeJin", "HyunJin", "HaSeul", "YeoJin", "ViVi", "Kim Lip", "JinSoul", "Choerry", "Yves", "Chuu", "Go Won", "Olivia Hye"],
               recommendations=["love4eva", "Love & Live", "Go Won"], more="https://kpop.fandom.com/wiki/LOONA")
kpop9 = Artist(name="NewJeans", pop="kpop", attributes=["bubblegum pop", "r&b"],
               genres=["contemporary r&b", "dance pop", "indie"],top3=["Super Shy", "Supernatural", "How Sweet"],
               active="2022 - Present", company="HYBE Corporation",members=["Haerin", "Danielle", "Minji", "Hanni", "Hyein"],
               recommendations=["Ditto", "Hype Boy", "NewJeans 2nd EP 'Get Up'"], more="https://kpop.fandom.com/wiki/NewJeans")
kpop10 = Artist(name="NMIXX", pop="kpop", attributes=["electronic", "hip hop"],
                genres=["dance pop", "pop rap", "hip hop"],top3=["Love Me Like This", "DASH", "DICE"],
                active="2022 - Present",company="JYP Entertainment",members=["Lily", "Haewon", "Sullyoon", "Bae", "Jiwoo", "Kyujin"],
                recommendations=["Party O'Clock", "Passionfruit", "Fe304: BREAK"], more="https://kpop.fandom.com/wiki/NMIXX")
kpop11 = Artist(name="Red Velvet", pop="kpop", attributes=["electronic", "r&b", "city pop"],
                genres=["dance pop", "contemporary r&b", "electropop"],top3=["Cosmic", "Psycho", "Russian Roulette"],
                active="2014 - Present", company="SM Entertainment",members=["Irene", "Seulgi", "Wendy", "Joy", "Yeri"],
                recommendations=["Bad Boy", "Last Drop", "Cosmic"], more="https://kpop.fandom.com/wiki/Red_Velvet")
kpop12 = Artist(name="STAYC", pop="kpop", attributes=["bubblegum pop", "electronic", "r&b"],
                genres=["dance pop", "electropop", "contemporary r&b"],top3=["ASAP", "Stereotype", "RUN2U"],
                active="2020 - Present",company="High Up Entertainment", members=["Sumin", "Sieun", "Isa", "Seeun", "Yoon", "J"],
                recommendations=["SO BAD", "POPPY (Japanese Ver.)", "YOUNG-LUV.COM"], more="https://kpop.fandom.com/wiki/STAYC")
kpop13 = Artist(name="TWICE", pop="kpop", attributes=["bubblegum pop", "electronic", "city pop", "EDM"],
                genres=["dance pop", "bubblegum pop", "electropop"],top3=["What is Love?", "The Feels", "FANCY"],
                active="2015 - Present",company="JYP Entertainment", members=["Nayeon", "Jeongyeon", "Momo", "Sana", "Jihyo", "Mina", "Dahyun", "Chaeyoung", "Tzuyu"],
                recommendations=["I CAN'T STOP ME", "LOVE FOOLISJ", "Formula of Love: O+T=<3"], more="https://kpop.fandom.com/wiki/TWICE")

#list of jpop artists
jpop1 = Artist(name="Ado", pop="jpop", attributes=["rock", "city pop", "electronic", "hip hop"],
               genres=["pop rock", "power pop", "jazz pop", "yakousei", "shimokita-kei"],top3=["Show", "Usseewa", "New Genesis"], 
               active="2020 - Present", company="Geffen Records",members=["Ado"], 
               recommendations=["Sakura Biyori and Time Machine with Hatsune Miku", "Value", "Zanmu"], more="https://utaite.fandom.com/wiki/Ado")
jpop2 = Artist(name="ATARASHII GAKKO!", pop="jpop", attributes=["rock", "EDM", "electronic"],
               genres=["pop rock", "jazz rock", "jazz pop", "shimokita-kei"],top3=["OTTONABLUE", "Tokyo Calling", "Fly High"], 
               active="2015 - Present", company="88rising",members=["Suzuka", "Rei", "Kanon", "Miju"], 
               recommendations=["JANAINDAYO", "The Edge", "AG! Callling"], more="https://jpop.fandom.com/wiki/Atarashii_Gakkou_no_Leaders")
jpop3 = Artist(name="Eve", pop="jpop", attributes=["rock", "electronic"],
               genres=["yakousei", "pop rock", "shimokita-kei", "indie"],top3=["Kaikai Kitan", "Dramaturgy", "Fightsong"], 
               active="2009 - Present", company="Toy's Factor",members=["Eve"], 
               recommendations=["Bokurano", "Taikutsuwo Saienshinaide", "Kaizin"], more="https://jpop.fandom.com/wiki/Eve_(Singer-songwriter)")
jpop4 = Artist(name="Fujii Kaze", pop="jpop", attributes=["rock", "r&b", "city pop"],
               genres=["contemporary r&b", "pop soul", "acoustic rock"],top3=["Shinunoga E-Wa", "Kirari", "Matsuri"], 
               active="2010 - Present", company="HEHN Records",members=["Fujii Kaze"], 
               recommendations=["Hana", "Kiri Ga Naikara", "HELP EVER HURT NEVER"], more="https://jpop.fandom.com/wiki/Fujii_Kaze")
jpop5 = Artist(name="Kenshi Yonezu", pop="jpop", attributes=["rock"],
               genres=["alternative rock", "shimokita-kei", "pop rock"],top3=["KICK BACK", "Gatakuta - JUNK", "Sayounara Mataitsuka! - Sayonara"], 
               active="2009 - Present", company="SME Records",members=["Kenshi Yonezu"], 
               recommendations=["LOSER", "Eine Kleine", "YANKEE"], more="https://jpop.fandom.com/wiki/Yonezu_Kenshi")
jpop6 = Artist(name="mafumafu", pop="jpop", attributes=["rock"],
               genres=["shimokita-kei", "pop rock"],top3=["takt", "1 • 2 • 3", "Onnanoko Ni Naritai"], 
               active="2010 - Present", company="A-Sketch",members=["mafumafu"], 
               recommendations=["I wanna be a girl", "Tosenbo", "Kagurairo Artifact"], more="https://utaite.fandom.com/wiki/Mafumafu")
jpop7 = Artist(name="nqrse", pop="jpop", attributes=["rock", "electronic"],
               genres=["rap", "rock"],top3=["ULTRA C", "CR ANTHEM", "Utakata no yoru"], 
               active="2013 - Present", company="StudioLama",members=["nqrse"], 
               recommendations=["KING", "Roki", "Diorama"], more="https://utaite.fandom.com/wiki/Nqrse")
jpop8 = Artist(name="Reol", pop="jpop", attributes=["EDM", "electronic", "hip hop"],
               genres=["electropop", "pop rap", "shimokita-kei", "Japanese hip hop"],top3=["The Sixth Sense", "No title", "drop pop candy"], 
               active="2012 - Present", company="Victor Entertainment",members=["Reol"], 
               recommendations=["LUVORATORRRRRY!", "Saisaki", "No title-"], more="https://utaite.fandom.com/wiki/Reol")
jpop9 = Artist(name="soraru", pop="jpop", attributes=["electronic", "rock"],
               genres=["electropop", "pop rock"],top3=["1 • 2 • 3", "World Domination", "Papeki Hero"], 
               active="2008 - Present", company="Virgin Music",members=["soraru"], 
               recommendations=["Yurayura", "Jailbreak","Soraru no Utattemita [2011-2012]"], more="https://utaite.fandom.com/wiki/Soraru")
jpop10 = Artist(name="takayan", pop="jpop", attributes=["hip hop"],
               genres=["Japanese hip hop", "pop rap"],top3=["Bad example", "Toy", "It's okay to envy"], 
               active="2015 - Present", company="Hentai Gorizal Records",members=["takayan"], 
               recommendations=["What's the meaning of living", "Persecution complex", "Happiness and correct answer"], more="https://jpop.fandom.com/wiki/Takayan")
jpop11 = Artist(name="Tuyu", pop="jpop", attributes=["rock", "bubblegum pop"],
               genres=["yakousei", "power pop", "shimokita-kei", "pop rock", "new rave"],
               top3=["I'm getting on the bus to the other world, see ya!", "Compared Child", "Being as low as dirt, taking what's important from me"], 
               active="2019 - 2024", company="PONY CANYON",members=["Pusu", "Rei", "miro"], 
               recommendations=["What If This Isn't A Slave?", "If There Was An Endpoint.", "I'll put you in misery"], more="https://jpop.fandom.com/wiki/TUYU")
jpop12 = Artist(name="Vaundy", pop="jpop", attributes=["city pop", "r&b"],
               genres=["shimokita-kei", "indie pop", "alt-pop", "pop rock"],top3=["Kaiju no Kanauta", "Odoriko", "Time Paradox"], 
               active="2019 - Present", company="SDR",members=["Vaundy"], 
               recommendations=["Tokyo Flash","okitegami" "strobo"], more="https://jpop.fandom.com/wiki/Vaundy")
jpop13 = Artist(name="Yorushika", pop="jpop", attributes=["r&b"],
               genres=["yakousei", "pop rock", "indie rock", "shimokita-kei", "indie pop"],top3=["Tada Kimi ni Hare", "Yu Sansan", "Hareru"], 
               active="2017 - Present", company="Universal Music Japan",members=["n-buna", "suis"], 
               recommendations=["Dakara Boku Wa Ongaku Wo Yameta", "Itte", "Natsukusa ga Jyama wo Suru"], more="https://jpop.fandom.com/wiki/Yorushika")

