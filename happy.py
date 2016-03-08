def clapYourHands():
    print "clap clap"
def stompYourFeet():
    print "stomp stomp"
def main():
        youreHappy=raw_input("Are you happy? ( Y or N)" ) == "Y"
        youKnowIt=raw_input("Do you know it? ( Y or N)" ) == "Y"

        if youreHappy and youKnowIt:
            clapYourHands()
            stompYourFeet()

    print "Good bye"
main()
