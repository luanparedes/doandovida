from Presenter.LoginScreen import LoginScreen


class Control:
    screen = ''

    def test(self, *args):
        self.screen = LoginScreen.to_screen
        return self.screen