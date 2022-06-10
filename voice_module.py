import requests
import soundrecord as sr
import speech2text as stt

bot_response = ""

while bot_response not in ["À bientôt", "Au revoir", "À plus", "Bye"]:
    message = "Bye"
    start = input("Voulez vous enregistrer n message (N/y): ")
    if start.lower() == "y":
        filename = sr.recording()
        message = stt.make_prediction(file=filename)

    print("you ->", message)
    response = requests.post(
        "http://localhost:5002/webhooks/rest/webhook", json={"message": message}
    )
    print("bot -> ", end=" ")
    for r in response.json():
        bot_response = r["text"] if bot_response else "Pouvez-vous repeter svp?"
        print(bot_response)
