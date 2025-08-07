from flask import Flask, render_template, request
from utils.screenshot import capture_screenshot
from utils.alt_checker import check_alt_text
from utils.favicon_checker import check_favicon
from utils.heading_checker import check_headings
from utils.links_checker import check_links
from utils.og_checker import check_open_graph
from utils.seo import check_seo_tags
from utils.speed_checker import check_speed
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]

        # Screenshot
        image_path = capture_screenshot(url)
        if not image_path:
            return "Screenshot capture failed."


        # Baaki audits
        alt_results = check_alt_text(url)
        favicon_result = check_favicon(url)
        headings_result = check_headings(url)
        links_result = check_links(url)
        og_result = check_open_graph(url)
        seo_result = check_seo_tags(url)
        speed_result = check_speed(url)

        results = {
            "image_file": os.path.basename(image_path),
            "alt_results": alt_results,
            "favicon_result": favicon_result,
            "headings_result": headings_result,
            "links_result": links_result,
            "og_result": og_result,
            "seo_result": seo_result,
            "speed_result": speed_result,
        }

        return render_template("result.html", results=results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
