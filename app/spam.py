def check_spam(text: str) -> tuple:
    text = text.lower().strip()
    if not text:
        return "ham", 0
    
    # 스팸 키워드 목록
    spam_keywords = [
        "free", "win", "winner", "prize", "click", 
        "buy now", "urgent", "cash", "money", "offer", "deal"
    ]
    
    hit = 0
    for kw in spam_keywords:
        if kw in text:
            hit += 1
            
    # 키워드가 2개 이상이면 스팸으로 분류
    label = "spam" if hit >= 2 else "ham"
    return label, hit