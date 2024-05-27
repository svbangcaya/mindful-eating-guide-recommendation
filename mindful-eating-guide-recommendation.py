import streamlit as st
import random
import google.generativeai as genai
from dotenv import load_dotenv

# Dictionary of mindful eating tips categorized by area of focus
mindful_eating_tips = {
    "Portion Control": [
        {"tip": "Use smaller plates", "description": "Using smaller plates can help you eat less by making portions appear larger."},
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
        {"tip": "Listen to your body", "description": "Eat when you're hungry and stop when you're satisfied, not full. Paying attention to your body's hunger and fullness cues can help you avoid overeating and make healthier choices about when and how much to eat."},
        {"tip": "Choose whole foods", "description": "Opt for whole, unprocessed foods that nourish your body and provide sustained energy. Whole foods are typically more nutrient-dense and can help you feel fuller longer."},
        {"tip": "Balance your plate", "description": "Include a variety of food groups in your meals to ensure balanced nutrition. Aim for a mix of proteins, carbohydrates, fats, and plenty of fruits and vegetables to cover all nutritional bases."},
        {"tip": "Enjoy your food", "description": "Take time to savor each bite and enjoy the flavors and textures. Eating slowly and mindfully can enhance your eating experience and help you recognize when you're satisfied."}
    ]
}

# Function to recommend a mindful eating tip based on focus area
def recommend_tip(area, tip=None):
    if area in mindful_eating_tips:
        if tip:
            for t in mindful_eating_tips[area]:
                if t['tip'] == tip:
                    return t
        return random.choice(mindful_eating_tips[area])
    else:
        return "Sorry, we don't have tips for that focus area."

# Main function to run the Streamlit app
def main():
    st.title("Mindful Eating Guide")
    st.subheader("Welcome to the Mindful Eating Guide! Get personalized tips for developing a healthier relationship with food.")
    
    st.markdown("""
    ### Mindful Eating Guide Recommendation
    **by Samantha V. Bangcaya - BSCS 3B AI**
    Welcome to the Mindful Eating Guide! This application is designed to offer you personalized tips for developing a healthier relationship with food. Created by Samantha V. Bangcaya, a student from BSCS 3B AI, this guide is inspired by my own journey through various eating habits and challenges.

    I have personally experienced the struggles of emotional eating, binge eating, and the need for better portion control. These experiences motivated me to develop a tool that can help others navigate their eating habits more mindfully. The Mindful Eating Guide provides practical and easy-to-follow tips that cater to different aspects of mindful eating, whether it's managing portion sizes, addressing emotional triggers, or simply enjoying your meals more consciously.
    """)

    # Ask user for their area of focus
    area = st.selectbox("Select your area of focus:", ["Portion Control", "Emotional Eating", "Binge Eating", "General Tips"])

    # Recommend a tip based on the user's preference
    if st.button("Get Tip"):
        tips = [t['tip'] for t in mindful_eating_tips[area]]
        tip = st.selectbox("Select a tip:", tips)
        
        recommendation = recommend_tip(area, tip)
        if isinstance(recommendation, dict):
            st.success(f"Tip: {recommendation['tip']}\n\nDescription: {recommendation['description']}")
        else:
            st.error(recommendation)

    # Get a random tip
    if st.button("Get Random Tip"):
        random_area = random.choice(list(mindful_eating_tips.keys()))
        random_tip = recommend_tip(random_area)
        st.info(f"Random Tip: {random_tip['tip']}\n\nDescription: {random_tip['description']}")

if __name__ == "__main__":
    main()
