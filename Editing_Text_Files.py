rudewords = {"arse bandit":"a********",
    "arse-licker":"a********",
    "brussel sprout fondler":"b*******************",
    "budgie smuggler":"b************",
    "bullshit":"b*****",
    "cheese eating surrender monkey":"c************************",
    "cunt":"c**",
    "dickhead":"d*****",
    "fudge packer":"f*********",
    "jerk":"j**",
    "knob":"k**",
    "knob jockey":"k********",
    "knobhead":"k*****",
    "meatstick sucker":"m*************",
    "prick":"p***",
    "pussy":"p***",
    "royal nitwit":"r*********",
    "shithead":"s*****",
    "turd burgler":"t*********",
    "twat":"t**",
    "twerp":"t***",
    "wanker":"w****",
    "shit":"s***",
    "fuck":"f**",
    "fucking":"f**",
    "crap":"c**",
    "whore":"w***",
    "puta":"p**",
    "cock sucker":"c********",
    "butthole":"b*****",
    "butt muncher":"b*********",
    "motherfucker":"m*********",
    "mother fucker":"m**********",
    "merde":"m***",
    "cock":"c**",
    "cock hungry":"c********",
    "nit wit":"n****",
    "nitwit":"n****"}
    
with open('text.txt', 'w') as f:
    f.write("You fucking idiot")

with open('text.txt', 'r') as f:
    for storedText in f.readlines():
        newText = []
        newText = storedText.split()
        alteredText = newText 
        for comparedWord in newText:
            if comparedWord in rudewords:
                print(f"{comparedWord} is a rude word")
                censoredWord = rudewords[comparedWord]
                alteredText = list(map(lambda item:item.replace(comparedWord, censoredWord), alteredText))
            else:
                print(f"{comparedWord} is not a rude word")


finalText = ' '.join(alteredText)
print(finalText)

with open('text.txt', 'w') as f:
    f.write(finalText) 