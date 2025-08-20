from tkinter import *
from tkinter import messagebox

def England():
    top=Toplevel()
    top.geometry("500x510")
    top.title("English league")
    english_label=Label(top,text="Premier league clubs")
    english_listbox=Listbox(top)
    with open("premier_league.txt")as file:
        for i in file:
            english_listbox.insert(END,i)

    english_label2=Label(top,text="Championship clubs")
    english_listbox2=Listbox(top)
    with open("championship.txt")as file:
        for i in file:
            english_listbox2.insert(END,i)

    english_label3=Label(top,text="Insert the league name to see info about upcoming matches:")
    english_entry=Entry(top)
    english_listbox3=Listbox(top)

    def Premier_league_clubs_trophies():
        top1=Toplevel()
        top1.title("Premier league trophies")
        top1.geometry("300x300")
        trophies_label=Label(top1,text="Number of trophies of all Premier league clubs")
        trophies_listbox=Listbox(top1)
        with open("trophies_premier_league.txt")as file:
            for i in file:
                trophies_listbox.insert(END,i)

        trophies_listbox.config(height=15,width=27)
        trophies_label.pack()
        trophies_listbox.pack()

    def Championship_clubs_trophies():
        top2=Toplevel()
        top2.title("Championship trophies")
        top2.geometry("300x300")
        trophies_label2=Label(top2,text="Number of trophies of all Championship clubs")
        trophies_listbox2=Listbox(top2)
        with open("trophies_championship.txt")as file:
            for i in file:
                trophies_listbox2.insert(END,i)

        trophies_listbox2.config(height=15, width=27)
        trophies_label2.pack()
        trophies_listbox2.pack()

    def Matches_schedule():
        try:
            if english_entry.get()=="Premier league" or english_entry.get()=="premier league":
                top_games_schedule=Toplevel()
                top_games_schedule.title("Premier league matches schedule")
                top_games_schedule_listbox=Listbox(top_games_schedule)
                top_games_schedule_listbox.pack()
                top_games_schedule_listbox.config(height=20,width=60)

                with open("matches_schedule_premier_league.txt")as file:
                    for i in file:
                        top_games_schedule_listbox.insert(END,i)

            if english_entry.get().isdigit()==True:
                raise ValueError

            if english_entry.get()=="":
                raise ValueError

            if english_entry.get()!="Premier league" and english_entry.get()!="premier league" and english_entry.get()!="Championship" and english_entry.get()!="championship":
                raise ValueError

            if english_entry.get().isnumeric() == True:
                raise ValueError

            if english_entry.get() == "Championship" or english_entry.get() == "championship":
                top_games_schedule = Toplevel()
                top_games_schedule.title("Championship matches schedule")
                top_games_schedule_listbox = Listbox(top_games_schedule)
                top_games_schedule_listbox.pack()
                top_games_schedule_listbox.config(height=20, width=60)

                with open("matches_schedule_championship.txt") as file:
                    for i in file:
                        top_games_schedule_listbox.insert(END, i)

        except ValueError:
            messagebox.showerror("Error","You need to insert correct league name in order to see Matches schedule!")

    def Online_shop():
        top3=Toplevel()
        top3.title("English Online Shop")
        top3.geometry("400x435")
        shop_label=Label(top3,text="Select an item to add to your cart")
        cart_label = Label(top3, text="Cart of selected articles from Online Shop")
        shop_listbox=Listbox(top3)
        shop_listbox2=Listbox(top3)
        with open("shop_england.txt")as file:
            for i in file:
                shop_listbox.insert(END,i)

        def Cart():
            try:
                get=shop_listbox.get(shop_listbox.curselection())
                shop_listbox2.insert(END,get)

            except Exception:
                messagebox.showinfo("Message","You need to select an article to add it to the cart!")


        def Buy_articles_from_cart():
            try:
                buying=len(shop_listbox2.get(0,END))
                if buying==0:
                    raise ValueError
                shop_listbox2.delete(0,END)

                messagebox.showinfo("Transaction completed",f"You successfully bought {buying} articles from the cart! ")

            except ValueError:
                messagebox.showinfo("Message","There has to be at least one article in the cart to complete the transaction!")

        buying_article_button = Button(top3, text="Buy articles from the cart", command=Buy_articles_from_cart)

        def Delete_articles_from_cart():
            try:
                delete=shop_listbox2.curselection()
                shop_listbox2.delete(delete)

            except Exception:
                messagebox.showerror("Error","You need to select an article in order to delete it!")

        deleting_article_button=Button(top3,text="Remove article from the cart",command=Delete_articles_from_cart)

        def Tickets_premier_league():
            top4=Toplevel()
            top4.title("Tickets for Premier league matches")
            top4.geometry("300x120")
            tickets_label=Label(top4,text="Select the ticket that you want to buy")
            tickets_listbox=Listbox(top4)
            with open("tickets_premier_league.txt")as file:
                for i in file:
                    tickets_listbox.insert(END,i)
            tickets_label.pack()
            tickets_listbox.pack()
            tickets_listbox.config(height=4,width=35)

            def Buying_tickets_premier_league():
                try:
                    get_ticket=tickets_listbox.get(tickets_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Buy tickets(amount)")
                    top6.geometry("300x100")
                    buying_label=Label(top6,text="Enter the amount of tickets you want to buy")
                    buying_entry=Entry(top6)
                    buying_label.pack()
                    buying_entry.pack()

                except Exception:
                    messagebox.showinfo("Message","You need to select a ticket!")

                def Buying_amount():
                    try:
                        if buying_entry.get()=="" or buying_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Message",f"You bought {buying_entry.get()} tickets for {get_ticket}")

                    except ValueError:
                        messagebox.showerror("Error","You need to enter the amount of tickets with numbers!")
                try:

                    buying_button=Button(top6,text="Confirm",command=Buying_amount)
                    buying_button.pack()

                except Exception:
                    messagebox.showerror("Error","You need to select a ticket!")

            try:
                tickets_button = Button(top4, text="Buy a ticket", command=Buying_tickets_premier_league)
                tickets_button.pack()

            except Exception:
                messagebox.showinfo("Message", "You need to select a ticket!")

        def Tickets_championship():
            top5=Toplevel()
            top5.title("Tickets for Championship league matches")
            top5.geometry("300x120")
            tickets_championship_label=Label(top5,text="Select the ticket that you want to buy")
            tickets_championship_listbox=Listbox(top5)
            with open("tickets_championship.txt")as file:
                for i in file:
                    tickets_championship_listbox.insert(END,i)

            tickets_championship_label.pack()
            tickets_championship_listbox.pack()
            tickets_championship_listbox.config(height=4,width=35)

            def Buying_tickets_championship():
                try:
                    get_ticket=tickets_championship_listbox.get(tickets_championship_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Buy tickets(amount)")
                    top6.geometry("300x100")
                    buying_label=Label(top6,text="Enter the amount of tickets you want to buy")
                    buying_entry=Entry(top6)
                    buying_label.pack()
                    buying_entry.pack()

                except Exception:
                    messagebox.showinfo("Message","You need to select a ticket!")

                def Buying_amount():
                    try:
                        if buying_entry.get()=="" or buying_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Message",f"You bought {buying_entry.get()} tickets for {get_ticket}")

                    except ValueError:
                        messagebox.showerror("Error","You need to enter the amount of tickets with numbers!")

                try:

                    buying_button = Button(top6, text="Confirm", command=Buying_amount)
                    buying_button.pack()

                except Exception:
                    messagebox.showerror("Error", "You need to select a ticket!")

            try:
                tickets_button = Button(top5, text="Buy a ticket", command=Buying_tickets_championship)
                tickets_button.pack()

            except Exception:
                messagebox.showinfo("Message", "You need to select a ticket!")

        shop_button = Button(top3,text="Add to cart",command=Cart)
        shop_button2=Button(top3,text="Tickets for Premier league matches",command=Tickets_premier_league)
        shop_button3=Button(top3,text="Tickets for Championship league matches",command=Tickets_championship)
        shop_label.pack()
        shop_listbox.pack()
        shop_button.pack()
        cart_label.pack()
        shop_listbox2.pack()
        buying_article_button.pack()
        deleting_article_button.pack()
        shop_button2.pack()
        shop_button3.pack()
        shop_listbox.config(height=8, width=36)
        shop_listbox2.config(height=8, width=36)

    english_button3=Button(top,text="Premier league clubs trophies",command=Premier_league_clubs_trophies)
    english_button4=Button(top,text="Championship league clubs trophies",command=Championship_clubs_trophies)
    english_button5=Button(top,text="Online shop",command=Online_shop)
    english_button6=Button(top,text="Matches schedule",command=Matches_schedule)

    english_listbox.config(width=25)
    english_listbox2.config(width=25)

    english_label.pack()
    english_listbox.pack()
    english_button3.pack()
    english_label2.pack()
    english_listbox2.pack()
    english_button4.pack()
    english_label3.pack()
    english_entry.pack()
    english_button6.pack()
    english_button5.pack()

def Spain():
    top=Toplevel()
    top.geometry("500x510")
    top.title("Spanish league")
    spanish_label=Label(top,text="La liga clubs")
    spanish_listbox=Listbox(top)
    with open("laliga.txt")as file:
        for i in file:
            spanish_listbox.insert(END,i)

    spanish_label2=Label(top,text="Segunda liga clubs")
    spanish_listbox2=Listbox(top)
    with open("segunda.txt")as file:
        for i in file:
            spanish_listbox2.insert(END,i)

    spanish_label3=Label(top,text="Insert the league name to see info about upcoming matches:")
    spanish_entry=Entry(top)

    def La_liga_clubs_trophies():
        top1=Toplevel()
        top1.title("La liga trophies")
        top1.geometry("300x300")
        trophies_label=Label(top1,text="Number of trophies of all La liga clubs")
        trophies_listbox=Listbox(top1)
        with open("trophies_laliga.txt")as file:
            for i in file:
                trophies_listbox.insert(END,i)

        trophies_listbox.config(height=15,width=27)
        trophies_label.pack()
        trophies_listbox.pack()

    def Segunda_clubs_trophies():
        top2=Toplevel()
        top2.title("Segunda liga trophies")
        top2.geometry("300x300")
        trophies_label2=Label(top2,text="Number of trophies of all Segunda liga clubs")
        trophies_listbox2=Listbox(top2)
        with open("trophies_segunda.txt")as file:
            for i in file:
                trophies_listbox2.insert(END,i)

        trophies_listbox2.config(height=15,width=27)
        trophies_label2.pack()
        trophies_listbox2.pack()

    def Matches_schedule():
        try:
            if spanish_entry.get()=="La liga" or spanish_entry.get()=="la liga":
                top_games_schedule=Toplevel()
                top_games_schedule.title("La liga matches schedule")
                top_games_schedule_listbox=Listbox(top_games_schedule)
                top_games_schedule_listbox.pack()
                top_games_schedule_listbox.config(height=20,width=60)

                with open("matches_schedule_laliga.txt")as file:
                    for i in file:
                        top_games_schedule_listbox.insert(END,i)

            if spanish_entry.get().isdigit()==True:
                raise ValueError

            if spanish_entry.get()=="":
                raise ValueError

            if spanish_entry.get()!="La liga" and spanish_entry.get()!="la liga" and spanish_entry.get()!="Segunda liga" and spanish_entry.get()!="segunda liga":
                raise ValueError

            if spanish_entry.get().isnumeric()==True:
                raise ValueError

            if spanish_entry.get() == "Segunda liga" or spanish_entry.get() == "segunda liga":
                top_games_schedule = Toplevel()
                top_games_schedule.title("Segunda liga matches schedule")
                top_games_schedule_listbox = Listbox(top_games_schedule)
                top_games_schedule_listbox.pack()
                top_games_schedule_listbox.config(height=20, width=60)

                with open("matches_schedule_segunda.txt") as file:
                    for i in file:
                        top_games_schedule_listbox.insert(END, i)

        except ValueError:
            messagebox.showerror("Error","You need to insert correct league name in order to see Matches schedule!")

    def Online_shop():
        top3 = Toplevel()
        top3.title("Spanish Online Shop")
        top3.geometry("400x435")
        shop_label = Label(top3, text="Select an item to add to your cart")
        cart_label = Label(top3, text="Cart of selected articles from Online Shop")
        shop_listbox = Listbox(top3)
        shop_listbox2 = Listbox(top3)
        with open("shop_spain.txt") as file:
            for i in file:
                shop_listbox.insert(END, i)

        def Cart():
            try:
                get = shop_listbox.get(shop_listbox.curselection())
                shop_listbox2.insert(END, get)

            except Exception:
                messagebox.showinfo("Message", "You need to select an article to add it to the cart!")

        def Buy_articles_from_cart():
            try:
                buying = len(shop_listbox2.get(0, END))
                if buying == 0:
                    raise ValueError
                shop_listbox2.delete(0,END)

                messagebox.showinfo("Transaction completed", f"You successfully bought {buying} articles from the cart! ")

            except ValueError:
                messagebox.showinfo("Message","There has to be at least one article in the cart to complete the transaction!")

        buying_article_button = Button(top3, text="Buy articles from the cart", command=Buy_articles_from_cart)

        def Delete_articles_from_cart():
            try:
                delete = shop_listbox2.curselection()
                shop_listbox2.delete(delete)

            except Exception:
                messagebox.showerror("Error","You need to select an article in order to delete it!")

        deleting_article_button = Button(top3, text="Remove article from the cart", command=Delete_articles_from_cart)

        def Tickets_laliga():
            top4 = Toplevel()
            top4.title("Tickets for La liga matches")
            top4.geometry("300x120")
            tickets_label = Label(top4, text="Select the ticket that you want to buy")
            tickets_listbox = Listbox(top4)
            with open("tickets_laliga.txt") as file:
                for i in file:
                    tickets_listbox.insert(END, i)
            tickets_label.pack()
            tickets_listbox.pack()
            tickets_listbox.config(height=4, width=35)

            def Buying_tickets_laliga():
                try:
                    get_ticket=tickets_listbox.get(tickets_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Buy tickets(amount)")
                    top6.geometry("300x100")
                    buying_label=Label(top6,text="Enter the amount of tickets you want to buy")
                    buying_entry=Entry(top6)
                    buying_label.pack()
                    buying_entry.pack()

                except Exception:
                    messagebox.showinfo("Message","You need to select a ticket!")

                def Buying_amount():
                    try:
                        if buying_entry.get()=="" or buying_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Message",f"You bought {buying_entry.get()} tickets for {get_ticket}")

                    except ValueError:
                        messagebox.showerror("Error","You need to enter the amount of tickets with numbers!")

                try:

                    buying_button=Button(top6,text="Confirm",command=Buying_amount)
                    buying_button.pack()

                except Exception:
                    messagebox.showerror("Error","You need to select a ticket!")

            try:
                tickets_button = Button(top4, text="Buy a ticket", command=Buying_tickets_laliga)
                tickets_button.pack()

            except Exception:
                messagebox.showinfo("Message", "You need to select a ticket!")

        def Tickets_segundaliga():
            top5 = Toplevel()
            top5.title("Tickets for Segunda liga matches")
            top5.geometry("300x120")
            tickets_segunda_label = Label(top5, text="Select the ticket that you want to buy")
            tickets_segunda_listbox = Listbox(top5)
            with open("tickets_segunda.txt") as file:
                for i in file:
                    tickets_segunda_listbox.insert(END, i)

            tickets_segunda_label.pack()
            tickets_segunda_listbox.pack()
            tickets_segunda_listbox.config(height=4, width=35)

            def Buying_tickets_segundaliga():
                try:
                    get_ticket=tickets_segunda_listbox.get(tickets_segunda_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Buy tickets(amount)")
                    top6.geometry("300x100")
                    buying_label=Label(top6,text="Enter the amount of tickets you want to buy")
                    buying_entry=Entry(top6)
                    buying_label.pack()
                    buying_entry.pack()

                except Exception:
                    messagebox.showinfo("Message","You need to select a ticket!")

                def Buying_amount():
                    try:
                        if buying_entry.get()=="" or buying_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Message",f"You bought {buying_entry.get()} tickets for {get_ticket}")

                    except ValueError:
                        messagebox.showerror("Error","You need to enter the amount of tickets with numbers!")

                try:

                    buying_button = Button(top6, text="Confirm", command=Buying_amount)
                    buying_button.pack()

                except Exception:
                    messagebox.showerror("Error", "You need to select a ticket!")

            try:
                tickets_button = Button(top5, text="Buy a ticket", command=Buying_tickets_segundaliga)
                tickets_button.pack()

            except Exception:
                messagebox.showinfo("Message", "You need to select a ticket!")

        shop_button = Button(top3, text="Add to cart", command=Cart)
        shop_button2 = Button(top3, text="Tickets for La liga matches", command=Tickets_laliga)
        shop_button3 = Button(top3, text="Tickets for Segunda liga matches", command=Tickets_segundaliga)
        shop_label.pack()
        shop_listbox.pack()
        cart_label.pack()
        shop_button.pack()
        shop_listbox2.pack()
        buying_article_button.pack()
        deleting_article_button.pack()
        shop_button2.pack()
        shop_button3.pack()
        shop_listbox.config(height=8, width=36)
        shop_listbox2.config(height=8, width=36)

    spanish_button3=Button(top,text="La liga clubs trophies",command=La_liga_clubs_trophies)
    spanish_button4=Button(top,text="Segunda liga clubs trophies",command=Segunda_clubs_trophies)
    spanish_button5=Button(top,text="Online Shop",command=Online_shop)
    spanish_button6=Button(top,text="Matches schedule",command=Matches_schedule)

    spanish_listbox.config(width=25)
    spanish_listbox2.config(width=25)
    spanish_label.pack()
    spanish_listbox.pack()
    spanish_button3.pack()
    spanish_label2.pack()
    spanish_listbox2.pack()
    spanish_button4.pack()
    spanish_label3.pack()
    spanish_entry.pack()
    spanish_button6.pack()
    spanish_button5.pack()

def Italy():
    top=Toplevel()
    top.title("Italian league")
    top.geometry("500x510")
    italian_label=Label(top,text="Serie A clubs")
    italian_listbox=Listbox(top)
    with open("serie_a.txt")as file:
        for i in file:
            italian_listbox.insert(END,i)

    italian_label2=Label(top,text="Serie B clubs")
    italian_listbox2=Listbox(top)
    with open("serie_b.txt")as file:
        for i in file:
            italian_listbox2.insert(END,i)

    italian_label3=Label(top,text="Insert the league name to see info about upcoming matches:")
    italian_entry=Entry(top)

    def Serie_a_clubs_trophies():
        top1=Toplevel()
        top1.title("Serie A trophies")
        top1.geometry("300x300")
        trophies_label=Label(top1,text="Number of trophies of all Serie A clubs")
        trophies_listbox=Listbox(top1)
        with open("trophies_serie_a.txt")as file:
            for i in file:
                trophies_listbox.insert(END,i)

        trophies_listbox.config(height=15,width=27)
        trophies_label.pack()
        trophies_listbox.pack()

    def Serie_b_clubs_trophies():
        top2=Toplevel()
        top2.title("Serie B trophies")
        top2.geometry("300x300")
        trophies_label2=Label(top2,text="Number of trophies of all Serie B clubs")
        trophies_listbox2=Listbox(top2)
        with open("trophies_serie_b.txt")as file:
            for i in file:
                trophies_listbox2.insert(END,i)

        trophies_listbox2.config(height=15,width=27)
        trophies_label2.pack()
        trophies_listbox2.pack()

    def Matches_schedule():
        try:
            if italian_entry.get()=="Serie A" or italian_entry.get()=="serie a":
                top_games_schedule=Toplevel()
                top_games_schedule.title("Serie A matches schedule")
                top_games_schedule_listbox=Listbox(top_games_schedule)
                top_games_schedule_listbox.pack()
                top_games_schedule_listbox.config(height=20,width=60)

                with open("matches_schedule_serie_a.txt")as file:
                    for i in file:
                        top_games_schedule_listbox.insert(END,i)

            if italian_entry.get().isdigit()==True:
                raise ValueError

            if italian_entry.get()=="":
                raise ValueError

            if italian_entry.get()!="Serie A" and italian_entry.get()!="serie a" and italian_entry.get()!="Serie B" and italian_entry.get()!="serie b":
                raise ValueError

            if italian_entry.get().isnumeric()==True:
                raise ValueError

            if italian_entry.get() == "Serie B" or italian_entry.get() == "serie b":
                top_games_schedule = Toplevel()
                top_games_schedule.title("Serie B matches schedule")
                top_games_schedule_listbox = Listbox(top_games_schedule)
                top_games_schedule_listbox.pack()
                top_games_schedule_listbox.config(height=20, width=60)

                with open("matches_schedule_serie_b.txt") as file:
                    for i in file:
                        top_games_schedule_listbox.insert(END, i)

        except ValueError:
            messagebox.showerror("Error","You need to insert correct league name in order to see Matches schedule!")

    def Online_shop():
        top3 = Toplevel()
        top3.title("Italian Online Shop")
        top3.geometry("400x435")
        shop_label = Label(top3, text="Select an item to add to your cart")
        cart_label = Label(top3, text="Cart of selected articles from Online Shop")
        shop_listbox = Listbox(top3)
        shop_listbox2 = Listbox(top3)
        with open("shop_italy.txt") as file:
            for i in file:
                shop_listbox.insert(END, i)

        def Cart():
            try:
                get = shop_listbox.get(shop_listbox.curselection())
                shop_listbox2.insert(END, get)

            except Exception:
                messagebox.showinfo("Message", "You need to select an article to add it to the cart!")

        def Buy_articles_from_cart():
            try:
                buying = len(shop_listbox2.get(0, END))
                if buying == 0:
                    raise ValueError
                shop_listbox2.delete(0,END)
                messagebox.showinfo("Transaction completed", f"You successfully bought {buying} articles from the cart! ")

            except ValueError:
                messagebox.showinfo("Message","There has to be at least one article in the cart to complete the transaction!")

        buying_article_button = Button(top3, text="Buy articles from the cart", command=Buy_articles_from_cart)

        def Delete_articles_from_cart():
            try:
                delete = shop_listbox2.curselection()
                shop_listbox2.delete(delete)

            except Exception:
                messagebox.showerror("Error","You need to select an article in order to delete it!")

        deleting_article_button = Button(top3, text="Remove article from the cart", command=Delete_articles_from_cart)

        def Tickets_serie_a():
            top4 = Toplevel()
            top4.title("Tickets for Serie A league matches")
            top4.geometry("300x120")
            tickets_label = Label(top4, text="Select the ticket that you want to buy")
            tickets_listbox = Listbox(top4)
            with open("tickets_serie_a.txt") as file:
                for i in file:
                    tickets_listbox.insert(END, i)
            tickets_label.pack()
            tickets_listbox.pack()
            tickets_listbox.config(height=4, width=35)

            def Buying_tickets_serie_a():
                try:
                    get_ticket=tickets_listbox.get(tickets_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Buy tickets(amount)")
                    top6.geometry("300x100")
                    buying_label=Label(top6,text="Enter the amount of tickets you want to buy")
                    buying_entry=Entry(top6)
                    buying_label.pack()
                    buying_entry.pack()

                except Exception:
                    messagebox.showinfo("Message","You need to select a ticket!")

                def Buying_amount():
                    try:
                        if buying_entry.get()=="" or buying_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Message",f"You bought {buying_entry.get()} tickets for {get_ticket}")

                    except ValueError:
                        messagebox.showerror("Error","You need to enter the amount of tickets with numbers!")

                try:

                    buying_button=Button(top6,text="Confirm",command=Buying_amount)
                    buying_button.pack()

                except Exception:
                    messagebox.showerror("Error","You need to select a ticket!")

            try:
                tickets_button = Button(top4, text="Buy a ticket", command=Buying_tickets_serie_a)
                tickets_button.pack()

            except Exception:
                messagebox.showinfo("Message", "You need to select a ticket!")

        def Tickets_serie_b():
            top5 = Toplevel()
            top5.title("Tickets for Serie B league matches")
            top5.geometry("300x120")
            tickets_serieb_label = Label(top5, text="Select the ticket that you want to buy")
            tickets_serieb_listbox = Listbox(top5)
            with open("tickets_serie_b.txt") as file:
                for i in file:
                    tickets_serieb_listbox.insert(END, i)

            tickets_serieb_label.pack()
            tickets_serieb_listbox.pack()
            tickets_serieb_listbox.config(height=4, width=35)

            def Buying_tickets_serie_b():
                try:
                    get_ticket=tickets_serieb_listbox.get(tickets_serieb_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Buy tickets(amount)")
                    top6.geometry("300x100")
                    buying_label=Label(top6,text="Enter the amount of tickets you want to buy")
                    buying_entry=Entry(top6)
                    buying_label.pack()
                    buying_entry.pack()

                except Exception:
                    messagebox.showinfo("Message","You need to select a ticket!")

                def Buying_amount():
                    try:
                        if buying_entry.get()=="" or buying_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Message",f"You bought {buying_entry.get()} tickets for {get_ticket}")

                    except ValueError:
                        messagebox.showerror("Error","You need to enter the amount of tickets with numbers!")

                try:

                    buying_button = Button(top6, text="Confirm", command=Buying_amount)
                    buying_button.pack()

                except Exception:
                    messagebox.showerror("Error", "You need to select a ticket!")

            try:
                tickets_button = Button(top5, text="Buy a ticket", command=Buying_tickets_serie_b)
                tickets_button.pack()

            except Exception:
                messagebox.showinfo("Message", "You need to select a ticket!")

        shop_button = Button(top3, text="Add to cart", command=Cart)
        shop_button2 = Button(top3, text="Tickets for Serie A league matches", command=Tickets_serie_a)
        shop_button3 = Button(top3, text="Tickets for Serie B league matches", command=Tickets_serie_b)
        shop_label.pack()
        shop_listbox.pack()
        shop_button.pack()
        cart_label.pack()
        shop_listbox2.pack()
        buying_article_button.pack()
        deleting_article_button.pack()
        shop_button2.pack()
        shop_button3.pack()
        shop_listbox.config(height=8, width=36)
        shop_listbox2.config(height=8, width=36)

    italian_button3=Button(top,text="Serie A clubs trophies",command=Serie_a_clubs_trophies)
    italian_button4=Button(top,text="Serie B clubs trophies",command=Serie_b_clubs_trophies)
    italian_button5=Button(top,text="Online Shop",command=Online_shop)
    italian_button6=Button(top,text="Matches schedule",command=Matches_schedule)

    italian_listbox.config(width=25)
    italian_listbox2.config(width=25)
    italian_label.pack()
    italian_listbox.pack()
    italian_button3.pack()
    italian_label2.pack()
    italian_listbox2.pack()
    italian_button4.pack()
    italian_label3.pack()
    italian_entry.pack()
    italian_button6.pack()
    italian_button5.pack()

def Germany():
    top=Toplevel()
    top.title("German league")
    top.geometry("500x510")
    german_label=Label(top,text="Bundesliga clubs")
    german_listbox=Listbox(top)
    with open("bundesliga.txt")as file:
        for i in file:
            german_listbox.insert(END,i)

    german_label2=Label(top,text="Bundesliga 2 clubs")
    german_listbox2=Listbox(top)
    with open("bundesliga2.txt")as file:
        for i in file:
            german_listbox2.insert(END,i)

    german_label3=Label(top,text="Insert the league name to see info about upcoming matches:")
    german_entry=Entry(top)

    def Bundesliga_clubs_trophies():
        top1=Toplevel()
        top1.title("Bundesliga trophies")
        top1.geometry("300x300")
        trophies_label=Label(top1,text="Number of trophies of all Bundesliga clubs")
        trophies_listbox=Listbox(top1)
        with open("trophies_bundesliga.txt")as file:
            for i in file:
                trophies_listbox.insert(END,i)

        trophies_listbox.config(height=15,width=27)
        trophies_label.pack()
        trophies_listbox.pack()

    def Bundesliga2_clubs_trophies():
        top2=Toplevel()
        top2.title("Bundesliga 2 trophies")
        top2.geometry("300x300")
        trophies_label2=Label(top2,text="Number of trophies of all Bundesliga 2 clubs")
        trophies_listbox2=Listbox(top2)
        with open("trophies_bundesliga2.txt")as file:
            for i in file:
                trophies_listbox2.insert(END,i)

        trophies_listbox2.config(height=15,width=27)
        trophies_label2.pack()
        trophies_listbox2.pack()

    def Matches_schedule():
        try:
            if german_entry.get()=="Bundesliga" or german_entry.get()=="bundesliga":
                top_games_schedule=Toplevel()
                top_games_schedule.title("Bundesliga matches schedule")
                top_games_schedule_listbox=Listbox(top_games_schedule)
                top_games_schedule_listbox.pack()
                top_games_schedule_listbox.config(height=20,width=60)

                with open("matches_schedule_bundesliga.txt")as file:
                    for i in file:
                        top_games_schedule_listbox.insert(END,i)

            if german_entry.get().isdigit()==True:
                raise ValueError

            if german_entry.get()=="":
                raise ValueError

            if german_entry.get()!="Bundesliga" and german_entry.get()!="bundesliga" and german_entry.get()!="Bundesliga 2" and german_entry.get()!="bundesliga 2":
                raise ValueError

            if german_entry.get().isnumeric()==True:
                raise ValueError

            if german_entry.get() == "Bundesliga 2" or german_entry.get() == "bundesliga 2":
                top_games_schedule = Toplevel()
                top_games_schedule.title("Bundesliga2 matches schedule")
                top_games_schedule_listbox = Listbox(top_games_schedule)
                top_games_schedule_listbox.pack()
                top_games_schedule_listbox.config(height=20, width=60)

                with open("matches_schedule_bundesliga2.txt") as file:
                    for i in file:
                        top_games_schedule_listbox.insert(END, i)

        except ValueError:
            messagebox.showerror("Error","You need to insert correct league name in order to see Matches schedule!")

    def Online_shop():
        top3 = Toplevel()
        top3.title("German Online Shop")
        top3.geometry("400x435")
        shop_label = Label(top3, text="Select an item to add to your cart")
        cart_label = Label(top3, text="Cart of selected articles from Online Shop")
        shop_listbox = Listbox(top3)
        shop_listbox2 = Listbox(top3)
        with open("shop_germany.txt") as file:
            for i in file:
                shop_listbox.insert(END, i)

        def Cart():
            try:
                get = shop_listbox.get(shop_listbox.curselection())
                shop_listbox2.insert(END, get)

            except Exception:
                messagebox.showinfo("Message", "You need to select an article to add it to the cart!")

        def Buy_articles_from_cart():
            try:
                buying = len(shop_listbox2.get(0, END))
                if buying == 0:
                    raise ValueError
                shop_listbox2.delete(0,END)

                messagebox.showinfo("Transaction completed", f"You successfully bought {buying} articles from the cart! ")

            except ValueError:
                messagebox.showinfo("Message","There has to be at least one article in the cart to complete the transaction!")

        buying_article_button = Button(top3, text="Buy articles from the cart", command=Buy_articles_from_cart)

        def Delete_articles_from_cart():
            try:
                delete = shop_listbox2.curselection()
                shop_listbox2.delete(delete)

            except Exception:
                messagebox.showerror("Error","You need to select an article in order to delete it!")

        deleting_article_button = Button(top3, text="Remove article from the cart", command=Delete_articles_from_cart)

        def Tickets_bundesliga():
            top4 = Toplevel()
            top4.title("Tickets for Bundesliga league matches")
            top4.geometry("300x120")
            tickets_label = Label(top4, text="Select the ticket that you want to buy")
            tickets_listbox = Listbox(top4)
            with open("tickets_bundesliga.txt") as file:
                for i in file:
                    tickets_listbox.insert(END, i)
            tickets_label.pack()
            tickets_listbox.pack()
            tickets_listbox.config(height=4, width=35)

            def Buying_tickets_bundesliga():
                try:
                    get_ticket=tickets_listbox.get(tickets_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Buy tickets(amount)")
                    top6.geometry("300x100")
                    buying_label=Label(top6,text="Enter the amount of tickets you want to buy")
                    buying_entry=Entry(top6)
                    buying_label.pack()
                    buying_entry.pack()

                except Exception:
                    messagebox.showinfo("Message","You need to select a ticket!")

                def Buying_amount():
                    try:
                        if buying_entry.get()=="" or buying_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Message",f"You bought {buying_entry.get()} tickets for {get_ticket}")

                    except ValueError:
                        messagebox.showerror("Error","You need to enter the amount of tickets with numbers!")

                try:

                    buying_button=Button(top6,text="Confirm",command=Buying_amount)
                    buying_button.pack()

                except Exception:
                    messagebox.showerror("Error","You need to select a ticket!")

            try:
                tickets_button = Button(top4, text="Buy a ticket", command=Buying_tickets_bundesliga)
                tickets_button.pack()

            except Exception:
                messagebox.showinfo("Message", "You need to select a ticket!")

        def Tickets_bundesliga2():
            top5 = Toplevel()
            top5.title("Tickets for Bundesliga 2 league matches")
            top5.geometry("300x120")
            tickets_bundesliga2_label = Label(top5, text="Select the ticket that you want to buy")
            tickets_bundesliga2_listbox = Listbox(top5)
            with open("tickets_bundesliga2.txt") as file:
                for i in file:
                    tickets_bundesliga2_listbox.insert(END, i)

            tickets_bundesliga2_label.pack()
            tickets_bundesliga2_listbox.pack()
            tickets_bundesliga2_listbox.config(height=4, width=35)

            def Buying_tickets_bundesliga2():
                try:
                    get_ticket=tickets_bundesliga2_listbox.get(tickets_bundesliga2_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Buy tickets(amount)")
                    top6.geometry("300x100")
                    buying_label=Label(top6,text="Enter the amount of tickets you want to buy")
                    buying_entry=Entry(top6)
                    buying_label.pack()
                    buying_entry.pack()

                except Exception:
                    messagebox.showinfo("Message","You need to select a ticket!")

                def Buying_amount():
                    try:
                        if buying_entry.get()=="" or buying_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Message",f"You bought {buying_entry.get()} tickets for {get_ticket}")

                    except ValueError:
                        messagebox.showerror("Error","You need to enter the amount of tickets with numbers!")

                try:

                    buying_button = Button(top6, text="Confirm", command=Buying_amount)
                    buying_button.pack()

                except Exception:
                    messagebox.showerror("Error", "You need to select a ticket!")

            try:
                tickets_button = Button(top5, text="Buy a ticket", command=Buying_tickets_bundesliga2)
                tickets_button.pack()

            except Exception:
                messagebox.showinfo("Message", "You need to select a ticket!")

        shop_button = Button(top3, text="Add to cart", command=Cart)
        shop_button2 = Button(top3, text="Tickets for Bundesliga league matches", command=Tickets_bundesliga)
        shop_button3 = Button(top3, text="Tickets for Bundesliga 2 league matches", command=Tickets_bundesliga2)
        shop_label.pack()
        shop_listbox.pack()
        shop_button.pack()
        cart_label.pack()
        shop_listbox2.pack()
        buying_article_button.pack()
        deleting_article_button.pack()
        shop_button2.pack()
        shop_button3.pack()
        shop_listbox.config(height=8, width=36)
        shop_listbox2.config(height=8, width=36)

    german_button3=Button(top,text="Bundesliga clubs trophies",command=Bundesliga_clubs_trophies)
    german_button4=Button(top,text="Bundesliga 2 clubs trophies",command=Bundesliga2_clubs_trophies)
    german_button5=Button(top,text="Online Shop",command=Online_shop)
    german_button6=Button(top,text="Matches schedule",command=Matches_schedule)

    german_listbox.config(width=25)
    german_listbox2.config(width=25)
    german_label.pack()
    german_listbox.pack()
    german_button3.pack()
    german_label2.pack()
    german_listbox2.pack()
    german_button4.pack()
    german_label3.pack()
    german_entry.pack()
    german_button6.pack()
    german_button5.pack()

def France():
    top=Toplevel()
    top.title("French league")
    top.geometry("500x510")
    french_label=Label(top,text="Ligue 1 clubs")
    french_listbox=Listbox(top)
    with open("ligue1.txt")as file:
        for i in file:
            french_listbox.insert(END,i)

    french_label2=Label(top,text="Ligue 2 clubs")
    french_listbox2=Listbox(top)
    with open("ligue2.txt")as file:
        for i in file:
            french_listbox2.insert(END,i)

    french_label3=Label(top,text="Insert the league name to see info about upcoming matches:")
    french_entry=Entry(top)

    def Ligue1_clubs_trophies():
        top1=Toplevel()
        top1.geometry("300x300")
        top1.title("Ligue 1 trophies")
        trophies_label=Label(top1,text="Number of trophies of all Ligue 1 clubs")
        trophies_listbox=Listbox(top1)
        with open("trophies_ligue1.txt")as file:
            for i in file:
                trophies_listbox.insert(END,i)

        trophies_listbox.config(height=15,width=27)
        trophies_label.pack()
        trophies_listbox.pack()

    def Ligue2_clubs_trophies():
        top2=Toplevel()
        top2.geometry("300x300")
        top2.title("Ligue 2 trophies")
        trophies_label2=Label(top2,text="Number of trophies of all Ligue 2 clubs")
        trophies_listbox2=Listbox(top2)
        with open("trophies_ligue2.txt")as file:
            for i in file:
                trophies_listbox2.insert(END,i)

        trophies_listbox2.config(height=15,width=27)
        trophies_label2.pack()
        trophies_listbox2.pack()

    def Matches_schedule():
        try:
            if french_entry.get()=="Ligue 1" or french_entry.get()=="ligue 1":
                top_games_schedule=Toplevel()
                top_games_schedule.title("Ligue 1 matches schedule")
                top_games_schedule_listbox=Listbox(top_games_schedule)
                top_games_schedule_listbox.pack()
                top_games_schedule_listbox.config(height=20,width=60)

                with open("matches_schedule_ligue1.txt")as file:
                    for i in file:
                        top_games_schedule_listbox.insert(END,i)

            if french_entry.get().isdigit()==True:
                raise ValueError

            if french_entry.get()=="":
                raise ValueError

            if french_entry.get()!="Ligue 1" and french_entry.get()!="ligue 1" and french_entry.get()!="Ligue 2" and french_entry.get()!="ligue 2":
                raise ValueError

            if french_entry.get().isnumeric()==True:
                raise ValueError

            if french_entry.get() == "Ligue 2" or french_entry.get() == "ligue 2":
                top_games_schedule = Toplevel()
                top_games_schedule.title("Ligue 2 matches schedule")
                top_games_schedule_listbox = Listbox(top_games_schedule)
                top_games_schedule_listbox.pack()
                top_games_schedule_listbox.config(height=20, width=60)

                with open("matches_schedule_ligue2.txt") as file:
                    for i in file:
                        top_games_schedule_listbox.insert(END, i)

        except ValueError:
            messagebox.showerror("Error","You need to insert correct league name in order to see Matches schedule!")

    def Online_shop():
        top3 = Toplevel()
        top3.title("French Online Shop")
        top3.geometry("400x435")
        shop_label = Label(top3, text="Select an item to add to your cart")
        cart_label = Label(top3, text="Cart of selected articles from Online Shop")
        shop_listbox = Listbox(top3)
        shop_listbox2 = Listbox(top3)
        with open("shop_france.txt") as file:
            for i in file:
                shop_listbox.insert(END, i)

        def Cart():
            try:
                get = shop_listbox.get(shop_listbox.curselection())
                shop_listbox2.insert(END, get)

            except Exception:
                messagebox.showinfo("Message", "You need to select an article to add it to the cart!")

        def Buy_articles_from_cart():
            try:
                buying = len(shop_listbox2.get(0, END))
                if buying == 0:
                    raise ValueError
                shop_listbox2.delete(0,END)

                messagebox.showinfo("Transaction completed", f"You successfully bought {buying} articles from the cart! ")

            except ValueError:
                messagebox.showinfo("Message","There has to be at least one article in the cart to complete the transaction!")

        buying_article_button = Button(top3, text="Buy articles from the cart", command=Buy_articles_from_cart)

        def Delete_articles_from_cart():
            try:
                delete = shop_listbox2.curselection()
                shop_listbox2.delete(delete)

            except Exception:
                messagebox.showerror("Error","You need to select an article in order to delete it!")

        deleting_article_button = Button(top3, text="Remove article from the cart", command=Delete_articles_from_cart)

        def Tickets_ligue1():
            top4 = Toplevel()
            top4.title("Tickets for Ligue 1 league matches")
            top4.geometry("300x120")
            tickets_label = Label(top4, text="Select the ticket that you want to buy")
            tickets_listbox = Listbox(top4)
            with open("tickets_ligue1.txt") as file:
                for i in file:
                    tickets_listbox.insert(END, i)
            tickets_label.pack()
            tickets_listbox.pack()
            tickets_listbox.config(height=4, width=35)

            def Buying_tickets_league1():
                try:
                    get_ticket=tickets_listbox.get(tickets_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Buy tickets(amount)")
                    top6.geometry("300x100")
                    buying_label=Label(top6,text="Enter the amount of tickets you want to buy")
                    buying_entry=Entry(top6)
                    buying_label.pack()
                    buying_entry.pack()

                except Exception:
                    messagebox.showinfo("Message","You need to select a ticket!")

                def Buying_amount():
                    try:
                        if buying_entry.get()=="" or buying_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Message",f"You bought {buying_entry.get()} tickets for {get_ticket}")

                    except ValueError:
                        messagebox.showerror("Error","You need to enter the amount of tickets with numbers!")

                try:

                    buying_button=Button(top6,text="Confirm",command=Buying_amount)
                    buying_button.pack()

                except Exception:
                    messagebox.showerror("Error","You need to select a ticket!")

            try:
                tickets_button = Button(top4, text="Buy a ticket", command=Buying_tickets_league1)
                tickets_button.pack()

            except Exception:
                messagebox.showinfo("Message", "You need to select a ticket!")

        def Tickets_ligue2():
            top5 = Toplevel()
            top5.title("Tickets for Ligue 2 league matches")
            top5.geometry("300x120")
            tickets_ligue2_label = Label(top5, text="Select the ticket that you want to buy")
            tickets_ligue2_listbox = Listbox(top5)
            with open("tickets_ligue2.txt") as file:
                for i in file:
                    tickets_ligue2_listbox.insert(END, i)

            tickets_ligue2_label.pack()
            tickets_ligue2_listbox.pack()
            tickets_ligue2_listbox.config(height=4, width=35)

            def Buying_tickets_league2():
                try:
                    get_ticket=tickets_ligue2_listbox.get(tickets_ligue2_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Buy tickets(amount)")
                    top6.geometry("300x100")
                    buying_label=Label(top6,text="Enter the amount of tickets you want to buy")
                    buying_entry=Entry(top6)
                    buying_label.pack()
                    buying_entry.pack()

                except Exception:
                    messagebox.showinfo("Message","You need to select a ticket!")

                def Buying_amount():
                    try:
                        if buying_entry.get()=="" or buying_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Message",f"You bought {buying_entry.get()} tickets for {get_ticket}")

                    except ValueError:
                        messagebox.showerror("Error","You need to enter the amount of tickets with numbers!")

                try:

                    buying_button = Button(top6, text="Confirm", command=Buying_amount)
                    buying_button.pack()

                except Exception:
                    messagebox.showerror("Error", "You need to select a ticket!")

            try:
                tickets_button = Button(top5, text="Buy a ticket", command=Buying_tickets_league2)
                tickets_button.pack()

            except Exception:
                messagebox.showinfo("Message", "You need to select a ticket!")

        shop_button = Button(top3, text="Add to cart", command=Cart)
        shop_button2 = Button(top3, text="Tickets for Ligue 1 league matches", command=Tickets_ligue1)
        shop_button3 = Button(top3, text="Tickets for Ligue 2 league matches", command=Tickets_ligue2)
        shop_label.pack()
        shop_listbox.pack()
        shop_button.pack()
        cart_label.pack()
        shop_listbox2.pack()
        buying_article_button.pack()
        deleting_article_button.pack()
        shop_button2.pack()
        shop_button3.pack()
        shop_listbox.config(height=8, width=36)
        shop_listbox2.config(height=8, width=36)

    french_button3=Button(top,text="Ligue 1 clubs trophies",command=Ligue1_clubs_trophies)
    french_button4=Button(top,text="Ligue 2 clubs trophies",command=Ligue2_clubs_trophies)
    french_button5=Button(top,text="Online Shop",command=Online_shop)
    french_button6=Button(top,text="Matches schedule",command=Matches_schedule)

    french_listbox.config(width=25)
    french_listbox2.config(width=25)
    french_label.pack()
    french_listbox.pack()
    french_button3.pack()
    french_label2.pack()
    french_listbox2.pack()
    french_button4.pack()
    french_label3.pack()
    french_entry.pack()
    french_button6.pack()
    french_button5.pack()

def Netherlands():
    top=Toplevel()
    top.geometry("500x510")
    top.title("Dutch league")
    dutch_label=Label(top,text="Eredivisie clubs")
    dutch_listbox=Listbox(top)
    with open("eredivisie.txt")as file:
        for i in file:
            dutch_listbox.insert(END,i)


    dutch_label2=Label(top,text="Erstedivisie clubs")
    dutch_listbox2=Listbox(top)
    with open("erstedivise.txt")as file:
        for i in file:
            dutch_listbox2.insert(END,i)

    dutch_label3=Label(top,text="Insert the league name to see info about upcoming matches:")
    dutch_entry=Entry(top)

    def Eredivisie_clubs_trophies():
        top1=Toplevel()
        top1.geometry("300x300")
        top1.title("Eredivisie trophies")
        trophies_label=Label(top1,text="Number of trophies of all Eredivisie clubs")
        trophies_listbox=Listbox(top1)
        with open("trophies_eredivisie.txt")as file:
            for i in file:
                trophies_listbox.insert(END,i)

        trophies_label.pack()
        trophies_listbox.pack()
        trophies_listbox.config(height=15,width=27)

    def Erstedivisie_clubs_trophies():
        top2=Toplevel()
        top2.geometry("300x300")
        top2.title("Erstedivisie trophies")
        trophies_label2=Label(top2,text="Number of trophies of all Erstedivisie clubs")
        trophies_listbox2=Listbox(top2)
        with open("trophies_erstedivisie.txt")as file:
            for i in file:
                trophies_listbox2.insert(END,i)

        trophies_listbox2.config(height=15,width=27)
        trophies_label2.pack()
        trophies_listbox2.pack()

    def Matches_schedule():
        try:
            if dutch_entry.get()=="Eredivisie" or dutch_entry.get()=="eredivisie":
                top_games_schedule=Toplevel()
                top_games_schedule.title("Eredivisie matches schedule")
                top_games_schedule_listbox=Listbox(top_games_schedule)
                top_games_schedule_listbox.pack()
                top_games_schedule_listbox.config(height=20,width=60)

                with open("matches_schedule_eredivisie.txt")as file:
                    for i in file:
                        top_games_schedule_listbox.insert(END,i)

            if dutch_entry.get().isdigit()==True:
                raise ValueError

            if dutch_entry.get()=="":
                raise ValueError

            if dutch_entry.get()!="Erstedivisie" and dutch_entry.get()!="erstedivisie" and dutch_entry.get()!="Eredivisie" and dutch_entry.get()!="eredivisie":
                raise ValueError

            if dutch_entry.get().isnumeric()==True:
                raise ValueError

            if dutch_entry.get() == "Erstedivisie" or dutch_entry.get() == "erstedivisie":
                top_games_schedule = Toplevel()
                top_games_schedule.title("Erstedivisie matches schedule")
                top_games_schedule_listbox = Listbox(top_games_schedule)
                top_games_schedule_listbox.pack()
                top_games_schedule_listbox.config(height=20, width=60)

                with open("matches_schedule_erstedivisie.txt") as file:
                    for i in file:
                        top_games_schedule_listbox.insert(END, i)

        except ValueError:
            messagebox.showerror("Error","You need to insert correct league name in order to see Matches schedule!")

    def Online_shop():
        top3 = Toplevel()
        top3.title("Dutch Online Shop")
        top3.geometry("400x435")
        shop_label = Label(top3, text="Select an item to add to your cart")
        cart_label = Label(top3, text="Cart of selected articles from Online Shop")
        shop_listbox = Listbox(top3)
        shop_listbox2 = Listbox(top3)
        with open("shop_netherlands.txt") as file:
            for i in file:
                shop_listbox.insert(END, i)

        def Cart():
            try:
                get = shop_listbox.get(shop_listbox.curselection())
                shop_listbox2.insert(END, get)

            except Exception:
                messagebox.showinfo("Message", "You need to select an article to add it to the cart!")

        def Buy_articles_from_cart():
            try:
                buying = len(shop_listbox2.get(0, END))
                if buying == 0:
                    raise ValueError
                shop_listbox2.delete(0,END)

                messagebox.showinfo("Transaction completed", f"You successfully bought {buying} articles from the cart! ")

            except ValueError:
                messagebox.showinfo("Message","There has to be at least one article in the cart to complete the transaction!")

        buying_article_button = Button(top3, text="Buy articles from the cart", command=Buy_articles_from_cart)

        def Delete_articles_from_cart():
            try:
                delete = shop_listbox2.curselection()
                shop_listbox2.delete(delete)

            except Exception:
                messagebox.showerror("Error","You need to select an article in order to delete it!")

        deleting_article_button = Button(top3, text="Remove article from the cart", command=Delete_articles_from_cart)

        def Tickets_eredivisie():
            top4 = Toplevel()
            top4.title("Tickets for Eredivisie league matches")
            top4.geometry("300x120")
            tickets_label = Label(top4, text="Select the ticket that you want to buy")
            tickets_listbox = Listbox(top4)
            with open("tickets_eredivisie.txt") as file:
                for i in file:
                    tickets_listbox.insert(END, i)
            tickets_label.pack()
            tickets_listbox.pack()
            tickets_listbox.config(height=4, width=35)

            def Buying_tickets_eredivisie():
                try:
                    get_ticket=tickets_listbox.get(tickets_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Buy tickets(amount)")
                    top6.geometry("300x100")
                    buying_label=Label(top6,text="Enter the amount of tickets you want to buy")
                    buying_entry=Entry(top6)
                    buying_label.pack()
                    buying_entry.pack()

                except Exception:
                    messagebox.showinfo("Message","You need to select a ticket!")

                def Buying_amount():
                    try:
                        if buying_entry.get()=="" or buying_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Message",f"You bought {buying_entry.get()} tickets for {get_ticket}")

                    except ValueError:
                        messagebox.showerror("Error","You need to enter the amount of tickets with numbers!")

                try:

                    buying_button=Button(top6,text="Confirm",command=Buying_amount)
                    buying_button.pack()

                except Exception:
                    messagebox.showerror("Error","You need to select a ticket!")

            try:
                tickets_button = Button(top4, text="Buy a ticket", command=Buying_tickets_eredivisie)
                tickets_button.pack()

            except Exception:
                messagebox.showinfo("Message", "You need to select a ticket!")

        def Tickets_erstedivisie():
            top5 = Toplevel()
            top5.title("Tickets for Erstedivisie league matches")
            top5.geometry("300x120")
            tickets_erstedivisie_label = Label(top5, text="Select the ticket that you want to buy")
            tickets_erstedivisie_listbox = Listbox(top5)
            with open("tickets_erstedivisie.txt") as file:
                for i in file:
                    tickets_erstedivisie_listbox.insert(END, i)

            tickets_erstedivisie_label.pack()
            tickets_erstedivisie_listbox.pack()
            tickets_erstedivisie_listbox.config(height=4, width=35)

            def Buying_tickets_erstedivisie():
                try:
                    get_ticket=tickets_erstedivisie_listbox.get(tickets_erstedivisie_listbox.curselection())
                    top6=Toplevel()
                    top6.title("Buy tickets(amount)")
                    top6.geometry("300x100")
                    buying_label=Label(top6,text="Enter the amount of tickets you want to buy")
                    buying_entry=Entry(top6)
                    buying_label.pack()
                    buying_entry.pack()

                except Exception:
                    messagebox.showinfo("Message","You need to select a ticket!")

                def Buying_amount():
                    try:
                        if buying_entry.get()=="" or buying_entry.get().isdigit()==False:
                            raise ValueError
                        messagebox.showinfo("Message",f"You bought {buying_entry.get()} tickets for {get_ticket}")

                    except ValueError:
                        messagebox.showerror("Error","You need to enter the amount of tickets with numbers!")

                try:

                    buying_button = Button(top6, text="Confirm", command=Buying_amount)
                    buying_button.pack()

                except Exception:
                    messagebox.showerror("Error", "You need to select a ticket!")

            try:
                tickets_button = Button(top5, text="Buy a ticket", command=Buying_tickets_erstedivisie)
                tickets_button.pack()

            except Exception:
                messagebox.showinfo("Message", "You need to select a ticket!")

        shop_button = Button(top3, text="Add to cart", command=Cart)
        shop_button2 = Button(top3, text="Tickets for Eredivisie league matches", command=Tickets_eredivisie)
        shop_button3 = Button(top3, text="Tickets for Erstedivisie league matches", command=Tickets_erstedivisie)
        shop_label.pack()
        shop_listbox.pack()
        shop_button.pack()
        cart_label.pack()
        shop_listbox2.pack()
        buying_article_button.pack()
        deleting_article_button.pack()
        shop_button2.pack()
        shop_button3.pack()
        shop_listbox.config(height=8, width=36)
        shop_listbox2.config(height=8, width=36)

    dutch_button3=Button(top,text="Eredivisie clubs trophies",command=Eredivisie_clubs_trophies)
    dutch_button4=Button(top,text="Erstedivisie clubs trophies",command=Erstedivisie_clubs_trophies)
    dutch_button5=Button(top,text="Online Shop",command=Online_shop)
    dutch_button6=Button(top,text="Matches schedule",command=Matches_schedule)

    dutch_listbox.config(width=25)
    dutch_listbox2.config(width=25)
    dutch_label.pack()
    dutch_listbox.pack()
    dutch_button3.pack()
    dutch_label2.pack()
    dutch_listbox2.pack()
    dutch_button4.pack()
    dutch_label3.pack()
    dutch_entry.pack()
    dutch_button6.pack()
    dutch_button5.pack()

root=Tk()
root.title("EuroTop6")
root.geometry("250x165")
england=Button(root,text="English league",command=England)
spain=Button(root,text="Spanish league",command=Spain)
italy=Button(root,text="Italian league",command=Italy)
germany=Button(root,text="German league",command=Germany)
france=Button(root,text="French league",command=France)
netherlands=Button(root,text="Dutch league",command=Netherlands)
england.pack()
spain.pack()
italy.pack()
germany.pack()
france.pack()
netherlands.pack()
mainloop()