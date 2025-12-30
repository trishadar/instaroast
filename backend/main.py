# main.py
from fastapi import FastAPI
from analysis import get_instagram_profile
from image_analysis import analyze_image
from roast_ai import generate_roast

app = FastAPI()

@app.get("/roast/")
def roast_profile(link: str):
    # Extract username from link
    username = link.rstrip("/").split("/")[-1]
    
    # Get profile data
    profile_data = get_instagram_profile(username)
    
    # Analyze profile picture + posts
    image_insights = []
    image_insights.append(analyze_image(profile_data["profile_pic_url"]))
    for post in profile_data["recent_posts"]:
        image_insights.append(analyze_image(post["image_url"]))
    
    # Generate roast
    roast = generate_roast(profile_data, image_insights)
    return {"profile": profile_data, "roast": roast}
