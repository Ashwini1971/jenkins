import check_even


def test_is_even():
    assert check_even.is_even(10), 'number is not even'



'''
http://localhost:8081/github-webhook --> the url is private / load
        6. To make the url public -->
            1. download and unzip ngrok
            2. ngrok config add-authtoken $YOUR_AUTHTOKEN
            3. go to ngrok location, open command prompt, enter ngrok http http://localhost:8081
            4. we will get the https url --> demo (https://75af-27-59-96-121.ngrok-free.app/github-webhook)
'''