# Task 1: Keyword Highlighter

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good.", "excellent.", "bad", "poor", "average."]
updated_reviews = []

for review in reviews:
    new_review = ""
    for word in review.split():
        if word.lower() in keywords:
            new_review += f" {word.upper()}"
            print(new_review)
        else:
            new_review += f" {word}"
    updated_reviews.append(new_review)

for review in updated_reviews:
    print(review[1:])


# Task 2: Sentiment Tally

def positive_and_negative_count(list_of_reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    positive_word_count = 0
    negative_word_count = 0
    for review in list_of_reviews:
        split_reviews = review.split()
        for word in split_reviews:
            if word.lower() in positive_words or word[:-1] in positive_words:
                positive_word_count += 1
            if word.lower() in negative_words or word[:-1] in negative_words:
                negative_word_count += 1
    print(f"Total number of positive words: {positive_word_count}")
    print(f"Total number of negative words: {negative_word_count}")
positive_and_negative_count(reviews)


# Task 3: Review Summary

def summarize_review(reviews_list):
    for review in reviews:
        if review[30] == " ":
            review_summary = review[:30]
            print(f"{review_summary}...")
        elif review[29] == " ":
            review_summary = review[:29]
            print(f"{review_summary}...")
        elif review[28] == " ":
            review_summary = review[:28]
            print(f"{review_summary}...")
        elif review[27] == " ":
            review_summary = review[:27]
            print(f"{review_summary}...")
        elif review[26] == " ":
            review_summary = review[:26]
            print(f"{review_summary}...")
        elif review[25] == " ":
            review_summary = review[:25]
            print(f"{review_summary}...")
        elif review[24] == " ":
            review_summary = review[:24]
            print(f"{review_summary}...")
        elif review[23] == " ":
            review_summary = review[:23]
            print(f"{review_summary}...")
            
summarize_review(reviews)
