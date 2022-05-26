#should be in dc-app-performance-toolkit/app/extension/jira
import random

from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Intercom
from selenium_ui.jira.pages.selectors import IntercomSelectors

def intercom_issue_load_action(webdriver, datasets):
    intercom_issue_page = get_intercom_issue_page(webdriver, datasets)

    @print_timing('selenium_intercom_issue_load')
    def measure():
        intercom_issue_page.go_to()
        intercom_issue_page.wait_for_page_loaded()

    measure()


def intercom_add_link_to_issue_action(webdriver, datasets):
    intercom_issue_page = get_intercom_issue_page(webdriver, datasets)

    @print_timing('selenium_intercom_add_link')
    def measure():
        @print_timing('selenium_intercom_add_link:load_issue')
        def sub_measure():
            intercom_issue_page.go_to()
            intercom_issue_page.wait_for_page_loaded()

        sub_measure()

        @print_timing('selenium_intercom_add_link:click_add_link_button')
        def sub_measure():
            con_url = intercom_issue_page.generate_link_url(intercom_issue_page.generate_random_id(10))

            intercom_issue_page.wait_until_clickable(IntercomSelectors.add_link_button).click()
            intercom_issue_page.wait_until_clickable(IntercomSelectors.link_input)
            intercom_issue_page.get_element(IntercomSelectors.link_input).send_keys(con_url)

        sub_measure()

    measure()


def intercom_chat_load_action(webdriver, datasets):
    intercom_issue_page = get_intercom_issue_page(webdriver, datasets)

    @print_timing('selenium_intercom_chat_load')
    def measure():
        @print_timing('selenium_intercom_chat_load:load_issue')
        def sub_measure():
            intercom_issue_page.go_to()
            intercom_issue_page.wait_for_page_loaded()
            intercom_issue_page.wait_until_visible(IntercomSelectors.conversation_button)

        sub_measure()

        @print_timing('selenium_intercom_chat_load:click_chat_button')
        def sub_measure():
            chat_elements = intercom_issue_page.get_elements(IntercomSelectors.conversation_button)
            random.choice(chat_elements).click()

        sub_measure()

        @print_timing('selenium_intercom_chat_load:wait_until_chat_load')
        def sub_measure():
            intercom_issue_page.wait_until_visible(IntercomSelectors.chat_selector)

        sub_measure()

    measure()


def intercom_chat_information_load_action(webdriver, datasets):
    intercom_issue_page = get_intercom_issue_page(webdriver, datasets)

    @print_timing('selenium_intercom_chat_information_load_action')
    def measure():
        @print_timing('selenium_intercom_chat_information_load_action:load_issue')
        def sub_measure():
            intercom_issue_page.go_to()
            intercom_issue_page.wait_for_page_loaded()
            intercom_issue_page.wait_until_visible(IntercomSelectors.information_button)

        sub_measure()

        @print_timing('selenium_intercom_chat_information_load_action:click_chat_information_button')
        def sub_measure():
            chat_elements = intercom_issue_page.get_elements(IntercomSelectors.information_button)
            random.choice(chat_elements).click()

        sub_measure()

        @print_timing('selenium_intercom_chat_information_load_action:wait_until_chat_information_load')
        def sub_measure():
            intercom_issue_page.wait_until_present(IntercomSelectors.all_information_inside_selector)

        sub_measure()

    measure()


def get_intercom_issue_page(webdriver, datasets):
    return Intercom(webdriver, get_issue_key(select_random_custom_issue_data(datasets)))


def get_issue_key(issue_data): 
    return issue_data[0]


def select_random_custom_issue_data(datasets):
    return random.choice(datasets['custom_issues'])
