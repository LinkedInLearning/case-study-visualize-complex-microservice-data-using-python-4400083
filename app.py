import json
import plantuml
import requests


def load_data():
    response = requests.get(
        "https://randomuser.me/api/?format=json", timeout=5000)
    if response.status_code == 200:
        return response.json()["results"][0]
    else:
        print("Data did not load correctly")
        return None


def write_plantuml_file(res):
    nodeName = res["name"]["first"] + "_" + res["name"]["last"]
    with open("plantuml.txt", "w", encoding="utf-8") as pf:
        pf.write("@startuml \n")
        pf.write("object " + nodeName + " \n")
        pf.write(nodeName + " : email = " + res["email"] + "\n")
        pf.write(nodeName + " : phone = " + res["phone"] + "\n")
        pf.write(nodeName + " : age = " + str(res["dob"]["age"]) + "\n")
        pf.write("@enduml \n")


def create_plantuml_image():
    plantuml.PlantUML("http://www.plantuml.com/plantuml/img/").processes_file(
        "plantuml.txt", outfile=None, errorfile=None)


if __name__ == '__main__':
    response_json = load_data()
    if response_json != None:
        write_plantuml_file(response_json)
        create_plantuml_image()
