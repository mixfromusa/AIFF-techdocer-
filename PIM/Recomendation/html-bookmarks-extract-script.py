from lxml import html

def process_bookmarks(filename):
    bookmarks = []
    current_folder = None
    for event, element in html.iterparse(filename, events=("start", "end")):
        if event == "start":
            if element.tag == "H3":
                current_folder = element.text
            elif element.tag == "A":
                bookmark = {
                    "url": element.get("HREF"),
                    "title": element.text,
                    "date_added": element.get("ADD_DATE"),
                    "folder": current_folder
                }
                bookmarks.append(bookmark)
    return bookmarks