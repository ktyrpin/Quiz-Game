questions = [
    {
        "prompt": "1. Which country won the FIFA World Cup in 2018?",
        "options": ["A. Germany", "B. Brazil", "C. France", "D. Argentina"],
        "answer": "C"
    },
    {
        "prompt": "2. Who is the top scorer in the history of the UEFA Champions League?",
        "options": ["A. Lionel Messi", "B. Cristiano Ronaldo", "C. Robert Lewandowski", "D. Karim Benzema"],
        "answer": "B"
    },
    {
        "prompt": "3. Which club won the English Premier League in the 2020-2021 season?",
        "options": ["A. Manchester City", "B. Liverpool", "C. Chelsea", "D. Manchester United"],
        "answer": "A"
    },
    {
        "prompt": "4. Which player has won the most Ballon d'Or awards?",
        "options": ["A. Michel Platini", "B. Johan Cruyff", "C. Lionel Messi", "D. Cristiano Ronaldo"],
        "answer": "C"
    },
    {
        "prompt": "5. Which country hosted the FIFA World Cup in 2006?",
        "options": ["A. South Africa", "B. Germany", "C. Brazil", "D. Japan"],
        "answer": "B"
    },
    {
        "prompt": "6. Who is known as the 'King of Football'?",
        "options": ["A. Diego Maradona", "B. Zinedine Zidane", "C. Pelé", "D. Johan Cruyff"],
        "answer": "C"
    },
    {
        "prompt": "7. Which team has won the most UEFA Champions League titles?",
        "options": ["A. AC Milan", "B. Liverpool", "C. Real Madrid", "D. Bayern Munich"],
        "answer": "C"
    },
    {
        "prompt": "8. Who scored the 'Hand of God' goal?",
        "options": ["A. Pelé", "B. Diego Maradona", "C. Lionel Messi", "D. Zinedine Zidane"],
        "answer": "B"
    },
    {
        "prompt": "9. Which country won the first ever FIFA World Cup in 1930?",
        "options": ["A. Argentina", "B. Brazil", "C. Uruguay", "D. Italy"],
        "answer": "C"
    },
    {
        "prompt": "10. Which country has won the most FIFA World Cup titles?",
        "options": ["A. Germany", "B. Brazil", "C. Italy", "D. Argentina"],
        "answer": "B"
    },
]

def quiz(questions): 
  score = 0 
  for question in questions:
    print(question["prompt"])
    for option in question["options"]:
      print(option)
    answer = input("Enter your answer (A, B, C, D): ").upper()
    if answer == question["answer"]:
      print("Correct answer \n")
      score += 1
    else: 
      print("Incorrect answer \n")

  print(f"You got {score} out of {len(questions)} questions correct.")

quiz(questions)