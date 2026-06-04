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
    "promotion", "limited", "deal","buy"
],
"hate_words":[
    "racist", "never","bigot", "supremacy", "inferior", "discrimination",
    "extremist", "segregation", "genocide", "hate", "hatred","despise ",
    "prejudice", "intolerance", "hostility", "bias", "oppression","hate"
],
"creepy_words": [
    "send pics","baby","bby","send me pics","send photo","send me photo","send image","nude","nudes","alone","video call","meet alone"
],
"threat_words": [
    "kill", "murder","regret", "attack", "destroy", "harm", "shoot",
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
positive_words =intents["normal_words"]+intents["love_words"]+[
    "happy", "great", "excellent", "amazing", "awesome",
    "fantastic", "wonderful", "brilliant", "good", "success",
    "win", "smile", "kind", "helpful", "respect", "joy",
    "peace", "hope", "cheerful", "positive","love"
]
negative_words = intents["spam_words"]+intents["scam_phishing_words"]+intents["profanity_words"]+intents["threat_words"]+intents["hate_words"]+intents["creepy_words"]+["sad", "angry", "upset", "depressed", "lonely", "hurt",
    "stress", "cry", "pain", "fear", "anxiety", "worried",
    "tired", "broken", "disappointed", "frustrated", "miserable",
    "guilty", "regret", "failure","hate","bitchi"
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
    return best_intent

                                                                             #Intent : care                                                                  ##Sentiment : Positive
                                                                             #Action : KEEP

def chech_sentiment(text):
    positive=0
    negative=0
    for word in positive_words:
        if word in text:
            positive+=1
    for word in negative_words:
        if word in text:
            negative+=1
    if positive >negative:
        return "positive"
    elif positive< negative:
        return "negative"
    return "netural"

def decision_make(intent,sentiment):
    
    if intent in ["spam_words","scam_phishing_words","threat_words"]:
        return "Block"
    elif intent in ["hate_words","creepy_words"]:
        return "Block"
    elif intent in ["profanity_words","harassment_word","negative_words","hate_words"]:
        return "Block"
    elif intent in ["help_request_words"]:
        return "Review"
    elif intent in ["normal_words","love_words"]:
        return "Keep"
    if sentiment == "negative":
        print("Negative sentiment detected")

    return "Keep"    


while True:
    text=input("enter message: ").lower()
    if text=="exit":
        print("program ended")
        break
    intent=check_intent(text)
    sentiment=chech_sentiment(text)
    decision=decision_make(intent,sentiment)

    print("Intent :",intent)
    print("Sentiment :",sentiment)
    print("Decision :", decision)
