import random

# List of positive pep talk templates
POSITIVE_PEP_TALK_TEMPLATES = [
    'You are doing a great job!',
    'Keep up the good work!',
    'You are a valuable member of the team.',
    'Your hard work and dedication is appreciated.',
    'You are making a difference.',
    'Believe in yourself and your abilities.',
    'Stay positive, work hard, make it happen.',
    'You are capable of more than you know.',
    'The harder you work for something, the greater you will feel when you achieve it.',
    'Dream it. Wish it. Do it.',
    'Success doesn’t just find you. You have to go out and get it.',
    'The harder you work for something, the greater you’ll feel when you achieve it.',
    'Dream bigger. Do bigger.',
    'Wake up with determination. Go to bed with satisfaction.',
    'Do something today that your future self will thank you for.',
    'It’s going to be hard, but hard does not mean impossible.',
    'Don’t wait for opportunity. Create it.',
    'Sometimes we’re tested not to show our weaknesses, but to discover our strengths.',
    'The key to success is to focus on goals, not obstacles.',
    'Dream it. Believe it. Build it.'
]

# List of motivational pep talk templates
MOTIVATIONAL_PEP_TALK_TEMPLATES = [
    'Keep pushing, the results will come.',
    'Don’t stop when you’re tired. Stop when you’re done.',
    'Great things never come from comfort zones.',
    'Push yourself, because no one else is going to do it for you.',
    'Don’t wait for opportunity. Create it.',
    'Your limitation—it’s only your imagination.',
    'The key to success is to focus on goals, not obstacles.',
    'Keep going. Everything you need will come to you at the perfect time.',
    'Believe you can and you’re halfway there.',
    'Start where you are. Use what you have. Do what you can.',
    'Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.',
    'The only way to achieve the impossible is to believe it is possible.',
    'It always seems impossible until it’s done.',
    'Don’t watch the clock; do what it does. Keep going.',
    'There will be obstacles. There will be doubters. There will be mistakes. But with hard work, there are no limits.',
    'Perseverance is not a long race; it is many short races one after the other.',
    'Start by doing what’s necessary; then do what’s possible; and suddenly you are doing the impossible.',
    'Believe in yourself, take on your challenges, dig deep within yourself to conquer fears. Never let anyone bring you down. You got this.',
    'Challenges are what make life interesting and overcoming them is what makes life meaningful.',
    'He who is not courageous enough to take risks will accomplish nothing in life.'
]

def generate_pep_talk(is_positive):
    # Randomly select a pep talk template based on the game result
    if is_positive:
        pep_talk = random.choice(POSITIVE_PEP_TALK_TEMPLATES)
    else:
        pep_talk = random.choice(MOTIVATIONAL_PEP_TALK_TEMPLATES)
    return pep_talk

# Example usage
print(generate_pep_talk(True))
print(generate_pep_talk(False))