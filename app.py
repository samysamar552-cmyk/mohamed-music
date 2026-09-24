from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    songs = [
        {
            "title": "My First Song",
            "artist": "Mohamed Music",
            "image": "https://images.unsplash.com/photo-1511379938547-c1f69419868d"
        },
        {
            "title": "Night Vibes",
            "artist": "Mohamed Music",
            "image": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f"
        },
        {
            "title": "Dream",
            "artist": "Mohamed Music",
            "image": "https://images.unsplash.com/photo-1524368535928-5b5e00ddc76b"
        }
    ]

    return render_template("index.html", songs=songs)


if __name__ == "__main__":
    app.run(debug=True)