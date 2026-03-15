def title_extract(html: str) -> str:
    title_tag = "<title>"
    title_tag_start = html.index("<title>") + len(title_tag)
    title_tag_end = html.index("</title>")
    title = html[title_tag_start:title_tag_end].strip()
    return title
