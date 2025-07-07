import pytest
import requests


def test_requests_get_called(mocker):
    mock_get = mocker.patch("requests.get", autospec=True)
    url = "http://desarrollo-software.com"
    requests.get(url)
    mock_get.assert_called_with(url)


def test_requests_get_multiple_calls(mocker):
    mock_get = mocker.patch("requests.get", autospec=True)
    urls = [
        "http://desarrollo-software-1.com",
        "http://desarrollo-software-2.com"
    ]
    for url in urls:
        requests.get(url)
    assert mock_get.call_count == 2
    assert [call.args[0] for call in mock_get.call_args_list] == urls


def test_requests_get_network_error(mocker):
    mocker.patch(
        "requests.get",
        autospec=True,
        side_effect=requests.exceptions.ConnectionError
    )
    with pytest.raises(requests.exceptions.ConnectionError):
        requests.get("http://desarrollo-software.com")
