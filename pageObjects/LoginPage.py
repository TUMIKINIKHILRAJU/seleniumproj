class LoginPage:
    # Login Page
    __textbox_username_id = "Email"
    __textbox_password_id = "Password"
    __button_login_xpath = "//input[@value='Log in']"
    __link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.__textbox_username_id).clear()
        self.driver.find_element_by_id(self.__textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.__textbox_password_id).clear()
        self.driver.find_element_by_id(self.__textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.__button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.__link_logout_linktext).click()