def test_base_url(base_url):
    print("\nA env var URL:", base_url)
    assert base_url.startswith("https://")