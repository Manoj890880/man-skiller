import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


# Test create_portfolio_manager
def test_create_portfolio_manager(client):
    new_manager_data = {
        'name': 'John Doe',
        'status': True,
        'role': 'Administrator',
        'bio': 'Experienced project manager',
        'start_date': '2023-01-15',
    }

    response = client.post('/portfolio-managers', json=new_manager_data)
    assert response.status_code == 200
    assert response.get_json() is not None


# Test get_portfolio_manager_by_id
def test_get_portfolio_manager_by_id(client):
    # Assuming you have the ID of a portfolio manager to fetch
    manager_id = 1

    response = client.get(f'/portfolio-managers/{manager_id}')
    assert response.status_code == 200
    assert response.get_json() is not None


# Test update_portfolio_manager
def test_update_portfolio_manager(client):
    # Assuming you have the ID of a portfolio manager to update
    manager_id = 1

    updated_manager_data = {
        'name': 'Updated Name',
        'status': False,
        'role': 'Viewer',
        'bio': 'Experienced project manager (updated)',
        'start_date': '2023-01-20',
        'email': 'updated_email@example.com',
        'password': 'updated_password'
    }

    response = client.put(f'/portfolio-managers/{manager_id}', json=updated_manager_data)
    assert response.status_code == 200
    assert response.get_json() is not None


# Test delete_portfolio_manager
def test_delete_portfolio_manager(client):
    # Assuming you have the ID of a portfolio manager to delete
    manager_id = 1

    response = client.delete(f'/portfolio-managers/{manager_id}')
    assert response.status_code == 200
    assert response.get_json() is not None





if __name__ == '__main__':
    pytest.main(['-vv'])
