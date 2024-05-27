import streamlit as st
import random
import google.generativeai as genai
from dotenv import load_dotenv

# Dictionary of mindful eating tips categorized by area of focus
mindful_eating_tips = {
    "Portion Control": [
        {
            "tip": "Use smaller plates",
            "description": "Using smaller plates can help you control your portions better. When you use a smaller plate, your servings look larger, which can make you feel more satisfied with less food. This simple change can help you reduce your calorie intake without feeling deprived.\n\nDid you know that studies have shown people tend to eat less when they use smaller plates, leading to a reduction in calorie intake by up to 30%? (Source: Journal of Consumer Research)"
        },
        {
            "tip": "Measure your food",
            "description": "Measuring your food portions with cups and spoons can help you be more aware of how much you are eating. It ensures that you are not consuming more than you need, which can help you maintain a healthy weight and avoid overeating.\n\nDid you know that consistently measuring your food can help you understand portion sizes better, making it easier to make healthier choices without overindulging? (Source: American Journal of Clinical Nutrition)"
        },
        {
            "tip": "Serve from the kitchen",
            "description": "Serving your food directly from the kitchen instead of placing serving dishes on the dining table can prevent you from taking second helpings. This strategy helps you stick to your initial portion size, reducing the temptation to overeat.\n\nDid you know that research suggests people eat about 20% less when food is served from the kitchen instead of having serving dishes on the table? (Source: Cornell University)"
        },
        {
            "tip": "Eat slowly",
            "description": "Taking your time to chew thoroughly and savor your food can help you recognize when you are full. Eating slowly allows your brain to catch up with your stomach, preventing overeating and promoting better digestion.\n\nDid you know that eating slowly can reduce calorie intake and aid digestion? It takes about 20 minutes for your brain to register that you are full. (Source: Harvard Health)"
        }
    ],
    "Emotional Eating": [
        {
            "tip": "Identify triggers",
            "description": "Keeping a food diary to note when and why you eat can help you recognize patterns and emotional triggers. Understanding these triggers can help you develop healthier coping mechanisms for stress, boredom, or other emotions.\n\nDid you know that identifying emotional eating triggers can help reduce stress-related eating by up to 50%, leading to healthier eating habits? (Source: Mayo Clinic)"
        },
        {
            "tip": "Find alternatives",
            "description": "Engaging in activities like walking, reading, or talking to a friend can be great alternatives to eating when you're feeling stressed or emotional. Finding other ways to cope with your feelings can help you break the cycle of emotional eating.\n\nDid you know that finding non-food-related activities can reduce the urge to eat by providing a distraction and helping to manage emotions more effectively? (Source: American Psychological Association)"
        },
        {
            "tip": "Practice mindfulness",
            "description": "Before eating, take a few deep breaths and assess your hunger level. This practice helps ensure that you are eating because you are genuinely hungry and not just eating out of habit or emotion.\n\nDid you know that practicing mindfulness before eating can decrease calorie intake and improve overall emotional well-being? (Source: Mindful Eating Research)"
        },
        {
            "tip": "Seek support",
            "description": "Talking to a counselor or joining a support group can provide you with the support you need to manage emotional eating. Sharing your experiences with others can help you feel less alone and give you new strategies to cope with your emotions.\n\nDid you know that support groups can offer a sense of community and accountability, which can be crucial in overcoming emotional eating habits? (Source: National Eating Disorders Association)"
        }
    ],
    "Binge Eating": [
        {
            "tip": "Plan your meals",
            "description": "Having regular meals and snacks can help prevent extreme hunger, which can lead to binging. Planning your meals ensures that you are eating balanced, nutritious foods throughout the day, keeping your hunger and cravings in check.\n\nDid you know that meal planning can reduce the frequency of binge eating episodes by providing structure and ensuring balanced nutrition? (Source: International Journal of Eating Disorders)"
        },
        {
            "tip": "Avoid distractions",
            "description": "Eating without distractions like TV or phones allows you to focus on your meal and recognize when you are full. Being mindful during meals can help you enjoy your food more and prevent overeating.\n\nDid you know that eating without distractions can improve digestion and reduce overeating by increasing awareness of satiety signals? (Source: American Journal of Clinical Nutrition)"
        },
        {
            "tip": "Portion control",
            "description": "Serving yourself a portion and putting away the rest can help you avoid continuous eating. Sticking to a single portion helps you control your intake and prevents the temptation to go back for more.\n\nDid you know that practicing portion control can lead to a 25% reduction in daily calorie intake, aiding in weight management and preventing overeating? (Source: Centers for Disease Control and Prevention)"
        },
        {
            "tip": "Stay hydrated",
            "description": "Drinking water throughout the day can help manage your hunger and prevent overeating. Sometimes, thirst can be mistaken for hunger, so staying hydrated can help you better understand your body's true needs.\n\nDid you know that staying hydrated can reduce hunger pangs and aid in overall body function, making it easier to distinguish between hunger and thirst? (Source: National Institutes of Health)"
        }
    ],
    "General Tips": [
        {
            "tip": "Listen to your body",
            "description": "Eat when you're hungry and stop when you're satisfied, not full. Paying attention to your body's hunger and fullness cues can help you avoid overeating and make healthier choices about when and how much to eat.\n\nDid you know that listening to your body's signals can improve eating habits and reduce the risk of overeating, leading to better overall health? (Source: Harvard Health)"
        },
        {
            "tip": "Choose whole foods",
            "description": "Opt for whole, unprocessed foods that nourish your body. Whole foods like fruits, vegetables, whole grains, and lean proteins are packed with nutrients and can help you feel more satisfied than processed foods.\n\nDid you know that choosing whole foods can provide essential nutrients and improve satiety, reducing the likelihood of overeating processed foods? (Source: Academy of Nutrition and Dietetics)"
        },
        {
            "tip": "Balance your plate",
            "description": "Including a variety of food groups in your meals ensures balanced nutrition. A balanced plate with proteins, carbohydrates, fats, and vegetables can provide you with all the essential nutrients your body needs to function well.\n\nDid you know that a balanced diet can enhance overall health and energy levels, supporting a well-functioning body and mind? (Source: World Health Organization)"
        },
        {
            "tip": "Enjoy your food",
            "description": "Take time to savor each bite and enjoy the flavors and textures of your food. Eating mindfully can enhance your eating experience, making meals more enjoyable and helping you appreciate the food you are eating.\n\nDid you know that mindful eating can improve digestion and satisfaction, making mealtime a more fulfilling and enjoyable experience? (Source: American Journal of Clinical Nutrition)"
        }
    ]
}

# Healthy Filipino recipes
filipino_recipes = {
    "Portion Control": [
        {
            "dish": "Ensaladang Talong",
            "reason": "This eggplant salad is light and low in calories, perfect for portion control."
        },
        {
            "dish": "Tinolang Manok",
            "reason": "A healthy chicken soup that is nutritious and low in calories."
        }
    ],
    "Emotional Eating": [
        {
            "dish": "Lumpiang Sariwa",
            "reason": "Fresh vegetable rolls that are both healthy and comforting."
        },
        {
            "dish": "Ginisang Ampalaya",
            "reason": "Bitter melon stir-fry that helps in reducing stress and is nutritious."
        }
    ],
    "Binge Eating": [
        {
            "dish": "Pancit Bihon",
            "reason": "A light noodle dish that is filling but not heavy, helping to control binge eating."
        },
        {
            "dish": "Sinigang na Hipon",
            "reason": "A sour shrimp soup that is both satisfying and low in calories."
        }
    ],
    "General Tips": [
        {
            "dish": "Laing",
            "reason": "A healthy vegetable dish made from taro leaves and coconut milk."
        },
        {
            "dish": "Pinakbet",
            "reason": "A vegetable dish that is nutritious and helps in maintaining a balanced diet."
        }
    ]
}

# Physical activities recommendations
physical_activities = {
    "Portion Control": [
        {
            "activity": "Yoga",
            "description": "Practicing yoga can help you become more mindful of your body and hunger cues."
        },
        {
            "activity": "Walking",
            "description": "Taking a walk after meals can help with digestion and prevent overeating."
        }
    ],
    "Emotional Eating": [
        {
            "activity": "Meditation",
            "description": "Meditation can help you manage stress and reduce emotional eating."
        },
        {
            "activity": "Dance",
            "description": "Dancing is a fun way to release emotions and reduce stress without turning to food."
        }
    ],
    "Binge Eating": [
        {
            "activity": "Running",
            "description": "Running can help you manage stress and reduce the urge to binge eat."
        },
        {
            "activity": "Strength Training",
            "description": "Strength training can boost your metabolism and help control your appetite."
        }
    ],
    "General Tips": [
        {
            "activity": "Swimming",
            "description": "Swimming is a full-body workout that helps maintain a healthy weight."
        },
        {
            "activity": "Cycling",
            "description": "Cycling is a fun way to stay active and maintain overall fitness."
        }
    ]
}

# Initialize session state for saved tips
if "saved_tips" not in st.session_state:
    st.session_state.saved_tips = []
if "last_recommendation" not in st.session_state:
    st.session_state.last_recommendation = None

# Function to recommend a mindful eating tip based on focus area and tip selection
def recommend_tip(area, selected_tip):
    if area in mindful_eating_tips:
        for tip in mindful_eating_tips[area]:
            if tip["tip"] == selected_tip:
                st.session_state.last_recommendation = tip
                return tip
    return "Sorry, we don't have tips for that focus area."

# Function to recommend a random mindful eating tip from any category
def recommend_random_tip():
    all_tips = [tip for tips in mindful_eating_tips.values() for tip in tips]
    random_tip = random.choice(all_tips)
    st.session_state.last_recommendation = random_tip
    return random_tip

# Function to recommend a Filipino recipe based on focus area
def recommend_recipe(area):
    if area in filipino_recipes:
        return random.choice(filipino_recipes[area])
    return "Sorry, we don't have recipes for that focus area."

# Function to recommend a physical activity based on focus area
def recommend_activity(area):
    if area in physical_activities:
        return random.choice(physical_activities[area])
    return "Sorry, we don't have activities for that focus area."

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
                    st.success(f"Description: {recommendation['description']}")
                    recipe = recommend_recipe(area)
                    if isinstance(recipe, dict):
                        st.info(f"Healthy Food Recommendation: {recipe['dish']}\n\nReason: {recipe['reason']}")
                    activity = recommend_activity(area)
                    if isinstance(activity, dict):
                        st.info(f"Recommended Physical Activity: {activity['activity']}\n\nDescription: {activity['description']}")
                else:
                    st.error(recommendation)
        else:
            st.error("The entered area of focus is not part of our categories.")
    
    # Add a button to get a random tip
    if st.button("Get Random Tip"):
        random_recommendation = recommend_random_tip()
        st.info(f"Random Tip: {random_recommendation['tip']}\n\nDescription: {random_recommendation['description']}")
        recipe = recommend_recipe("General Tips")
        if isinstance(recipe, dict):
            st.info(f"Healthy Food Recommendation: {recipe['dish']}\n\nReason: {recipe['reason']}")
        activity = recommend_activity("General Tips")
        if isinstance(activity, dict):
            st.info(f"Recommended Physical Activity: {activity['activity']}\n\nDescription: {activity['description']}")

if __name__ == "__main__":
    main()
