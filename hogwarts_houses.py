from flask import Flask, render_template, request

app = Flask(__name__)

ANSWER_WEIGHTS = {
    # Q1
    "take_responsibility": {"Gryffindor": 3, "Hufflepuff": 1},
    "deep_analysis": {"Ravenclaw": 3},
    "coordinate_team": {"Hufflepuff": 3, "Gryffindor": 1},
    "strategic_choice": {"Slytherin": 3, "Ravenclaw": 1},

    # Q2
    "just_do_it": {"Gryffindor": 2},
    "check_confluence": {"Ravenclaw": 3},
    "clarify_scope": {"Hufflepuff": 2, "Ravenclaw": 1},
    "risk_management": {"Slytherin": 3},

    # Q3
    "careful_change": {"Gryffindor": 2},
    "full_understanding": {"Ravenclaw": 3},
    "leave_it_better": {"Hufflepuff": 3},
    "use_constraints": {"Slytherin": 3},

    # Q4
    "take_the_hit": {"Gryffindor": 3},
    "failure_analysis": {"Ravenclaw": 3},
    "future_proof": {"Hufflepuff": 3, "Ravenclaw": 1},
    "gain_control": {"Slytherin": 3},

    # Q5
    "fix_and_ship": {"Gryffindor": 2},
    "prevent_recurrence": {"Ravenclaw": 3},
    "fix_and_document": {"Hufflepuff": 3},
    "pipeline_control": {"Slytherin": 3},
}

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        houses = {
            "Gryffindor": 0,
            "Ravenclaw": 0,
            "Hufflepuff": 0,
            "Slytherin": 0,
        }

        for _, answer_key in request.form.items():
            if answer_key in ANSWER_WEIGHTS:
                for house, points in ANSWER_WEIGHTS[answer_key].items():
                    houses[house] += points

        sorted_houses = sorted(houses.items(), key=lambda x: x[1], reverse=True)
        primary, secondary = sorted_houses[0], sorted_houses[1]

        return render_template(
            "result.html",
            house=primary[0],
            score=primary[1],
            close_house=secondary[0],
        )

    return render_template("quiz.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
