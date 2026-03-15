from solution.ex2_extracting_from_html import title_extract

def test_title_extract():
    html = "<html><head><title>My Title</title></head><body></body></html>"
    expected_title = "My Title"
    result = title_extract(html)
    assert result == expected_title

def test_empty_title():
    html = "<html><head><title></title></head><body></body></html>"
    expected_title = ""
    result = title_extract(html)
    assert result == expected_title

def test_title_with_spaces():
    html = "<html><head><title>  Adham  </title></head><body></body></html>"
    expected_title = "Adham"
    result = title_extract(html)
    assert result == expected_title