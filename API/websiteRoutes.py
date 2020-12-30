from API import app
from flask import request, redirect
import requests
import json


@app.route('/contactForm', methods=["POST"])
def contactForm():
    try:
        name = request.form["FullName"]
        email = request.form["Email"]
        message = request.form["Message"]
    except Exception:
        return "", 500

    url = "https://discordapp.com/api/webhooks/741723691615780945/UvEMpK7yX4o1OOJvuOC9vbgD1uBj3oxO5RfIrVCat9qvKKPMUxug43DmG3_SVo76x5vK"  # webhook url

    data = {}
    data["username"] = "Volunteerio Contact Form"

    embed = {}
    embed["title"] = name
    embed["fields"] = [
        {
            "name": "Email",
            "value": email
        },
        {
            "name": "Message",
            "value": message
        },
        {
            "name": "IP Addr",
            "value": f"[{request.remote_addr}](https://whatismyipaddress.com/ip/{request.remote_addr})"
        }
    ]
    data["embeds"] = [embed]

    result = requests.post(url, data=json.dumps(data), headers={
                           "Content-Type": "application/json"})

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        print(result.content)
        return redirect("https://volunteerio.us")

    return redirect("https://volunteerio.us")


@app.route('/demoForm', methods=["POST"])
def demoForm():
    try:
        name = request.form["FullName"]
        email = request.form["Email"]
        schoolName = request.form["SchoolName"]
        message = request.form["Message"]
    except Exception:
        return "", 500

    url = "https://discordapp.com/api/webhooks/741723691615780945/UvEMpK7yX4o1OOJvuOC9vbgD1uBj3oxO5RfIrVCat9qvKKPMUxug43DmG3_SVo76x5vK"  # webhook url

    data = {}
    data["username"] = "Volunteerio Demo Form"

    embed = {}
    embed["title"] = name
    embed["fields"] = [
        {
            "name": "School Name",
            "value": schoolName
        },
        {
            "name": "Email",
            "value": email
        },
        {
            "name": "Message",
            "value": message
        },
        {
            "name": "IP Addr",
            "value": f"[{request.remote_addr}](https://whatismyipaddress.com/ip/{request.remote_addr})"
        }
    ]
    data["embeds"] = [embed]

    result = requests.post(url, data=json.dumps(data), headers={
                           "Content-Type": "application/json"})

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        print(result.content)
        return redirect("https://volunteerio.us")

    return redirect("https://volunteerio.us")
