import random
import tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number card 1 to 10
        for card in range(1, 11):
            name = 'png/{}_{}.{}'.format(suit, str(card), 'png')
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # next face cards
        for card in face_cards:
            name = 'png/{}_{}.{}'.format(suit, str(card), 'png')
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value

        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    # dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins!")


def initial_deal():
    deal_player()
    dealer_hand.append( deal_card( dealer_card_frame ) )
    dealer_score_label.set( score_hand( dealer_hand ) )
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    dealer_card_frame.destroy()
    player_card_frame.destroy()

    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    result_text.set("")

    dealer_hand = []
    player_hand = []
    initial_deal()


def shuffle():
        random.shuffle(deck)


def play():
    initial_deal()
    mainWindow.mainloop()



mainWindow = tkinter.Tk()

mainWindow.title("BlackJack")
mainWindow.geometry('640x480')
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)
# embedded frame hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)
# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

newgame_button = tkinter.Button(button_frame, text="New Game", command=new_game)
newgame_button.grid(row=0, column=2)

# load cards

cards = []
load_images(cards)
print(cards)
deck = list(cards) + list(cards) + list(cards)

shuffle()

dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()





# svg = rsvg.Handle(file='cards.svg')
# pixbuf = svg.get_pixbuf(id='#3_diamond')
#
# mainWindow.title("Hello World")
# mainWindow.geometry('640x480+8+400')
# canvas = tkinter.Canvas(mainWindow, width=640, height=480)
# canvas.grid(row=0, column=0)
# canvas.create_image(pixbuf)
# mainWindow.mainloop()
