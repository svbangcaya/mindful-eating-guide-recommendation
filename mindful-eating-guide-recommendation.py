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
            "fact": "Did you know that studies have shown people tend to eat less when they use smaller plates, leading to a reduction in calorie intake by up to 30%? (Source: Journal of Consumer Research)",
            "food": "Tinolang Manok",
            "food_reason": "A healthy chicken soup with vegetables that is filling and low in calories.",
            "activity": "Walking",
            "activity_description": "Walking is a simple yet effective way to burn calories and stay active.",
            "activity_fact": "Did you know that walking for 30 minutes a day can help improve cardiovascular health and aid in weight management? (Source: American Heart Association)"
        },
        {
            "tip": "Measure your food",
            "description": "Measuring your food portions with cups and spoons can help you be more aware of how much you are eating. It ensures that you are not consuming more than you need, which can help you maintain a healthy weight and avoid overeating.",
            "fact": "Did you know that consistently measuring your food can help you understand portion sizes better, making it easier to make healthier choices without overindulging? (Source: American Journal of Clinical Nutrition)",
            "food": "Ensaladang Talong",
            "food_reason": "A nutritious eggplant salad that helps you keep portions in check.",
            "activity": "Cycling",
            "activity_description": "Cycling is a fun way to get exercise and burn calories.",
            "activity_fact": "Did you know that cycling for an hour can burn up to 600 calories? (Source: Harvard Health)"
        },
        {
            "tip": "Serve from the kitchen",
            "description": "Serving your food directly from the kitchen instead of placing serving dishes on the dining table can prevent you from taking second helpings. This strategy helps you stick to your initial portion size, reducing the temptation to overeat.",
            "fact": "Did you know that research suggests people eat about 20% less when food is served from the kitchen instead of having serving dishes on the table? (Source: Cornell University)",
            "food": "Sinigang na Isda",
            "food_reason": "A flavorful fish soup that is nutritious and helps control portions.",
            "activity": "Jogging",
            "activity_description": "Jogging is a great cardiovascular exercise that helps burn calories and improve fitness.",
            "activity_fact": "Did you know that jogging for 30 minutes can burn around 300 calories? (Source: Mayo Clinic)"
        },
        {
            "tip": "Eat slowly",
            "description": "Taking your time to chew thoroughly and savor your food can help you recognize when you are full. Eating slowly allows your brain to catch up with your stomach, preventing overeating and promoting better digestion.",
            "fact": "Did you know that eating slowly can reduce calorie intake and aid digestion? It takes about 20 minutes for your brain to register that you are full. (Source: Harvard Health)",
            "food": "Pinakbet",
            "food_reason": "A vegetable dish that is nutritious and helps in maintaining a balanced diet.",
            "activity": "Yoga",
            "activity_description": "Yoga helps improve flexibility, strength, and mindfulness.",
            "activity_fact": "Did you know that practicing yoga can help reduce stress and improve overall well-being? (Source: National Institutes of Health)"
        }
    ],
    "Emotional Eating": [
        {
            "tip": "Identify triggers",
            "description": "Keeping a food diary to note when and why you eat can help you recognize patterns and emotional triggers. Understanding these triggers can help you develop healthier coping mechanisms for stress, boredom, or other emotions.",
            "fact": "Did you know that identifying emotional eating triggers can help reduce stress-related eating by up to 50%, leading to healthier eating habits? (Source: Mayo Clinic)",
            "food": "Ginisang Ampalaya",
            "food_reason": "Bitter melon stir-fry that helps in reducing stress and is nutritious.",
            "activity": "Journaling",
            "activity_description": "Writing about your feelings can be a healthy way to process emotions and reduce the urge to eat for comfort.",
            "activity_fact": "Did you know that journaling can help identify emotional triggers and develop healthier coping strategies? (Source: Journal of Clinical Psychology)"
        },
        {
            "tip": "Find alternatives",
            "description": "Engaging in activities like walking, reading, or talking to a friend can be great alternatives to eating when you're feeling stressed or emotional. Finding other ways to cope with your feelings can help you break the cycle of emotional eating.",
            "fact": "Did you know that finding non-food-related activities can reduce the urge to eat by providing a distraction and helping to manage emotions more effectively? (Source: American Psychological Association)",
            "food": "Lumpiang Sariwa",
            "food_reason": "Fresh vegetable rolls that are both healthy and comforting.",
            "activity": "Dancing",
            "activity_description": "Dancing is a fun way to exercise and lift your spirits.",
            "activity_fact": "Did you know that dancing can help reduce stress and improve mood? (Source: National Institute of Dance Medicine and Science)"
        },
        {
            "tip": "Practice mindfulness",
            "description": "Before eating, take a few deep breaths and assess your hunger level. This practice helps ensure that you are eating because you are genuinely hungry and not just eating out of habit or emotion.",
            "fact": "Did you know that practicing mindfulness before eating can decrease calorie intake and improve overall emotional well-being? (Source: Mindful Eating Research)",
            "food": "Ginataang Gulay",
            "food_reason": "A vegetable dish cooked in coconut milk that promotes mindful eating.",
            "activity": "Meditation",
            "activity_description": "Meditation helps you become more aware of your thoughts and emotions, reducing the likelihood of emotional eating.",
            "activity_fact": "Did you know that meditation can reduce stress and improve emotional health? (Source: National Center for Complementary and Integrative Health)"
        },
        {
            "tip": "Seek support",
            "description": "Talking to a counselor or joining a support group can provide you with the support you need to manage emotional eating. Sharing your experiences with others can help you feel less alone and give you new strategies to cope with your emotions.",
            "fact": "Did you know that support groups can offer a sense of community and accountability, which can be crucial in overcoming emotional eating habits? (Source: National Eating Disorders Association)",
            "food": "Arroz Caldo",
            "food_reason": "A comforting rice porridge that is both nutritious and soothing.",
            "activity": "Support Groups",
            "activity_description": "Joining a support group can provide you with the encouragement and advice needed to overcome emotional eating.",
            "activity_fact": "Did you know that support groups can significantly improve your chances of overcoming emotional eating? (Source: American Psychological Association)"
        }
    ],
    "Binge Eating": [
        {
            "tip": "Plan your meals",
            "description": "Having regular meals and snacks can help prevent extreme hunger, which can lead to binging. Planning your meals ensures that you are eating balanced, nutritious foods throughout the day, keeping your hunger and cravings in check.",
            "fact": "Did you know that meal planning can reduce the frequency of binge eating episodes by providing structure and ensuring balanced nutrition? (Source: International Journal of Eating Disorders)",
            "food": "Adobong Sitaw",
            "food_reason": "A healthy string bean dish that is easy to prepare and keeps you full longer.",
            "activity": "Meal Prepping",
            "activity_description": "Preparing your meals in advance helps you control portions and avoid impulsive eating.",
            "activity_fact": "Did you know that meal prepping can save time and help you stick to your dietary goals? (Source: Journal of Nutrition Education and Behavior)"
        },
        {
            "tip": "Avoid distractions",
            "description": "Eating without distractions like TV or phones allows you to focus on your meal and recognize when you are full. Being mindful during meals can help you enjoy your food more and prevent overeating.",
            "fact": "Did you know that eating without distractions can improve digestion and reduce overeating by increasing awareness of satiety signals? (Source: American Journal of Clinical Nutrition)",
            "food": "Laing",
            "food_reason": "A flavorful dish made with taro leaves that can be easily portioned to avoid overeating.",
            "activity": "Strength Training",
            "activity_description": "Strength training exercises can help you build muscle and burn calories.",
            "activity_fact": "Did you know that strength training can increase metabolism and help with weight management? (Source: Mayo Clinic)"
        },
        {
            "tip": "Stay hydrated",
            "description": "Drinking water throughout the day can help manage your hunger and prevent overeating. Sometimes, thirst can be mistaken for hunger, so staying hydrated can help you better understand your body's true needs.",
            "fact": "Did you know that staying hydrated can reduce hunger pangs and aid in overall body function, making it easier to distinguish between hunger and thirst? (Source: National Institutes of Health)",
            "food": "Tinolang Tahong",
            "food_reason": "A mussel soup that is hydrating and provides essential nutrients.",
            "activity": "Swimming",
            "activity_description": "Swimming is a full-body workout that helps maintain a healthy weight.",
            "activity_fact": "Did you know that swimming can burn up to 500 calories per hour and improve cardiovascular health? (Source: Centers for Disease Control and Prevention)"
        }
    ],
    "General Tips": [
        {
            "tip": "Listen to your body",
            "description": "Eat when you're hungry and stop when you're satisfied, not full. Paying attention to your body's hunger and fullness cues can help you avoid overeating and make healthier choices about when and how much to eat.",
            "fact": "Did you know that listening to your body's signals can improve eating habits and reduce the risk of overeating, leading to better overall health? (Source: Harvard Health)",
            "food": "Pako Salad",
            "food_reason": "A fern salad that is light and helps you listen to your hunger cues.",
            "activity": "Mindful Breathing",
            "activity_description": "Practicing mindful breathing helps you stay in tune with your body's signals.",
            "activity_fact": "Did you know that mindful breathing can reduce stress and improve overall well-being? (Source: National Institutes of Health)"
        },
        {
            "tip": "Choose whole foods",
            "description": "Opt for whole, unprocessed foods that nourish your body. Whole foods like fruits, vegetables, whole grains, and lean proteins are packed with nutrients and can help you feel more satisfied than processed foods.",
            "fact": "Did you know that choosing whole foods can provide essential nutrients and improve satiety, reducing the likelihood of overeating processed foods? (Source: Academy of Nutrition and Dietetics)",
            "food": "Pinakbet",
            "food_reason": "A nutritious mixed vegetable dish that is rich in vitamins and minerals.",
            "activity": "Hiking",
            "activity_description": "Hiking is a great way to enjoy nature and get some exercise.",
            "activity_fact": "Did you know that hiking can burn up to 400 calories per hour and improve cardiovascular health? (Source: American Hiking Society)"
        },
        {
            "tip": "Balance your plate",
            "description": "Including a variety of food groups in your meals ensures balanced nutrition. A balanced plate with proteins, carbohydrates, fats, and vegetables can provide you with all the essential nutrients your body needs to function well.",
            "fact": "Did you know that a balanced diet can enhance overall health and energy levels, supporting a well-functioning body and mind? (Source: World Health Organization)",
            "food": "Kare-Kare",
            "food_reason": "A balanced dish with meat, vegetables, and peanut sauce providing a mix of nutrients.",
            "activity": "Pilates",
            "activity_description": "Pilates helps improve flexibility, strength, and balance.",
            "activity_fact": "Did you know that Pilates can help improve core strength and overall fitness? (Source: Pilates Method Alliance)"
        },
        {
            "tip": "Enjoy your food",
            "description": "Take time to savor each bite and enjoy the flavors and textures of your food. Eating mindfully can enhance your eating experience, making meals more enjoyable and helping you appreciate the food you are eating.",
            "fact": "Did you know that mindful eating can improve digestion and satisfaction, making mealtime a more fulfilling and enjoyable experience? (Source: American Journal of Clinical Nutrition)",
            "food": "Lechon Kawali",
            "food_reason": "A tasty Filipino dish that can be enjoyed in moderation as part of a mindful eating practice.",
            "activity": "Gardening",
            "activity_description": "Gardening is a relaxing activity that gets you moving and can be a great way to grow your own healthy foods.",
            "activity_fact": "Did you know that gardening can burn up to 330 calories per hour and reduce stress? (Source: National Gardening Association)"
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
                    st.info(f"Healthy Food Recommendation: {recommendation['food']}\n\nReason: {recommendation['food_reason']}")
                    st.info(f"Recommended Physical Activity: {recommendation['activity']}\n\nDescription: {recommendation['activity_description']}\n\nInteresting Fact: {recommendation['activity_fact']}")
                else:
                    st.error(recommendation)
        else:
            st.error("The entered area of focus is not part of our categories.")

    # Add a button to get a random tip
    if st.button("Get Random Tip"):
        random_recommendation = recommend_random_tip()
        st.info(f"Random Tip: {random_recommendation['tip']}\n\nDescription: {random_recommendation['description']}\n\nInteresting Fact: {random_recommendation['fact']}")
        st.info(f"Healthy Food Recommendation: {random_recommendation['food']}\n\nReason: {random_recommendation['food_reason']}")
        st.info(f"Recommended Physical Activity: {random_recommendation['activity']}\n\nDescription: {random_recommendation['activity_description']}\n\nInteresting Fact: {random_recommendation['activity_fact']}")

if __name__ == "__main__":
    main()
