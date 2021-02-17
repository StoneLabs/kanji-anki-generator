questions = [
    ('Kanji -> Meaning', 
        {
            "name": "Kanji Meaning",
            "qfmt": '<center><p>What is the meaning of the following Kanji:</p><h1>{{kanji}}</h1></center>',
            "afmt": '{{FrontSide}}<center><p>The following meanings are correct:</p><h2>{{translation}}</h2></center>',
        }
    ), 
    ('Meaning -> Kanji', 
        {
            "name": "Kanji Meaning Reverse",
            "qfmt": '<center><p>What Kanji has the following meaning:</p><h2>{{translation}}</h2></center>',
            "afmt": '{{FrontSide}}<center><p>The following Kanji is the correct answer:</p><h1>{{kanji}}</h1></center>',
        }
    ), 
    ('Kanji Stroke count', 
        {
            "name": "Stroke Count",
            "qfmt": '<center><p>How many <b>strokes</b> does the following Kanji have:</p><h1>{{kanji}}</h1></center>',
            "afmt": '{{FrontSide}}<center><p>It has this many strokes:</p><h1>{{strokes}}</h1></center>',
        }
    ), 
    ('Kanji -> On Reading', 
        {
            "name": "Kanji On Reading",
            "qfmt": '<center><p>What are the <b>on</b> readings for the following Kanji:</p><h1>{{kanji}}</h1></center>',
            "afmt": '{{FrontSide}}<center><p>The following are correct answeres:</p><h2>{{onread}}</h2></center>',
        }
    ), 
    ('Kanji -> Kun Reading', 
        {
            "name": "Kanji Kun Reading",
            "qfmt": '<center><p>What are the <b>kun</b> readings for the following Kanji:</p><h1>{{kanji}}</h1></center>',
            "afmt": '{{FrontSide}}<center><p>The following are correct answeres:</p><h2>{{kunread}}</h2></center>',
        }
    ), 
    ('Meaning -> On Reading', 
        {
            "name": "Meaning On Reading",
            "qfmt": '<center><p>What are the <b>on</b> readings for the kanji with the following meaning:</p><h2>{{translation}}</h2></center>',
            "afmt": '{{FrontSide}}<center><p>The following are correct answeres:</p><h2>{{onread}}</h2></center>',
        }
    ), 
    ('Meaning -> Kun Reading', 
        {
            "name": "Meaning Kun Reading",
            "qfmt": '<center><p>What are the <b>kun</b> readings for the kanji with the following meaning:</p><h2>{{translation}}</h2></center>',
            "afmt": '{{FrontSide}}<center><p>The following are correct answeres:</p><h2>{{kunread}}</h2></center>',
        }
    )
]