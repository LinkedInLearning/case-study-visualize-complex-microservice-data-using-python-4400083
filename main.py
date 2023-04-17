import json
import plantuml


def load_data():
    with open("./profile_service_response.json", encoding="utf-8") as profile_file:
        profile_json = json.load(profile_file)

    with open("./posts_management_service_response.json", encoding="utf-8") as posts_file:
        posts_json = json.load(posts_file)

    with open("./moderation_service_response.json", encoding="utf-8") as moderation_file:
        moderation_json = json.load(moderation_file)

    return (profile_json, posts_json, moderation_json)


def write_plantuml_file(profile_data, posts_data, moderation_data):
    with open("plantuml.txt", "w", encoding="utf-8") as pf:
        # object nameOfNode
        pf.write("@startuml \n")
        pf.write("object " + profile_data["username"] + "\n")
        # nameOfNode : nameOfAttribute = attributeValue
        pf.write(profile_data["username"] +
                 " : name = " + profile_data["name"] + "\n")
        pf.write(profile_data["username"] + " : biography = " +
                 profile_data["biography"] + "\n")
        pf.write(profile_data["username"] + " : hyperlink = " +
                 profile_data["hyperlink"] + "\n")
        pf.write(profile_data["username"] + " : is_reported = " +
                 str(profile_data["is_reported"]) + "\n")
        pf.write(profile_data["username"] + " : is_shadowbanned = " +
                 str(profile_data["is_shadowbanned"]) + "\n")
        pf.write(profile_data["username"] + " : number_of_followers = " +
                 str(profile_data["number_of_followers"]) + "\n")
        pf.write(profile_data["username"] + " : number_of_posts = " +
                 str(profile_data["number_of_posts"]) + "\n")
        pf.write(profile_data["username"] + " : number_of_following = " +
                 str(profile_data["number_of_following"]) + "\n")

        for post in posts_data:
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
            # nameOfNodeOne -> nameOfNodeTwo
            pf.write(profile_data["username"] + " -down-> " +
                     "post_" + str(post["post_id"]) + "\n")

        for moderated_post in moderation_data:
            pf.write("post_" + str(moderated_post["post_id"]) +
                     " : is_reported = " + str(moderated_post["is_reported"]) + "\n")
            pf.write("post_" + str(moderated_post["post_id"]) +
                     " : is_manual = " + str(moderated_post["is_manual"]) + "\n")
            pf.write("post_" + str(moderated_post["post_id"]) +
                     " : reason = " + moderated_post["reason"] + "\n")

            if "reported_by" in moderated_post:
                pf.write(
                    "post_" + str(moderated_post["post_id"]) + " : reported_by = " + moderated_post["reported_by"] + "\n")
        pf.write("@enduml \n")


def create_plantuml_image():
    plantuml.PlantUML("http://www.plantuml.com/plantuml/img/").processes_file(
        "plantuml.txt", outfile=None, errorfile=None)


if __name__ == '__main__':
    profile, posts, moderation = load_data()
    write_plantuml_file(profile, posts, moderation)
    create_plantuml_image()
