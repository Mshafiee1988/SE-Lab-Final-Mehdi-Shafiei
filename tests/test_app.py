from app import app

client = app.test_client()


def test_get_students():
    # Arrange

    # Act
    response = client.get('/api/students')

    # Assert
    assert response.status_code == 200


def test_get_existing_student():
    # Arrange

    # Act
    response = client.get('/api/students/1')

    # Assert
    assert response.status_code == 200


def test_get_non_existing_student():
    # Arrange

    # Act
    response = client.get('/api/students/999')

    # Assert
    assert response.status_code == 404
