import streamlit as st
import random
import google.generativeai as genai
from dotenv import load_dotenv

# Dictionary of mindful eating tips categorized by area of focus
mindful_eating_tips = {
    "Portion Control": [
        {
            "tip": "Use smaller plates",
            "description": "Using smaller plates can help you control your portions better. When you use a smaller plate, your servings look larger, which can make you feel more satisfied with less food. This simple change can help you reduce your calorie intake without feeling deprived.",
            "fact": "Studies have shown that people tend to eat less when they use smaller plates, leading to a reduction in calorie intake by up to 30%."
        },
        {
            "tip": "Measure your food",
            "description": "Measuring your food portions with cups and spoons can help you be more aware of how much you are eating. It ensures that you are not consuming more than you need, which can help you maintain a healthy weight and avoid overeating.",
            "fact": "Consistently measuring your food can help you understand portion sizes better, making it easier to make healthier choices without overindulging."
        },
        {
            "tip": "Serve from the kitchen",
            "description": "Serving your food directly from the kitchen instead of placing serving dishes on the dining table can prevent you from taking second helpings. This strategy helps you stick to your initial portion size, reducing the temptation to overeat.",
            "fact": "Research suggests that people eat about 20% less when food is served from the kitchen instead of having serving dishes on the table."
        },
        {
            "tip": "Eat slowly",
            "description": "Taking your time to chew thoroughly and savor your food can help you recognize when you are full. Eating slowly allows your brain to catch up with your stomach, preventing overeating and promoting better digestion.",
            "fact": "Eating slowly can reduce calorie intake and aid digestion. It takes about 20 minutes for your brain to register that you are full."
        }
    ],
    "Emotional Eating": [
        {
            "tip": "Identify triggers",
            "description": "Keeping a food diary to note when and why you eat can help you recognize patterns and emotional triggers. Understanding these triggers can help you develop healthier coping mechanisms for stress, boredom, or other emotions.",
            "fact": "Identifying emotional eating triggers can help reduce stress-related eating by up to 50%, leading to healthier eating habits."
        },
        {
            "tip": "Find alternatives",
            "description": "Engaging in activities like walking, reading, or talking to a friend can be great alternatives to eating when you're feeling stressed or emotional. Finding other ways to cope with your feelings can help you break the cycle of emotional eating.",
            "fact": "Finding non-food-related activities can reduce the urge to eat by providing a distraction and helping to manage emotions more effectively."
        },
        {
            "tip": "Practice mindfulness",
            "description": "Before eating, take a few deep breaths and assess your hunger level. This practice helps ensure that you are eating because you are genuinely hungry and not just eating out of habit or emotion.",
            "fact": "Practicing mindfulness before eating can decrease calorie intake and improve overall emotional well-being."
        },
        {
            "tip": "Seek support",
            "description": "Talking to a counselor or joining a support group can provide you with the support you need to manage emotional eating. Sharing your experiences with others can help you feel less alone and give you new strategies to cope with your emotions.",
            "fact": "Support groups can offer a sense of community and accountability, which can be crucial in overcoming emotional eating habits."
        }
    ],
    "Binge Eating": [
        {
            "tip": "Plan your meals",
            "description": "Having regular meals and snacks can help prevent extreme hunger, which can lead to binging. Planning your meals ensures that you are eating balanced, nutritious foods throughout the day, keeping your hunger and cravings in check.",
            "fact": "Meal planning can reduce the frequency of binge eating episodes by providing structure and ensuring balanced nutrition."
        },
        {
            "tip": "Avoid distractions",
            "description": "Eating without distractions like TV or phones allows you to focus on your meal and recognize when you are full. Being mindful during meals can help you enjoy your food more and prevent overeating.",
            "fact": "Eating without distractions can improve digestion and reduce overeating by increasing awareness of satiety signals."
        },
        {
            "tip": "Portion control",
            "description": "Serving yourself a portion and putting away the rest can help you avoid continuous eating. Sticking to a single portion helps you control your intake and prevents the temptation to go back for more.",
            "fact": "Practicing portion control can lead to a 25% reduction in daily calorie intake, aiding in weight management and preventing overeating."
        },
        {
            "tip": "Stay hydrated",
            "description": "Drinking water throughout the day can help manage your hunger and prevent overeating. Sometimes, thirst can be mistaken for hunger, so staying hydrated can help you better understand your body's true needs.",
            "fact": "Staying hydrated can reduce hunger pangs and aid in overall body function, making it easier to distinguish between hunger and thirst."
        }
    ],
    "General Tips": [
        {
            "tip": "Listen to your body",
            "description": "Eat when you're hungry and stop when you're satisfied, not full. Paying attention to your body's hunger and fullness cues can help you avoid overeating and make healthier choices about when and how much to eat.",
            "fact": "Listening to your body's signals can improve eating habits and reduce the risk of overeating, leading to better overall health."
        },
        {
            "tip": "Choose whole foods",
            "description": "Opt for whole, unprocessed foods that nourish your body. Whole foods like fruits, vegetables, whole grains, and lean proteins are packed with nutrients and can help you feel more satisfied than processed foods.",
            "fact": "Choosing whole foods can provide essential nutrients and improve satiety, reducing the likelihood of overeating processed foods."
        },
        {
            "tip": "Balance your plate",
            "description": "Including a variety of food groups in your meals ensures balanced nutrition. A balanced plate with proteins, carbohydrates, fats, and vegetables can provide you with all the essential nutrients your body needs to function well.",
            "fact": "A balanced diet can enhance overall health and energy levels, supporting a well-functioning body and mind."
        },
        {
            "tip": "Enjoy your food",
            "description": "Take time to savor each bite and enjoy the flavors and textures of your food. Eating mindfully can enhance your eating experience, making meals more enjoyable and helping you appreciate the food you are eating.",
            "fact": "Mindful eating can improve digestion and satisfaction, making mealtime a more fulfilling and enjoyable experience."
        }
    ]
}

# Initialize session state for saved tips
if "saved_tips" not in st.session_state:
    st.session_state.saved_tips = []

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

# Function to save a tip
def save_tip(tip):
    if tip not in st.session_state.saved_tips:
        st.session_state.saved_tips.append(tip)

# Main function to run the Streamlit app
def main():
    st.title("Mindful Eating Guide Recommendation")
    st.subheader("Welcome to the Mindful Eating Guide! Get personalized tips for developing a healthier relationship with food.")

    st.markdown("""
    Created by Samantha V. Bangcaya, a student - BSCS 3B AI.
    This application is designed to offer you personalized tips for developing a healthier relationship with food. This guide is inspired by my own journey through various eating habits and challenges.

    Having experienced emotional eating, binge eating, and the need for better portion control, I was motivated to develop this tool to help others. The Mindful Eating Guide provides practical, easy-to-follow tips for managing portion sizes, addressing emotional triggers, and simply enjoying your meals more mindfully.
    """)
    
    # Ask user for their area of focus
    area = st.text_input("Type your area of focus (choose from Portion Control, Emotional Eating, Binge Eating, General Tips):")

    if area:
        if area in mindful_eating_tips:
            tips = [tip["tip"] for tip in mindful_eating_tips[area]]
            selected_tip = st.selectbox("Select a tip:", tips)

            if st.button("Get Tip"):
                recommendation = recommend_tip(area, selected_tip)
                if isinstance(recommendation, dict):
                    st.success(f"Description: {recommendation['description']}\n\nFact: {recommendation['fact']}")
                    if st.button("Save Tip"):
                        save_tip(recommendation)
                        st.info("Tip saved!")
                else:
                    st.error(recommendation)
        else:
            st.error("The entered area of focus is not part of our categories.")
    
    # Add a button to get a random tip
    if st.button("Get Random Tip"):
        random_recommendation = recommend_random_tip()
        st.info(f"Random Tip: {random_recommendation['tip']}\n\nDescription: {random_recommendation['description']}\n\nFact: {random_recommendation['fact']}")

    # Display saved tips
    if st.session_state.saved_tips:
        st.subheader("Saved Tips")
        for saved_tip in st.session_state.saved_tips:
            st.write(f"Tip: {saved_tip['tip']}\n\nDescription: {saved_tip['description']}\n\nFact: {saved_tip['fact']}")

if __name__ == "__main__":
    main()
