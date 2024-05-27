import streamlit as st
import random
import google.generativeai as genai
from dotenv import load_dotenv

# Dictionary of mindful eating tips categorized by area of focus
mindful_eating_tips = {
    "portion control": [
        {
            "tip": "Use smaller plates",
            "description": "Using smaller plates can help you control your portions better. When you use a smaller plate, your servings look larger, which can make you feel more satisfied with less food. This simple change can help you reduce your calorie intake without feeling deprived. Additionally, by visually tricking your brain into thinking you're eating more, smaller plates can help you enjoy your meals more and reduce the likelihood of overeating.",
            "fact": "Did you know that studies have shown people tend to eat less when they use smaller plates, leading to a reduction in calorie intake by up to 30%? (Source: Journal of Consumer Research)",
            "activity": "Walking",
            "activity_description": "Walking is a simple yet effective way to burn calories and stay active. It's a low-impact exercise that can be done anywhere and doesn't require any special equipment."
        },
        {
            "tip": "Measure your food",
            "description": "Measuring your food portions with cups and spoons can help you be more aware of how much you are eating. It ensures that you are not consuming more than you need, which can help you maintain a healthy weight and avoid overeating. By taking the guesswork out of portion sizes, you can better manage your intake and make informed decisions about your meals.",
            "fact": "Did you know that consistently measuring your food can help you understand portion sizes better, making it easier to make healthier choices without overindulging? (Source: American Journal of Clinical Nutrition)",
            "activity": "Cycling",
            "activity_description": "Cycling is a fun way to get exercise and burn calories. It's a great cardiovascular workout that can help improve your overall fitness and endurance."
        },
        {
            "tip": "Serve from the kitchen",
            "description": "Serving your food directly from the kitchen instead of placing serving dishes on the dining table can prevent you from taking second helpings. This strategy helps you stick to your initial portion size, reducing the temptation to overeat. By controlling the serving process, you can better manage your portions and avoid mindless eating.",
            "fact": "Did you know that research suggests people eat about 20% less when food is served from the kitchen instead of having serving dishes on the table? (Source: Cornell University)",
            "activity": "Jogging",
            "activity_description": "Jogging is a great cardiovascular exercise that helps burn calories and improve fitness. It's a high-impact activity that can strengthen your muscles and boost your endurance."
        },
        {
            "tip": "Eat slowly",
            "description": "Taking your time to chew thoroughly and savor your food can help you recognize when you are full. Eating slowly allows your brain to catch up with your stomach, preventing overeating and promoting better digestion. By giving yourself time to enjoy each bite, you can enhance your dining experience and better appreciate the flavors and textures of your meal.",
            "fact": "Did you know that eating slowly can reduce calorie intake and aid digestion? It takes about 20 minutes for your brain to register that you are full. (Source: Harvard Health)",
            "activity": "Yoga",
            "activity_description": "Yoga helps improve flexibility, strength, and mindfulness. It's a holistic practice that combines physical postures, breathing exercises, and meditation to promote overall well-being."
        }
    ],
    "emotional eating": [
        {
            "tip": "Identify triggers",
            "description": "Keeping a food diary to note when and why you eat can help you recognize patterns and emotional triggers. Understanding these triggers can help you develop healthier coping mechanisms for stress, boredom, or other emotions. By becoming more aware of your eating habits, you can better manage your emotional responses and make more mindful choices about when and what to eat.",
            "fact": "Did you know that identifying emotional eating triggers can help reduce stress-related eating by up to 50%, leading to healthier eating habits? (Source: Mayo Clinic)",
            "activity": "Journaling",
            "activity_description": "Writing about your feelings can be a healthy way to process emotions and reduce the urge to eat for comfort. Journaling provides an outlet for expressing your thoughts and can help you understand and manage your emotions better."
        },
        {
            "tip": "Find alternatives",
            "description": "Engaging in activities like walking, reading, or talking to a friend can be great alternatives to eating when you're feeling stressed or emotional. Finding other ways to cope with your feelings can help you break the cycle of emotional eating. By distracting yourself with enjoyable activities, you can reduce the urge to eat and develop healthier habits.",
            "fact": "Did you know that finding non-food-related activities can reduce the urge to eat by providing a distraction and helping to manage emotions more effectively? (Source: American Psychological Association)",
            "activity": "Dancing",
            "activity_description": "Dancing is a fun way to exercise and lift your spirits. It's a physical activity that can improve your mood and help you stay active."
        },
        {
            "tip": "Practice mindfulness",
            "description": "Before eating, take a few deep breaths and assess your hunger level. This practice helps ensure that you are eating because you are genuinely hungry and not just eating out of habit or emotion. By becoming more mindful of your hunger cues, you can make better decisions about when and how much to eat.",
            "fact": "Did you know that practicing mindfulness before eating can decrease calorie intake and improve overall emotional well-being? (Source: Mindful Eating Research)",
            "activity": "Meditation",
            "activity_description": "Meditation helps you become more aware of your thoughts and emotions, reducing the likelihood of emotional eating. It's a practice that can enhance your overall mental health and well-being."
        },
        {
            "tip": "Seek support",
            "description": "Talking to a counselor or joining a support group can provide you with the support you need to manage emotional eating. Sharing your experiences with others can help you feel less alone and give you new strategies to cope with your emotions. By connecting with others who understand your struggles, you can find encouragement and accountability in your journey toward healthier eating habits.",
            "fact": "Did you know that support groups can offer a sense of community and accountability, which can be crucial in overcoming emotional eating habits? (Source: National Eating Disorders Association)",
            "activity": "Support Groups",
            "activity_description": "Joining a support group can provide you with the encouragement and advice needed to overcome emotional eating. It's a space where you can share your experiences and learn from others."
        }
    ],
    "binge eating": [
        {
            "tip": "Plan your meals",
            "description": "Having regular meals and snacks can help prevent extreme hunger, which can lead to binging. Planning your meals ensures that you are eating balanced, nutritious foods throughout the day, keeping your hunger and cravings in check. By maintaining a consistent eating schedule, you can better manage your appetite and avoid the triggers that lead to binge eating.",
            "fact": "Did you know that meal planning can reduce the frequency of binge eating episodes by providing structure and ensuring balanced nutrition? (Source: International Journal of Eating Disorders)",
            "activity": "Meal Prepping",
            "activity_description": "Preparing your meals in advance helps you control portions and avoid impulsive eating. It's a practical way to ensure you have healthy options available throughout the week."
        },
        {
            "tip": "Avoid distractions",
            "description": "Eating without distractions like TV or phones allows you to focus on your meal and recognize when you are full. Being mindful during meals can help you enjoy your food more and prevent overeating. By eliminating distractions, you can pay better attention to your body's signals and stop eating when you're satisfied.",
            "fact": "Did you know that eating without distractions can improve digestion and reduce overeating by increasing awareness of satiety signals? (Source: American Journal of Clinical Nutrition)",
            "activity": "Strength Training",
            "activity_description": "Strength training exercises can help you build muscle and burn calories. It's a form of physical activity that can boost your metabolism and support overall health."
        },
        {
            "tip": "Stay hydrated",
            "description": "Drinking water throughout the day can help manage your hunger and prevent overeating. Sometimes, thirst can be mistaken for hunger, so staying hydrated can help you better understand your body's true needs. By keeping a water bottle with you, you can easily stay hydrated and avoid unnecessary snacking.",
            "fact": "Did you know that staying hydrated can reduce hunger pangs and aid in overall body function, making it easier to distinguish between hunger and thirst? (Source: National Institutes of Health)",
            "activity": "Swimming",
            "activity_description": "Swimming is a full-body workout that helps maintain a healthy weight. It's a low-impact exercise that can improve cardiovascular health and build strength."
        }
    ],
    "general tips": [
        {
            "tip": "Listen to your body",
            "description": "Eat when you're hungry and stop when you're satisfied, not full. Paying attention to your body's hunger and fullness cues can help you avoid overeating and make healthier choices about when and how much to eat. By tuning in to your body's signals, you can develop a more intuitive approach to eating.",
            "fact": "Did you know that listening to your body's signals can improve eating habits and reduce the risk of overeating, leading to better overall health? (Source: Harvard Health)",
            "activity": "Mindful Breathing",
            "activity_description": "Practicing mindful breathing helps you stay in tune with your body's signals. It's a simple practice that can reduce stress and improve your awareness of hunger and fullness."
        },
        {
            "tip": "Choose whole foods",
            "description": "Opt for whole, unprocessed foods that nourish your body. Whole foods like fruits, vegetables, whole grains, and lean proteins are packed with nutrients and can help you feel more satisfied than processed foods. By prioritizing whole foods, you can support your health and well-being.",
            "fact": "Did you know that choosing whole foods can provide essential nutrients and improve satiety, reducing the likelihood of overeating processed foods? (Source: Academy of Nutrition and Dietetics)",
            "activity": "Hiking",
            "activity_description": "Hiking is a great way to enjoy nature and get some exercise. It's an activity that can improve your physical fitness and mental well-being."
        },
        {
            "tip": "Balance your plate",
            "description": "Including a variety of food groups in your meals ensures balanced nutrition. A balanced plate with proteins, carbohydrates, fats, and vegetables can provide you with all the essential nutrients your body needs to function well. By aiming for balance, you can support your body's needs and maintain overall health.",
            "fact": "Did you know that a balanced diet can enhance overall health and energy levels, supporting a well-functioning body and mind? (Source: World Health Organization)",
            "activity": "Pilates",
            "activity_description": "Pilates helps improve flexibility, strength, and balance. It's a form of exercise that can enhance your physical fitness and promote a strong core."
        },
        {
            "tip": "Enjoy your food",
            "description": "Take time to savor each bite and enjoy the flavors and textures of your food. Eating mindfully can enhance your eating experience, making meals more enjoyable and helping you appreciate the food you are eating. By slowing down and focusing on your meal, you can improve your digestion and overall satisfaction.",
            "fact": "Did you know that mindful eating can improve digestion and satisfaction, making mealtime a more fulfilling and enjoyable experience? (Source: American Journal of Clinical Nutrition)",
            "activity": "Gardening",
            "activity_description": "Gardening is a relaxing activity that gets you moving and can be a great way to grow your own healthy foods. It's a hobby that can reduce stress and provide fresh, nutritious produce."
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
    normalized_area = area.lower()
    if normalized_area in mindful_eating_tips:
        for tip in mindful_eating_tips[normalized_area]:
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

# Main function to run the Streamlit app
def main():
    st.title("Mindful Eating Guide Recommendation")
    st.subheader("Welcome to the Mindful Eating Guide! Get personalized tips for developing a healthier relationship with food.")

    st.markdown("""
    Created by Samantha V. Bangcaya, a student - BSCS 3B AI.
    This application is designed to offer you personalized tips for developing a healthier relationship with food. This guide is inspired by my own journey through various eating habits and challenges.

    Having experienced emotional eating, binge eating, and the need for better portion control, I was motivated to develop this tool to help others. The Mindful Eating Guide provides practical, easy-to-follow tips for managing portion sizes, addressing emotional triggers, and simply enjoying your meals more mindfully.
    """)

    st.markdown("""
    **Type your area of focus (choose from: Portion Control, Emotional Eating, Binge Eating, General Tips):**
    """)

    # Ask user for their area of focus
    area = st.text_input("").strip().lower()

    if area:
        if area in mindful_eating_tips:
            tips = [tip["tip"] for tip in mindful_eating_tips[area]]
            selected_tip = st.selectbox("Select a tip:", tips)

            if st.button("Get Tip"):
                recommendation = recommend_tip(area, selected_tip)
                if isinstance(recommendation, dict):
                    st.success(f"Description: {recommendation['description']}")
                    st.info(f"Interesting Fact: {recommendation['fact']}")
                    st.info(f"Recommended Physical Activity: {recommendation['activity']}\n\nDescription: {recommendation['activity_description']}")
                else:
                    st.error(recommendation)
        else:
            st.error("The entered area of focus is not part of our categories.")

    # Add a button to get a random tip
    if st.button("Get Random Tip"):
        random_recommendation = recommend_random_tip()
        st.info(f"Random Tip: {random_recommendation['tip']}\n\nDescription: {random_recommendation['description']}")
        st.info(f"Interesting Fact: {random_recommendation['fact']}")
        st.info(f"Recommended Physical Activity: {random_recommendation['activity']}\n\nDescription: {random_recommendation['activity_description']}")

if __name__ == "__main__":
    main()
