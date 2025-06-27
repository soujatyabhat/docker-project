import pytest
from app import app, password_gen, alpha, non_alpha

# ---------- UNIT TESTS FOR password_gen FUNCTION ----------

def test_password_gen_lengths():
    result = password_gen(3, 4, 100)
    assert len(result) >= 8  # 3 + 4 + at least 1 digit
    assert any(c.isdigit() for c in result)
    assert any(c in non_alpha for c in result)
    assert any(c in alpha for c in result)

def test_password_gen_ranges():
    result = password_gen(5, 5, 10)
    digits = [c for c in result if c.isdigit()]
    assert int(''.join(digits)) < 10

# ---------- INTEGRATION TESTS FOR FLASK ROUTES ----------

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'True'

def test_pass_type_easy(client):
    response = client.get('/passtype/easy')
    data = response.get_json()
    assert response.status_code == 200
    assert data['passType'] == 'easy'
    assert len(data['value']) >= 8

def test_pass_type_hard(client):
    response = client.get('/passtype/hard')
    data = response.get_json()
    assert data['passType'] == 'hard'
    assert any(c in non_alpha for c in data['value'])
