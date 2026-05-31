intents={
    "harassment_word": [
    "idiot", "stupid", "loser", "pathetic", "worthless", "moron",
    "dumb", "fool", "jerk", "annoying", "clown", "trash",
    "garbage", "nonsense", "ugly", "crazy", "weirdo", "lame",
    "failure", "useless"
],
"spam_words": [
    "free", "offer", "discount", "winner", "lottery", "bonus",
    "cash", "reward", "claim", "prize", "earn", "income",
    "profit", "investment", "crypto", "click", "subscribe",
    "promotion", "limited", "deal"
],
"hate_words":[
    "racist", "bigot", "supremacy", "inferior", "discrimination",
    "extremist", "segregation", "genocide", "hate", "hatred",
    "prejudice", "intolerance", "hostility", "bias", "oppression"
],
"threat_words": [
    "kill", "murder", "attack", "destroy", "harm", "shoot",
    "stab", "bomb", "revenge", "threat", "hunt", "assault",
    "violence", "eliminate", "execute", "punish", "beat", "hurt"
],
"profanity_words": [
    "damn", "hell", "crap", "bastard", "asshole", "jerk",
    "scumbag", "douche", "wtf", "bullshit", "trash",
    "garbage", "screw", "freak", "nonsense"
],
"love_words": [
    "love", "darling", "sweetheart", "honey", "baby", "dear",
    "beloved", "adore", "care", "kiss", "romance", "crush",
    "soulmate", "affection", "lovely", "beautiful", "cute",
    "angel", "heart", "forever"
],
"help_request_words":[
    "help", "support", "guide", "assist", "question", "advice",
    "explain", "teach", "learn", "clarify", "understand",
    "solution", "problem", "issue", "suggest", "recommend",
    "instruction", "information", "answer", "query"
],
"scam_phishing_words": [
    "otp", "password", "cvv", "banking", "verification",
    "urgent", "account", "login", "credential", "wiretransfer",
    "giftcard", "bitcoin", "wallet", "pin", "securitycode",
    "authorize", "reset", "confirm", "transaction", "payment"
],
"normal_words": [
    "hello", "hi", "thanks", "welcome", "morning",
    "evening", "friend", "family", "school", "college",
    "study", "book", "computer", "food", "water",
    "travel", "music", "movie", "game", "work"
] 
}
positive_words = [
    "happy", "great", "excellent", "amazing", "awesome",
    "fantastic", "wonderful", "brilliant", "good", "success",
    "win", "smile", "kind", "helpful", "respect", "joy",
    "peace", "hope", "cheerful", "positive"
]

negative_words = [
    "sad", "angry", "upset", "depressed", "lonely", "hurt",
    "stress", "cry", "pain", "fear", "anxiety", "worried",
    "tired", "broken", "disappointed", "frustrated", "miserable",
    "guilty", "regret", "failure"
]

def check_intent(text):
    scores={}
    for intent, keywords in intents.items():
        count=0
    for keyword in keywords:
        if keyword in text:
            count+=1
        scores[intent]=count 
    best_intent=max(scores,key=scores.get)
    if scores[best_intent]==0:
        return "Normal"
    else:
        return best_intent


                                                                             #Intent : care
                                                                             ##Sentiment : Positive
                                                                             #Action : KEEP



def chech_sentiment(text):
    positive=0
    negative=0
    for word in text:
        if word in positive_words:
            positive+=1
    for word in text:
        if word in negative_words:
            negative+=1
    if positive >negative:
        print("Sentiment : Positive")
    elif positive< negative:
        print("Sentiment : Negative")
    else:
        print("Sentiment : Neutral ")

while True:
    text=input("enter message: ")
    if text=="exit":
        print("program ended")
        break
    intention=check_intent(text)
    sentiment=chech_sentiment(text)
    print("Intent :",intention)
    print("Sentiment :",sentiment)
