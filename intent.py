
posi_intent_words={
    "positive":[
    "love","care","help","support","guide","assist","teach","learn","share","thank",
    "thanks","appreciate","respect","trust","welcome","friend","kind","kindness","happy","joy",
    "smile","peace","hope","encourage","motivate","inspire","understand","listen","cooperate","collaborate",
    "teamwork","honest","honesty","loyal","loyalty","adore","cherish","comfort","protect","encouragement",
    "excellent","amazing","awesome","fantastic","wonderful","great","good","brilliant","positive","success",
    "successful","achievement","achieve","win","winner","progress","improve","improvement","growth","opportunity",
    "solution","solve","recommend","suggest","advice","clarify","explain","information","knowledge","education",
    "study","book","family","friendship","community","generous","gratitude","cheerful","delight","optimistic",
    "polite","courteous","gentle","lovely","beautiful","cute","sweet","dear","darling","heart",
    "affection","romance","beloved","soulmate","hug","kiss","blessing","faith","patience","forgive",
    "forgiveness","safe","security","trustworthy","valuable","creative","innovation","productive","productive"
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

"normal_words": [
    "hello", "hi", "thanks", "welcome", "morning",
    "evening", "friend", "family", "school", "college",
    "study", "book", "computer", "food", "water",
    "travel", "music", "movie", "game", "work"
] 
}
def positive_intent(text):
    scores={}
    for intent, keywords in posi_intent_words.items():
        count=0
        for keyword in keywords:
            if keyword in text:
                count+=1
        scores[intent]=count 
    best_intent=max(scores,key=scores.get)

    if scores[best_intent]==0:
        return "Normal_words"
    return best_intent

negative_intent_words = {
    "negative":[
    "hate","hatred","angry","anger","furious","rage","annoy","annoying","upset","sad",
    "depressed","cry","pain","hurt","harm","damage","destroy","attack","assault","violence",
    "kill","murder","shoot","stab","bomb","threat","revenge","punish","eliminate","execute",
    "racist","bigot","supremacy","inferior","discrimination","prejudice","hostility","bias","oppression","genocide",
    "idiot","stupid","loser","moron","worthless","pathetic","dumb","fool","jerk","clown",
    "garbage","trash","useless","failure","ugly","crazy","weirdo","lame","nonsense","scumbag",
    "asshole","bastard","douche","wtf","bullshit","damn","hell","crap","freak","hateyou",
    "scam","fraud","cheat","steal","theft","phishing","otp","password","cvv","credential",
    "hack","hacker","malware","virus","exploit","blackmail","extort","manipulate","deceive","fake",
    "nude","nudes","creepy","stalker","harass","harassment","abuse","abusive","toxic","toxicity",
    "regret","guilty","miserable","frustrated","broken","lonely","fear","anxiety","worried","stress",
    "despise","intolerance","extremist","segregation","hostile","revengeful","threatening","dangerous","harmful","negative"
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
    "promotion", "limited", "deal","buy"
],
"hate_words":[
    "racist", "never","bigot", "supremacy", "inferior", "discrimination",
    "extremist", "segregation", "genocide", "hate", "hatred","despise ",
    "prejudice", "intolerance", "hostility", "bias", "oppression","hate"
],
"creepy_words": [
    "send your pics","baby","bby","send me pics","send photo","send me photo","send image","nude","nudes","alone","video call","meet alone"
],
"threat_words": [
    "kill", "murder","regret", "attack", "destroy", "harm", "shoot",
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
            if keyword in text:
                count+=1
        scores[intent]=count 
    best_intent=max(scores,key=scores.get)

    if scores[best_intent]==0:
        return "Normal_words"
    return best_intent
    











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
    return result

while True:
    text=input("enter message: ")
    good_intent=positive_intent(text)
    bad_intent=negative_intent(text)
    print("positive intent:",good_intent)
    print("Negative intent:",bad_intent)