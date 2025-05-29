//halik app python file
from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webapp', methods=['POST'])
def send_email():
    # Email details
    msg = EmailMessage()
    msg['Subject'] = 'Hello from Flask App'
    msg['From'] = 'kajamydeenhalik@gmail.com'
    msg['To'] = 'nayaganavis2004@gmail.com'
    msg.set_content('This email was sent by clicking a button!')

    # Send via Gmail SMTP
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('kajamydeenhalik@gmail.com', 'aufgjvzqbqmspfnd')  # use your App Password
        smtp.send_message(msg)

    return "Email sent successfully!"

if __name__ == '__main__':
    app.run(debug=True)
//index.html
<!DOCTYPE html>
<html>
<head>
    <title>Send Email</title>
</head>
<body>
    <h1>Send Email</h1>
    <form action="/webapp" method="post">
        <button type="submit">Send Email</button>
    </form>
</body>
</html>


    ------------------------------------------------------------------------------------

    import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Sample newsletter text
newsletter_text = """
Welcome to our weekly newsletter! We are excited to introduce our new eco-friendly product line.
Enjoy a 20% discount this weekend! Read testimonials from happy customers and stay updated with the latest trends.
Our mission is to provide sustainable solutions.
"""

# Preprocessing: Remove special characters
def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove numbers & special characters
    return text.lower()

clean_text = preprocess_text(newsletter_text)

# Tokenization
words = word_tokenize(clean_text)
sentences = sent_tokenize(newsletter_text)

# Remove stopwords
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word not in stop_words]

# Extract keywords (most common words)
keyword_counts = Counter(filtered_words)
top_keywords = keyword_counts.most_common(5)

# Sentiment Analysis
sia = SentimentIntensityAnalyzer()
sentiment_score = sia.polarity_scores(newsletter_text)

# Print results
print("Top Keywords:", top_keywords)
print("Total Sentences:", len(sentences))
print("Sentiment Analysis:", sentiment_score)


//new php file
<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/SMTP.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name    = $_POST['name'];
    $email   = $_POST['email'];
    $message = $_POST['message'];

    $mail = new PHPMailer(true);

    try {
        $mail->isSMTP();
        $mail->Host       = 'smtp.gmail.com';
        $mail->SMTPAuth   = true;
        $mail->Username   = 'ajaymg137@gmail.com';        
        $mail->Password   = 'vreq wyom lexl bfuw';            
        $mail->SMTPSecure = 'tls';
        $mail->Port       = 587;

        $mail->setFrom('ajaymg137@gmail.com', 'Contact');  
        $mail->addAddress('sam9ple@gmail.com');         

        $mail->Subject = "New message from $name";
        $mail->Body    = "Name: $name\nEmail: $email\nMessage:\n$message";

        $mail->send();
        echo "✅ Message Sent!";
    } catch (Exception $e) {
        echo "❌ Failed to send email. Error: {$mail->ErrorInfo}";
    }
}
?>
//form html
<!DOCTYPE html>
<html>
<head>
    <title>Simple Email Form</title>
</head>
<body>
    <h2>Send Email</h2>
    <form action="send_email.php" method="post">
        <input type="text" name="name" placeholder="Your Name" required><br><br>
        <input type="email" name="email" placeholder="Your Email" required><br><br>
        <textarea name="message" placeholder="Your Message" required></textarea><br><br>
        <button type="submit">Send</button>
    </form>
</body>
</html>
