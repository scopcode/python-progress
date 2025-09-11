favourite_places = {"shubham" : ["manali", "kanha", "delhi"],
                    "elon" : ["miami", "newyork", "l.a"],
                    "putin" : ["russia", "moscow", "st.petersberg"],
                    }
for key,value in favourite_places.items():
    print(key.title() + "'s favourite places are :")
    for place in value:
        print(place.title())
    print("\n")