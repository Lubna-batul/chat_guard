posi_intent_words={
    "positive":[
    "care","help","support","guide","assist","teach","learn","thank",
    "thanks","appreciate","respect","trust","welcome","friend","kind","kindness","happy","joy",
    "smile","peace","hope","encourage","motivate","inspire","understand","listen","cooperate","collaborate",
    "teamwork","honest","honesty","loyal","loyalty","adore","cherish","comfort","protect","encouragement",
    "excellent","amazing","awesome","fantastic","wonderful","great","good","brilliant","positive","success",
    "successful","achievement","achieve","win","winner","progress","improve","improvement","growth","opportunity",
    "solution","solve","recommend","suggest","advice","clarify","explain","information","knowledge","education",
    "study","book","family","friendship","community","generous","gratitude","cheerful","delight","optimistic",
    "polite","courteous","gentle","lovely","beautiful","cute","sweet","dear","heart",
    "affection","beloved","soulmate","blessing","faith","patience","forgive",
    "forgiveness","safe","security","trustworthy","valuable","creative","innovation","productive","productive"
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
    "love", "dear","beloved", "adore", "care", "kiss", "romance", "crush",
    "soulmate", "affection", "beautiful",
    "angel", "heart", "forever","thanks"
],
"help_request_words":[
    "help", "support", "guide", "assist", "question", "advice",
    "explain", "teach", "learn", "clarify", "understand",
    "solution", "problem", "issue", "suggest", "recommend",
    "instruction", "information", "answer", "query"
],

"normal_words": [
    "hello","thanks", "welcome", "morning",
    "evening", "friend", "family", "school", "college",
    "study", "book", "computer", "food", "water",
    "travel", "music", "movie", "game", "work"
] 
}
def positive_intent(text):
    scores={}
    words=text.split()
    for intent, keywords in posi_intent_words.items():
        count=0
        for keyword in keywords:
          if keyword in words:
            count += 1
        scores[intent]=count 
    best_intent=max(scores,key=scores.get)

    if scores[best_intent]==0:
        return "Normal_words"
    return best_intent

negative_intent_words = {
    "negative":[
    "hate","can't","cannot","hatred","angry","anger","furious","rage","annoy","annoying","upset",
    "depressed","hurt","harm","wish","damage","met""destroy","attack","assault","violence",
    "kill","murder","shoot","stab","bomb","threat","revenge","punish","eliminate","execute",
    "racist","bigot","supremacy","inferior","discrimination","prejudice","hostility","bias","oppression","genocide",
    "idiot","stupid","loser","moron","worthless","pathetic","dumb","fool","jerk","clown",
    "garbage","trash","upset","useless","failure","ugly","crazy","weirdo","lame","nonsense","scumbag",
    "asshole","bastard","douche","wtf","bullshit","damn","hell","crap","freak","hateyou","meet","tonight"
    "scam","ruining","ruin","fraud","cheat","steal","theft","phishing","otp","password","cvv","credential",
    "hack","hacker","frustrated","malware","stand","virus","exploit","blackmail","extort","manipulate","deceive","fake",
    "nude","nudes","creepy","stalker","harass","harassment","abuse","abusive","toxic","toxicity",
    "regret","guilty","pathetic","miserable","frustrated","despise","intolerance","extremist","segregation","hostile","revengeful","threatening","dangerous","harmful","negative"
],  
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
    "promotion", "limited", "deal","buy","scam"
],
"hate_words":[
    "racist","fuck", "never","bigot", "idiot","supremacy", "inferior", "discrimination",
    "extremist", "segregation", "genocide", "hate", "hatred","despise ",
    "prejudice", "intolerance","attractive","hostility", "bias", "oppression","hate"
],
"creepy_words": [
    "baby","pictures","attractive","picture","honey","darling","face","come","us","privately","your place","live","living","alone","wearing","shy","show","shower","sex","together","thinking","kiss","show","hug","myplace","bby","babe","cutie","sweetheart","darling","dear","honey","princess","beautiful","gorgeous","sexy","hot","cute","angel","love","kiss","hug","romance","crush","date","girlfriend","boyfriend","wife","husband","alone","private","secret","meet","meet alone","video call","voice call","late night","midnight","pics","pic","photo","image","selfie","send pics","send me","send me pics","send photo","send image","nude","nudes","lingerie","bedroom","cuddle","touch","massage"
],
"threat_words": [
    "kill", "murder","location","regret", "attack", "destroy", "harm", "shoot",
    "stab", "bomb", "revenge", "threat", "hunt", "assault",
    "violence", "eliminate", "execute", "punish", "beat", "hurt"
],
"profanity_words": [
    "damn", "hell", "crap", "bastard", "asshole", "jerk",
    "scumbag", "douche", "wtf", "bullshit", "trash",
    "garbage", "screw", "freak", "nonsense","shit","bitch"
],
"scam_phishing_words": [
    "otp", "password", "cvv", "banking", "verification",
    "urgent", "account", "login", "credential", "wiretransfer",
    "giftcard", "bitcoin", "wallet", "pin", "securitycode",
    "authorize", "reset", "confirm", "transaction", "payment"
],}
def negative_intent(text):
    scores={}
    for intent, keywords in negative_intent_words.items():
        count=0
        for keyword in keywords:
            if f" {keyword} " in f" {text} ":
                count += 1
        scores[intent]=count 
    best_intent=max(scores,key=scores.get)

    if scores[best_intent]==0:
        return "Normal_words"
    return best_intent
    
def positive_sentiment(text):
    positive=0
    for words in posi_intent_words.values():
        for word in words:
            if f" {word} " in f" {text} ":
                positive +=1
    return positive


def negative_sentiment(text):
    negative=0
    for words in negative_intent_words.values():
        for word in words:
            if f" {word} " in f" {text} ":
                negative+= 1
    return negative


def sentiment_check(text):
    positive=positive_sentiment(text)
    negative=negative_sentiment(text)
    
    if positive>negative:
        return "Positive"
    elif negative>positive:
        return "Negative"
    else:
        return "Neutral"

def decision_make(bad_intent,good_intent,sentiment):
    # +intent and + sentiment
    if good_intent !="Normal_words" and bad_intent == "Normal_words" and sentiment=="Positive":
        return "Keep"
    # - intent and - sentiment
    elif bad_intent !="Normal_words" and sentiment=="Negative":
        return "Block"
    # - intent and + sentiment
    elif bad_intent !="Normal_words" and sentiment=="Positive":
        return "Block"
    # + intent and - sentiment 
    elif good_intent!="Normal_words" and sentiment=="Negative":
        return "Review"
    # neutral
    elif good_intent!="Normal_words" and sentiment=="Neutral":
        return "Keep"
    # + intent and neutral sentiment
    elif bad_intent!="Normal_words" and sentiment=="Neutral":
        return "Block"
    elif bad_intent!="Normal_words":
        return "Block"
    return "Keep"
def normalize_text(text):
    text=text.lower()
    replacements ={
        "@": "a",
        "8": "a",
        "4": "a",
        "8": "b",
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
        "*":"u",}
    result=""
    for ch in text:
        result+=replacements.get(ch,ch)
    for ch in ".,?:;()[]/_-":
        result=result.replace(ch,"")
    return result

while True:
    text=input("enter message: ")
    text=normalize_text(text)
    good_intent=positive_intent(text)
    bad_intent=negative_intent(text)
    sentiment=sentiment_check(text)
    decision=decision_make(bad_intent,good_intent, sentiment)
    if good_intent!="Normal_words":
        final_intent=good_intent
    elif bad_intent!="Normal_words":
        final_intent=bad_intent
    else:
        final_intent="Norml_words"
    print("Intent:",final_intent)
    print("Sentiment:",sentiment)
    print("Decision:",decision)