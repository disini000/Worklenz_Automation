from page_objects.InviteTeam.Setting_Invite import SettingInvite
from test_cases.conftest import setup
from utilities.ReadConfigurations import ReadConfig


class TestInvite:
    baseUrl = ReadConfig.get_application_url()

    def test_invite_team_member(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.invite = SettingInvite(self.driver)
        self.invite.invite_team_member()

    def test_invite_team_member_without_filling_jobTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.invite = SettingInvite(self.driver)
        self.invite.invite_team_member_without_filling_jobTitle()

    def test_invite_team_member_with_invalid_email(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.invite = SettingInvite(self.driver)
        self.invite.invite_team_member_with_invalid_email()

    def test_invite_team_member_with_empty_email(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.invite = SettingInvite(self.driver)
        self.invite.invite_team_member_with_empty_email()

    def test_invite_team_member_with_an_email_already_added_into_team(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.invite = SettingInvite(self.driver)
        self.invite.invite_team_member_with_an_email_already_added_into_team()