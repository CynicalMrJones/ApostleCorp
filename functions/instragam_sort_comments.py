from instagrapi import Client
from textblob import TextBlob


# Initialize Instagram Client


cl = Client()
def initialize():
    with open("InstagrapiLogins.txt", "r") as file:
        entry = file.readline()
        email, password = entry.split(" ")
        cl.login(email,password)

def botLogin(bot):
    bot.email
    cl.login(bot.email, bot.password)

def classify_comment(comment):
    # Classifies the comment as positive or negative using TextBlob sentiment analysis.
    analysis = TextBlob(comment)
    sentiment_score = analysis.sentiment.polarity
    return "positive" if sentiment_score > 0 else "negative"

def get_comments(post_url):
    # Fetch comments from a given Instagram post.
    post_id = cl.media_id(cl.media_pk_from_url(post_url))
    comments = cl.media_comments(post_id)
    return [comment.text for comment in comments]

def process_comments(post_url, output_file="comments.txt"):
    initialize()
    """Extracts, classifies, and saves comments to a text file."""
    comments = get_comments(post_url)

    positive_comments = []
    negative_comments = []

    for comment in comments:
        sentiment = classify_comment(comment)
        if sentiment == "positive":
            positive_comments.append(comment)
        else:
            negative_comments.append(comment)

    # Save results to a text file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("💬 Positive Comments:\n")
        file.write("\n".join(positive_comments[:5]) + "\n\n")
        file.write("💢 Negative Comments:\n")
        file.write("\n".join(negative_comments[:5]) + "\n")

    print(f"✅ Comments saved to {output_file}")

# Example usage: replace with the URL of the Instagram post
