import json

with open("./profile_service_response.json", encoding="utf-8") as profile_file:
    profile_json = json.load(profile_file)

with open("./posts_management_service_response.json", encoding="utf-8") as posts_file:
    posts_json = json.load(posts_file)

with open("./moderation_service_response.json", encoding="utf-8") as moderation_file:
    moderation_json = json.load(moderation_file)

context = {
    "name": profile_json["name"],
    "username": profile_json["username"],
    "biography": profile_json["biography"],
    "hyperlink": profile_json["hyperlink"],
    "is_reported": profile_json["is_reported"],
    "is_shadowbanned": profile_json["is_shadowbanned"],
    "number_of_followers": profile_json["number_of_followers"],
    "number_of_posts": profile_json["number_of_posts"],
    "posts": []
}

for post in posts_json:
    context_post = {
        "post_id": post["post_id"],
        "post_caption": post["post_caption"],
        "images": post["images"],
        "comments": post["comments"],
        "hashtags": post["hashtags"],
        "date_published": post["date_published"],
        "number_of_likes": post["number_of_likes"]
    }

    for moderated_post in moderation_json:
        if moderated_post["post_id"] == context_post["post_id"]:
            context_post["is_reported"] = moderated_post["is_reported"]
            context_post["is_manual"] = moderated_post["is_manual"]
            context_post["reason"] = moderated_post["reason"]
            if "reported_by" in moderated_post:
                context_post["reported_by"] = moderated_post["reported_by"]

    context["posts"].append(context_post)

print(context)
