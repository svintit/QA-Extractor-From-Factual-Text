n_chunk_q_dict = {
    "PERSON": [
        "Who is {ENT} in the context of this text?",
        "Why is {ENT} mentioned?",
        "Would it be said that {ENT} is an important character in this piece of text?"
    ],
    "ORG": [
        "Why did {ENT} appear in the text?",
    ],
    "GPE": [
        "What happened in {ENT}?",
        "{ENT} appears in the text, why is this the case?"
    ],
    "DATE": [
        "What happened {VERB} {ENT}?",
        "Why is {ENT} mentioned?"
    ],
    "LOC": [
        "What is stated about {ENT}?"
    ],
    "MONEY": [
        "Why {VERB} the amount of {ENT} mentioned?"
    ]
}

advanced_q_dict = {
    "PERSON": [
        "{WH} {EXTRACTED}?",
        "In the context of this text, {WH} {EXTRACTED}?",
        "As given in the text, {WH} {EXTRACTED}?",
        "{WH} {EXTRACTED}, as stated in the text?"
    ],
    "LOC": [
        "{WH} {EXTRACTED}?"
    ]
}
