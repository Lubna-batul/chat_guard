posi_intent_words = {
    "positive": [
        "care", "help", "support", "guide", "assist", "teach", "learn", "thank",
        "thanks", "appreciate", "respect", "trust", "welcome", "friend", "kind", "kindness", "happy", "joy",
        "smile", "peace", "hope", "encourage", "motivate", "inspire", "understand", "listen", "cooperate", "collaborate",
        "teamwork", "honest", "honesty", "loyal", "loyalty", "adore", "cherish", "comfort", "protect", "encouragement",
        "excellent", "amazing", "awesome", "fantastic", "wonderful", "great", "good", "brilliant", "positive", "success",
        "successful", "achievement", "achieve", "win", "winner", "progress", "improve", "improvement", "growth", "opportunity",
        "solution", "solve", "recommend", "suggest", "advice", "clarify", "explain", "information", "knowledge", "education",
        "study", "book", "family", "friendship", "community", "generous", "gratitude", "cheerful", "delight", "optimistic",
        "polite", "courteous", "gentle", "lovely", "beautiful", "cute", "sweet", "dear", "heart",
        "affection", "beloved", "soulmate", "blessing", "faith", "patience", "forgive",
        "forgiveness", "safe", "security", "trustworthy", "valuable", "creative", "innovation", "productive"
    ],
    "care_words": [
        "care", "caring", "support", "protect", "comfort", "encourage",
        "understand", "listen", "help", "assist", "guide", "advice",
        "concern", "worry", "check", "safe", "stay safe", "take care",
        "be careful", "rest", "sleep well", "eat well", "drink water",
        "get well soon", "recover", "healing", "hope", "trust", "respect",
        "kind", "kindness", "gentle", "patient", "patience", "peace",
        "calm", "relax", "smile", "cheer up", "happy", "joy",
        "friend", "friendship", "family", "together", "always here",
        "here for you", "with you", "believe in you", "proud of you",
        "stay strong", "don't worry", "everything will be okay",
        "take care of yourself", "miss you", "thinking of you"
    ],
    "love_words": [
        "love", "dear", "beloved", "adore", "care", "kiss", "romance", "crush",
        "soulmate", "affection", "beautiful",
        "angel", "heart", "forever", "thanks"
    ],
    "help_request_words": [
        "help", "support", "guide", "assist", "question", "advice",
        "explain", "teach", "learn", "clarify", "understand",
        "solution", "problem", "issue", "suggest", "recommend",
        "instruction", "information", "answer", "query"
    ],
    "normal_words": [
        "hello", "thanks", "welcome", "morning",
        "evening", "friend", "family", "school", "college",
        "study", "book", "computer", "food", "water",
        "travel", "music", "movie", "game", "work"
    ]
}


def positive_intent(text):
    scores = {}
    words = text.split()
    for intent, keywords in posi_intent_words.items():
        count = 0
        for keyword in keywords:
            if keyword in words:
                count += 1
        scores[intent] = count
    best_intent = max(scores, key=scores.get)

    if scores[best_intent] == 0:
        return "Normal_words"
    return best_intent


negative_intent_words = {
    "negative": [
        "hate", "can't", "cannot", "hatred", "angry", "anger", "furious", "rage", "annoy", "annoying", "upset",
        "depressed", "hurt", "harm", "wish", "damage", "destroy", "attack", "assault", "violence",
        "kill", "murder", "shoot", "stab", "bomb", "threat", "revenge", "punish", "eliminate", "execute",
        "racist", "bigot", "supremacy", "inferior", "discrimination", "prejudice", "hostility", "bias", "oppression", "genocide",
        "idiot", "stupid", "loser", "moron", "worthless", "pathetic", "dumb", "fool", "jerk", "clown",
        "garbage", "trash", "upset", "useless", "failure", "ugly", "crazy", "weirdo", "lame", "nonsense", "scumbag",
        "asshole", "bastard", "douche", "wtf", "bullshit", "damn", "hell", "crap", "freak", "meet", "tonight",
        "scam", "ruining", "ruin", "fraud", "cheat", "steal", "theft", "phishing", "otp", "password", "cvv", "credential",
        "hack", "hacker", "malware", "virus", "exploit", "blackmail", "extort", "manipulate", "deceive", "fake",
        "nude", "nudes", "creepy", "stalker", "harass", "harassment", "abuse", "abusive", "toxic", "toxicity",
        "regret", "guilty", "pathetic", "miserable", "frustrated", "despise", "intolerance", "extremist", "segregation",
        "hostile", "revengeful", "threatening", "dangerous", "harmful", "negative"
    ],
    "harassment_word": {
        "idiot": 3, "stupid": 3, "loser": 3,
        "pathetic": 3, "worthless": 4, "moron": 3, "dumb": 3, "fool": 2, "jerk": 2, "annoying": 1,
        "clown": 2, "trash": 2, "garbage": 2, "nonsense": 1, "ugly": 2, "crazy": 2, "weirdo": 2,
        "lame": 1, "failure": 3, "useless": 3
    },
    "spam_words": {
        "otp": 5, "password": 5, "cvv": 5, "banking": 3, "verification": 2, "urgent": 2, "account": 1,
        "login": 2, "credential": 4, "wiretransfer": 5, "giftcard": 4, "bitcoin": 2, "wallet": 2, "pin": 5,
        "securitycode": 5, "authorize": 2, "reset": 1, "confirm": 1, "transaction": 2, "payment": 1
    },
    "spam_words2": {
        "free": 2, "offer": 1, "discount": 1, "winner": 2, "lottery": 4, "bonus": 1, "cash": 2,
        "reward": 2, "claim": 2, "prize": 3, "earn": 1, "income": 1, "profit": 1,
        "investment": 2, "crypto": 2, "click": 2, "subscribe": 1, "promotion": 1, "limited": 1,
        "deal": 1, "buy": 1, "scam": 5
    },
    "hate_words": {
        "racist": 4, "bigot": 4, "supremacy": 5, "inferior": 3, "discrimination": 4, "extremist": 4,
        "segregation": 4, "genocide": 5, "hate": 4, "hatred": 4, "despise": 4, "prejudice": 3,
        "intolerance": 3, "hostility": 3, "bias": 2, "oppression": 4
    },
    "creepy_words": {
        "baby": 2, "babe": 2, "sweetheart": 2, "darling": 2, "honey": 2,
        "princess": 2, "sexy": 4, "hot": 3, "kiss": 3, "romance": 2, "crush": 1, "date": 1,
        "alone": 2, "private": 2, "secret": 2, "meet": 2, "video call": 2, "voice call": 2,
        "late night": 3, "midnight": 3, "pics": 3, "selfie": 3,
        "send pics": 4, "nude": 5, "nudes": 5, "lingerie": 4, "bedroom": 3, "cuddle": 2,
        "touch": 3, "massage": 3
    },
    "emotions": {
        "angry": 3, "anger": 3, "furious": 4, "rage": 4, "annoy": 1, "annoying": 1, "upset": 2,
        "depressed": 3, "regret": 3, "guilty": 2, "miserable": 3, "frustrated": 3, "hostile": 3,
        "dangerous": 4, "harmful": 4, "negative": 1
    },
    "threat_words": {
        "kill": 5, "murder": 5, "attack": 4, "destroy": 4, "harm": 4, "shoot": 5, "stab": 5,
        "bomb": 5, "revenge": 4, "threat": 4, "hunt": 4, "assault": 4, "violence": 4,
        "eliminate": 5, "execute": 5, "punish": 3, "beat": 4, "hurt": 2
    },
    "profanity_words": {
        "damn": 1, "hell": 1, "crap": 1, "bastard": 3, "asshole": 4, "jerk": 2, "scumbag": 3,
        "douche": 3, "wtf": 2, "bullshit": 3, "trash": 2, "garbage": 2, "screw": 2, "freak": 1,
        "nonsense": 1, "shit": 2, "bitch": 4
    },
    "scam_phishing_words": {
        "otp": 5, "password": 5, "cvv": 5, "banking": 3, "verification": 2,
        "urgent": 2, "account": 1,
        "login": 2, "credential": 4, "wiretransfer": 5, "giftcard": 4, "bitcoin": 2, "wallet": 2,
        "pin": 5, "securitycode": 5, "authorize": 2, "reset": 1, "confirm": 1, "transaction": 2, "payment": 1
    }
}


def negative_intent(text):
    scores = {}
    for intent, keywords in negative_intent_words.items():
        count = 0
        for keyword in keywords:
            if f" {keyword} " in f" {text} ":
                count += 1
        scores[intent] = count
    best_intent = max(scores, key=scores.get)

    if scores[best_intent] == 0:
        return "Normal_words"
    return best_intent


def positive_sentiment(text):
    positive = 0
    for words in posi_intent_words.values():
        for word in words:
            if f" {word} " in f" {text} ":
                positive += 1
    return positive


def negative_sentiment(text):
    negative = 0
    for words in negative_intent_words.values():
        for word in words:
            if f" {word} " in f" {text} ":
                negative += 1
    return negative


def sentiment_check(text):
    positive = positive_sentiment(text)
    negative = negative_sentiment(text)

    if positive >negative:
        return "Positive"
    elif negative >positive:
        return "Negative"
    else:
        return "Neutral"


def decision_make(bad_intent, good_intent, sentiment):
    # +intent and +sentiment
    if good_intent != "Normal_words" and bad_intent == "Normal_words" and sentiment == "Positive":
        return "Keep"
    # +intent and -sentiment
    if good_intent != "Normal_words" and sentiment == "Negative":
        return "Review"
    # +intent and neutral sentiment
    if good_intent != "Normal_words" and sentiment == "Neutral":
        return "Keep"
    # -intent and -sentiment
    if bad_intent != "Normal_words" and sentiment == "Negative":
        return "Block"
    # -intent and +sentiment
    if bad_intent != "Normal_words" and sentiment == "Positive":
        return "Block"
    # -intent and neutral sentiment
    if bad_intent != "Normal_words" and sentiment == "Neutral":
        return "Block"
    if bad_intent != "Normal_words":
        return "Block"
    return "Keep"

def normalize_text(text):
    text = text.lower()
    replacements = {
        "@": "a",
        "8": "b",  
       "4": "a",
        "(": "c",
        "<": "c",
        "3": "e",
        "6": "g",
        "9": "g",
        "!": "i",
        "1": "i",
        "|": "i",
        "0": "o",
        "$": "s",
        "5": "s",
        "7": "t",
        "+": "t",
        "2": "z",
        "*": "u",
    }
    result = ""
    for ch in text:
        result += replacements.get(ch, ch)
    for ch in ".,?:;()[]/_-":
        result = result.replace(ch, "")
    return result


while True:
    text = input("enter message: ")
    text = normalize_text(text)
    good_intent = positive_intent(text)
    bad_intent = negative_intent(text)
    sentiment = sentiment_check(text)
    decision = decision_make(bad_intent, good_intent, sentiment)
    if good_intent != "Normal_words":
        final_intent = good_intent
    elif bad_intent != "Normal_words":
        final_intent = bad_intent
    else:
        final_intent = "Normal_words"  # Fixed typo: was "Norml_words"
    print("Intent:", final_intent)
    print("Sentiment:", sentiment)
    print("Decision:", decision)