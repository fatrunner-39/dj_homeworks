import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


# Проверяем, что вернулся тот курс, который запрашивали
@pytest.mark.django_db
def test_get_course(client, course_factory):

    courses = course_factory(_quantity=1)

    response = client.get(f'/api/v1/courses/')

    assert response.status_code == 200

    data = response.json()
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


# Проверка получения списка курсов
@pytest.mark.django_db
def test_get_course_list(client, course_factory):

    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200

    assert len(data) == len(courses)


# Проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_courses_filter_by_id(client, course_factory):

    courses = course_factory(_quantity=10)

    response = client.get(f'/api/v1/courses/?id={courses[0].id}')

    assert response.status_code == 200


# Проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_courses_filter_by_name(client, course_factory):

    courses = course_factory(_quantity=10)

    response = client.get(f'/api/v1/courses/?name={courses[0].name}')

    assert response.status_code == 200

# Тест успешного создания курса
@pytest.mark.django_db
def test_success_create_course(client):
    count = Course.objects.count()

    response = client.post('/api/v1/courses/', data={'name': 'test'})

    assert response.status_code == 201

    assert Course.objects.count() == count + 1


# Тест успешного обновления курса
@pytest.mark.django_db
def test_success_update_course(client, course_factory):

    courses = course_factory(_quantity=10)

    count = Course.objects.count()

    response = client.patch(f'/api/v1/courses/{courses[0].id}/', data={'name': 'test'})

    assert response.status_code == 200

    assert Course.objects.count() == count


# Тест успешного удаления курса
@pytest.mark.django_db
def test_success_delete_course(client, course_factory):

    courses = course_factory(_quantity=10)

    count = Course.objects.count()

    response = client.delete(f'/api/v1/courses/{courses[0].id}/')

    assert response.status_code == 204

    assert Course.objects.count() == count - 1
