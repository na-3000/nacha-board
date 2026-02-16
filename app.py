from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 投稿をメモリで保存（サーバー再起動で消える）
posts = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "名無し")
        text = request.form.get("text", "")
        if text:
            posts.append({"name": name, "text": text})
        return redirect("/")  # 投稿後にリロード
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
