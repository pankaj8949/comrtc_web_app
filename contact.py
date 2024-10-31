from flask import render_template

def contact_routes(app):
    @app.route("/contact")
    def Contact():
        return render_template('contact.html') 