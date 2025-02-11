def test_base_url(base_url):
    print("\nA környezeti változó URL-je:", base_url)
    assert base_url.startswith("https://")