from flask import Flask, render_template, jsonify, request
from events import events

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/events')
def get_events():
    event_list = []
    for date, event in events.items():
        event_list.append({
            "title": event,
            "start": date
        })
    return jsonify(event_list)

@app.route('/event')
def get_event():
    date = request.args.get("date")
    if date in events:
        return jsonify({"event": events[date]})
    else:
        return jsonify({"event": "일정 없음"})

if __name__ == "__main__":
    app.run(debug=True)
