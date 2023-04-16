import json

with open("./profile_service_response.json", encoding="utf-8") as profile_file:
    profile_json = json.load(profile_file)

with open("./posts_management_service_response.json", encoding="utf-8") as posts_file:
    posts_json = json.load(posts_file)

with open("./moderation_service_response.json", encoding="utf-8") as moderation_file:
    moderation_json = json.load(moderation_file)
