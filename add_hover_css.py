import os
import glob

css_dir = r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com\wp-content\cache\autoptimize\css"

hover_css = """
/* Custom Hover Effect for Cards */
.card.card--overlay {
    position: relative;
    overflow: hidden;
}

.card.card--overlay .what-solutions__technologies {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #2f535d; /* Dark teal background */
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease, visibility 0.3s ease;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-content: center;
    padding: 20px;
    z-index: 2;
    box-sizing: border-box;
}

.card.card--overlay .what-solutions__technologies-logo {
    width: 30%;
    margin: 5%;
    opacity: 0.2;
    transition: opacity 0.3s ease;
    display: flex;
    justify-content: center;
    align-items: center;
}

.card.card--overlay .what-solutions__technologies-logo img {
    max-width: 100%;
    height: auto;
    filter: brightness(0); /* Make icons dark */
}

.card.card--overlay:hover .what-solutions__technologies {
    opacity: 1;
    visibility: visible;
}

.card.card--overlay .card__caption {
    position: absolute;
    top: 30px;
    left: 30px;
    right: 30px;
    z-index: 3;
    transition: all 0.3s ease;
    height: auto;
}

.card.card--overlay:hover .card__caption {
    top: auto;
    bottom: 30px;
    transform: translateY(0);
}

.card.card--overlay:hover .card__title {
    color: #fff !important;
    margin-bottom: 0 !important;
    padding-bottom: 0 !important;
}

.card.card--overlay:hover .card__title::before,
.card.card--overlay:hover .card__title::after {
    display: none !important;
}

.card.card--overlay:hover .card__img {
    opacity: 0;
}
"""

for file in glob.glob(os.path.join(css_dir, "autoptimize_*_v2.css")):
    # Ignore small files like print css which is ~2KB
    if os.path.getsize(file) > 100000:
        with open(file, "a", encoding="utf-8") as f:
            f.write("\n" + hover_css + "\n")
        print("Appended hover CSS to", file)
