from langchain_community.llms import Ollama

# Initialize Ollama model
ollama = Ollama(base_url='http://localhost:11434', model='tinyllama')

# Function to generate fitness advice
def fitness_chatbot(age, exercise_history, goal):
    prompt = f"""
    You are a professional fitness coach. A user has provided the following details:
    - Age: {age}
    - Exercise History: {exercise_history}
    - Fitness Goal: {goal}

    Based on this, give a **detailed** fitness plan, including:
    - Recommended workouts
    - Diet suggestions
    - Tips for staying consistent
    - Any warnings for their age or condition

    Keep it professional and easy to understand.
    """

    # Get response from Ollama
    response = ollama.invoke(prompt)
    return response

# Example usage
age = input("Enter your age: ")
exercise_history = input("Describe your past exercise routine: ")
goal = input("What is your fitness goal? ")

response = fitness_chatbot(age, exercise_history, goal)
print("\n💪 Fitness Advice:\n", response)
