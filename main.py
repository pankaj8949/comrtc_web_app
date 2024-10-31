from flask import Flask, render_template
from contact import contact_routes

app = Flask(__name__)
contact_routes(app)  # Register contact routes

@app.route("/")
def Home():
    return render_template('index.html')

@app.route("/organizing-committee")
def OrganizingCommittee():
    return render_template('screens/about/oc.html')

@app.route("/scientific-committee")
def ScientificCommittee():
    return render_template('screens/about/sc.html')

@app.route("/scientific-committee-lead")
def ScientificCommitteeLead():
    return render_template('screens/about/scl.html')

@app.route("/join-the-scientific-committee")
def JoinTheScientificCommittee():
    return render_template('screens/about/jtsc.html')

@app.route("/service")
def Service():
    return render_template('service.html')

@app.route("/important-dates")
def ImportantDates():
    return render_template('screens/Guide for authors/importantdates.html')

@app.route("/review-process")
def ReviewProcess():
    return render_template('screens/Guide for authors/reviewprocess.html')

@app.route("/submission-guidelines")
def SubmissionGuidelines():
    return render_template('screens/Guide for authors/subgl.html')

@app.route("/submission")
def Submission():
    return render_template('screens/Guide for authors/submission.html')

@app.route("/paper-status")
def PaperStatus():
    return render_template('screens/Guide for authors/paperstatus.html')

@app.route("/detailed-schedule")
def DetailedSchedule():
    return render_template('screens/program/detailedschedule.html')

@app.route("/awards-grants")
def AwardsAndGrants():
    return render_template('screens/program/awardsngrants.html')

if __name__ == '__main__':
    app.run(debug=True)
