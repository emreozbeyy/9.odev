import time

from pages.base_page import BasePage


class CampaignSuccessPage(BasePage):

    def partner_page_campaign_control(self, campaign_id):
        time.sleep(2)
        camp_local_storage = self.driver.execute_script("return spApi.storageData('sp-camp-{}')".format(campaign_id))
        if camp_local_storage:
            return camp_local_storage
        else:
            return ''
