from flask import Flask, render_template, request, redirect, url_for, send_file
import requests

app = Flask(__name__)

# Favorites list to store saved superheroes
favorites = []

@app.route("/", methods=["GET", "POST"])
def home():
    hero_data = None
    if request.method == "POST":
        hero_name = request.form.get("hero_name")
        if hero_name:
            # Fetch data from the SuperHero API
            api_url = f"https://superheroapi.com/api/6e0f688aa393865955a795e87e5705bb/search/{hero_name}"
            response = requests.get(api_url)  # External API request
            if response.status_code == 200:
                data = response.json()
                if data["response"] == "success":
                    hero_data = data["results"]
                else:
                    hero_data = []
            else:
                hero_data = []

    return render_template("index.html", hero_data=hero_data, favorites=favorites)

@app.route("/add_to_favorites/<hero_name>")
def add_to_favorites(hero_name):
    if hero_name not in favorites:
        favorites.append(hero_name)
    return redirect(url_for("home"))

@app.route("/remove_from_favorites/<hero_name>")
def remove_from_favorites(hero_name):
    if hero_name in favorites:
        favorites.remove(hero_name)
    return redirect(url_for("home"))

# Route to handle file download
@app.route("/download_hero_list")
def download_hero_list():
    try:
        return send_file(
            "hero_list.txt",
            as_attachment=True,
            download_name="hero_list.txt",
        )
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
