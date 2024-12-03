from pages.swag_labs import SwagLabs

def test_check_icon(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    assert demo_qa_page.exist_icon()


def test_check_username(browser):
    find_username = SwagLabs(browser)
    find_username.visit()
    assert find_username.field_username()

def test_check_password(browser):
    find_password = SwagLabs(browser)
    find_password.visit()
    assert find_password.field_password()