import streamlit as st
import random
import google.generativeai as genai
from dotenv import load_dotenv

# Dictionary of mindful eating tips categorized by area of focus
mindful_eating_tips = {
    "Portion Control": [
        {"tip": "Use smaller plates", "description": "Using smaller plates can help you control your portions better. When you use a smaller plate, your servings look larger, which can make you feel more satisfied with less food. This simple change can help you reduce your calorie intake without feeling deprived."},
        {"tip": "Measure your food", "description": "Measuring your food portions with cups and spoons can help you be more aware of how much you are eating. It ensures that you are not consuming more than you need, which can help you maintain a healthy weight and avoid overeating."},
        {"tip": "Serve from the kitchen", "description": "Serving your food directly from the kitchen instead of placing serving dishes on the dining table can prevent you from taking second helpings. This strategy helps you stick to your initial portion size, reducing the temptation to overeat."},
        {"tip": "Eat slowly", "description": "Taking your time to chew thoroughly and savor your food can help you recognize when you are full. Eating slowly allows your brain to catch up with your stomach, preventing overeating and promoting better digestion."}
    ],
    "Emotional Eating": [
        {"tip": "Identify triggers", "description": "Keeping a food diary to note when and why you eat can help you recognize patterns and emotional triggers. Understanding these triggers can help you develop healthier coping mechanisms for stress, boredom, or other emotions."},
        {"tip": "Find alternatives", "description": "Engaging in activities like walking, reading, or talking to a friend can be great alternatives to eating when you're feeling stressed or emotional. Finding other ways to cope with your feelings can help you break the cycle of emotional eating."},
        {"tip": "Practice mindfulness", "description": "Before eating, take a few deep breaths and assess your hunger level. This practice helps ensure that you are eating because you are genuinely hungry and not just eating out of habit or emotion."},
        {"tip": "Seek support", "description": "Talking to a counselor or joining a support group can provide you with the support you need to manage emotional eating. Sharing your experiences with others can help you feel less alone and give you new strategies to cope with your emotions."}
    ],
    "Binge Eating": [
        {"tip": "Plan your meals", "description": "Having regular meals and snacks can help prevent extreme hunger, which can lead to binging. Planning your meals ensures that you are eating balanced, nutritious foods throughout the day, keeping your hunger and cravings in check."},
        {"tip": "Avoid distractions", "description": "Eating without distractions like TV or phones allows you to focus on your meal and recognize when you are full. Being mindful during meals can help you enjoy your food more and prevent overeating."},
        {"tip": "Portion control", "description": "Serving yourself a portion and putting away the rest can help you avoid continuous eating. Sticking to a single portion helps you control your intake and prevents the temptation to go back for more."},
        {"tip": "Stay hydrated", "description": "Drinking water throughout the day can help manage your hunger and prevent overeating. Sometimes, thirst can be mistaken for hunger, so staying hydrated can help you better understand your body's true needs."}
    ],
    "General Tips": [
        {"tip": "Listen to your body", "description": "Eat when you're hungry and stop when you're satisfied, not full. Paying attention to your body's hunger and fullness cues can help you avoid overeating and make healthier choices about when and how much to eat."},
        {"tip": "Choose whole foods", "description": "Opt for whole, unprocessed foods that nourish your body. Whole foods like fruits, vegetables, whole grains, and lean proteins are packed with nutrients and can help you feel more satisfied than processed foods."},
        {"tip": "Balance your plate", "description": "Including a variety of food groups in your meals ensures balanced nutrition. A balanced plate with proteins, carbohydrates, fats, and vegetables can provide you with all the essential nutrients your body needs to function well."},
        {"tip": "Enjoy your food", "description": "Take time to savor each bite and enjoy the flavors and textures of your food. Eating mindfully can enhance your eating experience, making meals more enjoyable and helping you appreciate the food you are eating."}
    ]
}

# Function to recommend a mindful eating tip based on focus area and tip selection
def recommend_tip(area, selected_tip):
    if area in mindful_eating_tips:
        for tip in mindful_eating_tips[area]:
            if tip["tip"] == selected_tip:
                return tip
    return "Sorry, we don't have tips for that focus area."

# Function to recommend a random mindful eating tip from any category
def recommend_random_tip():
    all_tips = [tip for tips in mindful_eating_tips.values() for tip in tips]
    return random.choice(all_tips)

# Main function to run the Streamlit app
def main():
    st.title("Mindful Eating Guide")
    st.subheader("Welcome to the Mindful Eating Guide! Get personalized tips for developing a healthier relationship with food.")

    # Ask user for their area of focus
    area = st.selectbox("Select your area of focus:", ["Portion Control", "Emotional Eating", "Binge Eating", "General Tips"])

    if area:
        tips = [tip["tip"] for tip in mindful_eating_tips[area]]
        selected_tip = st.selectbox("Select a tip:", tips)

        if st.button("Get Tip"):
            recommendation = recommend_tip(area, selected_tip)
            if isinstance(recommendation, dict):
                st.success(f"Tip: {recommendation['tip']} - {recommendation['description']}")
            else:
                st.error(recommendation)
    
    # Add a button to get a random tip
    if st.button("Get Random Tip"):
        random_recommendation = recommend_random_tip()
        st.info(f"Random Tip: {random_recommendation['tip']} - {random_recommendation['description']}")

if __name__ == "__main__":
    main()
