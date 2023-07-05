import time

from pages.campaign_design_page import CampaignDesignPage
from pages.campaign_details_page import CampaignDetailsPage
from pages.campaign_generate_page import CampaignGeneratePage
from pages.campaign_launch_page import CampaignLaunchPage
from pages.campaign_rule_page import CampaignRulePage
from pages.campaign_start_page import CampaignStartPage
from pages.campaign_success_page import CampaignSuccessPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class MyStepsTest(BaseTest):
    email = "****"
    password = "****"
    rules = "Page Type is All Pages"
    priority = "7"
    campaign_status = "Visible"

    def test_steps(self):
        login_page = LoginPage(self.driver)
        login_page.fill_login_form(self.email, self.password)
        login_page.click_login_btn()
        campaign_start_page = CampaignStartPage(self.driver)
        campaign_start_page.select_instory()
        campaign_start_page.create_campaign()
        campaign_rule_page = CampaignRulePage(self.driver)
        campaign_rule_page.campaign_rule_step()
        campaign_design_page = CampaignDesignPage(self.driver)
        campaign_design_page.add_new_variation()
        campaign_design_page.select_template()
        campaign_design_page.insert_template()
        campaign_design_page.save_template()
        campaign_design_page.click_element(*campaign_design_page.NEXT_BUTTON)
        time.sleep(5)
        campaign_design_page.click_element(*campaign_design_page.NEXT_BUTTON)
        time.sleep(5)
        campaign_launch_page = CampaignLaunchPage(self.driver)
        campaign_launch_page.campaign_launch_step()
        campaign_generate_page = CampaignGeneratePage(self.driver)
        campaign_generate_page.campaign_generate_step()
        campaign_details_page = CampaignDetailsPage(self.driver)
        camp_id = campaign_details_page.go_to_campaign_details()
        self.assertIn(campaign_start_page.TEST_CAMPAIGN_NAME, campaign_details_page.get_campaign_name(),
                      "kampanya eşleşmiyor")
        self.assertEqual(self.priority, campaign_details_page.get_campaign_priority(), "priority eşleşmiyor")
        self.assertEqual(self.rules, campaign_details_page.get_campaign_rules(), "rules eşleşmiyor")
        self.assertEqual(campaign_launch_page.NOTE, campaign_details_page.get_campaign_note(), "note eşleşmiyor")
        campaign_details_page.close_detail_side_menu()
        campaign_details_page.campaign_open_test_link_step()
        campaign_success_page = CampaignSuccessPage(self.driver)
        campaign_success_page.partner_page_campaign_control(camp_id)
