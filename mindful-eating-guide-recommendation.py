import streamlit as st
import random
import google.generativeai as genai
from dotenv import load_dotenv

# Dictionary of mindful eating tips categorized by area of focus
mindful_eating_tips = {
    "Portion Control": [
        {"tip": "Use smaller plates", "description": "Smaller plates can help you eat less by making portions appear larger."},
        {"tip": "Measure your food", "description": "Use measuring cups and spoons to control portions accurately."},
        {"tip": "Serve from the kitchen", "description": "Avoid placing serving dishes on the table to prevent second helpings."},
        {"tip": "Eat slowly", "description": "Take your time to chew thoroughly and savor your food, which can help you recognize when you are full."}
    ],
    "Emotional Eating": [
        {"tip": "Identify triggers", "description": "Keep a food diary to note when and why you eat, helping you recognize emotional triggers."},
        {"tip": "Find alternatives", "description": "Engage in activities like walking, reading, or talking to a friend instead of eating when stressed."},
        {"tip": "Practice mindfulness", "description": "Take a few deep breaths and assess your hunger level before eating to ensure you are truly hungry."},
        {"tip": "Seek support", "description": "Talk to a counselor or join a support group to manage emotional eating."}
    ],
    "Binge Eating": [
        {"tip": "Plan your meals", "description": "Having regular meals and snacks can help prevent extreme hunger that leads to binging."},
        {"tip": "Avoid distractions", "description": "Eat without distractions like TV or phones to focus on your meal."},
        {"tip": "Portion control", "description": "Serve yourself a portion and put away the rest to avoid continuous eating."},
        {"tip": "Stay hydrated", "description": "Drink water throughout the day to help manage hunger and prevent overeating."}
    ],
    "General Tips": [
        {"tip": "Listen to your body", "description": "Eat when you're hungry and stop when you're satisfied, not full."},
        {"tip": "Choose whole foods", "description": "Opt for whole, unprocessed foods that nourish your body."},
        {"tip": "Balance your plate", "description": "Include a variety of food groups in your meals to ensure balanced nutrition."},
        {"tip": "Enjoy your food", "description": "Take time to savor each bite and enjoy the flavors and textures."}
    ]
}

# Function to recommend a mindful eating tip based on focus area
def recommend_tip(area):
    if area.lower() in mindful_eating_tips:
        return random.choice(mindful_eating_tips[area.lower()])
    else:
        return "Sorry, we don't have tips for that focus area."

# Main function to run the Streamlit app
def main():
    st.title("Mindful Eating Guide")
    st.subheader("Welcome to the Mindful Eating Guide! Get personalized tips for developing a healthier relationship with food.")

    # Ask user for their area of focus
    area = st.selectbox("Select your area of focus:", ["Portion Control", "Emotional Eating", "Binge Eating", "General Tips"])

    # Recommend a tip based on the user's preference
    if st.button("Get Tip"):
        recommendation = recommend_tip(area)
        if isinstance(recommendation, dict):
            st.success(f"Tip: {recommendation['tip']} - {recommendation['description']}")
        else:
            st.error(recommendation)

if __name__ == "__main__":
    main()
