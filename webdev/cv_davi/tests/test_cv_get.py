from django.urls import reverse


def test_status_code(client):
    resposta = client.get(reverse('cv_davi:home'))
    assert resposta.status_code == 200
