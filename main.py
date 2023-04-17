import json
import plantuml


def load_data():
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
        "number_of_following": profile_json["number_of_following"],
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
    return context


def write_plantuml_file(context):
    with open("plantuml.txt", "w", encoding="utf-8") as pf:
        # object nameOfNode
        pf.write("@startuml \n")
        pf.write("object " + context["username"] + "\n")
        # nameOfNode : nameOfAttribute = attributeValue
        pf.write(context["username"] + " : name = " + context["name"] + "\n")
        pf.write(context["username"] + " : biography = " +
                 context["biography"] + "\n")
        pf.write(context["username"] + " : hyperlink = " +
                 context["hyperlink"] + "\n")
        pf.write(context["username"] + " : is_reported = " +
                 str(context["is_reported"]) + "\n")
        pf.write(context["username"] + " : is_shadowbanned = " +
                 str(context["is_shadowbanned"]) + "\n")
        pf.write(context["username"] + " : number_of_followers = " +
                 str(context["number_of_followers"]) + "\n")
        pf.write(context["username"] + " : number_of_posts = " +
                 str(context["number_of_posts"]) + "\n")
        pf.write(context["username"] + " : number_of_following = " +
                 str(context["number_of_following"]) + "\n")

        for post in context["posts"]:
            pf.write("object post_" + str(post["post_id"]) + "\n")
            pf.write("post_" + str(post["post_id"]) +
                     " : post_caption = " + post["post_caption"] + "\n")
            pf.write("post_" + str(post["post_id"]) +
                     " : images = " + str(post["images"]) + "\n")
            pf.write("post_" + str(post["post_id"]) +
                     " : comments = " + str(post["comments"]) + "\n")
            pf.write("post_" + str(post["post_id"]) +
                     " : hashtags = " + str(post["hashtags"]) + "\n")
            pf.write("post_" + str(post["post_id"]) +
                     " : date_published = " + post["date_published"] + "\n")
            pf.write("post_" + str(post["post_id"]) +
                     " : is_reported = " + str(post["is_reported"]) + "\n")
            pf.write("post_" + str(post["post_id"]) +
                     " : is_manual = " + str(post["is_manual"]) + "\n")
            pf.write("post_" + str(post["post_id"]) +
                     " : reason = " + post["reason"] + "\n")

            if "reported_by" in post:
                pf.write(
                    "post_" + str(post["post_id"]) + " : reported_by = " + post["reported_by"] + "\n")

        pf.write("@enduml \n")


def create_plantuml_image():
    plantuml.PlantUML("http://www.plantuml.com/plantuml/img/").processes_file(
        "plantuml.txt", outfile=None, errorfile=None)


if __name__ == '__main__':
    context_json = load_data()
    write_plantuml_file(context_json)
    create_plantuml_image()
