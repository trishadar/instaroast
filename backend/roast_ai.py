# roast_ai.py
import openai, os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_roast(profile_data, image_insights):
    prompt = f"""
    Roast this Instagram profile in a funny, sarcastic way. Do NOT be hateful.

    Username: {profile_data['username']}
    Bio: {profile_data['bio']}
    Followers: {profile_data['followers']}
    Following: {profile_data['following']}
    Number of Posts: {profile_data['num_posts']}
    Recent Posts Captions: {[p['caption'] for p in profile_data['recent_posts']]}
    Recent Posts Image Insights: {image_insights}
    Profile Pic URL: {profile_data['profile_pic_url']}

    Generate 5 short roast lines.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message["content"]
