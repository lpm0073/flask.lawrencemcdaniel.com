from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')

@app.route('/sitemap_index.xml')
def sitemap_index():
    return app.send_static_file('sitemap_index.xml')

@app.route('/main-sitemap.xsl')
def mainsitemap():
    return app.send_static_file('main-sitemap.xsl')



if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')
