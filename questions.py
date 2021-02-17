questions = [
    ('Kanji -> Meaning', 
        {
            "name": "Kanji -> Meaning",
            "qfmt": '<center><p>What is the meaning of the following Kanji:</p><h1>{{kanji}}</h1></center>',
            "afmt": '{{FrontSide}}<center><p>The following meanings are correct:</p><h2>{{translation}}</h2></center>',
        }
    ), 
    ('Meaning -> Kanji', 
        {
            "name": "Meaning -> Kanji",
            "qfmt": '<center><p>What Kanji has the following meaning:</p><h2>{{translation}}</h2></center>',
            "afmt": '{{FrontSide}}<center><p>The following Kanji is the correct answer:</p><h1>{{kanji}}</h1></center>',
        }
    )
]