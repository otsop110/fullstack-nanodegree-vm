import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///filmgenrecatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()


user1 = User(name="Test User", email="test_user@gmail.com")


category1 = Category(name="Action")
category2 = Category(name="Adventure")
category3 = Category(name="Animation")
category4 = Category(name="Biography")
category5 = Category(name="Comedy")
category6 = Category(name="Crime")
category7 = Category(name="Documentary")
category8 = Category(name="Drama")
category9 = Category(name="Family")
category10 = Category(name="Fantasy")
category11 = Category(name="Film-Noir")
category12 = Category(name="History")
category13 = Category(name="Horror")
category14 = Category(name="Music")
category15 = Category(name="Musical")
category16 = Category(name="Mystery")
category17 = Category(name="Romance")
category18 = Category(name="Sci-fi")
category19 = Category(name="Sport")
category20 = Category(name="Thriller")
category21 = Category(name="War")
category22 = Category(name="Western")


db_session.add(category1)
db_session.add(category2)
db_session.add(category3)
db_session.add(category4)
db_session.add(category5)
db_session.add(category6)
db_session.add(category7)
db_session.add(category8)
db_session.add(category9)
db_session.add(category10)
db_session.add(category11)
db_session.add(category12)
db_session.add(category13)
db_session.add(category14)
db_session.add(category15)
db_session.add(category16)
db_session.add(category17)
db_session.add(category18)
db_session.add(category19)
db_session.add(category20)
db_session.add(category21)
db_session.add(category22)
db_session.commit()

item1 = Item(name="Spider-Man: Homecoming (2017)",
             description="Peter Parker tries to balance his life as an "
             "ordinary high school student in Queens with his superhero "
             "alter-ego Spider-Man, and must confront a new menace prowling "
             "the skies of New York City.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category1,
             user=user1)

item2 = Item(name="Valerian and the City of a Thousand Planets (2017)",
             description="A dark force threatens Alpha, a vast metropolis "
             "and home to species from a thousand planets. Special operatives "
             "Valerian and Laureline must race to identify the marauding "
             "menace and safeguard not just Alpha, but the future of the "
             "universe.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category1,
             user=user1)

item3 = Item(name="Wonder Woman (2017)",
             description="Before she was Wonder Woman, she was Diana, "
             "princess of the Amazons, trained warrior. When a pilot crashes "
             "and tells of conflict in the outside world, she leaves home "
             "to fight a war, discovering her full powers and true destiny.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category1,
             user=user1)

item4 = Item(name="Fantastic Beasts and Where to Find Them (2016)",
             description="The adventures of writer Newt Scamander in New "
             "York's secret community of witches and wizards seventy years "
             "before Harry Potter reads his book in school.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category2,
             user=user1)

item5 = Item(name="Harry Potter and the Sorcerer's Stone (2001)",
             description="Rescued from the outrageous neglect of his aunt "
             "and uncle, a young boy with a great destiny proves his worth "
             "while attending Hogwarts School of Witchcraft and Wizardry.",
             category=category2,
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             user=user1)

item6 = Item(name="Miss Peregrine's Home for Peculiar Children (2016)",
             description="When Jacob discovers clues to a mystery that "
             "stretches across time, he finds Miss Peregrine's Home for "
             "Peculiar Children. But the danger deepens after he gets to "
             "know the residents and learns about their special powers.",
             category=category2,
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             user=user1)

item7 = Item(name="Sing (2016)",
             description="In a city of humanoid animals, a hustling theater "
             "impresario's attempt to save his theater with a singing "
             "competition becomes grander than he anticipates even as its "
             "finalists' find that their lives will never be the same.",
             category=category3,
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             user=user1)

item8 = Item(name="The Emoji Movie (2017)",
             description="Gene, a multi-expressional emoji, sets out on a "
             "journey to become a normal emoji.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category3,
             user=user1)

item9 = Item(name="Moana (2016)",
             description="In Ancient Polynesia, when a terrible curse "
             "incurred by the Demigod Maui reaches Moana's island, she "
             "answers the Ocean's call to seek out the Demigod to set "
             "things right.",
             created_at=datetime.datetime.now(),
             updated_at=datetime.datetime.now(),
             category=category3,
             user=user1)

item10 = Item(name="Molly's Game (2017)",
              description="The true story of an Olympic-class skier who ran "
              "the world's most exclusive high-stakes poker game and became "
              "an FBI target. Her players included movie stars, business "
              "titans and unbeknownst to her, the Russian mob.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category4,
              user=user1)

item11 = Item(name="The Glass Castle (2017)",
              description="A young girl comes of age in a dysfunctional "
              "family of nonconformist nomads with a mother who's an "
              "eccentric artist and an alcoholic father who would stir the "
              "children's imagination with hope as a distraction to their "
              "poverty.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category4,
              user=user1)

item12 = Item(name="Hacksaw Ridge (2016)",
              description="WWII American Army Medic Desmond T. Doss, who "
              "served during the Battle of Okinawa, refuses to kill people, "
              "and becomes the first man in American history to receive the "
              "Medal of Honor without firing a shot.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category4,
              user=user1)

item13 = Item(name="Logan Lucky (2017)",
              description="Two brothers attempt to pull off a heist during "
              "a NASCAR race in North Carolina.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category5,
              user=user1)

item14 = Item(name="Naked (2017)",
              description="Nervous about finally getting married, a guy is "
              "forced to relive the same nerve-wracking hours over and over "
              "again until he gets things right on his wedding day.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category5,
              user=user1)

item15 = Item(name="The Meyerowitz Stories (New and Selected) (2017)",
              description="An estranged family gathers together in New York "
              "for an event celebrating the artistic work of their father.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category5,
              user=user1)

item16 = Item(name="Shot Caller (2017)",
              description="A newly released prison gangster is forced by "
              "the leaders of his gang to orchestrate a major crime with a "
              "brutal rival gang on the streets of Southern California.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category6,
              user=user1)

item17 = Item(name="Detroit (2017)",
              description="Amidst the chaos of the Detroit Rebellion, with "
              "the city under curfew and as the Michigan National Guard "
              "patrolled the streets, three young African American men were "
              "murdered at the Algiers Motel.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category6,
              user=user1)

item18 = Item(name="Good Time (2017)",
              description="A bank robber finds himself unable to evade his "
              "pursuers.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category6,
              user=user1)

item19 = Item(name="Icarus (2017)",
              description="When Bryan Fogel sets out to uncover the truth "
              "about doping in sports, a chance meeting with a Russian "
              "scientist transforms his story from a personal experiment "
              "into a geopolitical thriller involving dirty urine, "
              "unexplained death and Olympic Gold-exposing the biggest "
              "scandal in sports history.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category7,
              user=user1)

item20 = Item(name="An Inconvenient Sequel: Truth to Power (2017)",
              description="A decade after An Inconvenient Truth brought "
              "climate change into the heart of popular culture comes the "
              "follow-up that shows just how close we are to a real energy "
              "revolution.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category7,
              user=user1)

item21 = Item(name="What the Health (2017)",
              description="An intrepid filmmaker on a journey of discovery as "
              "he uncovers possibly the largest health secret of our time and "
              "the collusion between industry, government, pharmaceutical and "
              "health organizations keeping this information from us.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category7,
              user=user1)

item22 = Item(name="It (2017)",
              description="A group of bullied kids band together when a "
              "monster, taking the appearance of a clown, begins hunting "
              "children.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category8,
              user=user1)

item23 = Item(name="Rememory (2017)",
              description="The widow of a wise professor stumbles upon one "
              "of his inventions that's able to record and play a person's "
              "memory.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category8,
              user=user1)

item24 = Item(name="Mother! (2017)",
              description="A couple's relationship is tested when uninvited "
              "guests arrive at their home, disrupting their tranquil "
              "existence.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category8,
              user=user1)

item25 = Item(name="Beauty and the Beast (2017)",
              description="An adaptation of the fairy tale about a "
              "monstrous-looking prince and a young woman who fall in love.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category9,
              user=user1)

item26 = Item(name="The Boss Baby (2017)",
              description="A suit-wearing, briefcase-carrying baby pairs up "
              "with his 7-year old brother to stop the dastardly plot of "
              "the CEO of Puppy Co.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category9,
              user=user1)

item27 = Item(name="Cinderella (2015)",
              description="When her father unexpectedly passes away, young "
              "Ella finds herself at the mercy of her cruel stepmother and "
              "her scheming step-sisters. Never one to give up hope, Ella's "
              "fortunes begin to change after meeting a dashing stranger.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category9,
              user=user1)

item28 = Item(name="Death Note (2017)",
              description="Light Turner, a bright student, stumbles across "
              "a mystical notebook that has the power to kill any person "
              "whose name he writes in it. Light decides to launch a secret "
              "crusade to rid the streets of criminals. Soon, the "
              "student-turned-vigilante finds himself pursued by a famous "
              "detective known only by the alias L.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item29 = Item(name="Hansel & Gretel: Witch Hunters (2013)",
              description="Hansel & Gretel are bounty hunters who track and "
              "kill witches all over the world. As the fabled Blood Moon "
              "approaches, the siblings encounter a new form of evil that "
              "might hold a secret to their past.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item30 = Item(name="Alice in Wonderland (2010)",
              description="Nineteen-year-old Alice returns to the magical "
              "world from her childhood adventure, where she reunites with "
              "her old friends and learns of her true destiny: to end the "
              "Red Queen's reign of terror.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category10,
              user=user1)

item31 = Item(name="The Strange Love of Martha Ivers (1946)",
              description="A ruthless, domineering woman is married to an "
              "alcoholic D.A., her childhood companion and the only living "
              "witness to her murder of her rich aunt seventeen years "
              "earlier.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category11,
              user=user1)

item32 = Item(name="Sunset Blvd. (1950)",
              description="A screenwriter is hired to rework a faded silent "
              "film star's script only to find himself developing a dangerous "
              "relationship.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category11,
              user=user1)

item33 = Item(name="Crime of Passion (1957)",
              description="Kathy leaves the newspaper business to marry "
              "homicide detective Bill but is frustrated by his lack of "
              "ambition and the banality of life in the suburbs. Her drive "
              "to advance Bill's career soon takes her down a dangerous path.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category11,
              user=user1)

item34 = Item(name="Hidden Figures (2016)",
              description="The story of a team of female African-American "
              "mathematicians who served a vital role in NASA during the "
              "early years of the U.S. space program.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category12,
              user=user1)

item35 = Item(name="Schindler's List (1993)",
              description="In German-occupied Poland during World War II, "
              "Oskar Schindler gradually becomes concerned for his Jewish "
              "workforce after witnessing their persecution by the Nazi "
              "Germans.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category12,
              user=user1)

item36 = Item(name="The Zookeeper's Wife (2017)",
              description="The Zookeeper's Wife tells the account of "
              "keepers of the Warsaw Zoo, Antonina and Jan Zabinski, who "
              "helped save hundreds of people and animals during the German "
              "invasion.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category12,
              user=user1)

item37 = Item(name="Annabelle: Creation (2017)",
              description="Twelve years after the tragic death of their "
              "little girl, a dollmaker and his wife welcome a nun and "
              "several girls from a shuttered orphanage into their home, "
              "where they soon become the target of the dollmaker's "
              "possessed creation, Annabelle.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category13,
              user=user1)

item38 = Item(name="Alien: Covenant (2017)",
              description="The crew of a colony ship, bound for a remote "
              "planet, discover an uncharted paradise with a threat beyond "
              "their imagination, and must attempt a harrowing escape.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category13,
              user=user1)

item39 = Item(name="Leatherface (2017)",
              description="A teenage Leatherface escapes from a mental "
              "hospital with three other inmates, kidnapping a young nurse "
              "and taking her on a road trip from hell while being pursued "
              "by an equally deranged lawman out for revenge.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category13,
              user=user1)

item40 = Item(name="Baby Driver (2017)",
              description="After being coerced into working for a crime "
              "boss, a young getaway driver finds himself taking part in "
              "a heist doomed to fail.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category14,
              user=user1)

item41 = Item(name="Whiplash (2014)",
              description="A promising young drummer enrolls at a cut-throat "
              "music conservatory where his dreams of greatness are mentored "
              "by an instructor who will stop at nothing to realize a "
              "student's potential.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category14,
              user=user1)

item42 = Item(name="Dirty Dancing (1987)",
              description="Spending the summer at a Catskills resort with her "
              "family, Frances 'Baby' Houseman falls in love with the camp's "
              "dance instructor, Johnny Castle.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category14,
              user=user1)

item43 = Item(name="La La Land (2016)",
              description="While waiting for their big breaks, two proper "
              "L.A. dreamers, a suavely- charming, soft-spoken jazz pianist "
              "and a brilliant, vivacious playwright, attempt to reconcile "
              "aspirations and relationship in a magical old-school romance.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category15,
              user=user1)

item44 = Item(name="Mamma Mia! (2008)",
              description="The story of a bride-to-be trying to find her "
              "real father told using hit songs by the popular '70s group "
              "ABBA.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category15,
              user=user1)

item45 = Item(name="Grease (1978)",
              description="Good girl Sandy and greaser Danny fell in love "
              "over the summer. When they unexpectedly discover they're now "
              "in the same high school, will they be able to rekindle their "
              "romance?",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category15,
              user=user1)

item46 = Item(name="Annabelle: Creation (2017)",
              description="Twelve years after the tragic death of their "
              "little girl, a dollmaker and his wife welcome a nun and "
              "several girls from a shuttered orphanage into their home, "
              "where they soon become the target of the dollmaker's possessed "
              "creation, Annabelle.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category16,
              user=user1)

item47 = Item(name="Annabelle (2014)",
              description="A couple begins to experience terrifying "
              "supernatural occurrences involving a vintage doll shortly "
              "after their home is invaded by satanic cultists.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category16,
              user=user1)

item48 = Item(name="Wind River (2017)",
              description="An FBI agent teams with a town's veteran game "
              "tracker to investigate a murder that occurred on a Native "
              "American reservation.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category16,
              user=user1)

item49 = Item(name="Wet Hot American Summer (2001)",
              description="Set on the last day of camp, in the hot summer "
              "of 1981, a group of counselors try to complete their "
              "unfinished business before the day ends.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category17,
              user=user1)

item50 = Item(name="Our Souls at Night (2017)",
              description="Fonda and Redford will star as Addie Moore and "
              "Louis Waters, a widow and widower who've lived next to each "
              "other for years. The pair have almost no relationship, but "
              "that all changes when Addie tries to make a connection with "
              "her neighbor.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category17,
              user=user1)

item51 = Item(name="Everything, Everything (2017)",
              description="A teenager who's spent her whole life confined to "
              "her home falls for the boy next door.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category17,
              user=user1)

item52 = Item(name="Guardians of the Galaxy Vol. 2 (2017)",
              description="The Guardians must fight to keep their newfound "
              "family together as they unravel the mystery of Peter Quill's "
              "true parentage.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category18,
              user=user1)

item53 = Item(name="The Dark Tower (2017)",
              description="TThe last Gunslinger, Roland Deschain, has been "
              "locked in an eternal battle with Walter O'Dim, also known as "
              "the Man in Black, determined to prevent him from toppling the "
              "Dark Tower, which holds the universe together. With the fate "
              "of the worlds at stake, good and evil will collide in the "
              "ultimate battle as only Roland can defend the Tower from the "
              "Man in Black.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category18,
              user=user1)

item54 = Item(name="What Happened to Monday (2017)",
              description="In a world where families are limited to one "
              "child due to overpopulation, a set of identical septuplets "
              "must avoid being put to a long sleep by the government and "
              "dangerous infighting while investigating the disappearance of "
              "one of their own.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category18,
              user=user1)

item55 = Item(name="Goon: Last of the Enforcers (2017)",
              description="A hockey player plagued by injuries is confronted "
              "with the possibility of retirement when a tough new player "
              "challenges his status as the league's top enforcer.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category19,
              user=user1)

item56 = Item(name="Dangal (2016)",
              description="TFormer wrestler Mahavir Singh Phogat and his "
              "two wrestler daughters struggle towards glory at the "
              "Commonwealth Games in the face of societal oppression.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category19,
              user=user1)

item57 = Item(name="Warrior (2011)",
              description="The youngest son of an alcoholic former boxer "
              "returns home, where he's trained by his father for competition "
              "in a mixed martial arts tournament - a path that puts the "
              "fighter on a collision course with his estranged, older "
              "brother.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category19,
              user=user1)

item58 = Item(name="The Nun (2018)",
              description="A priest named Father Burke is sent to Rome to "
              "investigate the mysterious death of a nun.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category20,
              user=user1)

item59 = Item(name="Split (2016)",
              description="TThree girls are kidnapped by a man with a "
              "diagnosed 23 distinct personalities. They must try to escape "
              "before the apparent emergence of a frightful new 24th.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category20,
              user=user1)

item60 = Item(name="Life (2017)",
              description="A team of scientists aboard the International "
              "Space Station discover a rapidly evolving life form, that "
              "caused extinction on Mars, and now threatens the crew and "
              "all life on Earth.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category20,
              user=user1)

item61 = Item(name="Dunkirk (2017)",
              description="Allied soldiers from Belgium, the British Empire "
              "and France are surrounded by the German army and evacuated "
              "during a fierce battle in World War II.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category21,
              user=user1)

item62 = Item(name="The Wall (2017)",
              description="Two American Soldiers are trapped by a lethal "
              "sniper, with only an unsteady wall between them.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category21,
              user=user1)

item63 = Item(name="Inglourious Basterds (2009)",
              description="n Nazi-occupied France during World War II, a "
              "plan to assassinate Nazi leaders by a group of Jewish U.S. "
              "soldiers coincides with a theatre owner's vengeful plans for "
              "the same.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category21,
              user=user1)

item64 = Item(name="Hell or High Water (2016)",
              description="A divorced father and his ex-con older brother "
              "resort to a desperate scheme in order to save their family's "
              "ranch in West Texas.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category22,
              user=user1)

item65 = Item(name="Tombstone (1993)",
              description="TA successful lawman's plans to retire anonymously "
              "in Tombstone, Arizona, are disrupted by the kind of outlaws he "
              "was famous for eliminating.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category22,
              user=user1)

item66 = Item(name="The Magnificent Seven (2016)",
              description="Seven gunmen in the old west gradually come "
              "together to help a poor village against savage thieves.",
              created_at=datetime.datetime.now(),
              updated_at=datetime.datetime.now(),
              category=category22,
              user=user1)


db_session.add(item1)
db_session.add(item2)
db_session.add(item3)
db_session.add(item4)
db_session.add(item5)
db_session.add(item6)
db_session.add(item7)
db_session.add(item8)
db_session.add(item9)
db_session.add(item10)
db_session.add(item11)
db_session.add(item12)
db_session.add(item13)
db_session.add(item14)
db_session.add(item15)
db_session.add(item16)
db_session.add(item17)
db_session.add(item18)
db_session.add(item19)
db_session.add(item20)
db_session.add(item21)
db_session.add(item22)
db_session.add(item23)
db_session.add(item24)
db_session.add(item25)
db_session.add(item26)
db_session.add(item27)
db_session.add(item28)
db_session.add(item29)
db_session.add(item30)
db_session.add(item31)
db_session.add(item32)
db_session.add(item33)
db_session.add(item34)
db_session.add(item35)
db_session.add(item36)
db_session.add(item37)
db_session.add(item38)
db_session.add(item39)
db_session.add(item40)
db_session.add(item41)
db_session.add(item42)
db_session.add(item43)
db_session.add(item44)
db_session.add(item45)
db_session.add(item46)
db_session.add(item47)
db_session.add(item48)
db_session.add(item49)
db_session.add(item50)
db_session.add(item51)
db_session.add(item52)
db_session.add(item53)
db_session.add(item54)
db_session.add(item55)
db_session.add(item56)
db_session.add(item57)
db_session.add(item58)
db_session.add(item59)
db_session.add(item60)
db_session.add(item61)
db_session.add(item62)
db_session.add(item63)
db_session.add(item64)
db_session.add(item65)
db_session.add(item66)
db_session.commit()

print "Added all genres and films!"
