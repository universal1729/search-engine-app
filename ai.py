import webbrowser
from threading import Timer
from flask import Flask, render_template_string

app = Flask(__name__)


GOOGLE_LOGO = "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg"
YAHOO_LOGO  = "https://upload.wikimedia.org/wikipedia/commons/2/23/Yahoo%21_%282009-2013%29.svg"

BING_LOGO   = "https://upload.wikimedia.org/wikipedia/commons/e/e3/Bing_Fluent_Logo_Text.svg"

DUCK_LOGO   = "https://upload.wikimedia.org/wikipedia/en/9/90/The_DuckDuckGo_Duck.png"


# --- Search engine data ---
search_engines = {
    "Gemini": {"url": "https://www.gemini.com", "logo": GOOGLE_LOGO},
    "Grok": {"url": "https://www.grok.com", "logo": YAHOO_LOGO},
    "Copilot": {"url": "https://www.copilot.com", "logo": BING_LOGO},
    "ChatGPT": {"url": "https://www.chatgpt.com", "logo": DUCK_LOGO},
}

HTML = """
<!doctype html>
<html>
<head>
<title>Search Engine Selector</title>

<style>
body{
    background:#f5f7fa;
    font-family:Segoe UI, sans-serif;
}
h1{
    text-align:center;
    color:#0066cc;
}
.card{
    background:white;
    max-width:420px;
    margin:40px auto;
    padding:25px;
    border-radius:14px;
    box-shadow:0 4px 12px rgba(0,0,0,.15);
}
button{
    width:100%;
    padding:12px;
    cursor:pointer;
    border-radius:10px;
    border:1px solid #007bff;
    background:white;
}
#goBtn{
    margin-top:12px;
    background:#28a745;
    color:white;
    border:none;
    font-size:16px;
}
#goBtn:hover{
    background:#218838;
}
.list{
    display:none;
    margin-top:8px;
    border:1px solid #ddd;
    border-radius:10px;
}
.item{
    display:flex;
    align-items:center;
    padding:8px;
}
.item:hover{
    background:#eee;
}
img{
    width:24px;
    height:24px;
    margin-right:10px;
}
footer{
    margin-top:50px;
    text-align:center;
    color:#777;
}
</style>
</head>

<body>

<h1>AI Website Selector</h1>

<div class="card">

    <button onclick="toggle()">Select an AI website ▼</button>

    <div id="dropdown" class="list">

        {% for name, info in engines.items() %}
        <div class="item" onclick="pick('{{ info.url }}','{{ info.logo }}','{{ name }}')">
            <img src="{{ info.logo }}">
            {{ name }}
        </div>
        {% endfor %}

    </div>

    <button id="goBtn" onclick="go()">Go</button>

</div>

<footer>
    2025 - Single File AI Search App
</footer>

<script>
let url = null

function toggle() {
    document.getElementById("dropdown").style.display =
    document.getElementById("dropdown").style.display === "block"
        ? "none"
        : "block";
}

function pick(u,logo,name){
    url = u;
    document.querySelector("button").innerHTML =
        `<img src="${logo}">${name} ▼`
    document.getElementById("dropdown").style.display="none";
}

function go(){
    if(!url) alert("Please select an AI website!");
    else window.open(url,"_blank");
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, engines=search_engines)

if __name__ == "__main__":
    import threading
    import time

    def open_browser():
        time.sleep(1.5)
        webbrowser.open("http://127.0.0.1:5000", new=1)

    threading.Thread(target=open_browser).start()
    app.run(debug=True)
