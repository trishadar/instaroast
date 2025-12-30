# analysis.py
import instaloader

def get_instagram_profile(username, max_posts=5):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    
    profile_data = {
        "username": profile.username,
        "bio": profile.biography,
        "followers": profile.followers,
        "following": profile.followees,
        "num_posts": profile.mediacount,
        "profile_pic_url": profile.profile_pic_url,
        "recent_posts": [],
        "recent_likes": [],
    }

    for i, post in enumerate(profile.get_posts()):
        if i >= max_posts:
            break
        profile_data["recent_posts"].append({
            "caption": post.caption,
            "image_url": post.url
        })
        profile_data["recent_likes"].append(post.likes)

    return profile_data
