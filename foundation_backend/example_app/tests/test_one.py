def test_api(api_client, db):
    response = api_client.get('')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, world!'}
